#!/usr/bin/env python3
"""
sync_issues.py -- Integrate phase of the GTD reading workflow.

Finds closed GitHub Issues labeled ``inbox``, matches them to local paper .md
files via the ``issue:`` frontmatter field, appends any user comments to the
``## My Notes`` section, patches ``inputs``/``outputs``/``methods`` YAML lists
from structured comment sections, marks the paper ``status: read``, and clears
the ``issue:`` field to prevent re-syncing.

Structured comment format (any heading level, singular or plural spelling):

    ## inputs
    - posed-multi-view-images
    - video

    ## outputs
    - novel-view
    - 3d-gaussians

    ## methods
    - 3dgs

    Any free-form text here goes to ## My Notes.

Usage:
    python scripts/sync_issues.py             # sync all newly closed issues
    python scripts/sync_issues.py --dry-run   # preview without writing
    python scripts/sync_issues.py --issue 42  # sync a specific issue number
"""

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# tag_utils lives in the same scripts/ directory
sys.path.insert(0, str(Path(__file__).resolve().parent))
from tag_utils import (
    normalize_tag,
    load_known_tags,
    correct_tags,
)


# ---------------------------------------------------------------------------
# gh CLI helpers
# ---------------------------------------------------------------------------

def _run_gh(*args: str) -> str:
    """Run a ``gh`` command and return its stdout. Raises on non-zero exit."""
    try:
        result = subprocess.run(
            ["gh", *args],
            capture_output=True, text=True, check=True,
        )
        return result.stdout.strip()
    except FileNotFoundError:
        print("ERROR: `gh` CLI not found. Install from https://cli.github.com")
        sys.exit(1)
    except subprocess.CalledProcessError as exc:
        err = exc.stderr.strip() if exc.stderr else str(exc)
        raise RuntimeError(f"gh command failed: {err}") from exc


def fetch_closed_inbox_issues() -> list[dict]:
    """Return a list of closed issues labeled ``inbox``."""
    raw = _run_gh(
        "issue", "list",
        "--label", "inbox",
        "--state", "closed",
        "--limit", "100",
        "--json", "number,title,closedAt,comments",
    )
    return json.loads(raw) if raw else []


def fetch_issue_with_comments(issue_number: int) -> dict:
    """Return issue metadata + comments for a single issue number."""
    raw = _run_gh(
        "issue", "view", str(issue_number),
        "--json", "number,title,closedAt,comments",
    )
    return json.loads(raw)


# ---------------------------------------------------------------------------
# Paper file helpers
# ---------------------------------------------------------------------------

