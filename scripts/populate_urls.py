#!/usr/bin/env python3
"""
populate_urls.py — Backfill website, code, and openreview URLs for existing papers.

Iterates over all paper .md files that are missing one or more URL fields
(website, code, openreview) and attempts to fill them automatically:

- website / code: extracted from the arXiv abstract page and PDF annotations.
- openreview: looked up via the OpenReview search API using the paper title.

Usage:
    python scripts/populate_urls.py            # process all papers with missing URLs
    python scripts/populate_urls.py --no-pdf   # skip PDF link extraction (faster)
    python scripts/populate_urls.py --no-openreview  # skip OpenReview lookup
"""
import argparse
import sys
from pathlib import Path
import re

sys.path.insert(0, str(Path(__file__).resolve().parent))
from add_paper import (
    fetch_text, extract_links_from_arxiv_page, extract_links_from_pdf,
    classify_links, extract_github_from_website, extract_openreview_url,
)


def update_paper(filepath: Path, no_pdf: bool = False, no_openreview: bool = False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse YAML block to find arxiv ID and title
    arxiv_match = re.search(r'^arxiv:\s*"?([\d\.v]+)"?', content, re.MULTILINE)
    if not arxiv_match:
        print(f"Skipping {filepath.name} (no arxiv ID found)")
        return

    arxiv_id = arxiv_match.group(1)

    title_match = re.search(r'^title:\s*"?(.*?)"?\s*$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else ""

    # Check which fields are already populated
    code_match = re.search(r'^code:[ \t]*(.*)$', content, re.MULTILINE)
    website_match = re.search(r'^website:[ \t]*(.*)$', content, re.MULTILINE)
    openreview_match = re.search(r'^openreview:[ \t]*(.*)$', content, re.MULTILINE)

    current_code = code_match.group(1).strip() if code_match else ""
    current_website = website_match.group(1).strip() if website_match else ""
    current_openreview = openreview_match.group(1).strip() if openreview_match else None  # None = field absent

    needs_website_code = not current_code or not current_website
    needs_openreview = (not no_openreview) and (current_openreview is not None) and (not current_openreview)

    if not needs_website_code and not needs_openreview:
        print(f"Skipping {filepath.name} (all URL fields already populated)")
        return

    print(f"\nProcessing {filepath.name} ({arxiv_id})")

    new_content = content
    updated = False

    # ------------------------------------------------------------------
    # website / code from arXiv page + PDF
    # ------------------------------------------------------------------
    if needs_website_code:
        try:
            html = fetch_text(f"https://arxiv.org/abs/{arxiv_id}")
        except Exception as e:
            print(f"  Failed to fetch arXiv HTML: {e}")
            html = ""

        if html:
            comments_urls, other_html_urls = extract_links_from_arxiv_page(html)
            pdf_links = [] if no_pdf else extract_links_from_pdf(arxiv_id)
            links = classify_links(comments_urls, other_html_urls, pdf_links)
            website = links["website"]
            code = links["code"]

            if website and not code:
                code = extract_github_from_website(website)

            if not current_code and code:
                new_content = re.sub(r'^code:[ \t]*(.*)$', f'code: {code}', new_content, count=1, flags=re.MULTILINE)
                updated = True
                print(f"  -> Added code: {code}")

            if not current_website and website:
                new_content = re.sub(r'^website:[ \t]*(.*)$', f'website: {website}', new_content, count=1, flags=re.MULTILINE)
                updated = True
                print(f"  -> Added website: {website}")

    # ------------------------------------------------------------------
    # openreview from OpenReview search API
    # ------------------------------------------------------------------
    if needs_openreview and title:
        openreview_url = extract_openreview_url(title)
        if openreview_url:
            new_content = re.sub(
                r'^openreview:[ \t]*(.*)$',
                f'openreview: {openreview_url}',
                new_content, count=1, flags=re.MULTILINE,
            )
            updated = True
            print(f"  -> Added openreview: {openreview_url}")
        else:
            print("  -> openreview: not found on OpenReview")
    elif needs_openreview and not title:
        print("  -> openreview: skipped (no title found)")

    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)


def main():
    parser = argparse.ArgumentParser(
        description="Backfill website, code, and openreview URLs for existing papers."
    )
    parser.add_argument(
        "--no-pdf",
        action="store_true",
        help="Skip PDF link extraction (faster, less accurate for website/code)",
    )
    parser.add_argument(
        "--no-openreview",
        action="store_true",
        help="Skip OpenReview URL lookup",
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    papers_dir = root / 'papers'

    for filepath in sorted(papers_dir.glob('*.md')):
        if filepath.name.startswith('_'):
            continue
        update_paper(filepath, no_pdf=args.no_pdf, no_openreview=args.no_openreview)


if __name__ == "__main__":
    main()
