---
title: "3DTurboQuant: Training-Free Near-Optimal Quantization for 3D Reconstruction Models"
date: 2026-04-07
arxiv: "2604.05366v1"
venue:
status: to-read

abstract: "Every existing method for compressing 3D Gaussian Splatting, NeRF, or transformer-based 3D reconstructors requires learning a data-dependent codebook through per-scene fine-tuning. We show this is unnecessary. The parameter vectors that dominate storage in these models, 45-dimensional spherical harmonics in 3DGS and 1024-dimensional key-value vectors in DUSt3R, fall in a dimension range where a single random rotation transforms any input into coordinates with a known Beta distribution. This makes precomputed, data-independent Lloyd-Max quantization near-optimal, within a factor of 2.7 of the information-theoretic lower bound. We develop 3D, deriving (1) a dimension-dependent criterion that predicts which parameters can be quantized and at what bit-width before running any experiment, (2) norm-separation bounds connecting quantization MSE to rendering PSNR per scene, (3) an entry-grouping strategy extending rotation-based quantization to 2-dimensional hash grid features, and (4) a composable pruning-quantization pipeline with a closed-form compression ratio. On NeRF Synthetic, 3DTurboQuant compresses 3DGS by 3.5x with 0.02dB PSNR loss and DUSt3R KV caches by 7.9x with 39.7dB pointmap fidelity. No training, no codebook learning, no calibration data. Compression takes seconds. The code will be released (this https URL)"

website: 
code: https://github.com/JaeLee18/3DTurboQuant
openreview: 
issue: 25

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

# 3DTurboQuant: Training-Free Near-Optimal Quantization for 3D Reconstruction Models

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

![Figure](https://arxiv.org/html/2604.05366v1/static/browse/0.3.4/images/arxiv-logo-one-color-white.svg)

*Figure 1: Overview of 3DTurboQuant. Parameter vectors from any 3D reconstruction model are normalized, randomly rotated, and scalar-quantized using a precomputed codebook. The same algorithm applies across all three approaches. Only the dimension dd differs.*

![Figure](https://arxiv.org/html/2604.05366v1/figures/lego_gt.png)

*Figure 2: Qualitative results of 3DTurboQuant on 3DGS. Rendered images across bit widths b=1,2,3,4b=1,2,3,4 on the Lego (top) and Mic (bottom) scenes. Rightmost column: 10×\times amplified error map at b=1b=1 relative to the fp32 baseline. At b=3b=3, the renders are visually indistinguishable from the uncompressed model.*

![Figure](https://arxiv.org/html/2604.05366v1/figures/dust3r_input.png)

*Figure 3: DUSt3R KV cache quantization: depth map visualization. Predicted depth maps (turbo colormap) from DUSt3R ViT-Large with KV cache quantized at various bit widths. At b=4b=4 (7.9×\times KV compression, 39.7 dB pointmap PSNR), the depth structure is indistinguishable from the unquantized baseline.*

## LLM Summary


