---
title: "OT-UVGS: Revisiting UV Mapping for Gaussian Splatting as a Capacity Allocation Problem"
date: 2026-04-21
arxiv: "2604.19127v1"
venue:
status: to-read

abstract: "UV-parameterized Gaussian Splatting (UVGS) maps an unstructured set of 3D Gaussians to a regular UV tensor, enabling compact storage and explicit control of representation capacity. Existing UVGS, however, uses a deterministic spherical pro- jection to assign Gaussians to UV locations. Because this mapping ignores the global Gaussian distribution, it often leaves many UV slots empty while causing frequent collisions in dense regions. We reinterpret UV mapping as a capacity-allocation problem under a fixed UV budget and propose OT-UVGS, a lightweight, separable one-dimensional optimal-transport-inspired mapping that globally couples assignments while preserving the original UVGS representation. The method is implemented with rank-based sorting, has O(N log N) complexity for N Gaussians, and can be used as a drop-in replacement for spherical UVGS. Across 184 object-centric scenes and the Mip-NeRF dataset, OT-UVGS consistently improves peak signal-to-noise ratio (PSNR), structural similarity (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS) under the same UV resolution and per-slot capacity (K=1). These gains are accompanied by substantially better UV utilization, including higher non-empty slot ratios, fewer collisions, and higher Gaussian retention. Our results show that revisiting the mapping alone can unlock a significant fraction of the latent capacity of UVGS."

website: https://orcid.org/0009-0005-4891-3487
code: 
openreview: 
issue: 36

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

# OT-UVGS: Revisiting UV Mapping for Gaussian Splatting as a Capacity Allocation Problem

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

![Figure](https://arxiv.org/html/2604.19127v1/figures/s2.png)

*(a) UVGS*

![Figure](https://arxiv.org/html/2604.19127v1/figures/ot2.png)

*(b) OT-UVGS*

![Figure](https://arxiv.org/html/2604.19127v1/figures/s4.png)

*(c) UVGS*

![Figure](https://arxiv.org/html/2604.19127v1/figures/ot4.png)

*(d) OT-UVGS*

![Figure](https://arxiv.org/html/2604.19127v1/figures/s6.png)

*(e) UVGS*

![Figure](https://arxiv.org/html/2604.19127v1/figures/ot6.png)

*(f) OT-UVGS*

![Figure](https://arxiv.org/html/2604.19127v1/figures/H1.png)

*(a) Scene A*

![Figure](https://arxiv.org/html/2604.19127v1/figures/H2.png)

*(b) Scene B*

![Figure](https://arxiv.org/html/2604.19127v1/figures/H3.png)

*(c) Scene C*

![Figure](https://arxiv.org/html/2604.19127v1/figures/H-ALL.png)

*(d) All scenes*

![Figure](https://arxiv.org/html/2604.19127v1/figures/k_sweep_gs_util.png)

*(a) Gaussian retention vs. KK*

![Figure](https://arxiv.org/html/2604.19127v1/figures/k_sweep_nonempty_ratio.png)

*(b) Non-empty UV ratio vs. KK*

![Figure](https://arxiv.org/html/2604.19127v1/figures/mip-s1.png)

*Figure 3: Full-scene qualitative comparison on a Mip-NeRF scene. Left column: spherical UVGS. Right column: OT-UVGS. OT-UVGS reduces missing regions and improves structural consistency across views under the same UV budget.*

## LLM Summary


