#!/usr/bin/env python3
"""
tag_utils.py -- Shared tag normalisation and fuzzy-correction utilities.

Used by sync_issues.py (incoming user tags from GitHub Issues) and any other
script that needs to canonicalise tag strings.

Tag format rule: lowercase kebab-case, e.g. ``posed-multi-view-images``.
  - All non-alphanumeric characters (spaces, underscores, dots, slashes…)
    are collapsed to a single hyphen.
  - Leading / trailing hyphens are stripped.
  - Empty strings and pure-punctuation inputs return ``""`` and are discarded.

Fuzzy correction:
  - Load known tags from all ``papers/YYMM_*.md`` frontmatter list fields.
  - For each incoming tag, if it doesn't exactly match a known tag, use
    ``difflib.get_close_matches`` to find the closest one above the threshold.
  - Corrections are logged so the caller can print them for the user.
"""

from __future__ import annotations

import difflib
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Normalisation
# ---------------------------------------------------------------------------

_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def normalize_tag(raw: str) -> str:
    """
    Convert any raw tag string to canonical lowercase kebab-case.

    Examples::

        "Multi_View"            -> "multi-view"
        "posed multi view imgs" -> "posed-multi-view-imgs"
        "3DGS"                  -> "3dgs"
        "  --3d-  "             -> "3d"
        ""                      -> ""
    """
    tag = raw.strip().lower()
    tag = _NON_ALNUM_RE.sub("-", tag)
    tag = tag.strip("-")
    return tag


# ---------------------------------------------------------------------------
# Known-tag loading
# ---------------------------------------------------------------------------

_TAG_FIELDS = ("inputs", "outputs", "methods", "benchmarks")

# Simple frontmatter list parser — avoids importing full yaml.
_FIELD_RE = re.compile(r"^([a-zA-Z_][a-zA-Z0-9_]*):\s*$")
_ITEM_RE  = re.compile(r"^\s{2,}-\s+(.+)")


def _iter_frontmatter_lists(text: str):
    """Yield (field_name, tag_value) pairs from a paper's YAML frontmatter."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return
    in_front = False
    current_field: str | None = None
    for line in lines[1:]:
        stripped = line.strip()
        if stripped == "---":
            if in_front:
                break
            in_front = True
            continue
        if not in_front:
            continue
        fm = _FIELD_RE.match(line)
        if fm:
            current_field = fm.group(1)
            continue
        im = _ITEM_RE.match(line)
        if im and current_field in _TAG_FIELDS:
            val = im.group(1).strip()
            if val:
                yield current_field, val


def load_known_tags(papers_dir: Path) -> dict[str, set[str]]:
    """
    Scan all ``papers/YYMM_*.md`` files and return a dict mapping each field
    name to the set of all existing canonical tags for that field.

    Tags are normalised before storage, so the returned sets contain only
    valid kebab-case strings.

    Example return value::

        {
          "inputs":  {"posed-multi-view-images", "video", ...},
          "outputs": {"novel-view", "3d-gaussians", ...},
          "methods": {"3dgs", "nerf", ...},
        }
    """
    known: dict[str, set[str]] = {f: set() for f in _TAG_FIELDS}
    for md_file in sorted(papers_dir.glob("*.md")):
        if md_file.name.startswith("_"):
            continue
        try:
            text = md_file.read_text(encoding="utf-8")
        except OSError:
            continue
        for field, raw_tag in _iter_frontmatter_lists(text):
            tag = normalize_tag(raw_tag)
            if tag:
                known[field].add(tag)
    return known


# ---------------------------------------------------------------------------
# Fuzzy correction
# ---------------------------------------------------------------------------

#: Similarity threshold — tags below this are left unchanged (we'd rather
#: keep an unknown tag than silently assign a wrong one).
FUZZY_CUTOFF = 0.82


def correct_tag(
    tag: str,
    known_tags: set[str],
    *,
    cutoff: float = FUZZY_CUTOFF,
) -> tuple[str, str | None]:
    """
    Return ``(final_tag, suggestion_or_None)``.

    - ``final_tag`` is always the normalised form of ``tag``.
    - If ``tag`` exactly matches a known tag, ``suggestion`` is ``None``
      (no correction needed).
    - If a close match is found above ``cutoff``, ``suggestion`` is the
      matched known tag and ``final_tag`` is that suggestion.
    - If no close match is found, ``suggestion`` is ``None`` and
      ``final_tag`` is the normalised original (kept as-is).

    The caller decides whether to print a notice about the correction.
    """
    normalised = normalize_tag(tag)
    if not normalised:
        return "", None

    if normalised in known_tags:
        return normalised, None  # exact match — no correction

    matches = difflib.get_close_matches(normalised, known_tags, n=1, cutoff=cutoff)
    if matches:
        suggestion = matches[0]
        return suggestion, suggestion  # (corrected_value, what_we_corrected_to)

    return normalised, None  # unknown but no close match — keep as-is


def correct_tags(
    tags: list[str],
    known: dict[str, set[str]],
    field: str,
    *,
    verbose: bool = True,
) -> list[str]:
    """
    Normalise and fuzzy-correct a list of raw tag strings for ``field``.

    Prints a notice for each correction when ``verbose=True``.
    Deduplicated; preserves order.
    """
    field_known = known.get(field, set())
    seen: set[str] = set()
    result: list[str] = []
    for raw in tags:
        final, corrected_to = correct_tag(raw, field_known)
        if not final:
            continue
        if corrected_to and verbose:
            original_norm = normalize_tag(raw)
            if original_norm != corrected_to:
                print(f"    [tag] '{original_norm}' → '{corrected_to}' (fuzzy-corrected from known tags)")
        if final not in seen:
            seen.add(final)
            result.append(final)
    return result


# ---------------------------------------------------------------------------
# CLI (quick diagnostic)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Quick test: python scripts/tag_utils.py [papers_dir]
    papers_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent / "papers"
    known = load_known_tags(papers_dir)
    total = sum(len(v) for v in known.values())
    print(f"Loaded {total} known tags from {papers_dir}")
    for field, tags in known.items():
        print(f"  {field}: {sorted(tags)}")

    print("\nTest normalisation:")
    samples = ["Multi_View", "posed multi view images", "3DGS", "  --bad--  ", "novel-view"]
    for s in samples:
        print(f"  {s!r:30s} → {normalize_tag(s)!r}")

    print("\nTest fuzzy correction:")
    test_cases = [
        ("inputs",  "posed_multi_view_images"),
        ("methods", "3d-gaussian-splating"),
        ("outputs", "novel_view"),
    ]
    for field, raw in test_cases:
        final, corr = correct_tag(raw, known.get(field, set()))
        status = f"corrected to '{final}'" if corr else f"kept as '{final}' (no close match)"
        print(f"  [{field}] {raw!r:35s} → {status}")
