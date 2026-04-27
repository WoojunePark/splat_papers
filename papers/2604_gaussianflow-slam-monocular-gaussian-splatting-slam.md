---
title: "GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow"
date: 2026-04-17
arxiv: "2604.15612v1"
venue:
status: to-read

abstract: "Gaussian splatting has recently gained traction as a compelling map representation for SLAM systems, enabling dense and photo-realistic scene modeling. However, its application to monocular SLAM remains challenging due to the lack of reliable geometric cues from monocular input. Without geometric supervision, mapping or tracking could fall in local-minima, resulting in structural degeneracies and inaccuracies. To address this challenge, we propose GaussianFlow SLAM, a monocular 3DGS-SLAM that leverages optical flow as a geometry-aware cue to guide the optimization of both the scene structure and camera poses. By encouraging the projected motion of Gaussians, termed GaussianFlow, to align with the optical flow, our method introduces consistent structural cues to regularize both map reconstruction and pose estimation. Furthermore, we introduce normalized error-based densification and pruning modules to refine inactive and unstable Gaussians, thereby contributing to improved map quality and pose accuracy. Experiments conducted on public datasets demonstrate that our method achieves superior rendering quality and tracking accuracy compared with state-of-the-art algorithms. The source code is available at: this https URL."

website: 
code: https://github.com/url-kaist/gaussianflow-slam
openreview: 
issue: 43

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

# GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow

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

