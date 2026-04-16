#!/usr/bin/env python3
"""
add_paper.py -- Create a paper entry from an arXiv ID.

Fetches metadata from the arXiv abstract page and scaffolds a paper .md file.
Automatically extracts ``website`` and ``code`` URLs by parsing:
  1. Hyperlinks in the arXiv abstract-page HTML (comments field + all anchors).
  2. Hyperlink annotations embedded in the PDF (via ``pypdf``).

Also creates a GitHub Issue (requires ``gh`` CLI) to populate the GTD inbox.
Use ``--no-issue`` to skip issue creation.

No LLM calls are made.

Usage:
    python scripts/add_paper.py 2308.04079
    python scripts/add_paper.py 2308.04079 --name 3d-gaussian-splatting
    python scripts/add_paper.py 2308.04079 --summary   # put abstract in LLM Summary
    python scripts/add_paper.py 2308.04079 --no-pdf    # skip PDF download
    python scripts/add_paper.py 2308.04079 --no-issue  # skip GitHub Issue creation
"""

import argparse
import io
import json
import re
import shutil
import subprocess
import sys
import urllib.request
import urllib.error
from pathlib import Path


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def fetch_bytes(url: str, timeout: int = 60) -> bytes:
    """Fetch a URL and return raw bytes."""
    req = urllib.request.Request(url, headers={"User-Agent": "splat-papers-bot/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def fetch_text(url: str, timeout: int = 30) -> str:
    """Fetch a URL and return decoded text (UTF-8)."""
    return fetch_bytes(url, timeout=timeout).decode("utf-8")


# ---------------------------------------------------------------------------
# arXiv abstract-page parser
# ---------------------------------------------------------------------------

def parse_arxiv_abstract_page(html: str) -> dict:
    """Extract title, abstract, date, and comment from arXiv HTML."""
    meta: dict = {}

    # Title
    m = re.search(r'<h1 class="title mathjax">\s*Title:\s*(.*?)</h1>', html, re.DOTALL)
    if not m:
        m = re.search(r'<h1 class="title mathjax">(.*?)</h1>', html, re.DOTALL)
    if m:
        title = re.sub(r"<[^>]+>", "", m.group(1)).strip()
        title = re.sub(r"\s+", " ", title)
        title = re.sub(r"^Title:\s*", "", title)
        meta["title"] = title

    # Abstract
    abstract_block = re.search(
        r'<blockquote class="abstract mathjax">\s*Abstract:\s*(.*?)</blockquote>',
        html, re.DOTALL,
    )
    if not abstract_block:
        abstract_block = re.search(
            r'<blockquote class="abstract mathjax">(.*?)</blockquote>',
            html, re.DOTALL,
        )
    if abstract_block:
        abstract = re.sub(r"<[^>]+>", "", abstract_block.group(1))
        abstract = re.sub(r"^\s*Abstract:\s*", "", abstract.strip())
        abstract = re.sub(r"\s+", " ", abstract).strip()
        meta["abstract"] = abstract

    # Submission date
    date_match = re.search(r"Submitted on (\d{1,2})\s+(\w{3})\s+(\d{4})", html)
    if not date_match:
        date_match = re.search(r"\[Submitted on (\d{1,2})\s+(\w{3})\s+(\d{4})", html)
    if date_match:
        day = int(date_match.group(1))
        month_str = date_match.group(2)
        year = int(date_match.group(3))
        months = {
            "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
            "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12,
        }
        meta["date"] = f"{year}-{months.get(month_str, 1):02d}-{day:02d}"

    # Comments field (often contains venue and project-page links)
    comment_match = re.search(
        r'<td class="tablecell comments mathjax">(.*?)</td>', html, re.DOTALL
    )
    if comment_match:
        meta["comment"] = re.sub(r"<[^>]+>", "", comment_match.group(1)).strip()

    return meta


# ---------------------------------------------------------------------------
# URL extraction helpers
# ---------------------------------------------------------------------------

# Matches a GitHub or GitLab repo URL
_CODE_REPO_RE = re.compile(
    r'https?://(github|gitlab)\.com/([A-Za-z0-9_.-]+)/([A-Za-z0-9_.-]+?)(?:/[^\s"\x27<>]*)?$'
)
# github.io / gitlab.io project pages
_GITHUB_IO_RE = re.compile(r'^https?://[A-Za-z0-9_.-]+\.github\.io(/[^\s"\x27<>]*)?$')

# URLs we never want as website/code
_BLOCKLIST_RE = re.compile(
    r"(arxiv\.org|doi\.org|semanticscholar|acm\.org|"
    r"openreview\.net|springer\.com|ieee\.org|proceedings\.mlr|huggingface\.co/papers|"
    r"paperswithcode\.com/paper|youtube\.com|youtu\.be|twitter\.com|x\.com|"
    r"linkedin\.com|facebook\.com|instagram\.com|"
    # GitHub meta-pages (not repos)
    r"github\.com/(login|join|features|marketplace|explore|about|contact|"
    r"orgs|apps|topics|collections|events|sponsors|blob|tree|commit|"
    r"issues|pulls|discussions|releases|actions|wiki|security|insights|"
    r"settings|forks|stargazers|watchers|network|graphs|license|"
    r"compare|search|archive|packages|codespaces|copilot|models|enterprise))",
    re.IGNORECASE,
)


def _clean_url(url: str) -> str:
    """Strip trailing punctuation and unwanted fragments."""
    url = url.split("?")[0]  # drop query strings
    url = url.rstrip(".,;:\"')/")
    url = re.sub(r"#.*$", "", url)
    return url


def _is_blocked(url: str) -> bool:
    return bool(_BLOCKLIST_RE.search(url))


def extract_links_from_arxiv_page(html: str) -> tuple[list[str], list[str]]:
    """
    Return ``(comments_urls, other_urls)`` found in the arXiv abstract page.

    - ``comments_urls``: links from the "Comments" metadata cell — very high
      signal (authors often post project-page / code links there explicitly).
    - ``other_urls``: all other external HTTP(S) anchors on the page.
    """
    comments_urls: list[str] = []
    other_urls: list[str] = []
    seen: set[str] = set()

    def _add(url: str, dest: list) -> None:
        u = _clean_url(url)
        if u and u.startswith("http") and u not in seen:
            seen.add(u)
            dest.append(u)

    # 1. Comments cell (high-signal)
    comment_match = re.search(
        r'<td class="tablecell comments mathjax">(.*?)</td>', html, re.DOTALL
    )
    if comment_match:
        cell = comment_match.group(1)
        for href in re.findall(r'href=["\x27]?(https?://[^"\x27>\s]+)', cell):
            _add(href, comments_urls)
        cell_text = re.sub(r"<[^>]+>", " ", cell)
        for bare in re.findall(r"https?://\S+", cell_text):
            _add(bare, comments_urls)

    # 2. All other anchors
    for href in re.findall(r'href=["\x27]?(https?://[^"\x27>\s]+)', html):
        _add(href, other_urls)

    return comments_urls, other_urls


def extract_figures_from_arxiv_html(arxiv_id: str) -> list[dict]:
    """
    Fetch the arxiv HTML version and extract figures.
    Returns a list of dicts: [{'src': 'url', 'caption': 'caption text'}, ...]
    """
    html_url = f"https://arxiv.org/html/{arxiv_id}"
    print(f"  Downloading HTML for figure extraction: {html_url} ...")
    try:
        html = fetch_text(html_url, timeout=30)
    except urllib.error.URLError as exc:
        print(f"  [warn] HTML version not available or download failed: {exc}")
        return []

    figures = []
    # Find all <figure> tags
    figure_blocks = list(re.finditer(r'<figure.*?>.*?</figure>', html, re.DOTALL | re.IGNORECASE))
    for match in figure_blocks:
        block = match.group(0)
        
        # Extract caption
        caption_match = re.search(r'<figcaption.*?>(.*?)</figcaption>', block, re.DOTALL | re.IGNORECASE)
        caption = ""
        if caption_match:
            # Strip HTML tags
            caption = re.sub(r'<[^>]+>', '', caption_match.group(1))
            # Clean up whitespace
            caption = re.sub(r'\s+', ' ', caption).strip()
            
        # Extract img src
        img_match = re.search(r'<img[^>]*src=["\']([^"\']+)["\']', block, re.IGNORECASE)
        src = ""
        if img_match:
            src = img_match.group(1)
        else:
            # If no img in the block, it might be a teaser figure where the <img> 
            # is placed right before the <figure> block in HTML.
            # Only look backwards if it's explicitly labeled as a Figure to avoid duplicates for Tables.
            if re.search(r'^(Figure|Fig\.)', caption, re.IGNORECASE):
                preceding_html = html[:match.start()]
                imgs_before = re.findall(r'<img[^>]*src=["\']([^"\']+)["\']', preceding_html, re.IGNORECASE)
                if imgs_before:
                    src = imgs_before[-1] # nearest one
                    
        if not src:
            continue
        
        # Build full URL if relative
        if not src.startswith("http"):
            src = src.lstrip('/')
            base_id = arxiv_id.split('v')[0]
            if src.startswith(base_id):
                src = f"https://arxiv.org/html/{src}"
            else:
                src = f"https://arxiv.org/html/{arxiv_id}/{src}"
        
        figures.append({"src": src, "caption": caption})
    
    return figures


# ---------------------------------------------------------------------------
# OpenReview URL lookup
# ---------------------------------------------------------------------------

def _strip_math(title: str) -> str:
    """Remove LaTeX math expressions from a title for plain-text search."""
    title = re.sub(r"\$[^$]+\$", "", title)       # $...$ inline math
    title = re.sub(r"\\\(.*?\\\)", "", title)      # \(...\) inline math
    title = re.sub(r"\s+", " ", title).strip()
    return title


def _get_title_from_note(note: dict) -> str:
    """Extract the title string from either 'forumContent' or 'content' field."""
    for field in ("forumContent", "content"):
        container = note.get(field) or {}
        title_val = container.get("title", {})
        if isinstance(title_val, dict):
            return title_val.get("value", "")
        if isinstance(title_val, str):
            return title_val
    return ""


def extract_openreview_url(title: str, timeout: int = 15) -> str:
    """
    Search OpenReview for a paper by title and return the forum URL if found.

    Uses the ``api2.openreview.net/notes/search`` endpoint.  Strips LaTeX math
    from the title before searching for better hit rates.  Returns an empty
    string when the paper is not found or the request fails (rate-limited, etc.).

    Rate-limit note: the API allows roughly 1 request per minute from a single
    IP without credentials.  Because ``add_paper.py`` is called once per paper
    this is usually fine, but errors are caught and silently skipped.
    """
    clean = _strip_math(title)
    url = (
        "https://api2.openreview.net/notes/search"
        f"?term={urllib.parse.quote(clean)}&offset=0&limit=25"
    )
    print(f"  Searching OpenReview: {clean!r} ...")
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "splat-papers-bot/1.0"}
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        if exc.code == 429:
            print("  [info] OpenReview rate-limited — skipping.")
        elif exc.code == 403:
            print("  [info] OpenReview access denied (rate limit) — skipping.")
        else:
            print(f"  [warn] OpenReview HTTP error {exc.code} — skipping.")
        return ""
    except urllib.error.URLError as exc:
        print(f"  [warn] OpenReview lookup failed: {exc.reason} — skipping.")
        return ""
    except Exception as exc:
        print(f"  [warn] OpenReview lookup unexpected error: {exc} — skipping.")
        return ""

    notes = data.get("notes", [])
    clean_lower = clean.lower()

    # Pass 1 — exact title match
    for note in notes:
        note_title = _get_title_from_note(note)
        if not note_title:
            continue
        if _strip_math(note_title).lower() == clean_lower:
            forum_id = note.get("forum") or note.get("id")
            if forum_id:
                return f"https://openreview.net/forum?id={forum_id}"

    # Pass 2 — fuzzy word-overlap >= 80 %
    title_words = set(clean_lower.split())
    best_url = ""
    best_score = 0.0
    for note in notes:
        note_title = _get_title_from_note(note)
        if not note_title:
            continue
        note_words = set(_strip_math(note_title).lower().split())
        if not note_words:
            continue
        score = len(title_words & note_words) / max(len(title_words), len(note_words))
        if score >= 0.8 and score > best_score:
            forum_id = note.get("forum") or note.get("id")
            if forum_id:
                best_score = score
                best_url = f"https://openreview.net/forum?id={forum_id}"

    return best_url


def extract_alphaxiv_summary(arxiv_id: str) -> str:
    """Check alphaxiv.org for a pre-generated LLM summary."""
    url = f"https://alphaxiv.org/overview/{arxiv_id}.md"
    print(f"  Checking alphaXiv for summary: {url} ...")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "splat-papers-bot/1.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            text = resp.read().decode("utf-8").strip()
            if text and not text.startswith("<!DOCTYPE html>"):
                # Clean up the redundant top-level header provided by alphaXiv
                text = re.sub(r"^##\s+Research Report[^\n]*\n+", "", text)
                return text.strip()
    except urllib.error.URLError as exc:
        if hasattr(exc, 'code') and exc.code == 404:
            print("  [info] alphaXiv summary not found (404).")
        else:
            print(f"  [warn] alphaXiv summary fetch failed: {exc}")
    except Exception as exc:
        print(f"  [warn] alphaXiv summary fetch unexpected error: {exc}")
    
    return ""


def extract_links_from_pdf(arxiv_id: str) -> list[tuple[int, str]]:
    """
    Download the arXiv PDF and extract all hyperlink annotation URIs.

    Returns a list of ``(page_index, url)`` tuples (0-based pages).
    Early pages are returned first so callers can weight them higher.

    Requires ``pypdf`` (``pip install pypdf``).  Returns ``[]`` and prints a
    warning if the library is not available or the download/parse fails.
    """
    try:
        from pypdf import PdfReader  # type: ignore[import]
    except ImportError:
        print("  [warn] pypdf not installed — skipping PDF link extraction.")
        print("         Install with: pip install pypdf")
        return []

    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    print(f"  Downloading PDF for link extraction: {pdf_url} ...")
    try:
        pdf_bytes = fetch_bytes(pdf_url, timeout=90)
    except urllib.error.URLError as exc:
        print(f"  [warn] PDF download failed: {exc}")
        return []

    results: list[tuple[int, str]] = []
    try:
        reader = PdfReader(io.BytesIO(pdf_bytes))
        for page_idx, page in enumerate(reader.pages):
            annots = page.get("/Annots")
            if annots is None:
                continue
            for annot_ref in annots:
                try:
                    annot = annot_ref.get_object()
                except Exception:
                    continue
                if annot.get("/Subtype") != "/Link":
                    continue
                action = annot.get("/A")
                if action is None:
                    continue
                try:
                    action_obj = action.get_object()
                except Exception:
                    action_obj = action
                uri = action_obj.get("/URI")
                if uri and isinstance(uri, str) and uri.startswith("http"):
                    results.append((page_idx, _clean_url(uri)))
    except Exception as exc:
        print(f"  [warn] PDF parsing error: {exc}")

    return results


def extract_github_from_website(website_url: str) -> str:
    """Fetch website HTML and search for a GitHub/GitLab repo link."""
    if not website_url or not website_url.startswith("http"):
        return ""
    
    try:
        # Some project pages block non-browser user agents
        req = urllib.request.Request(
            website_url, 
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read().decode("utf-8", errors="ignore")
    except Exception as exc:
        print(f"  [warn] Failed to fetch project page ({website_url}): {exc}")
        return ""

    for href in re.findall(r'href=["\x27]?(https?://[^"\x27>\s]+)', html):
        u = _clean_url(href)
        if _is_blocked(u):
            continue
        if _CODE_REPO_RE.search(u):
            return u

    # Check for bare links
    html_text = re.sub(r"<[^>]+>", " ", html)
    for bare in re.findall(r"https?://(?:github|gitlab)\.com/\S+", html_text):
        u = _clean_url(bare)
        if _is_blocked(u):
            continue
        if _CODE_REPO_RE.search(u):
            return u

    return ""


# ---------------------------------------------------------------------------
# Link classification
# ---------------------------------------------------------------------------

def classify_links(
    comments_urls: list[str],
    other_html_urls: list[str],
    pdf_links: list[tuple[int, str]],
) -> dict[str, str]:
    """
    Score all collected URLs and return the best ``website`` and ``code``.

    Scoring heuristic:
    - GitHub/GitLab repo URL → strong ``code`` candidate  (+10)
    - github.io URL          → strong ``website`` candidate (+10)
    - In comments cell       → +8  (explicit author mention)
    - Other HTML anchor      → +2
    - PDF page 0-1           → +5  (mentioned in abstract/intro)
    - PDF page 2-5           → +2
    - Blocked/academic       → discarded
    - Score >= 5 + unknown   → promoted to ``website``
    """
    from collections import defaultdict

    scores: dict[str, int] = defaultdict(int)
    category: dict[str, str] = {}  # url -> "code" | "website" | "unknown"

    def _register(url: str, bonus: int) -> None:
        if _is_blocked(url) or not url.startswith("http"):
            return
        scores[url] += bonus
        if url not in category:
            if _CODE_REPO_RE.search(url):
                category[url] = "code"
                scores[url] += 10
            elif _GITHUB_IO_RE.match(url):
                category[url] = "website"
                scores[url] += 10
            else:
                category[url] = "unknown"

    for url in comments_urls:
        _register(url, bonus=8)

    for url in other_html_urls:
        _register(url, bonus=2)

    for page_idx, url in pdf_links:
        page_bonus = 5 if page_idx <= 1 else (2 if page_idx <= 5 else 0)
        _register(url, bonus=page_bonus)

    # Promote "unknown" URLs with enough signal (likely project pages)
    for url, cat in list(category.items()):
        if cat == "unknown" and scores[url] >= 5:
            category[url] = "website"

    best_code = ""
    best_website = ""
    best_code_score = -1
    best_website_score = -1

    for url, score in scores.items():
        cat = category.get(url, "unknown")
        if cat == "code" and score > best_code_score:
            best_code = url
            best_code_score = score
        elif cat == "website" and score > best_website_score:
            best_website = url
            best_website_score = score

    return {"website": best_website, "code": best_code}


# ---------------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------------

def slugify(title: str) -> str:
    """Convert a title to kebab-case slug."""
    slug = re.sub(r"[^a-z0-9\s-]", "", title.lower())
    slug = re.sub(r"\s+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    parts = slug.split("-")
    return "-".join(parts[:6]) if len(parts) > 6 else slug


def generate_paper_md(
    arxiv_id: str,
    meta: dict,
    website: str,
    code: str,
    openreview: str = "",
    summary_text: str = "",
    figures: list[dict] = None,
    issue_number: int = 0,
) -> str:
    """Generate the markdown content for a paper entry."""
    title = meta.get("title", "")
    date_str = meta.get("date", "YYYY-MM-DD")

    llm_summary = summary_text or ""

    # Build abstract YAML field (verbatim, quoted)
    abstract_raw = meta.get("abstract", "")
    if abstract_raw:
        # Escape inner quotes for YAML block scalar
        abstract_yaml = f'abstract: "{abstract_raw.replace(chr(34), chr(39))}"'
    else:
        abstract_yaml = "abstract:"

    lines = [
        "---",
        f'title: "{title}"',
        f"date: {date_str}",
        f'arxiv: "{arxiv_id}"',
        "venue:",
        "status: to-read",
        "",
        abstract_yaml,
        "",
        f"website: {website}",
        f"code: {code}",
        f"openreview: {openreview}",
        f"issue: {issue_number if issue_number else ''}",
        "",
        "inputs:",
        "  - ",
        "",
        "outputs:",
        "  - ",
        "",
        "methods:",
        "  - ",
        "",
        "benchmarks:",
        "  - ",
        "",
        "related:",
        "  - ",
        "",
        "compared:",
        "  - ",
        "---",
        "",
        f"# {title}",
        "",
        "## My Notes",
        "",
        "",
        "## Results",
        "",
        "<!-- Optional: structured benchmark results for cross-paper comparison -->",
        "<!-- Example:",
        "| Benchmark | PSNR | SSIM | LPIPS |",
        "|---|---|---|---|",
        "| mipnerf360 | 27.21 | 0.815 | 0.214 |",
        "| tanks-and-temples | 23.14 | 0.841 | 0.183 |",
        "-->",
        "",
    ]

    if figures:
        lines.append("## Figures")
        lines.append("")
        for fig in figures[:10]:
            caption = fig.get("caption", "Figure")
            src = fig.get("src", "")
            lines.append(f"![Figure]({src})")
            lines.append("")
            lines.append(f"*{caption}*")
            lines.append("")

    lines.append("## LLM Summary")
    lines.append("")
    lines.append(llm_summary)
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# GitHub Issue creation (GTD Capture phase)
# ---------------------------------------------------------------------------

def _gh_available() -> bool:
    """Return True if the ``gh`` CLI is installed and reachable."""
    return shutil.which("gh") is not None


def _build_issue_body(
    arxiv_id: str,
    meta: dict,
    website: str,
    code: str,
    openreview: str,
    figures: list[dict],
) -> str:
    """Build the GitHub Issue body for the Capture phase."""
    title = meta.get("title", arxiv_id)
    date_str = meta.get("date", "")
    abstract = meta.get("abstract", "*(abstract not available)*")

    abs_url = f"https://arxiv.org/abs/{arxiv_id}"
    pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
    html_url = f"https://arxiv.org/html/{arxiv_id}"

    links = [f"[arXiv]({abs_url})", f"[PDF]({pdf_url})", f"[HTML]({html_url})"]
    if website:
        links.append(f"[Website]({website})")
    if code:
        links.append(f"[Code]({code})")
    if openreview:
        links.append(f"[OpenReview]({openreview})")

    lines = [
        f"## [{title}]({abs_url})",
        "",
        f"**Status:** `to-read` | **Published:** {date_str}",
        "",
        "### Abstract",
        "",
        f"> {abstract}",
        "",
        "### Links",
        "",
        " | ".join(links),
        "",
    ]

    top_figs = (figures or [])[:3]
    if top_figs:
        lines.append("### Figures")
        lines.append("")
        for fig in top_figs:
            src = fig.get("src", "")
            cap = fig.get("caption", "") or "Figure"
            cap_short = cap[:120] + "..." if len(cap) > 120 else cap
            if src:
                lines.append(f"![{cap_short}]({src})")
                lines.append(f"*{cap_short}*")
                lines.append("")

    lines += [
        "---",
        "",
        "### 📝 Reading Notes Template",
        "",
        "Leave a comment using the sections below.",
        "Bullet items under each heading are synced to the paper's YAML tags.",
        "Any other text goes to `## My Notes`.",
        "Heading level (`#` or `##`) and singular/plural spelling both work.",
        "",
        "```",
        "## inputs",
        "- ",
        "",
        "## outputs",
        "- ",
        "",
        "## methods",
        "- ",
        "",
        "Free-form reading notes here.",
        "```",
        "",
        "*Managed by splat-papers. "
        "Close this issue once you have read the paper.*",
    ]
    return "\n".join(lines)


def create_github_issue(
    arxiv_id: str,
    meta: dict,
    website: str,
    code: str,
    openreview: str,
    figures: list[dict],
) -> int:
    """
    Create a GitHub Issue using the ``gh`` CLI.

    Returns the issue number on success, or 0 on failure.
    The caller should store the number in the paper's ``issue:`` field.
    """
    if not _gh_available():
        print(
            "\n[skip] GitHub Issue NOT created — `gh` CLI not found.\n"
            "       Install it from https://cli.github.com and run `gh auth login`,\n"
            "       then re-run with: python scripts/add_paper.py {arxiv_id} --force"
        )
        return 0

    title = meta.get("title", arxiv_id)
    issue_title = title
    body = _build_issue_body(arxiv_id, meta, website, code, openreview, figures)

    # Ensure labels exist before using them (gh creates labels implicitly on GitHub,
    # but `gh issue create` can fail if labels don't exist in the repo).
    # We attempt creation and silently ignore errors (label may already exist).
    for label_spec in [
        ("inbox", "Inbox — paper added, not yet read", "0075ca"),
    ]:
        try:
            subprocess.run(
                ["gh", "label", "create", label_spec[0],
                 "--description", label_spec[1],
                 "--color", label_spec[2], "--force"],
                capture_output=True, check=False,
            )
        except Exception:
            pass

    try:
        result = subprocess.run(
            ["gh", "issue", "create",
             "--title", issue_title,
             "--body", body,
             "--label", "inbox",
             "--assignee", "@me"],
            capture_output=True, text=True, check=True,
        )
        # gh prints the issue URL on stdout, e.g. https://github.com/owner/repo/issues/42
        url = result.stdout.strip()
        print(f"  GitHub Issue created: {url}")
        # Extract issue number from URL
        m = re.search(r"/(\d+)$", url)
        return int(m.group(1)) if m else 0
    except subprocess.CalledProcessError as exc:
        err = exc.stderr.strip() if exc.stderr else str(exc)
        print(f"\n[warn] GitHub Issue creation failed: {err}")
        print("       You can create it manually or re-run after fixing `gh` auth.")
        return 0
    except Exception as exc:
        print(f"\n[warn] Unexpected error during issue creation: {exc}")
        return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a paper entry from an arXiv ID."
    )
    parser.add_argument("arxiv_id", help="ArXiv paper ID (e.g., 2308.04079)")
    parser.add_argument(
        "--name", "-n",
        help="Custom short name for the file (default: auto-generated from title)",
    )
    parser.add_argument(
        "--summary", "-s",
        action="store_true",
        help="Populate ## LLM Summary with the paper abstract",
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="Overwrite existing file",
    )
    parser.add_argument(
        "--no-pdf",
        action="store_true",
        help="Skip PDF download for link extraction (faster, less accurate)",
    )
    parser.add_argument(
        "--no-issue",
        action="store_true",
        help="Skip GitHub Issue creation (default: create issue in GTD inbox)",
    )

    args = parser.parse_args()
    arxiv_id = args.arxiv_id.strip()

    # Extract arXiv ID if a full URL was provided
    m = re.search(r"(\d{4}\.\d{4,5}(?:v\d+)?)", arxiv_id)
    if m and ("arxiv.org" in arxiv_id or "http" in arxiv_id or "/" in arxiv_id):
        arxiv_id = m.group(1)

    # Validate arXiv ID format
    if not re.match(r"^\d{4}\.\d{4,5}(v\d+)?$", arxiv_id):
        print(f"ERROR: '{arxiv_id}' doesn't look like an arXiv ID (expected e.g. 2308.04079)")
        sys.exit(1)

    # Resolve paths
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    papers_dir = root_dir / "papers"
    papers_dir.mkdir(exist_ok=True)

    # ------------------------------------------------------------------
    # 1. Fetch arXiv abstract page
    # ------------------------------------------------------------------
    abs_url = f"https://arxiv.org/abs/{arxiv_id}"
    print(f"Fetching {abs_url} ...")
    try:
        html = fetch_text(abs_url)
    except urllib.error.URLError as e:
        print(f"ERROR: Failed to fetch {abs_url}: {e}")
        sys.exit(1)

    meta = parse_arxiv_abstract_page(html)

    if not meta.get("title"):
        print("ERROR: Could not parse title from arXiv page")
        sys.exit(1)

    print(f"  Title:   {meta['title']}")
    print(f"  Date:    {meta.get('date', 'unknown')}")

    # ------------------------------------------------------------------
    # 2. Extract links (HTML page + PDF)
    # ------------------------------------------------------------------
    print("Extracting website/code links ...")
    comments_urls, other_html_urls = extract_links_from_arxiv_page(html)

    pdf_links: list[tuple[int, str]] = []
    if not args.no_pdf:
        pdf_links = extract_links_from_pdf(arxiv_id)
        print(f"  PDF annotation links found: {len(pdf_links)}")

    links = classify_links(comments_urls, other_html_urls, pdf_links)
    website = links["website"]
    code = links["code"]

    if website and not code:
        print(f"  Scanning project page for code link: {website} ...")
        code = extract_github_from_website(website)

    print(f"  website => {website or '(not found)'}")
    print(f"  code    => {code or '(not found)'}")

    print("Extracting figures from HTML ...")
    figures = extract_figures_from_arxiv_html(arxiv_id)
    if figures:
        print(f"  Found {len(figures)} figures")

    # ------------------------------------------------------------------
    # 3. Determine output filename
    # ------------------------------------------------------------------
    yymm = arxiv_id[:4]
    short_name = args.name if args.name else slugify(meta["title"])
    filename = f"{yymm}_{short_name}.md"
    filepath = papers_dir / filename

    if filepath.exists() and not args.force:
        print(f"\nFile already exists: {filepath}")
        print("Use --force to overwrite.")
        sys.exit(1)

    # ------------------------------------------------------------------
    # 4. Look up OpenReview URL
    # ------------------------------------------------------------------
    print("Looking up OpenReview ...")
    openreview = extract_openreview_url(meta.get("title", ""))
    if openreview:
        print(f"  openreview => {openreview}")
    else:
        print("  openreview => (not found)")

    # ------------------------------------------------------------------
    # 5. Create GitHub Issue (GTD Capture phase)
    # ------------------------------------------------------------------
    issue_number = 0
    if not args.no_issue:
        print("Creating GitHub Issue (GTD inbox) ...")
        issue_number = create_github_issue(arxiv_id, meta, website, code, openreview, figures)

    # ------------------------------------------------------------------
    # 6. Generate and write the paper entry
    # ------------------------------------------------------------------
    print("\nFetching alphaXiv summary ...")
    alphaxiv_summary = extract_alphaxiv_summary(arxiv_id)
    
    if alphaxiv_summary:
        summary_text = alphaxiv_summary
    else:
        summary_text = meta.get("abstract", "") if args.summary else ""

    content = generate_paper_md(
        arxiv_id, meta, website, code, openreview, summary_text, figures, issue_number
    )
    filepath.write_text(content, encoding="utf-8")

    print(f"\nCreated: {filepath}")
    if issue_number:
        print(f"GitHub Issue #{issue_number} opened — check GitHub mobile to read on the go.")

    # ------------------------------------------------------------------
    # 7. Rebuild INDEX.md automatically
    # ------------------------------------------------------------------
    build_index_script = script_dir / "build_index.py"
    if build_index_script.exists():
        print("\nRebuilding index ...")
        try:
            subprocess.run(
                [sys.executable, str(build_index_script)],
                check=True,
            )
        except subprocess.CalledProcessError as exc:
            print(f"[warn] build_index.py exited with code {exc.returncode} — index may be stale.")
        except Exception as exc:
            print(f"[warn] Could not run build_index.py: {exc}")
    else:
        print("[warn] build_index.py not found — skipping index rebuild.")

    print("\nNext steps:")
    print(f"  1. Edit {filename} - fill in tags, venue")
    if not website:
        print("  2. Manually add website URL (not found automatically)")
    if not code:
        print("  3. Manually add code URL (not found automatically)")
    print("  4. Run: python scripts/validate.py")
    if issue_number:
        print(f"  5. When done reading: close GitHub Issue #{issue_number}")
        print("     → sync_issues.py will sync your comments back to '## My Notes'")


if __name__ == "__main__":
    main()
