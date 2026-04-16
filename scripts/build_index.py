#!/usr/bin/env python3
"""
build_index.py — Generates INDEX.md and tags/*.md from paper frontmatter.

Usage:
    python scripts/build_index.py
"""

import re
import sys
from pathlib import Path
from datetime import date

# ---------------------------------------------------------------------------
# YAML frontmatter parser (no external dependencies)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown text. Returns (metadata, body)."""
    if not text.startswith("---"):
        return {}, text

    end = text.find("---", 3)
    if end == -1:
        return {}, text

    yaml_block = text[3:end].strip()
    body = text[end + 3:].strip()
    meta = _parse_yaml(yaml_block)
    return meta, body


def _parse_yaml(block: str) -> dict:
    """Minimal YAML parser supporting scalars and lists."""
    result = {}
    current_key = None
    current_list = None

    for line in block.split("\n"):
        # Skip empty lines and comments
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # List item (indented "- value")
        if line.startswith("  - ") or line.startswith("    - ") or line.startswith("\t- "):
            if current_key and current_list is not None:
                val = stripped[2:].strip()
                if val:
                    current_list.append(_parse_scalar(val))
            continue

        # Key: value pair
        match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*(.*)", line)
        if match:
            key = match.group(1)
            value = match.group(2).strip()

            if not value:
                # Could be start of a list
                current_key = key
                current_list = []
                result[key] = current_list
            else:
                current_key = key
                current_list = None
                result[key] = _parse_scalar(value)
        # Handle continued list items
        elif stripped.startswith("- ") and current_key and current_list is not None:
            val = stripped[2:].strip()
            if val:
                current_list.append(_parse_scalar(val))

    return result


def _parse_scalar(value: str):
    """Parse a YAML scalar value."""
    # Remove quotes
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        return value[1:-1]

    # Inline list [a, b, c]
    if value.startswith("[") and value.endswith("]"):
        items = value[1:-1].split(",")
        return [_parse_scalar(i.strip()) for i in items if i.strip()]

    # Boolean
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False

    # Try number
    try:
        return int(value)
    except ValueError:
        pass
    # Don't parse floats — arxiv IDs like 2308.04079 must stay as strings

    return value


# ---------------------------------------------------------------------------
# Paper loading
# ---------------------------------------------------------------------------

def load_papers(papers_dir: Path) -> list[dict]:
    """Load all paper .md files and return list of metadata dicts."""
    papers = []
    for md_file in sorted(papers_dir.glob("*.md")):
        if md_file.name.startswith("_"):
            continue  # skip template

        text = md_file.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)

        if not meta:
            print(f"  WARN: {md_file.name} has no frontmatter, skipping")
            continue

        meta["_filename"] = md_file.stem
        meta["_path"] = f"papers/{md_file.name}"
        papers.append(meta)

    return papers


# ---------------------------------------------------------------------------
# Tag aggregation (with broad prefix matching)
# ---------------------------------------------------------------------------

TAG_NAMESPACES = ["inputs", "outputs", "methods", "benchmarks"]
NS_LABELS = {
    "inputs": "input",
    "outputs": "output",
    "methods": "method",
    "benchmarks": "benchmark",
}


def collect_tags(papers: list[dict]) -> dict[str, dict[str, list[dict]]]:
    """
    Collect fine-grained tags per namespace.
    Returns: {namespace: {tag: [paper_meta, ...]}}
    """
    tags = {ns: {} for ns in TAG_NAMESPACES}

    for paper in papers:
        for ns in TAG_NAMESPACES:
            for tag in paper.get(ns, []) or []:
                if not isinstance(tag, str) or not tag:
                    continue
                tags[ns].setdefault(tag, []).append(paper)

    return tags


def compute_broad_tags(fine_tags: dict[str, list[dict]]) -> dict[str, list[dict]]:
    """
    Derive broad tags from fine-grained tags via suffix matching.

    If fine tags include 'posed-multi-view-images' and 'unposed-multi-view-images',
    a broad tag 'multi-view-images' is created that aggregates both.

    Only creates broad tags when multiple fine tags share a suffix.
    """
    # Group fine tags by potential broad suffixes
    suffix_groups: dict[str, list[str]] = {}
    for tag in fine_tags:
        parts = tag.split("-")
        # Try removing 1-word prefix, 2-word prefix, etc.
        for i in range(1, len(parts)):
            suffix = "-".join(parts[i:])
            if len(suffix) > 2:  # meaningful suffix
                suffix_groups.setdefault(suffix, []).append(tag)

    broad = {}
    for suffix, fine_tag_list in suffix_groups.items():
        if len(fine_tag_list) > 1 and suffix not in fine_tags:
            # Aggregate papers from all matching fine tags (deduplicated)
            seen = set()
            papers = []
            for ft in fine_tag_list:
                for p in fine_tags[ft]:
                    pid = p["_filename"]
                    if pid not in seen:
                        seen.add(pid)
                        papers.append(p)
            broad[suffix] = papers

    return broad


