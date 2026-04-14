# Gaussian Splat Papers Knowledge Base

A structured, LLM-friendly knowledge base for Gaussian Splatting research papers.

## Why

- **LLM-native**: Every paper is a self-contained `.md` file with YAML frontmatter — feed directly into any LLM as context
- **Git-synced**: Private GitHub repo, works from any machine, no Notion dependency
- **Filterable**: Tag-based system for inputs, outputs, methods, and benchmarks

## Quick Start

### Adding a paper

**Automatic** (from arXiv ID):

```bash
python scripts/add_paper.py 2308.04079
python scripts/add_paper.py 2308.04079 --name 3d-gaussian-splatting --summary
```

**Manual**:

1. Copy `papers/_template.md` → `papers/YYMM_paper-name.md`
2. Fill in the YAML frontmatter (title, date, arxiv ID, tags, etc.)
3. Write or paste the `## LLM Summary` section
4. Add your notes under `## My Notes`
5. Run `python scripts/build_index.py` to regenerate the index

### File naming

Use `YYMM_kebab-case-short-title.md` — the `YYMM` prefix matches arXiv's submission month:

```
2308_3d-gaussian-splatting.md     ← arXiv 2308.04079
2311_mip-splatting.md             ← arXiv 2311.16493
2403_2d-gaussian-splatting.md     ← arXiv 2403.17888
```

### Feeding to an LLM

```bash
# Feed everything (small KB, ≤50 papers)
cat papers/*.md | llm "Compare regularization approaches in 3DGS papers..."

# Feed the index first, then drill down
cat INDEX.md | llm "Which papers handle single-image input?"

# Feed a filtered subset
python scripts/query.py --input multi-view-images --method 3dgs
python scripts/query.py --status read --benchmark mipnerf360
python scripts/query.py --author Kerbl --list
```

## Schema

Each paper file has **YAML frontmatter** for structured metadata and a **markdown body** for content.

### Required fields

| Field | Type | Example |
|---|---|---|
| `title` | string | `"3D Gaussian Splatting for Real-Time Radiance Field Rendering"` |
| `date` | date | `2023-08-08` |
| `arxiv` | string | `"2308.04079"` (quoted — prevents YAML float parsing) |
| `status` | enum | `read`, `skimmed`, or `to-read` |
| `inputs` | list | `[posed-multi-view-images, sfm-point-cloud]` |
| `outputs` | list | `[novel-view, 3d-gaussians]` |
| `methods` | list | `[3dgs, differentiable-rasterization]` |

### Optional fields

| Field | Type | Example |
|---|---|---|
| `authors` | list | `[Bernhard Kerbl, George Drettakis]` |
| `venue` | string | `SIGGRAPH 2023` |
| `website` | URL | `https://...` |
| `code` | URL | `https://github.com/...` |
| `benchmarks` | list | `[mipnerf360, tanks-and-temples]` |
| `related` | list | `[2311_mip-splatting]` (filenames without `.md`) |
| `compared` | list | `[2003_nerf, 2201_instant-ngp]` |

### Required sections

| Section | Purpose |
|---|---|
| `## LLM Summary` | LLM-generated paper summary (fixed heading for script targeting) |
| `## Results` | Benchmark results table (optional content) |
| `## My Notes` | Personal observations (optional but recommended) |

## Tag System

Tags are **fine-grained by default**, with **broad filtering via prefix matching**.

```
Fine tag:     posed-multi-view-images
Broad match:  *multi-view-images  →  matches both "posed-" and "unposed-"
```

Tags are **open-ended** — add new ones as needed. `build_index.py` discovers all tags dynamically.

See [INDEX.md](INDEX.md) for the full tag listing and paper relationship graph.

## Scripts

| Script | Purpose |
|---|---|
| `scripts/add_paper.py` | Creates a paper entry from an arXiv ID |
| `scripts/needs_metadata.py` | Lists papers missing metadata or a proper LLM Summary (`--json` for agent use) |
| `scripts/query.py` | Filters papers and outputs content for LLM piping |
| `scripts/build_index.py` | Generates `INDEX.md`, tag pages, and relationship graph |
| `scripts/validate.py` | Validates frontmatter schema with cross-reference checks |

```bash
# Add a paper from arXiv
python scripts/add_paper.py 2308.04079 --summary

# Query papers
python scripts/query.py --method 3dgs --status read
python scripts/query.py --input multi-view-images --list
python scripts/query.py --author Kerbl --count

# Validate all papers
python scripts/validate.py

# Rebuild index and tag pages
python scripts/build_index.py
```

## Directory Structure

```
splat_papers/
├── README.md
├── INDEX.md              # auto-generated (table + graph)
├── papers/
│   ├── _template.md
│   ├── YYMM_paper-name.md
│   └── figures/          # key architecture diagrams
├── tags/                 # auto-generated
│   ├── input--tag-name.md
│   ├── output--tag-name.md
│   ├── method--tag-name.md
│   └── benchmark--tag-name.md
├── scripts/
│   ├── add_paper.py
│   ├── query.py
│   ├── build_index.py
│   └── validate.py
└── .github/
    └── workflows/
        └── validate.yml  # CI: validate + index check
```
