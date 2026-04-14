---
title: "GaussianVLM: Scene-centric 3D Vision-Language Models using Language-aligned Gaussian Splats for Embodied Reasoning and Beyond"
date: 2025-07-01
arxiv: "2507.00886"
venue:
status: to-read
authors:
  - Anna-Maria Halacheva
  - Jan-Nico Zaech
  - Xi Wang
  - Danda Pani Paudel
  - Luc Van Gool

abstract: "As multimodal language models advance, their application to 3D scene understanding is a fast-growing frontier, driving the development of 3D Vision-Language Models (VLMs). Current methods show strong dependence on object detectors, introducing processing bottlenecks and limitations in taxonomic flexibility. To address these limitations, we propose a scene-centric 3D VLM for 3D Gaussian splat scenes that employs language- and task-aware scene representations. Our approach directly embeds rich linguistic features into the 3D scene representation by associating language with each Gaussian primitive, achieving early modality alignment. To process the resulting dense representations, we introduce a dual sparsifier that distills them into compact, task-relevant tokens via task-guided and location-guided pathways, producing sparse, task-aware global and local scene tokens. Notably, we present the first Gaussian splatting-based VLM, leveraging photorealistic 3D representations derived from standard RGB images, demonstrating strong generalization: it improves performance of prior 3D VLM five folds, in out-of-the-domain settings."

website: https://insait-institute.github.io/gaussianvlm.github.io
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

![Figure](https://arxiv.org/html/2507.00886/x2.png)

*Figure 2: The GaussianVLM architecture processes a user task prompt (query and optional location) and a 3D scene (Gaussian Splat representation). A 3D vision module (SceneSplat Transformer) predicts per-Gaussian language features. These dense features are then sparsified by a dual sparsifier module. The decoder’s hidden states also inform the task-guided sparsifier. The dual sparsifier comprises: 1) a location-guided pathway that selects language features from Gaussians within a ROI around the task location, producing ROI tokens; and 2) a task-guided pathway that attends to dense scene tokens and SceneSplat decoder hidden states using task tokens (via cross-attention) to produce 128 task-selected scene tokens. The resulting sparse scene representation (ROI tokens + task-selected tokens), along with the task tokens, is input to an LLM for response generation.*

![Figure](https://arxiv.org/html/2507.00886/x3.png)

*Figure 3: Qualitative results on scene-centric tasks.*

![Figure](https://arxiv.org/html/2507.00886/x4.png)

*Figure 4: Qualitative results on object-centric tasks.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/GaussianVLM_v3_labels_dist_correct.png)

*Figure 5: Distribution of the questions on object counts, answered correctly by GaussianVLM. The distribution is according to object class labels. Overall, 254 questions answered correctly.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/LL3DA_v3_labels_dist_correct.png)

*Figure 6: Distribution of the questions on object counts, answered correctly by LL3DA. The distribution is according to object class labels. Overall, 44 questions answered correctly.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/GaussianVLMv3_labels_overlayed.png)

*Figure 7: Distribution of object count questions (correcly answered by GaussianVLM, vs all questions) according to object class labels.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/LL3DAv3_labels_overlayed.png)

*Figure 8: Distribution of object count questions (correcly answered by LL3DA, vs all questions) according to object class labels.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/v3_labels_dist_on_counts_True.png)

*Figure 9: Distribution of object count questions according to object count labels.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/GaussianVLMv3_labels_overlayed_on_counts_True.png)

*Figure 10: Distribution of object count questions (correcly answered by GaussianVLM, vs all questions) according to object count labels. Overall, 254 questions answered correctly. Logarithmic scaling for the distribution.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/LL3DAv3_labels_overlayed_on_counts_True.png)

*Figure 11: Distribution of object count questions (correcly answered by LL3DA, vs all questions) according to object count labels. Overall, 44 questions answered correctly. Logarithmic scaling for the distribution.*

## My Notes

