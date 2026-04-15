#!/usr/bin/env python3
"""
sync_issues.py -- Integrate phase of the GTD reading workflow.

Finds closed GitHub Issues labeled ``inbox``, matches them to local paper .md
files via the ``issue:`` frontmatter field, appends any user comments to the
``## My Notes`` section, marks the paper ``status: read``, and clears the
``issue:`` field to prevent re-syncing.

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

    block = "\n".join(new_lines)

    if m:
        insert_pos = m.end()
        # Skip one blank line immediately after the heading
        rest = text[insert_pos:]
        leading = len(rest) - len(rest.lstrip("\n"))
        insert_pos += leading
        return text[:insert_pos] + "\n" + block + "\n" + text[insert_pos:]
    else:
        return text.rstrip() + "\n\n## My Notes\n\n" + block + "\n"


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
    # Indent body lines for readability
    indented = "\n".join(f"> {ln}" if ln.strip() else ">" for ln in body.splitlines())
    return f"{prefix}\n{indented}"


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

    if dry_run:
        for c in user_comments:
            print(f"    → {format_comment(c)[:80]}...")
        print("  [dry-run] Would update: status=read, issue=, My Notes+=comments")
        return True

    text = md_file.read_text(encoding="utf-8")

    # 1. Update status → read
    text = _patch_frontmatter_field(text, "status", "read")

    # 2. Clear issue field (mark as synced)
    text = _patch_frontmatter_field(text, "issue", "")

    # 3. Append comments to ## My Notes
    note_lines = [format_comment(c) for c in user_comments if format_comment(c)]
    text = _append_to_my_notes(text, note_lines)

    md_file.write_text(text, encoding="utf-8")
    print(f"  ✓ Updated {md_file.name} (status=read, {len(note_lines)} notes synced)")
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
