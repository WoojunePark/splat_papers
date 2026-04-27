---
title: "MonoEM-GS: Monocular Expectation-Maximization Gaussian Splatting SLAM"
date: 2026-04-12
arxiv: "2604.10593v1"
venue:
status: to-read

abstract: "Feed-forward geometric foundation models can infer dense point clouds and camera motion directly from RGB streams, providing priors for monocular SLAM. However, their predictions are often view-dependent and noisy: geometry can vary across viewpoints and under image transformations, and local metric properties may drift between frames. We present MonoEM-GS, a monocular mapping pipeline that integrates such geometric predictions into a global Gaussian Splatting representation while explicitly addressing these inconsistencies. MonoEM-GS couples Gaussian Splatting with an Expectation--Maximization formulation to stabilize geometry, and employs ICP-based alignment for monocular pose estimation. Beyond geometry, MonoEM-GS parameterizes Gaussians with multi-modal features, enabling in-place open-set segmentation and other downstream queries directly on the reconstructed map. We evaluate MonoEM-GS on 7-Scenes, TUM RGB-D and Replica, and compare against recent baselines."

website: 
code: 
openreview: 
issue: 39

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

# MonoEM-GS: Monocular Expectation-Maximization Gaussian Splatting SLAM

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

![Figure](https://arxiv.org/html/2604.10593v1/images/logo2.jpg)

*Figure 1: MonoEM-GS constructs a map in which each Gaussian aggregates measurements over time. Despite contradictory point-cloud predictions at timestamps tt and t+1t{+}1, the Gaussians remain consistent, with only a single update step needed to incorporate new observations.*

![Figure](https://arxiv.org/html/2604.10593v1/images/pipeline.jpg)

*Figure 2: Single iteration of processing a new input image by MonoEM-GS. For each new RGB input, MapAnything [10] produces a dense point cloud prediction otNo^{N}_{t}. We align it with the new prediction for frame N-1: otN−1o^{N-1}_{t} using ICP [24, 3]. Since otN−1o^{N-1}_{t} and ot−1N−1o^{N-1}_{t-1} are created from the same frame at different timestamps, we employ the found correspondences between otN−1o^{N-1}_{t} and otNo^{N}_{t} to register otNo^{N}_{t} to ot−1N−1o^{N-1}_{t-1}. After the initial registration has been found, we perform colored ICP [23] alignment of otNo^{N}_{t} to the map and estimate the camera pose with respect to the map. The aligned prediction otNo^{N}_{t} is fused into the map and appended to the FIFO buffer.*

![Figure](https://arxiv.org/html/2604.10593v1/images/alignment.jpg)

*Figure 3: Views of the current prediction alignment with the map. View 1: misaligned current prediction otNo^{N}_{t}; View 2: predictions otN−1o^{N-1}_{t} and ot−1N−1o^{N-1}_{t-1} for the same buffered image at different timestamps; View 3: the found associations between otNo^{N}_{t} and ot−1N−1o^{N-1}_{t-1}; View 4: current prediction otNo^{N}_{t} aligned to the map.*

![Figure](https://arxiv.org/html/2604.10593v1/images/gs_mesh_features_black.jpg)

*Figure 4: Multi-domain scene reconstructions produced by MonoEM-GS. A: Gaussian Splatting created by the proposed approach; B: Mesh reconstructed from Gaussian centers and normals; C: DINOv3 [26] feature map; D: Open-set 3D semantic map.*

![Figure](https://arxiv.org/html/2604.10593v1/images/walls_comp_black.jpg)

*Figure 5: Qualitative comparison of VGGT-SLAM2 [16] (left) and MonoEM-GS (right) maps. A–A: VGGT-SLAM2 [16] point cloud and MonoEM-GS Gaussian centers on the TUM RGB-D [28] “desk2” sequence; B–B: VGGT-SLAM2 [16] point cloud and MonoEM-GS Gaussian centers on the 7-Scenes [6] “office” sequence; C–C: meshes reconstructed for both methods from the point clouds in B and B, respectively.*

![Figure](https://arxiv.org/html/2604.10593v1/images/reconstructions.jpg)

*Figure 6: Reconstructed Gaussians (upper row) and corresponding meshes (bottom row) created from the Gaussian centers and normals.*

![Figure](https://arxiv.org/html/2604.10593v1/images/semantic_gt_comparison.jpg)

*Figure 7: MonoEM-GS Gaussian centers colored by their predicted classes (right) and the nearest ground-truth points colored by their GT classes (left).*

## LLM Summary


