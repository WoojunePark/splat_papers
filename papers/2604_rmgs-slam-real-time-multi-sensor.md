---
title: "RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM"
date: 2026-04-14
arxiv: "2604.12942v1"
venue:
status: to-read

abstract: "Real-time 3D Gaussian splatting (3DGS)-based Simultaneous Localization and Mapping (SLAM) in large-scale real-world environments remains challenging, as existing methods often struggle to jointly achieve low-latency pose estimation, 3D Gaussian reconstruction in step with incoming sensor streams, and long-term global consistency. In this paper, we present a tightly coupled LiDAR-Inertial-Visual (LIV) 3DGS-based SLAM framework for real-time pose estimation and photorealistic mapping in large-scale real-world scenes. The system executes state estimation and 3D Gaussian primitive initialization in parallel with global Gaussian optimization, thereby enabling continuous dense mapping. To improve Gaussian initialization quality and accelerate optimization convergence, we introduce a cascaded strategy that combines feed-forward predictions with voxel-based principal component analysis (voxel-PCA) geometric priors. To enhance global consistency in large scenes, we further perform loop closure directly on the optimized global Gaussian map by estimating loop constraints through Gaussian-based Generalized Iterative Closest Point (GICP) registration, followed by pose-graph optimization. In addition, we collected challenging large-scale looped outdoor SLAM sequences with hardware-synchronized LiDAR-camera-IMU and ground-truth trajectories to support realistic and comprehensive evaluation. Extensive experiments on both public datasets and our dataset demonstrate that the proposed method achieves a strong balance among real-time efficiency, localization accuracy, and rendering quality across diverse and challenging real-world scenes."

website: 
code: 
openreview: 
issue: 42

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

# RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM

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

