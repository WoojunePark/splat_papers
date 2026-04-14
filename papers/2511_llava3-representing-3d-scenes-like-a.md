---
title: "LLaVA$^3$: Representing 3D Scenes like a Cubist Painter to Boost 3D Scene Understanding of VLMs"
date: 2025-11-20
arxiv: "2511.16454"
venue:
status: to-read
authors:
  - Doriand Petit
  - Steve Bourgeois
  - Vincent Gay-Bellile
  - Florian Chabot
  - Loïc Barthe

abstract: "Developing a multi-modal language model capable of understanding 3D scenes remains challenging due to the limited availability of 3D training data, in contrast to the abundance of 2D datasets used for vision-language models (VLM). As an alternative, we introduce LLaVA$^3$ (pronounced LLaVA-Cube), a novel method that improves the 3D scene understanding capabilities of VLM using only multi-view 2D images and without any fine-tuning. Inspired by Cubist painters, who represented multiple viewpoints of a 3D object within a single picture, we propose to describe the 3D scene for the VLM through omnidirectional visual representations of each object. These representations are derived from an intermediate multi-view 3D reconstruction of the scene. Extensive experiments on 3D VQA and 3D language grounding show that our approach outperforms previous 2D-based VLM solutions."

website: https://cea-list.github.io/LLaVA-Cube/
code: https://github.com/CEA-LIST/LLaVA-Cube/

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

![Figure](https://arxiv.org/html/2511.16454/x1.png)

*Figure 1: Overview of LLaVA3. We first reconstruct the 3D scene as a NeRF from multi-view images with an associated LLaVA feature field. We also derive a hierarchical 3D segmentation of our NeRF. For each object, we create an omni-directional visual-description as a set of tokens. After object re-ordering, we can finally feed them to the VLM for 3D interpretation.*

![Figure](https://arxiv.org/html/2511.16454/figures/exps.jpg)

*Figure 2: Qualitative performance of our method on 3D VQA and Grounding. By decomposing into objects the view-dependent features, our method avoids several very common issues in 3D VQA: (a) missing objects due to insufficient sampling, (b) weak inter-object spatial relationships, (c) loss of objects details and (d) bad multi-view understanding (i.e. relations between objects from different images). Our method can also perform grounding from different types of queries ((e),(f),(g),(h)).*

![Figure](https://arxiv.org/html/2511.16454/figures/sup-archi.jpg)

*Figure 3: Precise Architecture of the Feature Fields. NN stands for ”Normalization”.*

![Figure](https://arxiv.org/html/2511.16454/figures/sup-semseg.jpg)

*Figure 4: NeRF Semantic Segmentation Performance on Replica’s room0 scene.*

![Figure](https://arxiv.org/html/2511.16454/figures/sup-filtering.jpg)

*Figure 5: Examples of the Impact of Filtering on our segmentation.*

![Figure](https://arxiv.org/html/2511.16454/figures/sup-vqa1.jpg)

*Figure 6: Further Visual Question Answering Examples.*

![Figure](https://arxiv.org/html/2511.16454/figures/sup-donuts.jpg)

*Figure 7: Grounding and VQA example on the Donuts in-the-wild scene.*

![Figure](https://arxiv.org/html/2511.16454/figures/object-centric.jpg)

*Figure 8: Example of Object-centric VQA and sub-scale grounding.*

![Figure](https://arxiv.org/html/2511.16454/figures/sup-ovseg.jpg)

*Figure 9: Some Open-Vocabulary Segmentation examples on Replica’s room0, using the SAM and CLIP feature field.*

![Figure](https://arxiv.org/html/2511.16454/figures/sup-instance.jpg)

*Figure 10: Multi-Scale Instance Segmentation on ScanNet’s scene0086.*

## My Notes
