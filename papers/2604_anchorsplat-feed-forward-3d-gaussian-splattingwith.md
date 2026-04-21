---
title: "AnchorSplat: Feed-Forward 3D Gaussian SplattingWith 3D Geometric Priors"
date: 2026-04-08
arxiv: "2604.07053v1"
venue:
status: to-read

abstract: "Recent feed-forward Gaussian reconstruction models adopt a pixel-aligned formulation that maps each 2D pixel to a 3D Gaussian, entangling Gaussian representations tightly with the input images. In this paper, we propose AnchorSplat, a novel feed-forward 3DGS framework for scene-level reconstruction that represents the scene directly in 3D space. AnchorSplat introduces an anchor-aligned Gaussian representation guided by 3D geometric priors (e.g., sparse point clouds, voxels, or RGB-D point clouds), enabling a more geometry-aware renderable 3D Gaussians that is independent of image resolution and number of views. This design substantially reduces the number of required Gaussians, improving computational efficiency while enhancing reconstruction fidelity. Beyond the anchor-aligned design, we utilize a Gaussian Refiner to adjust the intermediate Gaussiansy via merely a few forward passes. Experiments on the ScanNet++ v2 NVS benchmark demonstrate the SOTA performance, outperforming previous methods with more view-consistent and substantially fewer Gaussian primitives."

website: 
code: 
openreview: 
issue: 20

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

# AnchorSplat: Feed-Forward 3D Gaussian SplattingWith 3D Geometric Priors

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

