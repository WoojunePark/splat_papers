---
title: "E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes"
date: 2026-04-20
arxiv: "2604.17969v1"
venue:
status: to-read

abstract: "Visual search in 3D environments requires embodied agents to actively explore their surroundings and acquire task-relevant evidence. However, existing visual search and embodied AI benchmarks, including EQA, typically rely on static observations or constrained egocentric motion, and thus do not explicitly evaluate fine-grained viewpoint-dependent phenomena that arise under unrestricted 5-DoF viewpoint control in real-world 3D environments, such as visibility changes caused by vertical viewpoint shifts, revealing contents inside containers, and disambiguating object attributes that are only observable from specific angles. To address this limitation, we introduce {E3VS-Bench}, a benchmark for embodied 3D visual search where agents must control their viewpoints in 5-DoF to gather viewpoint-dependent evidence for question answering. E3VS-Bench consists of 99 high-fidelity 3D scenes reconstructed using 3D Gaussian Splatting and 2,014 question-driven episodes. 3D Gaussian Splatting enables photorealistic free-viewpoint rendering that preserves fine-grained visual details (e.g., small text and subtle attributes) often degraded in mesh-based simulators, thereby allowing the construction of questions that cannot be answered from a single view and instead require active inspection across viewpoints in 5-DoF. We evaluate multiple state-of-the-art VLMs and compare their performance with humans. Despite strong 2D reasoning ability, all models exhibit a substantial gap from humans, highlighting limitations in active perception and coherent viewpoint planning specifically under full 5-DoF viewpoint changes."

website: 
code: 
openreview: 
issue: 46

inputs:
  - 

outputs:
  - 

methods:
  - 

benchmarks:
  - 

related:
  - 

compared:
  - 
---

# E3VS-Bench: A Benchmark for Viewpoint-Dependent Active Perception in 3D Gaussian Splatting Scenes

## My Notes


## Results

<!-- Optional: structured benchmark results for cross-paper comparison -->
<!-- Example:
| Benchmark | PSNR | SSIM | LPIPS |
|---|---|---|---|
| mipnerf360 | 27.21 | 0.815 | 0.214 |
| tanks-and-temples | 23.14 | 0.841 | 0.183 |
-->

## Figures

![Figure](https://arxiv.org/html/2604.17969v1/x1.png)

*Figure 1: Overview of the proposed Embodied 3D Visual Search (E3VS) task. Unlike 2D visual search, E3VS requires an agent to actively control its 5-DoF viewpoint to resolve occlusions and acquire fine-grained visual evidence, such as the production area label on an egg carton.*

![Figure](https://arxiv.org/html/2604.17969v1/x2.png)

*Figure 2: Dataset construction pipeline for E3VS-Bench. The pipeline consists of five stages: (1) 3D scene curation from SceneSplat++ [ma2025scenesplat++], (2) QA generation using a VLM, (3) invalid QA filtering with human verification, (4) viewpoint labeling to identify answerable viewpoints, and (5) answerability filtering to remove questions solvable without viewpoint transitions.*

![Figure](https://arxiv.org/html/2604.17969v1/x3.png)

*Figure 3: Comparison of rendering quality between traditional mesh-based (ScanNet++) and 3D Gaussian Splatting (SceneSplat++). 3DGS preserves sharp textures for small text (e.g., "WHEY" label), which is crucial for viewpoint-dependent visual reasoning.*

![Figure](https://arxiv.org/html/2604.17969v1/x4.png)

*Figure 4: Dataset Distribution. Each figure represents (a) question category distribution of unique QA pairs classified by GPT 5.1. (b) scene type distribution. (c) action distribution. (d) the number of words in each question. (e) the number of words in each answer.*

![Figure](https://arxiv.org/html/2604.17969v1/x5.png)

*Figure 5: Examples of E3VS task defined in our dataset. Each example illustrates a distinct reasoning type that requires viewpoint control in reconstructed 3D environments.*

![Figure](https://arxiv.org/html/2604.17969v1/x6.png)

*Figure 6: Effect of the number of input frames on E3VS performance. While more frames do not significantly impact the VLM judge score, they consistently lead to more efficient navigation (fewer steps) and safer trajectories (lower collision rates).*

![Figure](https://arxiv.org/html/2604.17969v1/x7.png)

*Figure 7: Qualitative Results. The orange bars represent the predicted answers after visual search by Gemini 3.0 Flash, while the blue bars indicate the human performance results.*

![Figure](https://arxiv.org/html/2604.17969v1/x8.png)

*Figure 9: Qualitative examples of viewpoint filtering by the VLM. Accepted viewpoints are highlighted with green bounding boxes, while filtered viewpoints are highlighted with red bounding boxes.*

![Figure](https://arxiv.org/html/2604.17969v1/figures/samples_qa_generation.png)

*Figure 10: Examples of Generated Question-answer pairs by Gemini 2.5 Flash.*

![Figure](https://arxiv.org/html/2604.17969v1/x9.png)

*Figure 12: Qualitative results of the penetrated viewpoint filtering. Viewpoints are marked red if they are filtered out due to camera penetration through scene geometry (e.g., walls or objects). Otherwise, they are marked green to indicate valid initial viewpoints for E3VS.*

## LLM Summary


