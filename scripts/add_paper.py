#!/usr/bin/env python3
"""
add_paper.py -- Create a paper entry from an arXiv ID.

Fetches metadata from the arXiv abstract page and scaffolds a paper .md file.
Automatically extracts ``website`` and ``code`` URLs by parsing:
  1. Hyperlinks in the arXiv abstract-page HTML (comments field + all anchors).
  2. Hyperlink annotations embedded in the PDF (via ``pypdf``).

No LLM calls are made.

Usage:
    python scripts/add_paper.py 2308.04079
    python scripts/add_paper.py 2308.04079 --name 3d-gaussian-splatting
    python scripts/add_paper.py 2308.04079 --summary   # put abstract in LLM Summary
    python scripts/add_paper.py 2308.04079 --no-pdf    # skip PDF download
"""

import argparse
import io
import re
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
    """Extract title, authors, abstract, date, and comment from arXiv HTML."""
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

    # Authors
    authors_block = re.search(r'<div class="authors">(.*?)</div>', html, re.DOTALL)
    if authors_block:
        author_links = re.findall(r">([^<]+)</a>", authors_block.group(1))
        if not author_links:
            text = re.sub(r"<[^>]+>", "", authors_block.group(1))
            text = re.sub(r"Authors?:\s*", "", text).strip()
            author_links = [a.strip() for a in text.split(",") if a.strip()]
        meta["authors"] = author_links

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
    r"(arxiv\.org|doi\.org|semanticscholar|acm\.org|openreview\.net|"
    r"springer\.com|ieee\.org|proceedings\.mlr|huggingface\.co/papers|"
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
    figure_blocks = re.findall(r'<figure.*?>(.*?)</figure>', html, re.DOTALL | re.IGNORECASE)
    for block in figure_blocks:
        # Extract img src
        img_match = re.search(r'<img[^>]*src=["\']([^"\']+)["\']', block, re.IGNORECASE)
        if not img_match:
            continue
        src = img_match.group(1)
        
        # Build full URL if relative
        if not src.startswith("http"):
            src = src.lstrip('/')
            base_id = arxiv_id.split('v')[0]
            if src.startswith(base_id):
                src = f"https://arxiv.org/html/{src}"
            else:
                src = f"https://arxiv.org/html/{arxiv_id}/{src}"

        # Extract caption
        caption_match = re.search(r'<figcaption.*?>(.*?)</figcaption>', block, re.DOTALL | re.IGNORECASE)
        caption = ""
        if caption_match:
            # Strip HTML tags
            caption = re.sub(r'<[^>]+>', '', caption_match.group(1))
            # Clean up whitespace
            caption = re.sub(r'\s+', ' ', caption).strip()
        
        figures.append({"src": src, "caption": caption})
    
    return figures



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
    summary_text: str = "",
    figures: list[dict] = None,
) -> str:
    """Generate the markdown content for a paper entry."""
    title = meta.get("title", "")
    date_str = meta.get("date", "YYYY-MM-DD")
    authors = meta.get("authors", [])

    authors_yaml = "\n".join(f"  - {a}" for a in authors) if authors else "  - "

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
        "authors:",
        authors_yaml,
        "",
        abstract_yaml,
        "",
        f"website: {website}",
        f"code: {code}",
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
        "## LLM Summary",
        "",
        llm_summary,
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

    lines.extend([
        "## My Notes",
        "",
        "",
    ])

    return "\n".join(lines)


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

    args = parser.parse_args()
    arxiv_id = args.arxiv_id.strip()

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
    authors_preview = meta.get("authors", [])
    preview_str = ", ".join(authors_preview[:3])
    if len(authors_preview) > 3:
        preview_str += " ..."
    # Safely print on Windows consoles that may not support all Unicode chars
    safe_preview = preview_str.encode(sys.stdout.encoding or "utf-8", errors="replace").decode(sys.stdout.encoding or "utf-8")
    print(f"  Authors: {safe_preview}")

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
    # 4. Generate and write the paper entry
    # ------------------------------------------------------------------
    summary_text = meta.get("abstract", "") if args.summary else ""
    content = generate_paper_md(arxiv_id, meta, website, code, summary_text, figures)
    filepath.write_text(content, encoding="utf-8")

    print(f"\nCreated: {filepath}")
    print("\nNext steps:")
    print(f"  1. Edit {filename} - fill in tags, venue")
    if not website:
        print("  2. Manually add website URL (not found automatically)")
    if not code:
        print("  3. Manually add code URL (not found automatically)")
    print("  4. Run: python scripts/validate.py")
    print("  5. Run: python scripts/build_index.py")


if __name__ == "__main__":
    main()
