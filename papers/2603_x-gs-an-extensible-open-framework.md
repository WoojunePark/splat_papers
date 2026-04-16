---
title: "X-GS: An Extensible Open Framework for Perceiving and Thinking via 3D Gaussian Splatting"
date: 2026-03-10
arxiv: "2603.09632"
venue:
status: to-read

abstract: "3D Gaussian Splatting (3DGS) has emerged as a powerful technique for novel view synthesis, subsequently extending into numerous spatial AI applications. However, most existing 3DGS methods operate in isolation, focusing on specific domains such as pose-free 3DGS, online SLAM, and semantic enrichment. In this paper, we introduce X-GS, an extensible open framework consisting of two major components: the X-GS-Perceiver, which unifies a broad range of 3DGS techniques to enable real-time online SLAM and distill semantic features; and the X-GS-Thinker, which interfaces with downstream multimodal models. In our implementation of the Perceiver, we integrate various 3DGS methods through three novel mechanisms: an online Vector Quantization (VQ) module, a GPU-accelerated grid-sampling scheme, and a highly parallelized pipeline design. The Thinker accommodates vision-language models and utilizes the resulting 3D semantic Gaussians, enabling downstream applications such as object detection, caption generation, and potentially embodied tasks. Experimental results on real-world datasets demonstrate the efficiency and newly unlocked multimodal capabilities of the X-GS framework."

website: 
code: 
openreview:
issue: 16

inputs:
  - monocular-video
  - rgbd-video
outputs:
  - 3d-gaussians
methods:
  - 3dgs
  - slam
  - vlm
benchmarks:
  - 

related:
  - 

compared:
  - 
---

# X-GS: An Extensible Open Framework for Perceiving and Thinking via 3D Gaussian Splatting

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

![Figure](https://arxiv.org/html/2603.09632v2/x1.png)

*Figure 1: X-GS is an extensible open framework that unifies previously isolated domains in 3D-GS. X-GS-Perceiver achieves real-time 3DGS-based online SLAM with semantics using an online VQ module, GPU-accelerated grid-sampling, and highly parallelized scheduling. X-GS-Thinker bridges the resulting 3D semantic Gaussians with diverse downstream multimodal models and tasks.*

![Figure](https://arxiv.org/html/2603.09632v2/x2.png)

*Figure 2: Overview of the X-GS framework. X-GS-Perceiver synergizes a memory-efficient Vector Quantization (VQ) module, grid-based semantic supervision, and an asynchronous parallelized pipeline to perform SLAM and distill semantics simultaneously in an online fashion, executing in real time at ∼\sim15 FPS. As an open framework, it accommodates both RGB-only and RGB-D inputs, and can flexibly integrate various Vision Foundation Models (VFMs). Furthermore, the X-GS-Thinker component is extensible to different multimodal models, enabling a wide range of downstream tasks.*

![Figure](https://arxiv.org/html/2603.09632v2/x3.png)

*Figure 3: Qualitative results of X-GS on scene reconstruction and semantic distillation. From left to right: Ground Truth (GT) RGB, Rendered RGB, GT Semantic Map (from VFMs, SAM + CLIP), Rendered Semantic Map, and an open-vocabulary Object Detection example.*

![Figure](https://arxiv.org/html/2603.09632v2/x4.png)

*Figure 4: Qualitative results of X-GS using RGB-D inputs. Depth map is optional and not the required input by X-GS-Perceiver.*

![Figure](https://arxiv.org/html/2603.09632v2/x5.png)

*Figure 5: Qualitative results of X-GS for 3D scene caption generation. The VLM generates captions in a zero-shot setting by taking 3D semantic Gaussians as input. Note that only a portion of the generated content is shown.*

## LLM Summary

**X-GS** provides an extensible, unified framework aimed to bridge the distinct silos of 3DGS-based SLAM, unposed 3DGS, semantic enrichment, and continuous multimodal Vision-Language Model deployment. Within the perception stack, the "X-GS-Perceiver" utilizes online Vector Quantization (VQ) codebooks with Exponential Moving Average updates, GPU-bound grid-sampled target prefetching, and detached parallel worker threads. Together, they allow complex 3D tracking, geometric mapping, and dense semantic distillation to occur entirely in real-time from either monocular or RGB-D video streams. The framework's modular "X-GS-Thinker" component immediately taps into these natively generated continuous semantic 3DGS fields, connecting with generative or contrastive VLMs for promptable object detection, open-world 3D scene captioning, and embodied actions.

> *Auto-generated summary. Do not edit manually.*