![Figure](https://arxiv.org/html/2604.15612v1/x1.png)

*Figure 1: Illustration of GaussianFlow SLAM process. Our method leverages optical flow XtX_{t} to optimize both 3DGS and camera pose. Along each pixel’s ray direction, the projected motion of 3DGS is guided to align with the optical flow. The resulting alignment gradient enables 3DGS to iteratively update its geometric structure and the camera pose. From the rasterized depth images, it can be observed that the geometric structure of 3DGS becomes increasingly refined, recovering more valid geometric shapes over time.*

![Figure](https://arxiv.org/html/2604.15612v1/x2.png)

*Figure 2: (a) The overall framework of GaussianFlow SLAM. Each of the three modules highlighted by the dashed box performs a recurrent update process during optimization. (b) The recurrent update process. The GaussianFlow ζt\zeta_{t} is passed to the ConvGRU (Convolutional Gated Recurrent Unit) module to predict optical flow XtX_{t}, which is then used by optimization kernels to update either the camera pose 𝐓\mathbf{T} or the 3DGS 𝒢\mathcal{G}. The updated 𝒢\mathcal{G} are subsequently used to re-estimate ζt\zeta_{t}. (c) Visualization of the complementary convergence between GaussianFlow ζt\zeta_{t} and optical flow XtX_{t} over time.*

![Figure](https://arxiv.org/html/2604.15612v1/x3.png)

*Figure 3: Visualization of per-Gaussian error types for the rendered image from an alternative viewpoint. For Eit​[𝒮t]E_{i}^{t}[\mathcal{S}_{t}], the density contribution of each Gaussian is not considered, so the errors tend to highlight spatially extended Gaussians. In contrast, E^it​[𝒮t]\hat{E}_{i}^{t}[\mathcal{S}_{t}] and E^it​[ℱt]\hat{E}_{i}^{t}[\mathcal{F}_{t}] account for the density contribution of each Gaussian, enabling delicate per-Gaussian error analysis.*

![Figure](https://arxiv.org/html/2604.15612v1/x4.png)

*Figure 4: Comparison of rendered images and rasterized depths for a challenging scene. Methods exploiting monocular depth priors, such as HI-SLAM2 [15] and WildGS-SLAM [16], learn incorrect 3DGS geometry when the depth prior is unreliable. In contrast, our GaussianFlow-based method robustly learns geometrically valid structures.*

![Figure](https://arxiv.org/html/2604.15612v1/x5.png)

*Figure 5: Qualitative comparison on the EuRoC dataset. By exploiting optical flow for geometric learning, our approach preserves fine object boundaries and achieves more detailed reconstructions compared with other methods.*

## LLM Summary

## Detailed Report: GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow

### 1. Authors and Institution(s)

The research paper "GaussianFlow SLAM: Monocular Gaussian Splatting SLAM Guided by GaussianFlow" was authored by Dong-Uk Seo, Jinwoo Jeon, Eungchang Mason Lee, and Hyun Myung. All authors are affiliated with the School of Electrical Engineering at KAIST (Korea Advanced Institute of Science and Technology), Daejeon, Republic of Korea. Hyun Myung is designated as the corresponding author.

### 2. How this Work Fits into the Broader Research Landscape

Visual Simultaneous Localization and Mapping (SLAM) is a foundational technology in robotics, augmented reality/virtual reality (AR/VR), and autonomous navigation. Traditionally, visual SLAM systems have relied on reconstructing sparse point clouds, which are sufficient for camera localization but lack the density and photorealistic quality required for detailed scene modeling or novel view synthesis.

The emergence of differentiable scene representations, such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), has enabled the creation of dense, high-fidelity scene reconstructions. Among these, 3DGS has gained traction due to its ability to achieve real-time rasterization and significantly faster training times compared to volume-based methods like NeRF. This speed and differentiability have led to the integration of 3DGS into SLAM pipelines, where Gaussians are typically initialized and optimized using explicit depth measurements from sensors such as RGB-D cameras, stereo setups, or LiDAR. These depth-supervised 3DGS-SLAM systems have demonstrated stable operation and accurate pose estimation.

However, applying 3DGS to monocular SLAM presents significant challenges. The absence of direct depth information makes it difficult to reliably initialize and constrain Gaussians, leading to potential issues such as local minima during optimization, overfitting to specific views, structural degeneracies, and inaccuracies in map reconstruction. Existing monocular 3DGS-SLAM approaches have attempted to address these issues by bootstrapping Gaussians from sparse 3D feature points or dense depth predictions from neural networks. Yet, sparse features can introduce mapping instability, and neural depth priors may suffer from scale misalignment and accumulation of geometric errors. Furthermore, many monocular 3DGS-SLAM methods primarily rely on photometric error minimization for camera pose estimation, which is susceptible to degradation if the underlying 3DGS map is imprecise, creating a feedback loop where map errors corrupt pose estimates, and vice versa. Some methods decouple tracking from mapping, but this reduces 3DGS to a passive visualizer without direct feedback to improve pose estimation.

Optical flow has a history in SLAM, initially used for sparse feature tracking in early systems. With advancements in neural networks, dense optical flow has become more accurate and is increasingly employed in learning-based pose estimation and robust residual modeling. While some research has explored training 3DGS with optical flow, these efforts have primarily focused on modeling dynamic content or improving offline scene understanding, rather than directly integrating it into a real-time SLAM system for geometry and pose optimization.

GaussianFlow SLAM positions itself within this landscape by addressing the fundamental geometric ambiguity in monocular 3DGS-SLAM. It introduces a mechanism to leverage dense optical flow as a geometry-aware cue to guide the joint optimization of both the 3DGS scene structure and camera poses. This work represents an advance in monocular 3DGS-SLAM by introducing direct optical flow supervision with closed-form analytic gradients, thereby enabling a more robust and geometrically consistent approach than prior monocular methods.

### 3. Key Objectives and Motivation

The primary objective of GaussianFlow SLAM is to overcome the inherent challenges of monocular 3D Gaussian Splatting (3DGS) SLAM, specifically the lack of reliable geometric cues from single-camera input. This deficiency leads to several issues:
1.  **Susceptibility to Local Minima and Overfitting**: Without explicit depth information, Gaussians often fail to converge to geometrically consistent 3D positions and may instead overfit to specific viewpoints, resulting in inaccurate and structurally degenerate map reconstructions.
2.  **Degraded Pose Estimation**: Existing monocular 3DGS-SLAM methods often estimate camera poses by minimizing photometric error between input images and rendered 3DGS views. If the 3DGS representation is imprecise or locally degenerate, the rendered image can be misaligned with the real scene, thereby degrading pose estimation accuracy. This can initiate a negative self-reinforcing loop where inaccurate maps lead to poor pose tracking, which in turn corrupts the map further.

The motivation behind GaussianFlow SLAM stems from the recognition that dense optical flow inherently encodes valuable information about relative camera motion and scene depth through per-pixel correspondences. By leveraging this information, the authors aim to:
1.  **Introduce Consistent Structural Cues**: Develop a mechanism to continuously correct the 3DGS geometry during optimization, even without direct depth measurements, by encouraging the projected motion of Gaussians (termed GaussianFlow) to align with the observed dense optical flow.
2.  **Improve Pose Estimation Feedback**: Utilize GaussianFlow to guide the convergence of optical flow within pose estimation modules. This is intended to establish a positive feedback loop where the mapping process actively improves tracking accuracy, moving beyond 3DGS as a passive renderer.
3.  **Enable Scalable and Robust Optimization**: Implement the optical flow supervision with closed-form analytic gradients directly within the 3DGS kernel. This aims to overcome the limitations of approximate gradient calculations or computationally expensive automatic differentiation, allowing for more efficient and scalable optimization of both Gaussian parameters and camera poses in SLAM settings.
4.  **Refine Map Quality and Stability**: Address potential issues such as under-densified inactive Gaussians or "floaters" that might arise from continuous geometry correction driven by GaussianFlow optimization. This motivates the development of normalized error-based densification and pruning modules to selectively adjust unstable Gaussians, thereby enhancing map quality and further contributing to pose accuracy.

In summary, the key objective is to enable robust and accurate monocular 3DGS-SLAM by integrating geometry-aware optical flow supervision with efficient, kernel-level gradient computation, supported by adaptive Gaussian management.

### 4. Methodology and Approach

GaussianFlow SLAM operates on incoming monocular camera frames and integrates optical flow as a geometry-aware cue for joint optimization of the 3DGS map and camera poses.

**A. Overall Framework**
The system begins by selecting keyframes based on optical flow relative to the last keyframe and incorporating them into an optimization window. An initial pose estimate is made for each new keyframe. Regions with insufficient Gaussian density or high rendering loss are identified, and new Gaussians are inserted. The core of the system is an alternating loop involving Dense Bundle Adjustment (DBA) guided by GaussianFlow for pose optimization and multi-view optimization using GaussianFlow loss for 3DGS refinement. During mapping, normalized error-based densification and pruning modules are employed to adjust Gaussians. This entire process features a recurrent update mechanism where GaussianFlow and optical flow are jointly refined with updated poses and the shared 3DGS map.

**B. GaussianFlow Optimization**
1.  **GaussianFlow Loss**: The concept of "GaussianFlow" is defined as the projected motion of Gaussians from one frame to a subsequent frame. For each pixel, GaussianFlow (ζ_t) is computed by normalizing contributing Gaussians to a canonical space and then unnormalizing them to the target image space. The flow loss (L_t_flow) is then calculated by comparing this projected GaussianFlow with dense optical flow (X_t) estimated by a neural network. To account for noise in optical flow estimation, a robust log-logistic residual model is adopted, which models both inlier and outlier probabilities.
2.  **Closed-Form Analytic Gradients**: A central methodological contribution is the derivation of closed-form analytic gradients for the GaussianFlow loss with respect to both Gaussian parameters (mean, covariance, opacity) and camera poses. Prior methods either approximated parts of the GaussianFlow calculation, hindering gradient propagation, or relied on PyTorch's automatic differentiation, which is computationally expensive and difficult to integrate into low-level, tile-based 3DGS rasterization kernels. The authors address this by:
    *   Decomposing the 2D projected covariance matrix Σ'_i,t into its eigen components (Q_i,t, S_i,t).
    *   Deriving closed-form derivatives for matrix functions involving Σ'_i,t through Q_i,t and S_i,t.
    *   Using the chain rule to propagate these gradients back to the original 3D Gaussian mean (x_i,t) and covariance (Σ_i,t), as well as to the camera poses (T_t, T_t+1). This allows for direct pose updates for both the source and target frames of the optical flow within the 3DGS GPU kernel, enhancing efficiency and scalability.

**C. Tracking and Mapping**
1.  **Initial Pose Estimation**: For a new keyframe, its initial pose (T_t+1) is estimated by minimizing a loss function comprising the photometric loss (L_t+1_image) for the new frame and GaussianFlow loss (L_t_flow, L_t-1_flow) between the new keyframe and two preceding, already optimized keyframes.
2.  **GaussianFlow-guided Dense Bundle Adjustment (DBA)**: After initial pose estimation, the poses of multiple keyframes within an optimization window are refined using DBA. This second-order optimization approach typically addresses highly non-linear pose refinement. In GaussianFlow SLAM, the GaussianFlow (ζ_t) is fed into a pretrained Convolutional Gated Recurrent Unit (ConvGRU) network to produce refined optical flow (X_t), which then guides the DBA process.
3.  **Multi-view Mapping**: With fixed poses from DBA, the 3DGS map (G) is optimized. The mapping loss includes the image loss (L_t^k_image), GaussianFlow loss (L_t^k_flow), an isotropic loss (L_iso) to regularize Gaussian shape, and an opacity entropy loss (L_opa) to prevent vague "floaters." The system iteratively alternates between DBA pose estimation and multi-view mapping.
4.  **Recurrent Update Process**: A recurrent refinement loop is used across the initial pose estimation, DBA, and multi-view mapping modules. This process jointly refines GaussianFlow and the optical flow predicted by ConvGRU, based on updated camera poses and the shared, continuously optimized 3DGS map. This iterative refinement is intended to improve both flow accuracy and overall pose and depth estimation.

**D. Gaussian Management and Filtering Modules**
1.  **Error-based Densification and Pruning**: To manage the quality and stability of the 3DGS map, the method introduces refined Gaussian management.
    *   **Normalized Error**: Beyond standard per-Gaussian error (E_t^i), a *normalized* error (Ê_t^i) is introduced. This normalization divides the per-Gaussian error by the Gaussian's density contribution, removing screen-space coverage bias and providing a scale-invariant score. This allows for more selective error analysis, distinguishing between errors from wide-coverage Gaussians and those from genuinely problematic ones.
    *   **Densification**: Gaussians are split based on specific masks (M_t^1, M_t^2, M_t^3) that identify: 1) large Gaussians with high errors but small position gradients (missed by original 3DGS densification), 2) large Gaussians with high normalized errors, and 3) overly large Gaussians.
    *   **Pruning**: Unstable Gaussians (floaters) are pruned using masks (M_t^4, M_t^5, M_t^6) that target: 1) small Gaussians with high normalized DSSIM or flow errors, 2) small-to-medium Gaussians with high normalized DSSIM errors, and 3) low-opacity Gaussians. This fine-grained pruning addresses specific failure modes in GaussianFlow optimization.