![Figure](https://arxiv.org/html/2604.12942v1/x1.png)

*Figure 1: Overview of the proposed system. The framework follows a four-module design. (i) A LIV front-end first estimates ego-motion and produces time-synchronized poses, RGB images, projected depth maps, and voxel-PCA geometric priors. (ii) These outputs are then used to initialize 3D Gaussian primitives through a cascaded strategy that combines feed-forward predictions with geometry-aware priors. (iii) The global Gaussian map is then optimized asynchronously under photometric, structural, and geometric constraints. (iv) To improve global consistency, loop closure is performed directly on the Gaussian representation via Gaussian GICP, and the resulting loop constraints are jointly optimized with odometry in a pose graph.*

![Figure](https://arxiv.org/html/2604.12942v1/x2.png)

*Figure 2: Cascaded Gaussian Primitives Initialization. (i) Each point is projected into the previous and current loopframe images, and the closer valid view is used. (ii) On the predicted per-pixel Gaussian attribute maps, only the closest point is retained at each pixel and its attributes are bilinearly interpolated. (iii) Model-initialized points are transformed to the world frame, while the rest are initialized from voxel-PCA priors or an isotropic heuristic.*

![Figure](https://arxiv.org/html/2604.12942v1/Figures/render_figures_inset/scene02_cs_scu01/05_gslic2/scene02_cs_scu01_05_gslic2_img02_inset.jpg)

*Figure 3: Qualitative comparison of rendering results. The blue boxed region is enlarged and displayed in the corner for detailed visual inspection.*

![Figure](https://arxiv.org/html/2604.12942v1/x3.png)

*Figure 4: Trajectory comparison for the Driving1 sequence. The upper-left subfigure shows the overall 3D trajectory, and the others show local zoomed-in views at approximately 8.3×8.3\times magnification.*

![Figure](https://arxiv.org/html/2604.12942v1/x4.png)

*Figure 5: Runtime analysis across mapping scales. The subfigure (a) presents the per-sample runtime breakdown over time, with samples recorded from online module snapshots at 0.5 s intervals. The subfigure (b) summarizes the corresponding time-weighted overall runtime composition using stacked bars.*

## LLM Summary

## Research Paper Report: RMGS-SLAM: Real-time Multi-sensor Gaussian Splatting SLAM

### 1. Authors and Institution(s)

The research was conducted by a team of authors from multiple institutions:
*   **Dongen Li, Yi Liu, Zewen Sun, Zefan Huang, Chengran Yuan, Francis E.H. Tay, and Marcelo H. Ang Jr.** are affiliated with the Advanced Robotics Centre, National University of Singapore.
*   **Junqi Liu and Hongliang Guo** are from the College of Computer Science, Sichuan University.
*   **Jiahui Liu** is with the School of Aeronautics and Astronautics, Shanghai Jiao Tong University.
*   **Shuo Sun** is affiliated with the Singapore-MIT Alliance for Research and Technology.
*   Dongen Li, Yi Liu, Junqi Liu, Zewen Sun, and Zefan Huang are noted as having contributed equally to this work.

### 2. How This Work Fits into the Broader Research Landscape

Simultaneous Localization and Mapping (SLAM) is a foundational capability for autonomous systems, allowing robots to determine their position while concurrently constructing a map of their environment. Historically, SLAM systems have often focused on geometry-centric maps, which provide structural information but generally lack photorealistic detail. The demand for more immersive visual applications and advanced robotic tasks, such as navigation and grasping in complex environments, has highlighted the need for richer, appearance-aware scene representations.

The advent of 3D Gaussian Splatting (3DGS) has introduced a new paradigm for scene representation. 3DGS utilizes explicit anisotropic Gaussian primitives to represent a scene, enabling efficient and differentiable rasterization. This approach offers an appearance-aware, continuous, and directly renderable map, making it attractive for SLAM applications where the map can serve both as a geometric reference for pose estimation and a photorealistic representation for perception and interaction.

However, the integration of 3DGS into real-time SLAM systems presents significant challenges. High-quality 3DGS reconstruction typically involves iterative optimization processes that are computationally intensive, often requiring full observations and prolonged offline training. Adapting this to real-time SLAM, where both pose estimation and map updates must keep pace with continuous, high-frequency sensor inputs, is difficult. Existing 3DGS-based SLAM systems have made progress, but many struggle to simultaneously achieve low-latency pose estimation, continuous 3D Gaussian reconstruction, and long-term global consistency in large-scale, dynamic real-world environments.

Early 3DGS-based SLAM methods primarily focused on visual SLAM, such as GS-SLAM, MonoGS, and SplaTAM. These systems often face limitations in unconstrained real-world settings due to factors like viewpoint variation, illumination changes, and imperfect geometry, which can degrade tracking robustness and reconstruction quality. To address these geometric perception and pose robustness issues, LiDAR integration has been explored. Loosely coupled LiDAR-assisted methods simplify integration but often struggle with real-time performance under high-rate sensor inputs due to asynchronous processing. Tightly coupled methods, exemplified by Gaussian-LIC, LVI-GS, and FusionGS-SLAM, aim for deeper multi-modal integration to improve spatio-temporal consistency. Despite these advancements, maintaining both real-time performance and global consistency in large-scale environments remains a challenge. Some systems improve efficiency by restricting representation size or optimization scope, but this can limit the recovery of fine photorealistic details or require post-stream optimization for satisfactory quality.

RMGS-SLAM positions itself within this landscape by seeking to overcome the aforementioned limitations. It proposes a tightly coupled LiDAR-Inertial-Visual (LIV) framework that aims to simultaneously achieve real-time performance, high-quality photorealistic mapping, and robust global consistency through explicit loop closure, particularly in large-scale real-world environments. This work contributes to the ongoing effort to develop robust, efficient, and perceptually rich SLAM systems for advanced robotic and immersive applications.

### 3. Key Objectives and Motivation

The primary objective of this research is to develop a real-time 3D Gaussian Splatting (3DGS)-based Simultaneous Localization and Mapping (SLAM) system capable of operating in large-scale, real-world environments. The authors identify three key challenges that existing methods often struggle to address concurrently:
1.  **Low-latency pose estimation**: The system must accurately and rapidly determine its position and orientation in real-time.
2.  **3D Gaussian reconstruction in step with incoming sensor streams**: The environment map, represented by 3D Gaussians, needs to be continuously updated and refined as new sensor data arrives, without significant lag.
3.  **Long-term global consistency**: In large environments, accumulated errors can lead to drift, causing the map to become inconsistent over time. The system must maintain global accuracy, especially when revisiting previously mapped areas.

The motivation behind RMGS-SLAM stems from the limitations of current 3DGS-based SLAM approaches:
*   **Computational burden of 3DGS optimization**: High-quality 3DGS reconstruction inherently relies on iterative optimization, which is computationally expensive. Integrating this into a real-time SLAM system, which requires continuous pose estimation and mapping, poses a significant performance challenge. Many existing systems, while supporting incremental updates, struggle to sustain both processes under high-frequency continuous sensor inputs.
*   **Suboptimal Gaussian initialization**: Current LiDAR-assisted methods often rely on LiDAR observations with limited geometric assumptions for Gaussian initialization, necessitating extensive online refinement, which consumes computational resources and can hinder real-time performance.
*   **Lack of explicit loop closure**: To maintain runtime efficiency, many existing 3DGS-based SLAM systems omit explicit loop closure mechanisms. This omission limits their ability to suppress long-term drift and ensure global consistency in large-scale environments, where accumulated errors can significantly degrade map quality and localization accuracy.

To address these motivations, the paper outlines several specific objectives:
*   **Develop a real-time, tightly coupled LiDAR-Inertial-Visual (LIV) 3DGS-SLAM framework**: This framework aims to achieve non-blocking dense mapping by executing pose estimation and Gaussian initialization in parallel with global Gaussian map optimization.
*   **Introduce a cascaded Gaussian initialization strategy**: This strategy is designed to improve the quality of primitive initialization and accelerate the convergence of Gaussian optimization. It combines feed-forward predictions with geometric priors derived from voxel-based Principal Component Analysis (voxel-PCA).
*   **Implement a 3DGS-based loop-closure method for large-scale scenes**: This method aims to extract relevant Gaussian sets from the global map, estimate loop constraints using Gaussian-based Generalized Iterative Closest Point (GICP) registration, and integrate these into a pose-graph optimization to suppress long-term drift and enhance global consistency.
*   **Provide a new real-world benchmark dataset**: This dataset, featuring synchronized LiDAR, camera, and IMU streams with ground-truth trajectories for challenging large-scale looped outdoor road scenes, is intended to facilitate comprehensive evaluation of 3DGS-based SLAM systems under practical conditions.

Through these objectives, RMGS-SLAM endeavors to achieve a balance among real-time efficiency, localization accuracy, and rendering quality across diverse and challenging real-world scenarios.

### 4. Methodology and Approach

The RMGS-SLAM system is structured around a four-module design (Fig. 1), which tightly couples LiDAR-Inertial-Visual (LIV) sensing for real-time pose estimation and photorealistic mapping.

**A. LIV Front-End (Implicitly within overall design):**
The front-end performs ego-motion estimation and generates time-synchronized outputs. These include corrected poses, RGB images, projected depth maps (likely derived from LiDAR), and voxel-PCA geometric priors. This integrated processing is crucial for providing consistent and synchronized data to subsequent modules.

**B. Voxel-PCA-based Geometric Fitting (Sec. III-A):**
To provide structured geometric priors for Gaussian initialization, the system utilizes a voxel-PCA-based fitting scheme.
*   **Voxelization**: The latest front-end processed colored point cloud, represented in the world frame, is partitioned into voxels using a hash-indexed octree structure.
*   **Statistical Analysis**: For each voxel, the mean (μ) and covariance (C) of the contained points are computed. Eigen-decomposition is then performed on the covariance matrix to obtain ordered eigenvalues (λmin ≤ λmid ≤ λmax) and their corresponding eigenvectors (vmin, vmid, vmax).
*   **Geometry Classification**: Based on eigenvalue distribution, local geometry is classified as planar (if λmin < τp) with normal vmin, or linear (if λmax/λmin > τl) with direction vmax. Structures not meeting these criteria are deemed unreliable.
*   **Geometric Descriptor**: A 6-dimensional geometric descriptor g = [v⊤k, μ⊤]⊤ is defined to characterize local geometry and its uncertainty, where vk is either vmin for planar or vmax for linear structures.
*   **Uncertainty Propagation**: The descriptor's covariance (Σg) is computed by propagating point-level covariances (ΣWi) within each voxel, considering measurement noise and pose uncertainty.
*   **Attributes Assignment**: Each point is assigned voxel-level attributes including its world-frame position, PCA eigenvectors (Rpca), scale derived from eigenvalues (spca), color, and a geometric reliability indicator. This compact representation serves as a structured prior.

**C. Cascaded 3D Gaussian Primitives Initialization (Sec. III-B):**
This module initializes new 3D Gaussian primitives based on keyframes and loopframes.
*   **Keyframe/Loopframe Selection**: Frames are periodically selected as keyframes based on an index gap. Loopframes are designated from keyframes when relative motion exceeds predefined thresholds, partitioning keyframe sequences into local segments.
*   **Gaussian Instantiation**: When a new loopframe is created, 3D points observed within the latest segment are aggregated. One Gaussian is instantiated per point, with its mean at the point location and DC component from the point color.
*   **Cascaded Attribute Initialization (Equation 3)**: The remaining attributes (scale, rotation, opacity, SH coefficients), collectively denoted Θ(p), are initialized through a cascaded strategy:
    *   **Model-based (Θmodel(p))**: If a valid feed-forward model prediction is available. Current and previous loopframe images are processed by a pre-trained model to predict per-pixel Gaussian attribute maps. Each 3D point is projected into both views, and attributes from the closer, valid view are selected. Occlusion and projection conflicts are handled by retaining only the closest point per pixel and using bilinear interpolation for attributes. Predicted rotation (quaternion) is transformed from camera to world frame. Predicted scale's axis-wise shape ratio is normalized and the absolute scale is anchored to LiDAR depth (Equation 4).
    *   **PCA-based (Θpca(p))**: If model prediction is invalid but geometry is reliable (from voxel-PCA). Rotation is directly derived from PCA eigenvectors. Anisotropic scale from PCA is adjusted by a bounded dynamic factor (β), which depends on the ratio of reliable but model-invalid points in the segment (Equation 5), to prevent over-stretched Gaussians in uncertain regions. Opacity is set to a constant, and higher-order SH coefficients to zero.
    *   **Heuristic-based (Θheur(p))**: If neither model prediction is valid nor geometry is reliable. Rotation is set to identity, and scale is initialized isotropically using the depth-to-focal-length ratio (Equation 6). Opacity and higher-order SH coefficients are initialized similarly to the PCA-based branch.
This cascaded approach aims to provide robust and high-quality initialization, accelerating subsequent optimization.

**D. Optimization (Sec. III-C):**
Newly initialized Gaussians are integrated into the global map and continuously refined.
*   **Map Management**: New Gaussians are inserted, and redundant ones are filtered based on spatial proximity tests to avoid duplicates.
*   **Supervision**: Optimization is supervised by keyframe images. Two temporal windows (recent and history) are maintained to balance adaptation and long-range consistency, with views sampled randomly from both. Only Gaussians in the most recent K segments are updated; older segments are frozen.
*   **Masking for Stability**: To ensure stable gradients, optimization is restricted to reliably reconstructed regions using a geometric support mask (Mgeo) derived from accumulated opacity, and a conservative interior mask (Mint) obtained via morphological erosion (Equation 7).
*   **Loss Function**: The overall objective function (L) comprises photometric (Lrgb), structural (Lssim), and depth consistency (Ldepth) terms (Equations 9-12). RGB color rendering and depth computation (Equation 8) follow standard differentiable Gaussian splatting principles.
*   **Refinement and Pruning**: Visible and unfrozen Gaussians are refined using a sparse gradient-based optimizer. Low-opacity Gaussians are periodically pruned under a bounded removal ratio to manage map size and suppress weak primitives.

**E. Gaussian-based Loop Closure (Sec. III-D):**
This module enforces global consistency in large-scale scenes by detecting and resolving loops.
*   **Loop Candidate Search**: For a current loopframe, historical loopframes are searched based on spatio-temporal distance, and sufficiently separated candidates are retained.
*   **Gaussian Set Construction**: For a candidate loop pair (current loopframe i, historical loopframe j), a source Gaussian set (Gsrc i) is formed by Gaussians associated with the current loopframe. A target Gaussian set (Gtar j) is extracted from the optimized global 3D Gaussian map by considering Gaussians within the camera frusta of neighboring keyframes around j, filtering out distant Gaussians and those already in Gsrc i (Equation 13).
*   **Gaussian GICP Registration**: The relative pose between Gsrc i and Gtar j is estimated using a Gaussian GICP (Generalized Iterative Closest Point) registration, an extension of GICP to Gaussian primitives. To improve robustness, each Gaussian covariance is regularized into a planar form. The loop relative pose (Tloop ij) is found by minimizing a cost function based on residuals and covariances for correspondences between source and target Gaussians (Equations 14-16).
*   **Pose Graph Optimization**: Accepted alignments (loop candidates with converged optimization and low residual error) are converted into loop edges. These are then jointly optimized with odometry constraints in a GTSAM-based pose graph.
*   **Map Update**: After pose-graph optimization, updated corrected poses are propagated to the associated Gaussian segments in the global 3D Gaussian map, and supervisory camera views are updated, thereby enforcing global consistency across the entire system.

### 5. Main Findings and Results

The evaluation of RMGS-SLAM was conducted on both publicly available datasets (FAST-LIVO2, MARS-LVIG) and a newly collected challenging large-scale outdoor dataset (Driving1, Driving2) featuring synchronized LiDAR–camera–IMU data with ground truth. Comparisons were made against MonoGS, SplaTAM, GS-LIVM, Gaussian-LIC2, and FAST-LIVO2 (for localization).

**A. Evaluation of Rendering Quality (Table I, Fig. 3):**
*   **Overall Performance**: RMGS-SLAM demonstrated the best or near-best performance across almost all evaluated sequences in terms of Peak Signal to Noise Ratio (PSNR), Structural Similarity (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS).
*   **Comparison with Baselines**:
    *   **GS-LIVM**: Exhibited degraded pose estimation and reconstruction quality, likely due to its reliance on sweep reconstruction assumptions that did not consistently hold.
    *   **SplaTAM and MonoGS**: When using LiDAR-derived depth maps (inherently sparse and noisy), SplaTAM, which relies heavily on depth for pose optimization and Gaussian initialization, yielded inferior reconstruction. MonoGS, relying more on photometric residuals, achieved competitive reconstruction quality among visual-only baselines but incurred substantially higher runtime.
    *   **Gaussian-LIC2**: Showed a favorable trade-off between reconstruction quality and efficiency, benefiting from robust pose estimation and incremental mapping. However, its lack of loop closure resulted in limited global consistency in large-scale scenes, evidenced by overlapping road markings in the qualitative results.
*   **Qualitative Observations**: RMGS-SLAM produced sharper RGB images with fewer artifacts under novel views. The introduced Gaussian-based loop closure led to a more coherent global Gaussian map reconstruction in revisited large-scale scenes compared to baselines. The cascaded initialization strategy was observed to provide better attribute initialization, contributing to a more faithful recovery of view-dependent lighting and shading effects.

**B. Evaluation of Localization Accuracy (Table II, Fig. 4):**
*   **Overall Performance**: RMGS-SLAM consistently achieved the best overall localization accuracy (measured by Absolute Trajectory Error - ATE RMSE) across all tested sequences.
*   **Global Consistency**: The integration of Gaussian-based loop closure was instrumental in achieving better global consistency and reducing accumulated drift, particularly noticeable in the vertical (z-axis) direction.
*   **Trajectory Closure**: RMGS-SLAM demonstrated superior trajectory closure and geometric consistency after traversing and revisiting previously mapped areas, whereas most baseline methods exhibited residual offsets or heading inconsistencies.
*   **Baseline Failures**: Several baselines (Gaussian-LIC2, GS-LIVM, MonoGS, SplaTAM) failed to complete the full sequence or exhibited significantly high ATE values on challenging datasets, indicating robustness limitations.

**C. Runtime Analysis (Table I, Fig. 5):**
*   **System-level Runtime**: RMGS-SLAM achieved Real-time factors close to 1 on most sequences, indicating near-real-time full-pipeline processing. This contrasts with several baseline methods that had substantially larger factors or failed to complete sequences due to high optimization overhead.
*   **Module-level Runtime**: The computational cost varied with scene scale. In smaller-scale sequences (e.g., HKU Campus), state estimation and Gaussian primitives optimization were the dominant runtime components. In large-scale, looped sequences (e.g., Driving1), loop closure became the primary bottleneck once activated, accompanied by increased GPU memory usage. Despite this shift in workload, the system maintained stable real-time performance across different scene scales, demonstrating sufficient runtime headroom in smaller scenes and keeping pace with sensor streams in larger ones.

**D. Ablation Study (Table III):**
*   **Feed-forward Model Choice**: G3Splat was chosen over DepthSplat for the cascaded initialization due to its superior rendering performance.
*   **Impact of Voxel-PCA**: Removing voxel-PCA from the cascaded initialization resulted in a noticeable drop in rendering quality, confirming its role in providing reliable geometric priors for Gaussian initialization.
*   **Impact of Loop Closure**: The loop closure mechanism significantly improved rendering performance in large-scale looped scenes (e.g., Driving1) by enhancing global consistency. Its introduction did not lead to noticeable degradation in smaller sequences, despite the additional computational overhead, indicating its targeted benefit for larger environments without compromising smaller-scale performance.

### 6. Significance and Potential Impact

The RMGS-SLAM system presents a notable advancement in the field of real-time 3D Gaussian Splatting (3DGS)-based SLAM, addressing several limitations of existing approaches. Its significance and potential impact can be summarized as follows:

*   **Real-time Photorealistic Mapping in Large-scale Environments**: By successfully integrating 3DGS with a tightly coupled LiDAR-Inertial-Visual (LIV) SLAM framework, RMGS-SLAM enables continuous, photorealistic 3D map reconstruction while maintaining real-time performance. This capability is crucial for applications requiring detailed visual fidelity and environmental understanding over extended areas.
*   **Enhanced Localization Accuracy and Global Consistency**: The system's multi-sensor fusion approach contributes to robust pose estimation. Critically, the explicit Gaussian-based loop closure mechanism directly addresses the challenge of accumulated drift in large-scale scenes, leading to significantly improved global consistency of both the trajectory and the 3D map. This is a key requirement for long-term autonomy and consistent environmental representations.
*   **Improved Gaussian Initialization Strategy**: The cascaded Gaussian initialization, combining feed-forward predictions with voxel-PCA geometric priors, is a methodological contribution that improves the quality of initial Gaussian primitives. This strategy accelerates the convergence of the subsequent optimization process, which is essential for achieving high-fidelity 3DGS maps efficiently in real-time.
*   **Robustness to Challenging Conditions**: The LIV fusion provides an inherent robustness benefit, making the system more resilient to various environmental challenges such as varying illumination, feature sparsity, and sensor noise, which often plague monomodal or loosely coupled systems.
*   **Contribution of a New Benchmark Dataset**: The collection and release of a challenging large-scale looped outdoor SLAM dataset with synchronized LiDAR, camera, IMU, and ground-truth trajectories provide a valuable resource for the research community. This dataset enables more comprehensive and realistic evaluations of future 3DGS-based SLAM systems under practical conditions.
*   **Foundation for Downstream Robotic Tasks**: The ability to generate real-time, globally consistent, and photorealistic 3D maps has broad implications for various robotic applications. These include enhanced autonomous navigation, where robots can use perceptually rich maps for path planning and obstacle avoidance; improved object manipulation, where high-fidelity scene representations can aid in grasping and interaction; and immersive augmented/virtual reality experiences that require accurate and visually detailed environment models.

While acknowledging that the current system relies on high-performance hardware, the foundational advancements in balancing real-time efficiency, localization accuracy, and rendering quality position RMGS-SLAM as a significant step towards practical and robust photorealistic SLAM for advanced robotic systems and immersive computing. Future work focused on computational efficiency could further broaden its applicability to a wider range of platforms and tasks.