![Figure](https://arxiv.org/html/2604.07053v1/x1.png)

*Figure 1: Novel view synthesis comparison between AnySplat [16] and our AnchorSplat. AnySplat, as a voxel-aligned feed-forward approach, often suffers from inaccurate geometry, leading to ghosting artifacts, floaters, and blurred structures, especially in regions with sparse or ambiguous depth cues. In contrast, given the same sequence of input images, our anchor-aligned approach performs feed-forward Gaussian reconstruction using nearly 20× fewer Gaussians and about half the reconstruction time, while producing sharper geometry, cleaner surfaces, artifact-free renderings, and more accurate depth estimation.*

![Figure](https://arxiv.org/html/2604.07053v1/x2.png)

*Figure 2: Comparison of pixel-aligned and anchor-aligned Gaussian representations. Pixel-aligned Gaussians exhibit inconsistent sampling across views, especially under occlusions, low-texture regions, and motion parallax, while anchor-aligned Gaussians provide a more stable and consistent 3D representation.*

![Figure](https://arxiv.org/html/2604.07053v1/x3.png)

*Figure 3: Overview of the proposed AnchorSplat pipeline. The framework consists of three components: a pretrained Multi-View stereo module that extracts 3D geometric priors and depth maps from posed images, a transformer-based Gaussian decoder that predicts anchor-aligned Gaussians guided by these priors, and a lightweight Gaussian refiner that further refines Gaussian attributes to improve reconstruction quality and view consistency.*

![Figure](https://arxiv.org/html/2604.07053v1/x4.png)

*Figure 4: Comparison of reconstructed 3D Gaussians. Compared with AnySplat, our AnchorSplat produces cleaner and more geometry-consistent structures with far fewer Gaussians, reducing floaters, ghost artifacts, and irregular density distributions.*

![Figure](https://arxiv.org/html/2604.07053v1/x5.png)

*Figure 5: Reconstruction quality and runtime comparison between AnySplat and AnchorSplat across input-view settings. Dashed lines denote runtime, solid lines denote novel-view PSNR, and marker size with annotated numbers indicates the number of Gaussians (NumGS). AnchorSplat achieves better quality with lower runtime and fewer Gaussians.*

![Figure](https://arxiv.org/html/2604.07053v1/x6.png)

*Figure 6: Visual comparison before and after applying the Gaussian Refiner. The refiner improves boundary sharpness, fills missing regions, and enhances color consistency, leading to better overall rendering quality.*

![Figure](https://arxiv.org/html/2604.07053v1/x7.png)

*Figure 7: Comparison visualization. AnchorSplat produces noticeably higher-quality renderings with more accurate geometry and sharper depth, while avoiding the multi-view inconsistencies that often lead to artifacts such as ghosting and floaters. For example, in the first row, the chair region rendered by AnySplat exhibits clear view-dependent artifacts caused by inconsistent multi-view alignment, whereas our method maintains clean geometry and coherent appearance. Similar improvements can be observed across various scenes in the visualization, highlighting the robustness and reliability of our anchor-aligned Gaussian representation.*

![Figure](https://arxiv.org/html/2604.07053v1/x8.png)

*Figure 8: PCA visualization of three feature aggregations.*

![Figure](https://arxiv.org/html/2604.07053v1/x9.png)

*Figure 9: Comparison of reconstructed Gaussians between AnySplat and AnchorSplat*

![Figure](https://arxiv.org/html/2604.07053v1/x10.png)

*Figure 10: Comparison of rendered RGB images and depth images between AnySplat and AnchorSplat*

## LLM Summary

This report provides a detailed analysis of the research paper "AnchorSplat: Feed-Forward 3D Gaussian Splatting With 3D Geometric Priors."

---

## Research Paper Report: AnchorSplat: Feed-Forward 3D Gaussian Splatting With 3D Geometric Priors

### 1. Authors and Institution(s)

The authors of this paper are Xiaoxue Zhang, Xiaoxu Zheng, Yixuan Yin, Tiao Zhao, Kaihua Tang, Michael Bi, Mi Zhan, Xu, and Dave Zhenyu Chen. All authors are affiliated with Huawei Technologies Ltd.

### 2. How This Work Fits into the Broader Research Landscape

The field of 3D reconstruction and novel view synthesis has seen substantial advancements, particularly with the emergence of Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS). These methods excel at achieving high-fidelity scene representations, but typically rely on computationally intensive per-scene iterative optimization. This characteristic limits their applicability in real-time or large-scale scenarios and restricts generalization across different scenes.

To address the computational overhead and improve generalization, recent research has explored feed-forward 3DGS models. These models aim to directly predict 3D scene representations from input images in a single forward pass, enabling cross-scene generalization. However, many existing feed-forward approaches adopt a "pixel-aligned" formulation, where each 2D input pixel is mapped to a 3D Gaussian. This approach ties the Gaussian representation directly to image resolution and the number of input views, leading to several limitations. These include reliance on the accuracy of predicted depth maps, potential for geometric inaccuracies such as "floaters" or fragmented surfaces due to weak 3D interaction, redundancy in simple regions and insufficient coverage in complex areas, sensitivity to occlusions and low-texture regions, and limitations in generalizing to large-scale environments or extrapolating to unseen viewpoints.

AnchorSplat contributes to this landscape by proposing an alternative feed-forward 3DGS framework. It introduces an "anchor-aligned" Gaussian representation that is guided by 3D geometric priors, decoupling the Gaussian generation from individual input pixels. This design positions AnchorSplat as an advancement aimed at improving geometric consistency, reducing the number of required Gaussians, and enhancing computational efficiency compared to prior pixel-aligned or even some voxel-aligned feed-forward methods, while maintaining or improving reconstruction fidelity.

### 3. Key Objectives and Motivation

The primary objective of this research is to develop a novel feed-forward 3D Gaussian Splatting (3DGS) framework, termed AnchorSplat, for scene-level 3D reconstruction. This framework aims to generate a 3D scene representation directly in 3D space, rather than relying on pixel-aligned formulations that are inherently tied to 2D input images.

The motivations behind this objective stem from several limitations observed in existing 3D reconstruction methods:

1.  **Computational Inefficiency of Optimization-Based Methods:** Traditional high-fidelity 3D reconstruction techniques, such as NeRF and the original 3DGS, require extensive per-scene iterative optimization. This process is computationally expensive and hinders their deployment in applications requiring real-time performance or rapid scene processing.
2.  **Geometric Inaccuracies and Artifacts in Pixel-Aligned Feed-Forward Methods:** While feed-forward 3DGS models offer improved efficiency and generalization, their pixel-aligned nature leads to issues. The reliance on predicted depth maps or cost volumes can result in inaccurate geometry, often manifesting as "floaters" (isolated spurious Gaussians), fragmented surfaces, and inconsistent geometry across different views. This is partly due to limited interaction among neighboring points in 3D space during feature aggregation.
3.  **Redundancy and Inefficient Representation in 2D-Bound Formulations:** Pixel-aligned approaches inherently produce a number of Gaussians directly proportional to the total number of pixels across all input views (V × H × W). This leads to an excessive number of redundant Gaussians in homogeneous or plain regions, while potentially offering insufficient coverage in geometrically intricate areas. The representation remains bound to the 2D grid, which is inefficient for 3D scene representation.
4.  **Sensitivity to Input View Characteristics:** Pixel-aligned formulations are sensitive to factors like occlusions, low-texture environments, and motion parallax. These challenges can lead to inconsistent sampling patterns across different views, degrading reconstruction quality and view consistency.
5.  **Limited Scalability and Generalization:** Many existing feed-forward methods struggle with reconstructing large-scale environments or extrapolating to novel, unseen viewpoints due to their reliance on interpolating within limited view ranges.

AnchorSplat is motivated to address these issues by:
*   Introducing an "anchor-aligned" Gaussian representation guided by 3D geometric priors (e.g., sparse point clouds or voxels). This aims to create a more geometry-aware and compact representation independent of image resolution and the number of views.
*   Substantially reducing the number of required Gaussians, thereby improving computational efficiency and reducing reconstruction time.
*   Enhancing reconstruction fidelity, particularly in terms of sharper geometry, cleaner surfaces, and artifact-free renderings, by promoting cross-view consistency directly in 3D space.
*   Developing a plug-and-play Gaussian Refiner module to further improve Gaussian attributes and geometric consistency with minimal additional computational cost.

Ultimately, the goal is to provide a practical, efficient, and generalizable solution for high-fidelity 3D scene-level reconstruction that is robust to varying input conditions and capable of supporting downstream 3D applications.

### 4. Methodology and Approach

AnchorSplat is designed as a feed-forward 3DGS pipeline comprising three primary components: an Anchor Predictor, a Gaussian Decoder, and a Gaussian Refiner. The overall approach focuses on deriving a sparse, consistent, and geometry-aware 3D Gaussian representation from multi-view inputs.

**4.1. Anchor Predictor**
The process begins with the Anchor Predictor, which leverages a pretrained Multi-View Stereo (MVS) module (e.g., MapAnything). This module takes a set of unposed input images $\{I_i\}_{i=1}^V$ and estimates their corresponding depths $\{D_i\}_{i=1}^V$ and camera poses (intrinsics $K_i$ and extrinsics $P_i$). The predicted 2D depth maps are then back-projected into 3D world coordinates using the camera parameters, yielding a dense set of 3D points.

To address the redundancy inherent in pixel-aligned representations, where each pixel from every view typically generates a 3D point, the dense 3D points are then downsampled into a sparser set of 3D anchors, $\{A_j\}_{j=1}^N$. This downsampling is achieved using the farthest point sampling (FPS) algorithm, with the target number of anchors ($N$) determined by voxelizing the 3D space. This step is critical for transforming a view-dependent, pixel-aligned point cloud into a more compact and spatially consistent set of 3D anchors, where $N \ll H \times W \times V$.

**4.2. Gaussian Decoder**
The Gaussian Decoder is responsible for predicting 3D Gaussian attributes based on the generated 3D anchors and multi-view features.
1.  **Feature Extraction:** A lightweight 2D U-Net processes each input image $I_i$, its corresponding depth map $D_i$, and camera ray embeddings (derived from $K_i, R_i, T_i$) to extract multi-view features, $F_i$.
2.  **Anchor Feature Aggregation:** The 2D features $\{F_i\}_{i=1}^V$ are then projected onto the 3D geometry anchors $\{A_j\}_{j=1}^N$ using the depth and camera poses, creating C-dimensional "anchor features" $\{\tilde{A}_j\}_{j=1}^N$. For anchors receiving multiple feature projections from different views, these features are aggregated into a single anchor feature (e.g., using average pooling, after visibility and depth-consistency checks).
3.  **Gaussian Prediction:** A transformer-based Gaussian predictor processes these anchor features to model 3D spatial interactions among all anchors. Subsequently, a Multi-Layer Perceptron (MLP) predicts the attributes for four Gaussians per anchor. These attributes include an offset for the Gaussian center ($\delta\mu$), opacity ($\alpha$), scale ($s$), rotation ($r$), and spherical harmonic coefficients ($sh$) for color. The final absolute Gaussian centers are obtained by adding the predicted offset to the anchor position ($\mu_j = A_j + \delta\mu_j$), typically constrained to a small range around the anchor. This design yields a total of $4N$ Gaussians, where $N$ is the number of anchors.

**4.3. Gaussian Refiner**
The Gaussian Refiner is designed as a plug-and-play module to enhance the quality of the Gaussians predicted by the decoder. It operates by iteratively refining Gaussian attributes based on rendering errors.
1.  **Error Feature Extraction:** For each input view, the rendered image ($\hat{I}_i$) from the current Gaussians is compared against the ground-truth image ($I_i$). A pretrained ResNet-18 extracts multi-scale features from both $\hat{I}_i$ and $I_i$. These features are then concatenated and the per-view rendering error ($e_i$) is computed as the difference between the ground-truth and rendered features.
2.  **3D Error Back-Projection and Aggregation:** The 2D rendering errors $\{e_i\}_{i=1}^V$ are differentiably back-projected to the corresponding 3D Gaussian locations using the depth maps and camera poses, and then aggregated into a set of 3D error features $\{E_j\}_{j=1}^{4N}$.
3.  **Gaussian Attribute Update:** A transformer block captures spatial interactions among these 3D error features. Finally, a Point Transformer updates the Gaussian attributes ($\delta G_j$) by considering the current Gaussian attributes ($G_j$), the aggregated anchor features ($\hat{F}_j$), and the refined error features ($E_j$). The final updated Gaussians are obtained by adding these offsets to the current attributes ($\hat{G}_j = G_j + \delta G_j$). This module can be applied independently without retraining the full model.

**4.4. Training Objective**
The training of AnchorSplat proceeds in two stages:
1.  **Gaussian Decoder Training:** The decoder is trained using a composite loss function that includes:
    *   **Rendering Loss ($\ell_I$):** A combination of L1 loss, SSIM (Structural Similarity Index Measure), and LPIPS (Learned Perceptual Image Patch Similarity) between rendered and ground-truth images.
    *   **Depth Loss ($\ell_D$):** L1 loss between predicted and ground-truth depth maps.
    *   **Regularization Terms:** Opacity regularization ($\ell_\alpha$) to prevent Gaussians from becoming overly transparent and scale regularization ($\ell_s$) to prevent excessively large Gaussians.
2.  **Gaussian Refiner Training:** In the second stage, the Gaussian Decoder is frozen, and only the Gaussian Refiner is trained. The objective here is solely the rendering loss ($\ell_I$) between the refined rendered images and ground-truth images.

### 5. Main Findings and Results

The experiments were conducted primarily on the ScanNet++ V2 dataset, with additional ablations on ARKitScenes, Replica, and Tanks and Temples (T&T).

**5.1. Novel View Synthesis and Geometric Accuracy:**
*   **Overall Performance:** AnchorSplat achieved competitive or superior performance in novel view synthesis quality across standard metrics (PSNR, SSIM, LPIPS) compared to optimization-based methods like 3DGS and Mip-Splatting, and the feed-forward voxel-aligned AnySplat. For instance, on ScanNet++ with 32 input views, AnchorSplat achieved a PSNR of 21.48, compared to 20.20 for AnySplat and approximately 20 for optimization-based methods (Table 1).
*   **Depth Accuracy:** The method demonstrated significantly improved depth estimation accuracy, indicated by lower Absolute Relative Error (AbsRel) and higher $\delta_1$ scores. AnchorSplat achieved an AbsRel of 0.066 and $\delta_1$ of 0.94, compared to AnySplat's 0.16 and 0.71, respectively (Table 1). This suggests a more accurate underlying 3D geometry.
*   **Geometric Consistency and Artifact Reduction:** Visualizations confirmed that AnchorSplat produced cleaner, sharper, and more geometrically consistent reconstructions with fewer artifacts such as floaters, ghost structures, and irregular density distributions compared to AnySplat (Figure 1, Figure 4, Figure 7). The anchor-aligned representation facilitated more coherent and spatially compact Gaussian distributions.

**5.2. Efficiency and Scalability:**
*   **Reduced Gaussian Count:** A core finding is the substantial reduction in the number of Gaussians required to represent a scene. AnchorSplat utilized approximately 247,153 Gaussians, which is nearly 20 times fewer than AnySplat (e.g., 5,550,940 Gaussians for 32 input views) and significantly fewer than optimization-based methods (Table 1).
*   **Lower Reconstruction Time:** Despite achieving higher or comparable quality, AnchorSplat exhibited lower reconstruction times. For 32 input views, it reconstructed scenes in 5.52 seconds, approximately half the time of AnySplat (6.83 seconds, plus AnySplat's preprocessing time, which is higher) and substantially faster than optimization-based 3DGS (391.44 seconds) (Table 1).
*   **Fixed Gaussian Count with Varying Views:** Unlike pixel- or voxel-aligned methods where Gaussian count scales with input views, AnchorSplat's anchor-aligned representation maintained a fixed number of Gaussians (e.g., 247,153) regardless of whether 32, 48, or 64 input views were used. This property highlights its efficiency and scalability, as reconstruction quality improved with more input views without a proportional increase in computational cost (Table 2, Figure 5).
*   **Robustness to View Density:** The method maintained stable performance under extremely sparse (3-5 views) and dense (128-256 views) input settings. AnySplat encountered Out-Of-Memory (OOM) errors at 256 input views, whereas AnchorSplat continued to function efficiently (Table 3).

**5.3. Gaussian Refiner Effectiveness:**
*   The plug-and-play Gaussian Refiner module was shown to effectively enhance reconstruction quality. Visual comparisons indicated improvements in boundary sharpness, filling of missing regions, and enhanced color consistency in areas where the initial Gaussian Decoder struggled (Figure 6). Quantitatively, AnchorSplat with the refiner (PSNR 21.48) consistently outperformed AnchorSplat without the refiner (AnchorSplat$^\star$, PSNR 20.96) (Table 1).

**5.4. Ablation Studies (Supplementary Material):**
*   **Input Modalities:** Incorporating RGB images, camera ray embeddings, and depth maps as input to the Gaussian Decoder yielded the best performance, emphasizing the importance of informed geometric and camera cues (Table 4).
*   **Number of Gaussians per Anchor:** An ablation showed that predicting 4 Gaussians per anchor offered the best balance between representational capacity, accuracy, and computational efficiency (Table 5).
*   **Dataset Generalization:** AnchorSplat demonstrated superior RGB and depth rendering quality and reconstruction efficiency across diverse indoor (ARKitScenes, Replica) and outdoor (T&T) datasets compared to AnySplat (Table 6).
*   **Aggregation Method:** Average pooling was identified as the most effective strategy for aggregating projected image features into single C-dimensional anchor features (Figure 8).
*   **Anchor Predictor Backbone:** Both MapAnything and DA3 backbones for depth prediction in the Anchor Predictor yielded comparable performance, confirming MapAnything as a reliable choice (Table 7).

### 6. Significance and Potential Impact

AnchorSplat introduces a methodological shift in feed-forward 3D Gaussian Splatting by adopting an anchor-aligned representation. This approach has several significant implications and potential impacts:

1.  **Enhanced Efficiency and Scalability:** By decoupling the Gaussian representation from individual pixels and the number of input views, AnchorSplat substantially reduces the number of Gaussian primitives required for scene representation. This leads to lower memory footprint and faster reconstruction times, making high-fidelity 3D reconstruction more accessible for applications with computational constraints. Its ability to maintain a fixed number of Gaussians regardless of input view count is a key enabler for scalability in large-scale or dynamic environments.
2.  **Improved Geometric Fidelity and Consistency:** The use of 3D geometric priors and an anchor-aligned framework leads to more accurate and consistent 3D geometry. This reduces common artifacts like floaters, ghosting, and blurred structures prevalent in pixel-aligned methods, resulting in cleaner surfaces and sharper details in novel view synthesis. The improved depth estimation further corroborates this enhanced geometric understanding.
3.  **Generalizability Across Diverse Conditions:** The method's demonstrated robustness to varying input view densities (from sparse to very dense) and generalization across different indoor and outdoor datasets suggests its broad applicability. This versatility makes it suitable for real-world scenarios where input data quality and quantity can vary.
4.  **Practical End-to-End Solution:** AnchorSplat provides an end-to-end framework for scale-consistent depth prediction and arbitrary-view rendering in a feed-forward manner. This reduces the complexity and computational demands associated with traditional per-scene optimization.
5.  **Modular Refinement Capability:** The plug-and-play Gaussian Refiner offers a practical way to incrementally improve reconstruction quality and view consistency without requiring a full model retraining. This modularity can simplify deployment and adaptation in different contexts.
6.  **Foundational for Downstream 3D Tasks:** The generation of high-precision, geometrically robust 3DGS representations can serve as a strong foundation for various downstream applications. These include scene understanding (e.g., semantic segmentation, object detection in 3D), robotic navigation, augmented reality, and 3D reasoning, where accurate and consistent 3D structure is critical.

In summary, AnchorSplat represents a step towards more efficient, robust, and geometrically accurate feed-forward 3D scene reconstruction, potentially expanding the practical utility of 3D Gaussian Splatting in a wider range of real-world computer vision and robotics applications.