2.  **Gaussian ID Assignment for Adaptive Window**: Each Gaussian is assigned a keyframe ID upon its first rasterization (insertion or splitting). This mechanism is used to maintain map consistency with a shared global 3DGS map and supports covisibility-based keyframe selection, providing implicit functionality similar to loop closure.

### 5. Main Findings and Results

The efficacy of GaussianFlow SLAM was evaluated through experiments on the TUM RGB-D and EuRoC datasets, focusing on pose accuracy, rendering quality, and qualitative reconstruction.

**A. Quantitative Comparison (Pose Accuracy)**
*   **RMSE of Absolute Trajectory Error (ATE)**: GaussianFlow SLAM demonstrated superior tracking accuracy across most sequences on both datasets compared to state-of-the-art monocular 3DGS-SLAM baselines (MonoGS, MM3DGS-SLAM, HI-SLAM2, WildGS-SLAM) and Photo-SLAM.
*   **Performance on Challenging Datasets**: While most methods performed reliably on the room-scale TUM RGB-D, several existing methods showed degradation on the larger-scale EuRoC dataset (e.g., MonoGS prone to local minima, MM3DGS-SLAM suffering from scale misalignment, WildGS-SLAM affected by depth-prior errors). GaussianFlow SLAM achieved competitive or superior results, indicating robustness to larger-scale and more challenging motion conditions.
*   **Specific Cases**: Photo-SLAM, which is based on sparse feature tracking (ORB-SLAM3), outperformed GaussianFlow SLAM on a few challenging sequences (EuRoC MH04/MH05 and TUM fr1/desk) where extremely low illumination or transient motion blur might render dense optical flow correspondences unreliable. However, the overall performance indicates that dense pixel supervision from optical flow generally provides more geometric information, leading to improved rendering quality and competitive pose accuracy.

