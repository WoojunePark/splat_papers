---
name: "Paper Management"
description: "How to read, write, and maintain paper entries in the Gaussian Splat papers knowledge base."
---

# Paper Management Skill

This skill covers how to interact with the `splat_papers` knowledge base — reading existing entries, creating new ones, and accessing external paper content (PDFs, code) without storing them locally.

## Knowledge Base Structure

```
splat_papers/
├── README.md                  # Human-facing guide
├── AGENT_GUIDE.md             # LLM agent guide (GTD workflow + field reference)
├── papers/
│   ├── _template.md          # Copy this to create new entries
│   ├── YYMM_paper-name.md    # One file per paper
│   └── figures/              # Key architecture diagrams
├── INDEX.md                   # Auto-generated master table + relationship graph
├── tags/                      # Auto-generated tag pages
└── scripts/
    ├── add_paper.py           # CAPTURE: Creates entry from arXiv ID + opens GitHub Issue
    ├── sync_issues.py         # INTEGRATE: Syncs closed issues → ## My Notes
    ├── query.py               # Filters papers for LLM piping
    ├── build_index.py         # Regenerates INDEX.md + tag pages
    └── validate.py            # Checks frontmatter schema + cross-refs
```

## Reading Papers

### Step 1: Find relevant papers

1. Read `INDEX.md` for the full paper listing with tags, stats, and relationship graph.
2. To filter by tag, read the appropriate file under `tags/` (e.g., `tags/input--posed-multi-view-images.md`).
3. Broad filtering: tag pages with shared suffixes aggregate fine-grained variants (e.g., `tags/input--multi-view-images.md` aggregates both `posed-` and `unposed-` variants).
4. Use `query.py` for programmatic filtering:

   ```bash
   python scripts/query.py --input multi-view-images --method 3dgs
   python scripts/query.py --status read --list
   python scripts/query.py --author Kerbl --benchmark mipnerf360
   ```

### Step 2: Read paper entries

Each `papers/YYMM_*.md` file is self-contained with:

- **YAML frontmatter**: structured metadata (title, date, arxiv ID, tags, etc.)
- **`## My Notes`**: the user's personal observations
- **`## LLM Summary`**: concise technical summary of the paper
- **`## Results`**: structured benchmark results table (PSNR, SSIM, LPIPS)
- **`## Figures`**: key architecture diagrams

### Step 3: Access full paper content (when the entry is not enough)

The knowledge base does **NOT** store PDFs or code. Access them on-demand:

#### Reading paper content

Try these sources **in order** — stop as soon as you have enough information:

1. **ArXiv HTML** (preferred — directly readable):

   ```
   https://arxiv.org/html/{arxiv_id}
   ```

   Example: `https://arxiv.org/html/2308.04079`
   Use `read_url_content` to fetch. Most recent papers have HTML versions.

2. **ArXiv abstract page** (fallback — always available):

   ```
   https://arxiv.org/abs/{arxiv_id}
   ```

   Contains the abstract, author list, and submission history.

3. **Project website** (if `website:` field exists in frontmatter):
   Often has method figures, result comparisons, and supplementary material.

4. **PDF download** (last resort — for deep reading):

   ```
   https://arxiv.org/pdf/{arxiv_id}
   ```

   Download to a temporary location if the agent needs to parse the actual PDF.
   Do NOT commit PDFs to the repository.

#### Reading code

The knowledge base stores only the code **URL** (the `code:` frontmatter field). Do NOT clone repositories.

To inspect code on-demand:

1. **Browse repo structure** — read the GitHub page or API:

   ```
   https://github.com/{owner}/{repo}
   ```

2. **Read specific files** — use raw GitHub URLs:

   ```
   https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}
   ```

   Example: `https://raw.githubusercontent.com/graphdeco-inria/gaussian-splatting/main/scene/gaussian_model.py`

3. **Search within a repo** — use GitHub search:

   ```
   https://github.com/{owner}/{repo}/search?q={query}
   ```