def _format_date(date_val) -> str:
    d = str(date_val)
    if not d:
        return ""
    parts = d.split("-")
    if len(parts) >= 2 and len(parts[0]) == 4:
        return f"{parts[0][2:]}.{parts[1]}"
    return d


def _shorten_title(title: str) -> str:
    """Return the part of the title before a colon, if present."""
    if not title:
        return ""
    return title.split(":")[0].strip()


# ---------------------------------------------------------------------------
# INDEX.md generation
# ---------------------------------------------------------------------------

def generate_index(papers: list[dict], tags: dict, root_dir: Path):
    """Generate INDEX.md master table."""
    # Sort by date descending
    papers_sorted = sorted(
        papers,
        key=lambda p: str(p.get("date", "0000-00-00")),
        reverse=True,
    )

    # Count tags
    total_tags = sum(len(t) for t in tags.values())

    # Reading stats
    status_counts = {}
    for p in papers:
        s = p.get("status", "unknown")
        status_counts[s] = status_counts.get(s, 0) + 1

    stats_parts = [f"{len(papers)} papers"]
    for status_key, icon in [("read", "read"), ("skimmed", "skimmed"), ("to-read", "to-read")]:
        count = status_counts.get(status_key, 0)
        if count:
            stats_parts.append(f"{count} {status_key}")
    stats_parts.append(f"{total_tags} unique tags")

    lines = [
        "# Paper Index\n",
        f"*Auto-generated by `build_index.py` on {date.today()} -- do not edit manually.*\n",
        f"**Stats**: {' | '.join(stats_parts)}\n",
        "| Paper | Date | Status | Venue | Inputs | Outputs | Methods | Benchmarks | Code | Website | OpenReview |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]

    for p in papers_sorted:
        title = _shorten_title(p.get("title", p["_filename"]))
        d = _format_date(p.get("date", ""))
        status = _status_icon(p.get("status", ""))
        venue = p.get("venue", "")
        inputs = _tag_list(p.get("inputs"))
        outputs = _tag_list(p.get("outputs"))
        methods = _tag_list(p.get("methods"))
        benchmarks = _tag_list(p.get("benchmarks"))
        code = f"[✓]({p['code']})" if p.get("code") else ""
        website = f"[✓]({p['website']})" if p.get("website") else ""
        openreview = f"[✓]({p['openreview']})" if p.get("openreview") else ""

        lines.append(
            f"| [{title}]({p['_path']}) | {d} | {status} | {venue} "
            f"| {inputs} | {outputs} | {methods} | {benchmarks} | {code} | {website} | {openreview} |"
        )

    # Tag summary section
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Tags")
    lines.append("")

    for ns in TAG_NAMESPACES:
        label = NS_LABELS[ns]
        ns_tags = sorted(tags[ns].keys())
        if not ns_tags:
            continue
        lines.append(f"### {label.capitalize()}s")
        lines.append("")
        for tag in ns_tags:
            count = len(tags[ns][tag])
            lines.append(f"- [{tag}](tags/{label}--{tag}.md) ({count})")
        lines.append("")

    # Relationship graph
    graph_lines = _generate_relationship_graph(papers)
    if graph_lines:
        lines.append("---")
        lines.append("")
        lines.append("## Paper Relationships")
        lines.append("")
        lines.extend(graph_lines)
        lines.append("")

    index_path = root_dir / "INDEX.md"
    index_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  Generated {index_path}")


def _generate_relationship_graph(papers: list[dict]) -> list[str]:
    """Generate a Mermaid graph of paper relationships."""
    # Collect all edges
    edges = []
    paper_set = {p["_filename"] for p in papers}

    for p in papers:
        src = p["_filename"]
        # Short label: remove YYMM_ prefix for readability
        src_label = src[5:] if len(src) > 5 else src

        for rel in p.get("related", []) or []:
            if isinstance(rel, str) and rel:
                rel_label = rel[5:] if len(rel) > 5 else rel
                edges.append((src, src_label, rel, rel_label, "related"))

        for comp in p.get("compared", []) or []:
            if isinstance(comp, str) and comp:
                comp_label = comp[5:] if len(comp) > 5 else comp
                edges.append((src, src_label, comp, comp_label, "compared"))

    if not edges:
        return []

    lines = [
        "```mermaid",
        "graph LR",
    ]

    # Deduplicate nodes (use node IDs safe for Mermaid)
    seen_nodes = set()
    for src, src_label, tgt, tgt_label, _ in edges:
        src_id = src.replace("-", "_")
        tgt_id = tgt.replace("-", "_")
        if src_id not in seen_nodes:
            lines.append(f'    {src_id}["{src_label}"]')
            seen_nodes.add(src_id)
        if tgt_id not in seen_nodes:
            lines.append(f'    {tgt_id}["{tgt_label}"]')
            seen_nodes.add(tgt_id)

    # Deduplicate edges
    seen_edges = set()
    for src, _, tgt, _, rel_type in edges:
        src_id = src.replace("-", "_")
        tgt_id = tgt.replace("-", "_")
        edge_key = (src_id, tgt_id, rel_type)
        if edge_key in seen_edges:
            continue
        seen_edges.add(edge_key)

        if rel_type == "related":
            lines.append(f"    {src_id} --- {tgt_id}")
        else:
            lines.append(f"    {src_id} -.->|compared| {tgt_id}")

    lines.append("```")
    return lines


def _status_icon(status: str) -> str:
    return {"read": "✅", "skimmed": "👀", "to-read": "📋"}.get(status, status)


def _tag_list(tags) -> str:
    if not tags or not isinstance(tags, list):
        return ""
    return ", ".join(str(t) for t in tags if t)


# ---------------------------------------------------------------------------
# Tag pages generation
# ---------------------------------------------------------------------------

def generate_tag_pages(tags: dict, root_dir: Path):
    """Generate per-tag .md pages under tags/."""
    tags_dir = root_dir / "tags"
    tags_dir.mkdir(exist_ok=True)

    # Clean old tag pages
    for old in tags_dir.glob("*.md"):
        old.unlink()

    for ns in TAG_NAMESPACES:
        label = NS_LABELS[ns]
        fine_tags = tags[ns]

        # Generate fine-grained tag pages
        for tag, papers in sorted(fine_tags.items()):
            _write_tag_page(tags_dir, label, tag, papers, is_broad=False)

        # Generate broad aggregate tag pages
        broad = compute_broad_tags(fine_tags)
        for tag, papers in sorted(broad.items()):
            _write_tag_page(tags_dir, label, tag, papers, is_broad=True)


def _write_tag_page(tags_dir: Path, label: str, tag: str, papers: list[dict], is_broad: bool):
    """Write a single tag page."""
    filename = f"{label}--{tag}.md"
    broad_note = " (broad)" if is_broad else ""

    papers_sorted = sorted(
        papers,
        key=lambda p: str(p.get("date", "0000-00-00")),
        reverse=True,
    )

    lines = [
        f"# {label}: {tag}{broad_note}\n",
        f"*{len(papers)} papers*\n",
        "| Paper | Date | Venue |",
        "|---|---|---|",
    ]

    for p in papers_sorted:
        title = _shorten_title(p.get("title", p["_filename"]))
        d = _format_date(p.get("date", ""))
        venue = p.get("venue", "")
        lines.append(f"| [{title}](../{p['_path']}) | {d} | {venue} |")

    (tags_dir / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Resolve paths relative to this script
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    papers_dir = root_dir / "papers"

    if not papers_dir.exists():
        print(f"ERROR: papers directory not found at {papers_dir}")
        sys.exit(1)

    print("Loading papers...")
    papers = load_papers(papers_dir)
    print(f"  Found {len(papers)} papers")

    if not papers:
        print("  No papers found. Add papers to papers/ and re-run.")
        sys.exit(0)

    print("Collecting tags...")
    tags = collect_tags(papers)

    print("Generating INDEX.md...")
    generate_index(papers, tags, root_dir)

    print("Generating tag pages...")
    generate_tag_pages(tags, root_dir)

    tag_count = sum(len(t) for t in tags.values())
    print(f"\nDone! {len(papers)} papers, {tag_count} unique tags.")


if __name__ == "__main__":
    main()
