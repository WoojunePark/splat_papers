---
title: "GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning"
date: 2026-03-19
arxiv: "2603.19137"
venue:
status: to-read
authors:
  - Yiren Lu
  - Yi Du
  - Disheng Liu
  - Yunlai Zhou
  - Chen Wang
  - Yu Yin

abstract: "Effective embodied exploration requires agents to accumulate and retain spatial knowledge over time. However, existing scene representations, such as discrete scene graphs or static view-based snapshots, lack \textit{post-hoc re-observability}. If an initial observation misses a target, the resulting memory omission is often irrecoverable. To bridge this gap, we propose \textbf{GSMem}, a zero-shot embodied exploration and reasoning framework built upon 3D Gaussian Splatting (3DGS). By explicitly parameterizing continuous geometry and dense appearance, 3DGS serves as a persistent spatial memory that endows the agent with \textit{Spatial Recollection}: the ability to render photorealistic novel views from optimal, previously unoccupied viewpoints. To operationalize this, GSMem employs a retrieval mechanism that simultaneously leverages parallel object-level scene graphs and semantic-level language fields. This complementary design robustly localizes target regions, enabling the agent to ``hallucinate&#39;&#39; optimal views for high-fidelity Vision-Language Model (VLM) reasoning. Furthermore, we introduce a hybrid exploration strategy that combines VLM-driven semantic scoring with a 3DGS-based coverage objective, balancing task-aware exploration with geometric coverage. Extensive experiments on embodied question answering and lifelong navigation demonstrate the robustness and effectiveness of our framework"

website: https://vulab-ai.github.io/GSMem
code: 

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

## LLM Summary



## Results

<!-- Optional: structured benchmark results for cross-paper comparison -->
<!-- Example:
| Benchmark | PSNR | SSIM | LPIPS |
|---|---|---|---|
| mipnerf360 | 27.21 | 0.815 | 0.214 |
| tanks-and-temples | 23.14 | 0.841 | 0.183 |
-->

## Figures

![Figure](https://arxiv.org/html/2603.19137v1/x1.png)

*Figure 1: With GS-Mem, previously explored regions can be retrieved and re-observed directly from the 3DGS memory without physically navigating to them.*

![Figure](https://arxiv.org/html/2603.19137v1/x2.png)

*Figure 2: Demonstration of Multi-level Retrieval-Rendering. Given a task-related target, the agent retrieves ROIs based on object-level and semantic-level cues. Subsequent viewpoint selection and rendering enable the agent to re-observe these regions for further reasoning.*

![Figure](https://arxiv.org/html/2603.19137v1/x3.png)

*Figure 3: Demonstration of our Hybrid Exploration Strategy. When frontier observations do not contain sufficient task-related cues for the VLM to make a decision, we incorporate an information gain-based score to select the most informative frontier for further exploration.*

![Figure](https://arxiv.org/html/2603.19137v1/x4.png)

*Figure 4: Case analysis. We analyze several cases where scene-graph and view-based representations fail, and demonstrate the advantages of 3DGS-based memory. The images shown correspond to the views selected by the VLM for answering the questions. The examples (a-c) illustrate failures of the scene-graph detector, while the last example (d) highlights how optimal viewpoint rendering benefits the VLM’s reasoning.*

![Figure](https://arxiv.org/html/2603.19137v1/x5.png)

*Figure 5: Runtime analysis for real-world multi-process setup.*

## My Notes

