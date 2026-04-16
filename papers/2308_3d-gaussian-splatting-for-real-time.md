---
title: "3D Gaussian Splatting for Real-Time Radiance Field Rendering"
date: 2023-08-08
arxiv: "2308.04079"
venue:
status: to-read
abstract: "Radiance Field methods have recently revolutionized novel-view synthesis of scenes captured with multiple photos or videos. However, achieving high visual quality still requires neural networks that are costly to train and render, while recent faster methods inevitably trade off speed for quality. For unbounded and complete scenes (rather than isolated objects) and 1080p resolution rendering, no current method can achieve real-time display rates. We introduce three key elements that allow us to achieve state-of-the-art visual quality while maintaining competitive training times and importantly allow high-quality real-time (&gt;= 30 fps) novel-view synthesis at 1080p resolution. First, starting from sparse points produced during camera calibration, we represent the scene with 3D Gaussians that preserve desirable properties of continuous volumetric radiance fields for scene optimization while avoiding unnecessary computation in empty space; Second, we perform interleaved optimization/density control of the 3D Gaussians, notably optimizing anisotropic covariance to achieve an accurate representation of the scene; Third, we develop a fast visibility-aware rendering algorithm that supports anisotropic splatting and both accelerates training and allows realtime rendering. We demonstrate state-of-the-art visual quality and real-time rendering on several established datasets."

website: https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting
code: https://github.com/graphdeco-inria/gaussian-splatting
openreview:

inputs:
  - posed-multi-view-images
  - point-cloud

outputs:
  - 3dgs
  
methods:
  
benchmarks:
  - 

related:
  - 

compared:
  - 
---

# 3D Gaussian Splatting for Real-Time Radiance Field Rendering

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

## LLM Summary

## Introduction

Neural Radiance Fields (NeRFs) have revolutionized the field of novel view synthesis by enabling photorealistic rendering from a set of input images. However, the computational demands of NeRFs have limited their practical application in real-time scenarios. The paper "3D Gaussian Splatting for Real-Time Radiance Field Rendering" introduces a groundbreaking approach that achieves real-time rendering speeds while maintaining high visual quality.

![Comparison of different radiance field methods showing rendering performance](https://paper-assets.alphaxiv.org/figures/2308.04079/img-0.jpeg)
*Figure 1: Comparison of different radiance field rendering methods. From left to right: InstantNGP, Plenoxels, Mip-NeRF360, 3D Gaussian Splatting (Ours) with two different training configurations, and Ground Truth. Note the significant frame rate advantages of the proposed method while maintaining high PSNR values.*

The work, conducted by researchers from Inria and Université Côte d'Azur in France, along with collaborators from the Max-Planck-Institut für Informatik in Germany, presents a novel representation based on 3D Gaussians that are rendered through a fast, differentiable splatting algorithm.

> *Auto-generated summary. Do not edit manually.*