**B. Quantitative Comparison (Rendering Quality)**
*   **PSNR, SSIM, LPIPS**: GaussianFlow SLAM achieved higher rendering quality, as measured by peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), and learned perceptual image patch similarity (LPIPS), compared to most baselines.
*   **Perceptual Quality (LPIPS)**: Notably, GaussianFlow SLAM often outperformed other methods in LPIPS, which is considered to reflect perceptual quality more accurately, even when other methods (e.g., HI-SLAM2) achieved higher PSNR and SSIM through noise suppression techniques.

**C. Qualitative Comparison**
*   **Geometric Validity**: Qualitative results demonstrated that GaussianFlow SLAM produces more geometrically valid rasterized depths compared to methods relying on monocular depth priors (e.g., HI-SLAM2, WildGS-SLAM), which can learn incorrect 3DGS geometry when their depth priors are unreliable.
*   **Detailed Reconstruction**: The method successfully reconstructed detailed structural characteristics of objects. In contrast, Photo-SLAM sometimes failed to capture sufficient details due to feature sparsity, while depth-prior methods missed structures due to errors in their priors.

**D. Ablation Study**
*   **GaussianFlow Guidance**: An ablation study on the EuRoC dataset confirmed that GaussianFlow guidance significantly improves pose accuracy (RMSE ATE) across most sequences. This indicates that leveraging the shared 3DGS geometry through GaussianFlow provides a beneficial feedback mechanism for pose estimation.
*   **Densification and Pruning Modules**: Replacing the proposed normalized error-based densification and pruning modules with the original densification and pruning (ODP) methods from 3DGS resulted in a degradation of both rendering quality (lower PSNR/SSIM, higher LPIPS) and pose accuracy (higher RMSE ATE). This confirms the essential role of the proposed Gaussian management strategy in mitigating floaters and maintaining geometric fidelity, particularly in the context of continuous geometry correction via GaussianFlow optimization.