Only fetch the specific files relevant to the question. Never clone the full repo.

## Writing New Paper Entries

### Option A: Automatic (from arXiv ID)

Use `add_paper.py` to scaffold an entry automatically:

```bash
python scripts/add_paper.py 2308.04079
python scripts/add_paper.py 2308.04079 --name 3d-gaussian-splatting --summary
python scripts/add_paper.py 2308.04079 --no-pdf   # skip PDF download (faster)
```

This fetches title and date from arXiv. It also **automatically extracts `website` and `code` URLs** by:
1. Parsing the arXiv abstract-page HTML — the "Comments" field often contains explicit project/code links.
2. Downloading the PDF and extracting all hyperlink annotations (requires `pip install pypdf`).

URLs are classified heuristically — GitHub/GitLab repos become `code:`, `*.github.io` pages become `website:`, and high-scoring unknown URLs get promoted to `website:`. You may still need to correct or fill in missing links manually.

Use `--no-pdf` to skip the PDF download if you want faster scaffolding and don't mind filling in links yourself.

You still need to fill in tags, venue, and refine the summary.

**ArXiv versioning**: Passing a bare ID (e.g. `2308.04079`) always fetches the **latest version** — ArXiv redirects automatically. Pass an explicit suffix (e.g. `2308.04079v1`) only if you need a specific older version. The script accepts both formats.

### Option B: Manual (from template)

Copy the template and name it following the `YYMM_kebab-case-name.md` convention:

```
papers/_template.md  →  papers/YYMM_paper-name.md
```

- `YYMM` = the ArXiv publication year-month (e.g., `2308` for August 2023)
- `paper-name` = short, recognizable kebab-case name

### Fill frontmatter

#### Required fields

| Field | Format | Example |
|---|---|---|
| `title` | Full paper title in quotes | `"3D Gaussian Splatting for..."` |
| `date` | arXiv publication date (`YYYY-MM-DD`) | `2023-08-08` |
| `arxiv` | ArXiv ID in quotes (prevents YAML float parsing) | `"2308.04079"` |
| `status` | One of: `read`, `skimmed`, `to-read` | `read` |
| `inputs` | List of kebab-case tags | `[posed-multi-view-images]` |
| `outputs` | List of kebab-case tags | `[novel-view, 3d-gaussians]` |
| `methods` | List of kebab-case tags | `[3dgs, mipmap]` |

#### Optional fields

| Field | Format | Notes |
|---|---|---|
| `abstract` | Quoted string | **Verbatim abstract from the paper** — copied exactly as written by the authors, not paraphrased |
| `venue` | Free text | `SIGGRAPH 2023`, `CVPR 2024` |
| `website` | URL | Project page |
| `code` | URL | GitHub / code repository |
| `benchmarks` | List of tags | Datasets used for evaluation |
| `related` | List of filenames (no `.md`) | Papers building on similar ideas |
| `compared` | List of filenames (no `.md`) | Papers compared against in experiments |

### Write sections

#### `## My Notes`

The user's personal observations — leave empty if unknown to the agent.

#### `## LLM Summary`

This section uses a **fixed heading** (`## LLM Summary`) so scripts can target it.

> **`abstract` vs `## LLM Summary`**: These are distinct and must not be confused.
> - `abstract` (frontmatter field) — the **verbatim abstract text as written by the paper's authors**. Copy it exactly from the ArXiv abstract page or paper PDF. Do not paraphrase.
> - `## LLM Summary` (body section) — an **LLM-generated technical summary** written in third person with structured bullet points. This is the agent's interpretation and analysis of the paper, not the authors' words.

Guidelines:

- Write in **third person, technical tone**
- Open with a one-sentence summary of the core contribution
- List key contributions as bullet points with **bold labels**
- Include quantitative results if notable (e.g., "achieves 30 fps at 1080p")
- Typical length: 100-200 words
- Mark with: `> *Auto-generated summary. Do not edit manually.*` if LLM-generated

#### `## Results`

Structured benchmark results table for cross-paper comparison:

```markdown
| Benchmark | PSNR | SSIM | LPIPS |
|---|---|---|---|
| mipnerf360 | 27.21 | 0.815 | 0.214 |
| tanks-and-temples | 23.14 | 0.841 | 0.183 |
```

#### `## Figures`

Section for embedded diagrams and architecture plots. See "Key figures" below for details on how to store and format these.

### Validate and rebuild index

```bash
python scripts/validate.py        # Check frontmatter schema + cross-refs
python scripts/build_index.py     # Regenerate INDEX.md + tag pages + graph
```

Always run both after adding or modifying papers.

## Key figures

Store one architecture/method diagram per paper in `papers/figures/`:

- Naming: `YYMM_paper-name.png` (matches the paper filename)
- Reference from paper entry: `![Architecture](figures/YYMM_paper-name.png)`
- Do NOT store full PDFs — only key diagrams

## Tag Conventions

### Canonical format: lowercase kebab-case

All tags **must** be lowercase kebab-case:

| ✅ Correct | ❌ Wrong | Rule |
|---|---|---|
| `multi-view-images` | `multi_view_images` | underscores → hyphens |
| `multi-view-images` | `Multi View Images` | spaces → hyphens, lowercase |
| `3dgs` | `3DGS` | always lowercase |
| `posed-multi-view-images` | `posedMultiViewImages` | no camelCase |

### Auto-normalisation (sync_issues.py)

When tags come in via GitHub Issue comments, `sync_issues.py` **automatically normalises** them:
- `Multi_View` → `multi-view`
- `3DGS` → `3dgs`
- `posed multi view images` → `posed-multi-view-images`

You do **not** need to worry about casing or separator style when writing comments on mobile.

### Fuzzy correction

After normalisation, `sync_issues.py` fuzzy-matches each tag against all existing tags in the corpus (using `difflib`). If a close match is found (≥ 82% similarity), the tag is silently corrected and a note is printed:

```
[tag] 'posed-multi-view-image' → 'posed-multi-view-images' (fuzzy-corrected from known tags)
```

If no close match exists, the tag is kept as-is (new tags are always welcome).

### validate.py hints

If a malformed tag slips into a `.md` file, `validate.py` shows a suggestion:

```
ERROR: Tag 'multi_view' in inputs has invalid format (use kebab-case) → did you mean 'multi-view'?
```

### Other tag rules

- Tags are **open-ended** — add new tags freely; `build_index.py` discovers them dynamically
- Use **fine-grained tags** by default; broad filtering is handled automatically via prefix matching
  - Fine: `posed-multi-view-images`, `unposed-multi-view-images`
  - Broad: `*multi-view-images` matches both
- Check existing tags in `INDEX.md` before creating duplicates

## Common Tasks

### "Add a paper to the GTD inbox" (Capture → Engage → Integrate)

The full three-phase workflow for adding and processing a new paper:

#### Phase 1 — CAPTURE (agent-driven)

Run `add_paper.py` to scaffold the entry AND open a GitHub Issue in one step:

```bash
python scripts/add_paper.py 2308.04079
# with options:
python scripts/add_paper.py 2308.04079 --name my-short-name --no-pdf
```

This will:
1. Create `papers/YYMM_<name>.md` with title, abstract, authors, extracted links, and top figures.
2. Open a GitHub Issue titled `[📥 Inbox] <Paper Title>` labeled `inbox` + `to-read`.
3. Store the issue number in the paper's `issue:` frontmatter field.

After running, also invoke the `populate_paper_metadata` skill to fill in tags.

If `gh` CLI is not installed, issue creation is skipped with a warning. See `README.md` for setup instructions.

#### Phase 2 — ENGAGE (human-driven, on GitHub mobile)

No agent action needed. The user opens the issue on mobile, reads the abstract/figures, leaves comments, and closes the issue when done.

The issue body contains a **Reading Notes Template**. Copy it into a comment and fill in the bullet lists to tag the paper on sync. Any text outside the structured sections becomes a `## My Notes` entry.

