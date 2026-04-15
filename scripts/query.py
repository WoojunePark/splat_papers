#!/usr/bin/env python3
"""
query.py -- Filter and output paper entries for LLM piping.

Reads all papers, filters by tags/status/date, and outputs their full markdown
content to stdout. Designed for piping into LLMs.

Usage:
    python scripts/query.py --input multi-view-images --method 3dgs
    python scripts/query.py --status read --output novel-view
    python scripts/query.py --after 2024-01-01
    python scripts/query.py --benchmark mipnerf360 --list
"""

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------------------
# YAML frontmatter parser (same as build_index.py)
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
                    current_list.append(_parse_scalar(val))
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
                result[key] = _parse_scalar(value)
        elif stripped.startswith("- ") and current_key and current_list is not None:
            val = stripped[2:].strip()
            if val:
                current_list.append(_parse_scalar(val))
    return result


def _parse_scalar(value: str):
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        return value[1:-1]
    if value.startswith("[") and value.endswith("]"):
        items = value[1:-1].split(",")
        return [_parse_scalar(i.strip()) for i in items if i.strip()]
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False
    try:
        return int(value)
    except ValueError:
        pass
    return value


# ---------------------------------------------------------------------------
# Filtering
# ---------------------------------------------------------------------------

def tag_matches(paper_tags: list, query: str) -> bool:
    """
    Check if any paper tag matches the query.
    Supports broad matching: query 'multi-view-images' matches 'posed-multi-view-images'.
    """
    if not paper_tags or not isinstance(paper_tags, list):
        return False
    for tag in paper_tags:
        if not isinstance(tag, str):
            continue
        # Exact match
        if tag == query:
            return True
        # Broad match: query is a suffix of the tag
        if tag.endswith(f"-{query}") or tag.endswith(query):
            return True
    return False


def paper_matches(paper: dict, args) -> bool:
    """Check if a paper matches all filter criteria."""
    # Tag filters (all must match — AND logic)
    if args.input and not tag_matches(paper.get("inputs", []), args.input):
        return False
    if args.output and not tag_matches(paper.get("outputs", []), args.output):
        return False
    if args.method and not tag_matches(paper.get("methods", []), args.method):
        return False
    if args.benchmark and not tag_matches(paper.get("benchmarks", []), args.benchmark):
        return False

    # Status filter
    if args.status and paper.get("status") != args.status:
        return False

    # Date filters
    date_str = str(paper.get("date", ""))
    if args.after and date_str < args.after:
        return False
    if args.before and date_str > args.before:
        return False


    if args.title:
        title = str(paper.get("title", "")).lower()
        if args.title.lower() not in title:
            return False

    return True


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Filter papers and output for LLM context.",
        epilog="Example: python scripts/query.py --input multi-view-images --method 3dgs"
    )

    # Tag filters
    parser.add_argument("--input", "-i", help="Filter by input tag (broad matching)")
    parser.add_argument("--output", "-o", help="Filter by output tag")
    parser.add_argument("--method", "-m", help="Filter by method tag")
    parser.add_argument("--benchmark", "-b", help="Filter by benchmark tag")

    # Metadata filters
    parser.add_argument("--status", "-s", choices=["read", "skimmed", "to-read"],
                        help="Filter by reading status")
    parser.add_argument("--after", help="Papers after date (YYYY-MM-DD)")
    parser.add_argument("--before", help="Papers before date (YYYY-MM-DD)")
    parser.add_argument("--title", "-t", help="Filter by title (substring)")

    # Output modes
    parser.add_argument("--list", "-l", action="store_true",
                        help="List matching filenames only (don't output content)")
    parser.add_argument("--frontmatter", "-f", action="store_true",
                        help="Output only frontmatter (no body)")
    parser.add_argument("--count", "-c", action="store_true",
                        help="Only print the count of matching papers")

    args = parser.parse_args()

    # Resolve paths
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    papers_dir = root_dir / "papers"

    if not papers_dir.exists():
        print("ERROR: papers directory not found", file=sys.stderr)
        sys.exit(1)

    # Load and filter papers
    matched = []
    for md_file in sorted(papers_dir.glob("*.md")):
        if md_file.name.startswith("_"):
            continue

        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)

        if not meta:
            continue

        meta["_filename"] = md_file.stem
        meta["_path"] = md_file
        meta["_text"] = text

        if paper_matches(meta, args):
            matched.append(meta)

    # Sort by date descending
    matched.sort(key=lambda p: str(p.get("date", "")), reverse=True)

    # Output
    if args.count:
        print(len(matched))
        return

    if not matched:
        print("No papers match the given filters.", file=sys.stderr)
        sys.exit(0)

    if args.list:
        for p in matched:
            title = p.get("title", p["_filename"])
            date_str = str(p.get("date", ""))
            print(f"{p['_filename']}.md  [{date_str}]  {title}")
        print(f"\n{len(matched)} papers found.", file=sys.stderr)
        return

    # Full output (for LLM piping)
    for i, p in enumerate(matched):
        if i > 0:
            print("\n" + "=" * 80 + "\n")

        if args.frontmatter:
            # Output only the frontmatter block
            text = p["_text"]
            end = text.find("---", 3)
            if end != -1:
                print(text[:end + 3])
        else:
            print(p["_text"])

    print(f"\n# {len(matched)} papers output.", file=sys.stderr)


if __name__ == "__main__":
    main()
