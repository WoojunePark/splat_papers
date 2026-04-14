---
title: "2D Gaussian Splatting for Geometrically Accurate Radiance Fields"
date: 2024-03-26
arxiv: "2403.17888"
venue:
status: to-read
authors:
  - Binbin Huang
  - Zehao Yu
  - Anpei Chen
  - Andreas Geiger
  - Shenghua Gao

abstract: "3D Gaussian Splatting (3DGS) has recently revolutionized radiance field reconstruction, achieving high quality novel view synthesis and fast rendering speed without baking. However, 3DGS fails to accurately represent surfaces due to the multi-view inconsistent nature of 3D Gaussians. We present 2D Gaussian Splatting (2DGS), a novel approach to model and reconstruct geometrically accurate radiance fields from multi-view images. Our key idea is to collapse the 3D volume into a set of 2D oriented planar Gaussian disks. Unlike 3D Gaussians, 2D Gaussians provide view-consistent geometry while modeling surfaces intrinsically. To accurately recover thin surfaces and achieve stable optimization, we introduce a perspective-correct 2D splatting process utilizing ray-splat intersection and rasterization. Additionally, we incorporate depth distortion and normal consistency terms to further enhance the quality of the reconstructions. We demonstrate that our differentiable renderer allows for noise-free and detailed geometry reconstruction while maintaining competitive appearance quality, fast training speed, and real-time rendering."

website: https://surfsplatting.github.io
code: https://github.com/autonomousvision/sdfstudio

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

![Figure](https://arxiv.org/html/2403.17888/x1.png)

*Figure 1. Our method, 2DGS, (a) optimizes a set of 2D oriented disks to represent and reconstruct a complex real-world scene from multi-view RGB images. These optimized 2D disks are tightly aligned to the surfaces. (b) With 2D Gaussian splatting, we allow real-time rendering of high quality novel view images with view consistent normals and depth maps. (c) Finally, our method provides detailed and noise-free triangle mesh reconstruction from the optimized 2D disks.*

![Figure](https://arxiv.org/html/2403.17888/extracted/6224839/figures/teaser2dgs.png)

*Figure 2. Comparison of 3DGS and 2DGS. 3DGS utilizes different intersection planes for value evaluation when viewing from different viewpoints, resulting in inconsistency. Our 2DGS provides multi-view consistent value evaluations.*

![Figure](https://arxiv.org/html/2403.17888/x2.png)

*Figure 3. Illustration of 2D Gaussian Splatting. 2D Gaussian Splats are elliptical disks characterized by a center point 𝐩ksubscript𝐩𝑘\mathbf{p}_{k}bold_p start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT, tangential vectors 𝐭usubscript𝐭𝑢\mathbf{t}_{u}bold_t start_POSTSUBSCRIPT italic_u end_POSTSUBSCRIPT and 𝐭vsubscript𝐭𝑣\mathbf{t}_{v}bold_t start_POSTSUBSCRIPT italic_v end_POSTSUBSCRIPT, and two scaling factors (susubscript𝑠𝑢s_{u}italic_s start_POSTSUBSCRIPT italic_u end_POSTSUBSCRIPT and svsubscript𝑠𝑣s_{v}italic_s start_POSTSUBSCRIPT italic_v end_POSTSUBSCRIPT) control the variance. Their elliptical projections are sampled through the ray-splat intersection ( Section 4.2) and accumulated via alpha-blending in image space. 2DGS reconstructs surface attributes such as colors, depths, and normals through gradient descent.*

![Figure](https://arxiv.org/html/2403.17888/x3.png)

*Figure 4. Visual comparisons (test-set view) between our method, 3DGS (Kerbl et al., 2023), and SuGaR (Guédon and Lepetit, 2023) using scenes from an real-world dataset (Barron et al., 2022b). Our method excels at synthesizing geometrically accurate radiance fields and surface reconstruction, outperforming 3DGS and SuGaR in capturing sharp edges and intricate details.*

![Figure](https://arxiv.org/html/2403.17888/extracted/6224839/figures/dtu.png)

*Figure 5. Qualitative comparison on the DTU benchmark (Jensen et al., 2014). Our 2DGS produces detailed and noise-free surfaces.*

![Figure](https://arxiv.org/html/2403.17888/x4.png)

*Figure 6. Qualitative studies for the regularization effects. From left to right – input image, surface normals without normal consistency, without depth distortion, and our full model. Disabling the normal consistency loss leads to noisy surface orientations; conversely, omitting depth distortion regularization results in blurred surface normals. The complete model, employing both regularizations, successfully captures sharp and flat features.*

![Figure](https://arxiv.org/html/2403.17888/x5.png)

*Figure 7. Visualization of a plane tiled by 2D Gaussians. Affine approximation (Zwicker et al., 2001b) adopted in 3DGS (Kerbl et al., 2023) causes perspective distortion and inaccurate depth, violating normal consistency.*

![Figure](https://arxiv.org/html/2403.17888/x6.png)

*(a) Ground-truth*

![Figure](https://arxiv.org/html/2403.17888/x7.png)

*(b) MipNeRF360 (Barron et al., 2022b), SSIM=0.813*

![Figure](https://arxiv.org/html/2403.17888/x12.png)

*Figure 9. Comparison of surface reconstruction using our 2DGS and 3DGS (Kerbl et al., 2023). Meshes are extracted by applying TSDF to the depth maps.*

## My Notes