```markdown
## inputs
- posed-multi-view-images

## outputs
- novel-view
- 3d-gaussians

## methods
- 3dgs

These are my reading notes — goes to ## My Notes.
```

**Heading level and spelling are flexible:** `# input`, `## inputs`, `### methods`, etc. all work.

#### Phase 3 — INTEGRATE (automatic via GitHub Actions, or manual)

**Automatic:** GitHub Actions fires when the issue is closed and commits notes back to `main`.

**Manual (if Actions did not run):**
```bash
python scripts/sync_issues.py             # sync all closed inbox issues
python scripts/sync_issues.py --dry-run  # preview without writing
python scripts/sync_issues.py --issue 42 # sync a specific issue
```

This patches the `.md` file: appends formatted comments to `## My Notes`, sets `status: read`, clears `issue:`, and rebuilds the index.

---

### "Add LLM Summary for all papers without one"

Use this task to batch-write proper LLM Summaries for any paper entries that have an empty or abstract-only summary.

1. **Find papers that need a summary** — run the helper script and read its output:

   ```bash
   python scripts/needs_metadata.py --json
   ```

   The script scans every `papers/YYMM_*.md` and outputs **only** the papers that need attention as a JSON array:

   ```json
   [
     { "file": "2311_mip-splatting.md", "arxiv": "2311.16493", "reason": "summary (empty)", "meta_missing": [], "summary_issue": "empty" },
     { "file": "2403_2d-gaussian-splatting.md", "arxiv": "2403.17888", "reason": "summary (no-structure)", "meta_missing": [], "summary_issue": "no-structure" }
   ]
   ```

   Summary tracking reasons:
   - `"empty"` — `## LLM Summary` section has no content
   - `"no-structure"` — has text but no bold labels or bullet points (likely a raw abstract paste)

   If the output is empty, all papers are already covered — stop here.

2. **For each paper in the list**:

   a. Fetch the ArXiv HTML via `read_url_content` (preferred — most content):
      ```
      https://arxiv.org/html/{arxiv_id}
      ```
   b. If the HTML version doesn't exist (404 / no content), fall back:
      ```
      https://arxiv.org/abs/{arxiv_id}
      ```
   c. Write the `## LLM Summary` section in the paper's `.md` file following the guidelines below.
   d. End the summary with the auto-generated marker:
      ```
      > *Auto-generated summary. Do not edit manually.*
      ```

3. **Summary writing guidelines**:
   - Third person, technical tone
   - First sentence: core contribution in one sentence
   - Bullet points with **bold labels** for key contributions
   - Include notable quantitative results if available (e.g., speed, PSNR)
   - Target length: 100–200 words

4. **After updating all papers**:
   ```bash
   python scripts/validate.py
   python scripts/build_index.py
   ```

### "Summarize a paper I haven't read yet"

1. Check if `papers/YYMM_*.md` already exists.
2. If not, run `python scripts/add_paper.py {arxiv_id} --summary` to scaffold.
3. If more detail needed, fetch ArXiv HTML (`https://arxiv.org/html/{id}`) via `read_url_content`.
4. Fill in tags, venue, website, code URL.
5. Write or refine the `## LLM Summary` from the paper content.
6. Set `status: to-read` (user hasn't read it yet).
7. Run `validate.py` + `build_index.py`.

### "Compare papers on topic X"

1. Run `python scripts/query.py --method {tag} --list` to find papers.
2. Read the matched `papers/*.md` files.
3. Compare `## Results` tables for quantitative comparison.
4. If the entries lack sufficient detail, fetch ArXiv HTML for specific papers.
5. Synthesize a comparison from the combined context.

### "What does paper X's code do for Y?"

1. Read `papers/YYMM_*.md` to get the `code:` URL.
2. Browse the GitHub repo structure.
3. Fetch specific source files via raw GitHub URLs.
4. Never clone the repository.

### "What has author X published?"

1. Run `python scripts/query.py --author "Last Name" --list` to find papers.
2. Read matched entries for details.
