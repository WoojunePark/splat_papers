---
title: "ReLaGS: Relational Language Gaussian Splatting"
date: 2026-03-18
arxiv: "2603.17605"
venue:
status: to-read
authors:
  - Yaxu Xie
  - Abdalla Arafa
  - Alireza Javanmardi
  - Christen Millerdurai
  - Jia Cheng Hu
  - Shaoxiang Wang
  - Alain Pagani
  - Didier Stricker

abstract: "Achieving unified 3D perception and reasoning across tasks such as segmentation, retrieval, and relation understanding remains challenging, as existing methods are either object-centric or rely on costly training for inter-object reasoning. We present a novel framework that constructs a hierarchical language-distilled Gaussian scene and its 3D semantic scene graph without scene-specific training. A Gaussian pruning mechanism refines scene geometry, while a robust multi-view language alignment strategy aggregates noisy 2D features into accurate 3D object embeddings. On top of this hierarchy, we build an open-vocabulary 3D scene graph with Vision Language derived annotations and Graph Neural Network-based relational reasoning. Our approach enables efficient and scalable open-vocabulary 3D reasoning by jointly modeling hierarchical semantics and inter/intra-object relationships, validated across tasks including open-vocabulary segmentation, scene graph generation, and relation-guided retrieval. Project page: this https URL"

website: https://dfki-av.github.io/ReLaGS
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

![Figure](https://arxiv.org/html/2603.17605v1/x2.png)

*Figure 2: ReLaGS Overview. Given a reconstructed Gaussian scene, redundant primitives are first pruned to improve geometric accuracy. Heuristic clustering under multi-level SAM supervision then forms a hierarchical scene structure, where each cluster is assigned a CLIP-based language feature with outlier rejection. Finally, open-vocabulary inter- and intra-object scene graphs are obtained either by lifting LLM-derived relations for semantic diversity or by using a pretrained graph network for efficient offline inference.*

![Figure](https://arxiv.org/html/2603.17605v1/x3.png)

*Figure 3: Illustration of proposed two improvement methods for hierarchical scene construction and two example scene graphs. (a): Low contribution Gaussian points (red) are removed to improve scene geometry. (b): Outlier features (e.g., due to occluded or inconsistent masks) are filtered before aggregation, producing a more coherent and consistent embedding for the target. (c): The spatial relationships are predicted by our GNN. (d): The more semantic-enriched relationship lifted with LLM, the root object is marked as -1.*

![Figure](https://arxiv.org/html/2603.17605v1/x4.png)

*Figure 4: Qualitative results of open vocabulary object segmentation. We show results on LERF dataset for segmentation mask on 2D view. With multi-hierarchy querying search and 3D scene graph for relation guidance, our method shows strong improvement against THGS.*

![Figure](https://arxiv.org/html/2603.17605v1/x5.png)

*Figure 5: Qualitative results on LERF, ScanNet++, ScanNet and 3D-OVS.*

![Figure](https://arxiv.org/html/2603.17605v1/x6.png)

*Figure 6: Visualization of multi-hierarchy scene reconstruction on LERF and 3D-OVS datasets.*

![Figure](https://arxiv.org/html/2603.17605v1/x7.png)

*Figure 7: Examples of our SoM+LLM scene graph annotation on 2D images from 3DSSG dataset.*

## My Notes

