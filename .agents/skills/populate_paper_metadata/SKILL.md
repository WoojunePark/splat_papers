---
name: "Populate Paper Metadata"
description: "How to automatically fill cross-references and generate LLM Summaries for a paper. Does NOT fill inputs/outputs/methods — those are human-only."
---

# Populate Paper Metadata

This skill instructs you on how to automatically populate the auto-fillable frontmatter fields (`benchmarks`, `related`, `compared`) of a newly added paper, and simultaneously generate a structured `## LLM Summary` section if needed.

> **Important:** `inputs`, `outputs`, and `methods` are **human-only fields**. They must be filled by a human who has actually read the paper (via the GitHub Issue ENGAGE workflow). **Do NOT auto-populate these fields**, even if you can infer plausible values from the abstract or paper content.

**Pre-requisite:** The paper must already have an entry scaffolded (e.g., via `add_paper.py`), and the target fields are currently empty (set to `-`) or the LLM Summary is missing/unstructured.

## Step 0: Find target papers

Run the following command to get a list of papers that need metadata or summaries:

```bash
python scripts/needs_metadata.py --json
```

Check the `meta_missing` and `summary_issue` fields to see exactly what needs to be filled for each paper.

## Step 1: Gather Information

To accurately categorize the paper, gather its context:

1. **Read the text:** Read the paper's `## LLM Summary` and `abstract:` from the markdown file.
2. **Fetch source:** For higher accuracy, you should fetch the arXiv abstract page via `https://arxiv.org/html/{arxiv_id}` or `https://arxiv.org/abs/{arxiv_id}`.
3. **Review existing tags:** Look at the `INDEX.md` or `tags/` folder to see what standard tags already exist. Try to reuse existing standard tags before inventing new ones (e.g., use `posed-multi-view-images` instead of `posed-images`).
4. **Identify papers:** Check the `INDEX.md` or list the `papers/` directory to identify the filenames of related or compared papers.

## Step 2: Determine Rules for Each Field

> **Human-only fields — do NOT fill:** `inputs`, `outputs`, `methods`.
> These must only be filled by a human who has read the paper. Leave them as empty placeholders (`- `).

### `benchmarks` ✅ auto-fillable

- **Definition:** Which datasets are used to evaluate the method?
- **Format:** List of kebab-case tags.
- **Examples:** `mipnerf360`, `tanks-and-temples`, `deep-blending`, `waymo`, `nerf-synthetic`.

### `related` ✅ auto-fillable

- **Definition:** Which existing papers in our knowledge base does this paper build upon, extend, or take direct inspiration from?
- **Format:** List of exact filenames **without the `.md` extension**.
- **Rule:** You MUST search the `papers/` directory. Only include a related paper if it already exists in our knowledge base.
- **Example:** `2308_3d-gaussian-splatting`

### `compared` ✅ auto-fillable

- **Definition:** Which prior works does this paper compare its results against?
- **Format:** List of exact filenames **without the `.md` extension**.
- **Rule:** You MUST search the `papers/` directory. Only include a paper if it already exists in our knowledge base.
- **Example:** `2003_nerf`, `2201_instant-ngp`

## Step 3: Write the LLM Summary

If the paper's `summary_issue` from Step 0 is not null (e.g. `empty` or `no-structure`), you must write or re-write the `## LLM Summary` section in the markdown body.

**Guidelines:**

- Write in **third person, technical tone**.
- Open with a one-sentence summary of the core contribution.
- List key contributions as bullet points with **bold labels**.
- Include quantitative results if notable (e.g., speed, PSNR).
- Target length: 100-200 words.
- *Must* end with: `> *Auto-generated summary. Do not edit manually.*`

## Step 4: Populate the File

Edit the paper's markdown file to replace the empty arrays with your findings and insert the `## LLM Summary`.

**Before:**

```yaml
inputs:
  - 

related:
  - 
```

```markdown
## LLM Summary

Abstract text here...
```

**After:**

```yaml
inputs:
  - posed-multi-view-images
  - sfm-point-cloud

related:
  - 2308_3d-gaussian-splatting
```

```markdown
## LLM Summary

This paper introduces a novel approach...
- **Core Algorithm**: Uses differentiable...
- **Performance**: Achieves 30 FPS at...

> *Auto-generated summary. Do not edit manually.*
```

*Note: Remove the empty `-` placeholder for fields you fill. Leave `inputs`, `outputs`, and `methods` as empty placeholders — they are filled exclusively by the human reader via the GitHub Issue workflow.*

## Step 5: Validate

After updating the file, run the validation and indexing scripts to ensure you didn't break the YAML schema or reference missing files.

```bash
python scripts/validate.py
python scripts/build_index.py
```