**E. Runtime and Scalability**
*   **Online Processing Speed**: The online processing speed of GaussianFlow SLAM was reported at 0.17 frames per second (FPS) on the EuRoC MH05 sequence, which is lower than other methods evaluated (ranging from 0.24 FPS to 18.59 FPS).
*   **Bottlenecks**: The primary computational bottleneck was identified as the tightly-coupled alternating loop of 3DGS map optimization and multi-pose optimization, which accounts for the majority of the time per frame (5,925 ms total, with 3,605 ms for 3DGS map optimization and 2,050 ms for initial pose optimization). While 3DGS rasterization itself is fast (466 FPS), the repeated optimization steps in the alternating design significantly impact overall runtime.
*   **Scalability**: As the number of Gaussians (N_t) in the map increases, the average FPS gradually decreases (e.g., from 0.29 FPS for [0, 150k) Gaussians to 0.14 FPS for [300k, 490k) Gaussians). This indicates that the current implementation's efficiency is affected by map growth. The map reached approximately 490,000 Gaussians with an 11% keyframe ratio during evaluation.

### 6. Significance and Potential Impact

GaussianFlow SLAM introduces an approach to monocular 3DGS-SLAM that addresses critical limitations in existing methods by integrating optical flow supervision with analytical gradient computation. Its significance and potential impact are multifaceted:

1.  **Advancement in Monocular 3DGS-SLAM**: The work represents a substantial step in monocular 3DGS-SLAM by providing a mechanism to robustly infer and refine 3D geometry from 2D optical flow. This directly tackles the lack of explicit depth cues, which has been a primary challenge for dense, photorealistic scene reconstruction from monocular input.
2.  **Geometry-Aware Cue for Robustness**: By aligning GaussianFlow with dense optical flow, the method introduces consistent structural cues. This reduces susceptibility to local minima and overfitting that plague photometric-only optimization in monocular settings, leading to more geometrically valid and stable 3DGS reconstructions.
3.  **Enhanced Pose-Map Interplay**: The use of GaussianFlow to guide pose estimation, particularly within a Dense Bundle Adjustment framework, establishes a tighter and more beneficial feedback loop between mapping and tracking. This allows the evolving 3DGS map to actively improve camera pose estimates, rather than serving as a passive rendering tool.
4.  **Efficient and Scalable Optimization**: The development of closed-form analytic gradients for optical flow supervision, integrated directly into the 3DGS kernel, is a technical innovation. This approach bypasses the limitations of approximations or computationally heavy automatic differentiation, paving the way for more efficient and scalable 3DGS optimization in complex SLAM environments.
5.  **Improved Map Quality and Stability**: The proposed normalized error-based densification and pruning modules contribute to higher map quality by selectively managing inactive and unstable Gaussians. This refined Gaussian management, tailored to the dynamics of GaussianFlow optimization, ensures that the reconstructed scenes maintain high fidelity and geometric accuracy.
6.  **State-of-the-Art Performance**: The reported superior tracking accuracy and photo-realistic reconstruction quality on public datasets demonstrate the practical effectiveness of GaussianFlow SLAM. This performance validates the core hypothesis that optical flow can serve as a potent geometry-aware cue for monocular 3DGS-SLAM.

**Potential Impact**:
*   **AR/VR and Robotics**: The ability to build accurate, dense, and photorealistic 3D maps from monocular cameras has significant implications for AR/VR applications requiring immersive environments and for robotics tasks demanding detailed scene understanding (e.g., navigation, manipulation).
*   **Foundation for Future Research**: The work lays a foundation for future research in several directions. The identified computational bottleneck suggests a need for more efficient second-order optimization methods within 3DGS itself, potentially reducing reliance on external DBA modules and enabling real-time operation.
*   **Dynamic Environments**: Extending the method to highly dynamic scenes, which are acknowledged as future work, could significantly broaden its applicability to real-world scenarios beyond predominantly static environments.
*   **Sensor Fusion**: While focused on monocular input, the analytical gradient framework could potentially be adapted or extended to fuse with other sensor modalities (e.g., IMU) in a more tightly coupled fashion, further enhancing robustness and accuracy.

Overall, GaussianFlow SLAM advances the capabilities of monocular vision systems in constructing high-quality, dense 3D representations, pushing the boundaries of what is achievable with a single camera for simultaneous localization and mapping.
