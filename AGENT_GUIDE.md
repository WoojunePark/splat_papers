# Gaussian Splat Papers — Agent Guide

> **This file is for LLM agents.** For the human-facing guide, see [README.md](README.md).

This guide describes the full workflow of the `splat_papers` GTD-style knowledge base from an agent's perspective.

---

## System Overview

```
splat_papers/
├── papers/              # One .md file per paper (YAML frontmatter + body)
├── INDEX.md             # Auto-generated master table + tag graph
├── tags/                # Auto-generated per-tag pages
├── scripts/
│   ├── add_paper.py     # CAPTURE: scaffold .md + open GitHub Issue
│   ├── sync_issues.py   # INTEGRATE: sync closed issues → My Notes
│   ├── needs_metadata.py
│   ├── query.py
│   ├── build_index.py
│   └── validate.py
└── .github/workflows/
    ├── validate.yml     # CI: validate schema on push
    └── sync_issues.yml  # CI: auto-sync when inbox issue is closed
```

---

## Three-Phase GTD Workflow

### Phase 1 — CAPTURE

**Trigger:** User provides an arXiv ID.

**Action:** Run `add_paper.py`. This does everything in one command:
1. Fetches title, abstract, date, authors from arXiv.
2. Extracts `website` and `code` URLs from the abstract page + PDF.
3. Extracts top figures from the arXiv HTML version.
4. Writes `papers/YYMM_<name>.md` with all metadata.
5. Opens a GitHub Issue labeled `inbox` + `to-read` (requires `gh` CLI).
6. Stores the issue number in the paper's `issue:` frontmatter field.

```bash
# Standard usage (creates .md + GitHub Issue)
python scripts/add_paper.py 2308.04079

# With options
python scripts/add_paper.py 2308.04079 --name 3d-gaussian-splatting
python scripts/add_paper.py 2308.04079 --summary    # populate LLM Summary with abstract
python scripts/add_paper.py 2308.04079 --no-pdf     # skip PDF download (faster)
python scripts/add_paper.py 2308.04079 --no-issue   # skip issue creation
python scripts/add_paper.py 2308.04079 --force      # overwrite existing file
```

**Post-capture:** agent should also run `populate_paper_metadata` skill to fill tags.

---

### Phase 2 — ENGAGE

**This phase is entirely human-driven.** No agent action required.

The user reads the paper via the GitHub Issue on mobile:
- Issue body contains: abstract, links (arXiv / PDF / HTML / website / code), top 3 figures.
- User leaves comments with reading notes.
- User closes the issue when done reading.

---

### Phase 3 — INTEGRATE

**Trigger:** GitHub Issue labeled `inbox` is closed.

**Automatic path (GitHub Actions):**
The `sync_issues.yml` workflow fires automatically. It:
1. Reads all comments from the closed issue via GitHub REST API.
2. Finds the matching `papers/YYMM_*.md` by `issue:` frontmatter field.
3. Appends formatted comments to `## My Notes`.
4. Sets `status: read` in frontmatter.
5. Clears the `issue:` field.
6. Runs `validate.py` + `build_index.py`.
7. Commits and pushes back to `main`.

**Manual path (local CLI):**
```bash
python scripts/sync_issues.py            # sync all closed inbox issues
python scripts/sync_issues.py --dry-run  # preview without writing
python scripts/sync_issues.py --issue 42 # sync a specific issue
```

---

## Key Frontmatter Fields Reference

| Field | Type | Notes |
|---|---|---|
| `title` | string | Full paper title, quoted |
| `date` | date | arXiv submission date |
| `arxiv` | string | arXiv ID, quoted |
| `status` | enum | `to-read` → `skimmed` → `read` |
| `issue` | int | GitHub Issue number (cleared after sync) |
| `website` | URL | Project page |
| `code` | URL | GitHub/GitLab repository |
| `inputs` | list | What data goes in |
| `outputs` | list | What the method produces |
| `methods` | list | Core algorithms/techniques |
| `benchmarks` | list | Evaluation datasets |
| `related` | list | Filenames of related papers (no `.md`) |
| `compared` | list | Filenames of compared papers (no `.md`) |

---

## Common Agent Tasks

### "Add a new paper"
1. Run `python scripts/add_paper.py <arxiv_id>` → creates `.md` + GitHub Issue.
2. Run `populate_paper_metadata` skill to fill tags.
3. Run `python scripts/validate.py` + `python scripts/build_index.py`.

### "Populate metadata for untagged papers"
1. Run `python scripts/needs_metadata.py --json` to find papers needing attention.
2. Follow the `populate_paper_metadata` skill instructions.

### "Sync reading notes from closed issues"
1. Run `python scripts/sync_issues.py` (or let GitHub Actions do it automatically).

### "Query papers"
```bash
python scripts/query.py --method 3dgs --status read
python scripts/query.py --input multi-view-images --list
python scripts/query.py --author Kerbl
```

### "Summarize a specific paper"
1. Read `papers/YYMM_*.md` for existing summary.
2. Fetch ArXiv HTML: `https://arxiv.org/html/<arxiv_id>` via `read_url_content`.
3. Write `## LLM Summary` following guidelines in `paper_management` skill.

---

## Important Rules

- **Never commit PDFs** to the repo. Access them on-demand via `https://arxiv.org/pdf/<id>`.
- **Never clone code repos.** Read specific files via raw GitHub URLs.
- **Always run `validate.py` + `build_index.py`** after modifying any paper `.md`.
- **The `issue:` field is a sync key** — do not modify it manually unless you know what you are doing.
- **`gh` CLI must be installed and authenticated** for GitHub Issue creation and local sync to work. See `README.md` for setup instructions.
