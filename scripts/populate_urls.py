import sys
from pathlib import Path
import re
import urllib.request
import urllib.error
from add_paper import (
    fetch_text, extract_links_from_arxiv_page, extract_links_from_pdf,
    classify_links, extract_github_from_website
)

def update_paper(filepath: Path):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse yaml block to find arxiv ID
    arxiv_match = re.search(r'^arxiv:\s*"?([\d\.v]+)"?', content, re.MULTILINE)
    if not arxiv_match:
        print(f"Skipping {filepath.name} (no arxiv ID found)")
        return

    arxiv_id = arxiv_match.group(1)
    
    # Check if code and website are already populated
    code_match = re.search(r'^code:[ \t]*(.*)$', content, re.MULTILINE)
    website_match = re.search(r'^website:[ \t]*(.*)$', content, re.MULTILINE)
    
    current_code = code_match.group(1).strip() if code_match else ""
    current_website = website_match.group(1).strip() if website_match else ""
    
    if current_code and current_website:
        print(f"Skipping {filepath.name} (code and website already present)")
        return

    print(f"\nProcessing {filepath.name} ({arxiv_id})")
    
    # Fetch html
    try:
        html = fetch_text(f"https://arxiv.org/abs/{arxiv_id}")
    except Exception as e:
        print(f"Failed to fetch arxiv html: {e}")
        return
        
    comments_urls, other_html_urls = extract_links_from_arxiv_page(html)
    pdf_links = extract_links_from_pdf(arxiv_id) and [] # optional, wait, let's include pdf links
    pdf_links = extract_links_from_pdf(arxiv_id)
    
    links = classify_links(comments_urls, other_html_urls, pdf_links)
    website = links["website"]
    code = links["code"]
    
    if website and not code:
        code = extract_github_from_website(website)
        
    updated = False
    
    new_content = content
    if not current_code and code:
        new_content = re.sub(r'^code:[ \t]*(.*)$', f'code: {code}', new_content, count=1, flags=re.MULTILINE)
        updated = True
        print(f"  -> Added code: {code}")
        
    if not current_website and website:
        new_content = re.sub(r'^website:[ \t]*(.*)$', f'website: {website}', new_content, count=1, flags=re.MULTILINE)
        updated = True
        print(f"  -> Added website: {website}")
        
    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

def main():
    root = Path(__file__).resolve().parent.parent
    papers_dir = root / 'papers'
    
    for filepath in papers_dir.glob('*.md'):
        if filepath.name.startswith('_'):
            continue
        update_paper(filepath)

if __name__ == "__main__":
    main()
