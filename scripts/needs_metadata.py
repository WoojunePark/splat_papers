#!/usr/bin/env python3
"""
needs_metadata.py — List papers that are missing a proper LLM Summary.

Note: `inputs`, `outputs`, and `methods` are human-only fields and are NOT
checked by this script. Only `benchmarks`, `related`, and `compared` may be
auto-populated by agents, but they are optional and not flagged here.

A paper needs a summary if its `## LLM Summary` section is empty or unstructured.

Usage:
    python scripts/needs_metadata.py                   # human-readable list
    python scripts/needs_metadata.py --json            # JSON output for agent use
    python scripts/needs_metadata.py --summary-only    # only show missing summaries
    python scripts/needs_metadata.py --metadata-only   # only show missing metadata
    python scripts/needs_metadata.py --count           # just print the count
"""

import argparse
import json
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# Frontmatter parser (copied from validate.py)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    yaml_block = text[3:end].strip()
    body = text[end + 3:].strip()
    return _parse_yaml(yaml_block), body


def _parse_yaml(block: str) -> dict:
    result = {}
    current_key = None
    current_list = None
    for line in block.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if line.startswith("  - ") or line.startswith("    - ") or line.startswith("\t- "):
            if current_key and current_list is not None:
                val = stripped[2:].strip()
                if val:
                    current_list.append(val)
            continue
        match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)", line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()
            if not value:
                current_key = key
                current_list = []
                result[key] = current_list
            else:
                current_key = key
                current_list = None
                # Strip surrounding quotes
                if (value.startswith('"') and value.endswith('"')) or \
                   (value.startswith("'") and value.endswith("'")):
                    value = value[1:-1]
                result[key] = value
    return result


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def extract_llm_summary(body: str) -> str:
    """Return the text content of the ## LLM Summary section (until next ##)."""
    m = re.search(r"##\s+LLM Summary\s*\n(.*?)(?=\n##\s|\Z)", body, re.DOTALL)
    if not m:
        return ""
    return m.group(1).strip()


def get_summary_issue(summary_text: str) -> str | None:
    """
    Return a reason string if the paper needs a summary, or None if it's OK.
    """
    if not summary_text:
        return "empty"

    has_bold = bool(re.search(r"\*\*[^*]+\*\*", summary_text))
    has_bullet = bool(re.search(r"^\s*[-*]\s", summary_text, re.MULTILINE))
    has_marker = "Auto-generated summary" in summary_text

    if has_bold or has_bullet or has_marker:
        return None

    return "no-structure"


def get_missing_metadata(meta: dict) -> list[str]:
    """Return a list of auto-fillable YAML frontmatter fields that are missing/empty.

    Note: `inputs`, `outputs`, and `methods` are human-only fields and are intentionally
    excluded from this check. They must be filled by a human who has read the paper.
    """
    # No auto-fillable required fields are currently enforced.
    # (benchmarks/related/compared are optional and not flagged.)
    return []


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="List papers missing metadata tags or a proper LLM Summary."
    )
    parser.add_argument(
        "--json", action="store_true",
        help="Output as JSON array (for agent use)"
    )
    parser.add_argument(
        "--count", action="store_true",
        help="Print only the count of match files"
    )
    parser.add_argument(
        "--summary-only", action="store_true",
        help="Only report papers missing a proper summary"
    )
    parser.add_argument(
        "--metadata-only", action="store_true",
        help="Only report papers missing required metadata tags"
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    papers_dir = root_dir / "papers"

    if not papers_dir.exists():
        print(f"ERROR: papers/ directory not found at {papers_dir}", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(
        f for f in papers_dir.glob("*.md") if not f.name.startswith("_")
    )

    results = []
    for filepath in md_files:
        text = filepath.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
        arxiv_id = meta.get("arxiv", "")

        meta_missing = get_missing_metadata(meta)
        summary = extract_llm_summary(body)
        summary_issue = get_summary_issue(summary)

        # Apply flags
        if args.summary_only and not summary_issue:
            continue
        if args.metadata_only and not meta_missing:
            continue
        if not summary_issue and not meta_missing:
            continue

        reasons = []
        if meta_missing:
            reasons.append(f"missing tags ({','.join(meta_missing)})")
        if summary_issue:
            reasons.append(f"summary ({summary_issue})")

        results.append({
            "file": filepath.name,
            "arxiv": arxiv_id,
            "reason": " + ".join(reasons),
            "meta_missing": meta_missing,
            "summary_issue": summary_issue,
        })

    if args.count:
        print(len(results))
        return

    if not results:
        print("All papers have complete metadata and summaries.")
        return

    if args.json:
        print(json.dumps(results, indent=2))
        return

    # Human-readable table
    col_file  = max((len(r["file"]) for r in results), default=4)
    col_arxiv = max((len(r["arxiv"]) for r in results), default=8)
    header = f"{'FILE':<{col_file}}  {'ARXIV_ID':<{col_arxiv}}  REASON"
    print(header)
    print("-" * len(header))
    for r in results:
        print(f"{r['file']:<{col_file}}  {r['arxiv']:<{col_arxiv}}  {r['reason']}")
    print(f"\n{len(results)} paper(s) need metadata or summary formatting.")


if __name__ == "__main__":
    main()
