---
title: "REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting"
date: 2025-10-18
arxiv: "2510.16410"
venue:
status: to-read

abstract: "Bridging the gap between complex human instructions and precise 3D object grounding remains a significant challenge in vision and robotics. Existing 3D segmentation methods often struggle to interpret ambiguous, reasoning-based instructions, while 2D vision-language models that excel at such reasoning lack intrinsic 3D spatial understanding. In this paper, we introduce REALM, an innovative MLLM-agent framework that enables open-world reasoning-based segmentation without requiring extensive 3D-specific post-training. We perform segmentation directly on 3D Gaussian Splatting representations, capitalizing on their ability to render photorealistic novel views that are highly suitable for MLLM comprehension. As directly feeding one or more rendered views to the MLLM can lead to high sensitivity to viewpoint selection, we propose a novel Global-to-Local Spatial Grounding strategy. Specifically, multiple global views are first fed into the MLLM agent in parallel for coarse-level localization, aggregating responses to robustly identify the target object. Then, several close-up novel views of the object are synthesized to perform fine-grained local segmentation, yielding accurate and consistent 3D masks. Extensive experiments show that REALM achieves remarkable performance in interpreting both explicit and implicit instructions across LERF, 3D-OVS, and our newly introduced REALM3D benchmarks. Furthermore, our agent framework seamlessly supports a range of 3D interaction tasks, including object removal, replacement, and style transfer, demonstrating its practical utility and versatility. Project page: this https URL."

website: https://ChangyueShi.github.io/REALM
code: https://github.com/ChangyueShi/REALM-Code
openreview:
issue: 1

inputs:
  - posed-multi-view-images
  - text-prompt
outputs:
  - 3d-gaussians
  - semantic-segmentation
methods:
  - 3dgs
  - mllm
  - agent
benchmarks:
  - 

related:
  - 

compared:
  - 
---

# REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting

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

![Figure](https://arxiv.org/html/2510.16410v3/x1.png)

*Figure 1: We propose REALM, an MLLM-agent framework designed for open-world 3D reasoning segmentation and editing within 3D Gaussian Splatting (3DGS). REALM can perform reasoning over implicit instructions and accurately segment the target object. REALM also supports various 3D editing instructions, including object removal, replacement, and style transfer.*

![Figure](https://arxiv.org/html/2510.16410v3/x2.png)

*Figure 2: REALM vs. Direct Image Inputs. Feeding one or a few random rendered views into the MLLM makes the outcome highly sensitive to viewpoint selection.*

![Figure](https://arxiv.org/html/2510.16410v3/x3.png)

*Figure 3: Overview of REALM. Top: Global-to-Local Spatial Grounding (GLSpaG) pipline hierarchically aggregates the outputs of LMSeg agents from global context to local refinement. Bottom left: We optimize a 3D feature field from 2D SAM masks for 3D consistent identification. Bottom right: MLLM-based Visual Segmenter (LMSeg) performs image-level reasoning on one viewpoint and integrates identity information from the optimized feature field to determine the selected instance ID.*

![Figure](https://arxiv.org/html/2510.16410v3/x4.png)

*Figure 4: Global reasoning process. We visualize reasoning outputs of the MLLM for each global view.*

![Figure](https://arxiv.org/html/2510.16410v3/x5.png)

*Figure 5: Qualitative Results on the LERF Dataset. The results demonstrate the ability of REALM to handle complex and implicit language queries with accurate visual grounding.*

![Figure](https://arxiv.org/html/2510.16410v3/x6.png)

*Figure 6: Examples in REALM3D benchmark. We use MLLM [3] and SAM [21] to annotate over 1K prompt–mask pairs, enabling quantitative evaluation on implicit queries.*

![Figure](https://arxiv.org/html/2510.16410v3/x7.png)

*Figure 7: Language-driven 3D editing. Once the object is grounded, we can perform a wide range of 3D editing tasks.*

![Figure](https://arxiv.org/html/2510.16410v3/x8.png)

*Figure 8: Ablation study on GLSpaG. The local grounding stage refines the 3D segmentation results.*

## LLM Summary

**REALM** presents an MLLM-agent framework focusing on open-world 3D reasoning segmentation and editing directly over 3D Gaussian Splatting representations. Current AI approaches distinctly segregate 3D open-vocabulary models—which excel at explicit direct queries—and 2D MLLMs that excel at reasoning but lack 3D spatial awareness. To bridge this gap without demanding costly 3D-specific retraining, REALM leverages 3DGS's fast spatial rendering. To circumvent the sensitivity and constraints of rendering single views to MLLMs, it introduces a "Global-to-Local Spatial Grounding" strategy. It employs multiple distinct camera views to coarsely localize targets based on intricate, implicit instructions via voting, followed by synthesizing close-up local views for highly accurate 3D mask generation. Empowering 3D interactions, it effortlessly supports precise object removal, replacement, and scene styling based on profound natural language commands.

> *Auto-generated summary. Do not edit manually.*
