#!/usr/bin/env python3
"""
validate.py — Validates frontmatter schema for all paper .md files.

Usage:
    python scripts/validate.py
"""

import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# YAML parser (same as build_index.py — kept standalone for independence)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from markdown text."""
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
# Validation rules
# ---------------------------------------------------------------------------

REQUIRED_FIELDS = ["title", "date", "arxiv", "status", "inputs", "outputs", "methods"]
OPTIONAL_LIST_FIELDS = ["authors", "benchmarks", "related", "compared"]
VALID_STATUSES = {"read", "skimmed", "to-read"}
TAG_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$")
FILENAME_PATTERN = re.compile(r"^\d{4}_.+\.md$")
REQUIRED_SECTIONS = ["## LLM Summary"]


def validate_paper(filepath: Path, all_paper_stems: set[str] | None = None) -> list[str]:
    """Validate a single paper file. Returns list of error messages.

    Args:
        filepath: Path to the paper .md file.
        all_paper_stems: Set of all paper file stems (without .md) for cross-ref validation.
    """
    errors = []

    # Filename check
    if not FILENAME_PATTERN.match(filepath.name):
        errors.append(f"Filename '{filepath.name}' doesn't match YYMM_name.md pattern")

    text = filepath.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)

    if not meta:
        errors.append("No YAML frontmatter found")
        return errors

    # Required fields
    for field in REQUIRED_FIELDS:
        if field not in meta:
            errors.append(f"Missing required field: {field}")
        elif isinstance(meta[field], list) and not any(meta[field]):
            errors.append(f"Field '{field}' is an empty list")
        elif isinstance(meta[field], str) and not meta[field]:
            errors.append(f"Field '{field}' is empty")

    # Status validation
    status = meta.get("status", "")
    if status and status not in VALID_STATUSES:
        errors.append(f"Invalid status '{status}' — must be one of: {', '.join(VALID_STATUSES)}")

    # Tag format validation
    for ns in ["inputs", "outputs", "methods", "benchmarks"]:
        tags = meta.get(ns, [])
        if not isinstance(tags, list):
            continue
        for tag in tags:
            if isinstance(tag, str) and tag and not TAG_PATTERN.match(tag):
                errors.append(f"Tag '{tag}' in {ns} has invalid format (use kebab-case)")

    # ArXiv ID format
    arxiv = meta.get("arxiv", "")
    if arxiv and isinstance(arxiv, str):
        if not re.match(r"^\d{4}\.\d{4,5}(v\d+)?$", arxiv):
            errors.append(f"ArXiv ID '{arxiv}' doesn't match expected format (e.g., 2308.04079)")

    # Required sections in body
    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"Missing required section: {section}")

    # URL validation (basic)
    for url_field in ["website", "code"]:
        url = meta.get(url_field, "")
        if url and isinstance(url, str) and not url.startswith("http"):
            errors.append(f"Field '{url_field}' doesn't look like a URL: {url}")

    # Related/compared reference validation
    for ref_field in ["related", "compared"]:
        refs = meta.get(ref_field, [])
        if not isinstance(refs, list):
            continue
        for ref in refs:
            if isinstance(ref, str) and ref:
                if not re.match(r"^\d{4}_.+$", str(ref)):
                    errors.append(
                        f"Reference '{ref}' in {ref_field} doesn't match YYMM_name format"
                    )
                # Cross-reference: check that the referenced file exists
                elif all_paper_stems is not None and ref not in all_paper_stems:
                    errors.append(
                        f"Reference '{ref}' in {ref_field} not found in papers/"
                    )

    # Authors validation (warn if empty, but not required)
    authors = meta.get("authors", [])
    if isinstance(authors, list) and authors:
        for a in authors:
            if not isinstance(a, str) or not a.strip():
                errors.append("Empty author entry in authors list")

    return errors


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent
    papers_dir = root_dir / "papers"

    if not papers_dir.exists():
        print(f"ERROR: papers directory not found at {papers_dir}")
        sys.exit(1)

    md_files = sorted(
        f for f in papers_dir.glob("*.md") if not f.name.startswith("_")
    )

    if not md_files:
        print("No paper files found.")
        sys.exit(0)

    # Collect all paper stems for cross-reference validation
    all_paper_stems = {f.stem for f in md_files}

    total_errors = 0
    total_warnings = 0
    total_files = len(md_files)

    for md_file in md_files:
        errors = validate_paper(md_file, all_paper_stems)
        if errors:
            # Separate cross-ref warnings from hard errors
            hard_errors = [e for e in errors if "not found in papers/" not in e]
            xref_warnings = [e for e in errors if "not found in papers/" in e]

            if hard_errors:
                print(f"\nFAIL {md_file.name}")
                for err in hard_errors:
                    print(f"    ERROR: {err}")
                total_errors += len(hard_errors)

            if xref_warnings:
                if not hard_errors:
                    print(f"\nWARN {md_file.name}")
                for w in xref_warnings:
                    print(f"    XREF:  {w}")
                total_warnings += len(xref_warnings)

            if not hard_errors and not xref_warnings:
                print(f"OK   {md_file.name}")
        else:
            print(f"OK   {md_file.name}")

    print(f"\n{'='*50}")
    print(f"Validated {total_files} files -- {total_errors} errors, {total_warnings} cross-ref warnings")

    if total_errors > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