def _parse_frontmatter(text: str) -> tuple[dict, int]:
    """
    Parse the YAML frontmatter from a markdown file.

    Returns ``(fields_dict, end_line_index)`` where ``end_line_index`` is the
    index of the closing ``---`` line.  Values are returned as raw strings.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, 0

    fields: dict[str, str] = {}
    i = 1
    while i < len(lines):
        line = lines[i]
        if line.strip() == "---":
            return fields, i
        m = re.match(r'^(\w[\w-]*):\s*(.*)', line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
        i += 1
    return fields, i


def find_paper_by_issue(papers_dir: Path, issue_number: int) -> Path | None:
    """Scan papers_dir for a .md file with ``issue: <issue_number>`` in its frontmatter."""
    for md_file in sorted(papers_dir.glob("*.md")):
        if md_file.name.startswith("_"):
            continue
        text = md_file.read_text(encoding="utf-8")
        fields, _ = _parse_frontmatter(text)
        if fields.get("issue", "").strip() == str(issue_number):
            return md_file
    return None


# ---------------------------------------------------------------------------
# Patching helpers
# ---------------------------------------------------------------------------

def _patch_frontmatter_field(text: str, field: str, new_value: str) -> str:
    """
    Replace ``field: <anything>`` with ``field: <new_value>`` in the
    frontmatter block.  If the field is not found it is NOT added.
    """
    lines = text.splitlines(keepends=True)
    in_front = False
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped == "---":
            in_front = not in_front
            result.append(line)
            continue
        if in_front:
            m = re.match(r'^(\w[\w-]*):\s*(.*)', line)
            if m and m.group(1) == field:
                # Preserve original indentation / line ending
                eol = "\r\n" if line.endswith("\r\n") else "\n"
                line = f"{field}: {new_value}{eol}"
        result.append(line)
    return "".join(result)


def _append_to_my_notes(text: str, new_lines: list[str]) -> str:
    """
    Append ``new_lines`` after the ``## My Notes`` heading.

    If the heading does not exist, append a new section at the end.
    """
    if not new_lines:
        return text

    notes_pattern = re.compile(r'^## My Notes\s*$', re.MULTILINE)
    m = notes_pattern.search(text)

    block = "\n\n".join(new_lines)

    if m:
        insert_pos = m.end()
        # Skip one blank line immediately after the heading
        rest = text[insert_pos:]
        leading = len(rest) - len(rest.lstrip("\n"))
        insert_pos += leading
        return text[:insert_pos] + "\n" + block + "\n" + text[insert_pos:]
    else:
        return text.rstrip() + "\n\n## My Notes\n\n" + block + "\n"


# ---------------------------------------------------------------------------
# Structured comment parsing
# ---------------------------------------------------------------------------

# Maps known heading spellings (singular + plural) to canonical field names.
_FIELD_HEADINGS: dict[str, str] = {
    "input":   "inputs",
    "inputs":  "inputs",
    "output":  "outputs",
    "outputs": "outputs",
    "method":  "methods",
    "methods": "methods",
}

# Matches any Markdown heading level (1-3 #) followed by a known field name.
_SECTION_RE = re.compile(
    r'^#{1,3}\s+(' + '|'.join(_FIELD_HEADINGS) + r')\s*$',
    re.IGNORECASE | re.MULTILINE,
)


def parse_structured_comment(
    body: str,
    known_tags: dict[str, set[str]] | None = None,
) -> dict:
    """
    Split a comment body into structured metadata fields and free-form notes.

    Recognises ``# inputs`` / ``## outputs`` / ``### methods`` headings
    (and their singular variants) at any heading level 1–3, case-insensitive.
    Bullet items (``- tag``) under those headings are normalised to
    kebab-case, then fuzzy-corrected against ``known_tags`` (if supplied).
    Everything else is collected as free-form notes text.

    Returns::

        {
            "inputs":  ["tag1", "tag2"],
            "outputs": ["tag3"],
            "methods": ["tag4"],
            "notes":   "remaining free text",
        }
    """
    result: dict[str, list | str] = {
        "inputs":  [],
        "outputs": [],
        "methods": [],
        "notes":   "",
    }

    lines = body.splitlines()
    current_field: str | None = None  # which structured field we're in
    notes_lines: list[str] = []
    # Raw accumulated tags per field (corrected in one pass at the end)
    raw_tags: dict[str, list[str]] = {"inputs": [], "outputs": [], "methods": []}

    for line in lines:
        heading_m = _SECTION_RE.match(line)
        if heading_m:
            current_field = _FIELD_HEADINGS[heading_m.group(1).lower()]
            continue

        if current_field is not None:
            # Check if this line starts a new *unknown* heading (exit struct mode)
            if re.match(r'^#{1,3}\s+', line):
                current_field = None
                notes_lines.append(line)
                continue
            # Bullet item inside a structured section
            bullet_m = re.match(r'^[-*]\s+(.+)', line)
            if bullet_m:
                tag = normalize_tag(bullet_m.group(1))
                if tag:
                    raw_tags[current_field].append(tag)
            # blank line: stay in section, ignore
            # non-bullet non-blank: treat as a note and exit field mode
            elif line.strip():
                current_field = None
                notes_lines.append(line)
        else:
            notes_lines.append(line)

    # Fuzzy-correct + dedup all accumulated tags
    for field in ("inputs", "outputs", "methods"):
        result[field] = correct_tags(
            raw_tags[field],
            known_tags or {},
            field,
            verbose=bool(known_tags),
        )

    result["notes"] = "\n".join(notes_lines).strip()
    return result


def _patch_frontmatter_list_field(text: str, field: str, new_tags: list[str]) -> str:
    """
    Merge ``new_tags`` into the YAML list field ``field`` in the frontmatter.

    - If the field's current list is empty (``- `` placeholder), replaces it.
    - Otherwise unions the existing tags with ``new_tags`` (dedup, order preserved).
    - If no tags to add, returns ``text`` unchanged.
    """
    if not new_tags:
        return text

    lines = text.splitlines(keepends=True)
    in_front = False
    front_end = 0
    i = 0
    fence_count = 0

    # Locate the frontmatter block boundaries
    field_line: int | None = None
    field_end: int | None = None   # first line that is NOT part of the list

    i = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped == "---":
            fence_count += 1
            if fence_count == 2:
                front_end = i
                break
            continue
        if fence_count == 1:
            if re.match(rf'^{re.escape(field)}:', line):
                field_line = i
            elif field_line is not None and field_end is None:
                if re.match(r'^\s+-', line):
                    pass  # still a list item
                else:
                    field_end = i  # first non-list line after field

    if field_line is None:
        return text  # field not found — leave unchanged

    if field_end is None:
        field_end = front_end  # list runs all the way to closing ---

    # Collect existing tags from the current list lines
    existing: list[str] = []
    for li in lines[field_line + 1 : field_end]:
        bm = re.match(r'^\s+-\s*(\S.*)', li)
        if bm:
            existing.append(bm.group(1).strip())

    # Union: existing (non-empty) + new_tags
    seen: set[str] = set()
    merged: list[str] = []
    for t in existing + new_tags:
        if t and t not in seen:
            seen.add(t)
            merged.append(t)

    if not merged:
        return text

    # Rebuild the block: field header line + list items
    eol = "\r\n" if lines[field_line].endswith("\r\n") else "\n"
    new_block = [f"{field}:{eol}"]
    for t in merged:
        new_block.append(f"  - {t}{eol}")

    result = lines[:field_line] + new_block + lines[field_end:]
    return "".join(result)


def format_comment(comment: dict) -> str:
    """Format a single GitHub issue comment as a Markdown block."""
    body = comment.get("body", "").strip()
    if not body:
        return ""
    created = comment.get("createdAt", "")
    date_str = ""
    if created:
        try:
            dt = datetime.fromisoformat(created.replace("Z", "+00:00"))
            date_str = dt.astimezone(timezone.utc).strftime("%Y-%m-%d")
        except Exception:
            date_str = created[:10]
    prefix = f"**[Note from GitHub{', ' + date_str if date_str else ''}]**"
    
    # Remove blockquotes for cleaner notes
    lines = body.splitlines()
    stripped_lines = []
    for line in lines:
        s = line.strip()
        if s.startswith('>'):
             stripped_lines.append(s[1:].strip())
        else:
             stripped_lines.append(s)
             
    body = "\n".join(stripped_lines)
    
    lines = body.splitlines()
    out_lines = []
    
    sub_level_re = re.compile(r'^\s*([0-9]+[-.][0-9]+[.)]?)\s+(.*)')
    top_level_re = re.compile(r'^\s*([0-9]+[.)])\s+(.*)')
    bullet_re = re.compile(r'^\s*([-*])\s+(.*)')
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            out_lines.append("")
            continue
            
        m_sub = sub_level_re.match(line)
        m_bullet = bullet_re.match(line)
        
        if m_sub:
            list_prefix = m_sub.group(1)
            content = m_sub.group(2)
            out_lines.append(f"    {list_prefix} {content}")
        elif m_bullet:
            list_prefix = m_bullet.group(1)
            content = m_bullet.group(2)
            out_lines.append(f"    {list_prefix} {content}")
        else:
            m_top = top_level_re.match(line)
            if m_top:
                list_prefix = m_top.group(1)
                content = m_top.group(2)
                out_lines.append(f"{list_prefix} {content}")
            else:
                out_lines.append(line)
                
    final_lines = []
    for line in out_lines:
        line_stripped = line.strip()
        if line_stripped == "" and (not final_lines or final_lines[-1].strip() == ""):
            continue
        final_lines.append(line.rstrip())

    formatted_body = "\n".join(final_lines).strip()
    return f"{prefix}\n\n{formatted_body}"


# ---------------------------------------------------------------------------
# Core sync logic
# ---------------------------------------------------------------------------

def sync_issue(
    issue: dict,
    papers_dir: Path,
    dry_run: bool = False,
) -> bool:
    """
    Sync a single closed issue back to its paper .md file.

    - Appends free-form comments to ``## My Notes``.
    - Merges structured ``## inputs`` / ``## outputs`` / ``## methods`` section
      items from comments into the paper's YAML frontmatter list fields.
    - Sets ``status: read`` and clears the ``issue:`` field.

    Returns True if a paper was found and updated (or would be), False otherwise.
    """
    number = issue["number"]
    title = issue.get("title", "")
    raw_comments = issue.get("comments", []) or []

    print(f"\nIssue #{number}: {title}")

    md_file = find_paper_by_issue(papers_dir, number)
    if md_file is None:
        print(f"  [skip] No paper found with issue: {number}")
        return False

    print(f"  Matched: {md_file.name}")

    # Filter out bot/automated comments (e.g. from GitHub Actions itself)
    user_comments = [
        c for c in raw_comments
        if c.get("author", {}).get("login", "") not in ("github-actions[bot]", "")
        and c.get("body", "").strip()
    ]

    if not user_comments:
        print("  No user comments to sync.")
    else:
        print(f"  Comments to sync: {len(user_comments)}")

    # Load known tags from the papers corpus for fuzzy correction
    known_tags = load_known_tags(papers_dir)

    # Parse all comments for structured metadata + free-form notes
    all_inputs:  list[str] = []
    all_outputs: list[str] = []
    all_methods: list[str] = []
    note_lines:  list[str] = []

    for c in user_comments:
        body = c.get("body", "").strip()
        parsed = parse_structured_comment(body, known_tags)
        all_inputs.extend(parsed["inputs"])
        all_outputs.extend(parsed["outputs"])
        all_methods.extend(parsed["methods"])
        # Format the free-form notes portion (may be empty)
        notes_comment = dict(c, body=parsed["notes"]) if parsed["notes"] else None
        if notes_comment:
            formatted = format_comment(notes_comment)
            if formatted:
                note_lines.append(formatted)

    if dry_run:
        if all_inputs:
            print(f"  [dry-run] inputs  tags to merge: {all_inputs}")
        if all_outputs:
            print(f"  [dry-run] outputs tags to merge: {all_outputs}")
        if all_methods:
            print(f"  [dry-run] methods tags to merge: {all_methods}")
        if note_lines:
            print(f"  [dry-run] {len(note_lines)} note block(s) → ## My Notes")
        print("  [dry-run] Would update: status=read, issue=<cleared>")
        return True

    text = md_file.read_text(encoding="utf-8")

    # 1. Update status → read
    text = _patch_frontmatter_field(text, "status", "read")

    # 2. Clear issue field (mark as synced)
    text = _patch_frontmatter_field(text, "issue", "")

    # 3. Merge structured tags into YAML list fields
    tag_summary: list[str] = []
    for field, tags in (("inputs", all_inputs), ("outputs", all_outputs), ("methods", all_methods)):
        if tags:
            text = _patch_frontmatter_list_field(text, field, tags)
            tag_summary.append(f"{field}+{len(tags)}")

    # 4. Append free-form notes to ## My Notes
    text = _append_to_my_notes(text, note_lines)

    md_file.write_text(text, encoding="utf-8")
    tag_info = f", tags: {' '.join(tag_summary)}" if tag_summary else ""
    print(f"  ✓ Updated {md_file.name} (status=read, {len(note_lines)} note(s){tag_info})")
    return True


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Integrate closed GitHub Issues back into paper .md files (GTD Integrate phase)."
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Preview changes without writing anything",
    )
    parser.add_argument(
        "--issue", "-i",
        type=int,
        metavar="NUMBER",
        help="Sync a specific issue number instead of all closed inbox issues",
    )
    parser.add_argument(
        "--no-rebuild",
        action="store_true",
        help="Skip running validate.py + build_index.py after sync",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    papers_dir = root_dir / "papers"

    # ------------------------------------------------------------------
    # Fetch issues
    # ------------------------------------------------------------------
    if args.issue:
        print(f"Fetching issue #{args.issue} ...")
        try:
            issues = [fetch_issue_with_comments(args.issue)]
        except RuntimeError as exc:
            print(f"ERROR: {exc}")
            sys.exit(1)
    else:
        print("Fetching closed inbox issues ...")
        issues = fetch_closed_inbox_issues()
        print(f"  Found {len(issues)} closed issue(s) labeled 'inbox'")

    if not issues:
        print("Nothing to sync.")
        return

    # ------------------------------------------------------------------
    # Sync each issue
    # ------------------------------------------------------------------
    updated = 0
    for issue in issues:
        if sync_issue(issue, papers_dir, dry_run=args.dry_run):
            updated += 1

    print(f"\nDone. {updated}/{len(issues)} paper(s) updated.")

    # ------------------------------------------------------------------
    # Re-validate and rebuild index
    # ------------------------------------------------------------------
    if not args.dry_run and updated > 0 and not args.no_rebuild:
        import subprocess as sp
        python = sys.executable
        for script in ("validate.py", "build_index.py"):
            script_path = script_dir / script
            if script_path.exists():
                print(f"\nRunning {script} ...")
                sp.run([python, str(script_path)], check=False)


if __name__ == "__main__":
    main()
