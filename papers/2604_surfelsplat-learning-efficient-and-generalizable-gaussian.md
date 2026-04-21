---
title: "SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction"
date: 2026-04-09
arxiv: "2604.08370v1"
venue:
status: to-read

abstract: "3D Gaussian Splatting (3DGS) has demonstrated impressive performance in 3D scene reconstruction. Beyond novel view synthesis, it shows great potential for multi-view surface reconstruction. Existing methods employ optimization-based reconstruction pipelines that achieve precise and complete surface extractions. However, these approaches typically require dense input views and high time consumption for per-scene optimization. To address these limitations, we propose SurfelSplat, a feed-forward framework that generates efficient and generalizable pixel-aligned Gaussian surfel representations from sparse-view images. We observe that conventional feed-forward structures struggle to recover accurate geometric attributes of Gaussian surfels because the spatial frequency of pixel-aligned primitives exceeds Nyquist sampling rates. Therefore, we propose a cross-view feature aggregation module based on the Nyquist sampling theorem. Specifically, we first adapt the geometric forms of Gaussian surfels with spatial sampling rate-guided low-pass filters. We then project the filtered surfels across all input views to obtain cross-view feature correlations. By processing these correlations through a specially designed feature fusion network, we can finally regress Gaussian surfels with precise geometry. Extensive experiments on DTU reconstruction benchmarks demonstrate that our model achieves comparable results with state-of-the-art methods, and predict Gaussian surfels within 1 second, offering a 100x speedup without costly per-scene training."

website: 
code: https://github.com/Simon-Dcs/Surfel_Splat
openreview: 
issue: 24

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

# SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction

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

![Figure](https://arxiv.org/html/2604.08370v1/x1.png)

*Figure 1: Our method delivers state-of-the-art surface reconstruction with ultra-fast inference speed. (a) Framework visualization: Given an image pair, our approach regresses Gaussian radiance fields capturing fine geometric details in just 1 second. (b) Quantitative comparisons: Our method achieves superior reconstruction accuracy while maintaining the fastest runtime among existing approaches.*

![Figure](https://arxiv.org/html/2604.08370v1/x2.png)

*Figure 2: Experimental Observation. (a) Current feed-forward networks generate geometrically inaccurate Gaussian radiance fields. (b) The correlated image regions of pixel-aligned Gaussian surfels exhibit rotation invariance, limiting the network’s ability to accurately infer surface orientations.*

![Figure](https://arxiv.org/html/2604.08370v1/x3.png)

*Figure 3: Pipeline. Given an image pair, our method first extracts initial image features using a backbone image encoder. We then predict Gaussian features and depth maps of the scene. Since 2D radiance fields are geometrically inaccurate, we apply Nyquist theorem-guided surfel adaptation to each surfel. In the feature aggregation module, we project the adapted surfels across views to identify image regions containing relevant geometric information. After refining the image features with these related regions, we regress the Gaussian radiance fields again to obtain accurate representations.*

![Figure](https://arxiv.org/html/2604.08370v1/x4.png)

*Figure 4: Qualitative Comparison of Surface Reconstruction with Sparse Views on DTU Benchmarks.*

![Figure](https://arxiv.org/html/2604.08370v1/x5.png)

*Figure 5: Visualization of Nyquist Theorem Verification*

![Figure](https://arxiv.org/html/2604.08370v1/x6.png)

*Figure 6: Nyquist Theorem Verification: (a) Before adaptation, most surfels exceed the Nyquist threshold, resulting in inaccurate geometry prediction. (b) After the adaptation module, all Gaussian primitives fall within the Nyquist threshold, ensuring accurate geometric feature learning.*

![Figure](https://arxiv.org/html/2604.08370v1/x7.png)

*Figure 7: Visual comparison of 2-view reconstruction on BlendedMVS dataset.*

![Figure](https://arxiv.org/html/2604.08370v1/x8.png)

*Figure 8: Visual comparison of novel view synthesis on DTU dataset.*

## LLM Summary

The following report provides a detailed analysis of the research paper "SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction."

---

## Detailed Report on "SurfelSplat: Learning Efficient and Generalizable Gaussian Surfel Representations for Sparse-View Surface Reconstruction"

### 1. Authors and Institution(s)

The authors of this research paper are Chensheng Dai, Shengjun Zhang, Min Chen, and Yueqi Duan. Chensheng Dai and Shengjun Zhang are noted as equal contributors, and Yueqi Duan is the corresponding author. All authors are affiliated with Tsinghua University.

### 2. How This Work Fits into the Broader Research Landscape

The reconstruction of accurate 3D surfaces from multi-view images is a long-standing challenge in computer vision. Historically, methods focused on Multi-View Stereo (MVS) techniques, which primarily capture geometric details. More recent advancements have centered around neural implicit representations, such as Neural Radiance Fields (NeRF) and Signed Distance Functions (SDFs). These methods, including NeuS, NeuSurf, and UFORecon, have demonstrated progress in recovering smooth and complete surfaces. However, a common limitation of many optimization-based neural implicit methods is their requirement for dense input views and extensive per-scene optimization, often taking hours to converge. While some works have addressed sparse-view reconstruction with neural implicit representations, they generally still require significant per-scene computation.

Concurrently, 3D Gaussian Splatting (3DGS) has emerged as a neural explicit representation, gaining attention for its rapid rendering speed and high visual fidelity in novel view synthesis. The 3DGS framework also holds potential for surface reconstruction, leading to adapted approaches like SuGaR, 2DGS, Gaussian Surfels, NeuSG, and GSDF. These methods modify the geometric shape of Gaussian representations or combine them with implicit representations to improve surface alignment and extraction. Nevertheless, these 3DGS-based methods typically require dense views to prevent overfitting to camera poses, which can lead to geometric inaccuracies or "collapse" when presented with limited viewpoint information, such as only two input images.

To circumvent the computational burden of per-scene optimization and achieve generalizable, efficient scene reconstruction, feed-forward networks have been developed. Examples include pixelNeRF, pixelSplat, and MVSplat. These models learn priors from large datasets, enabling direct prediction of 3D representations through a single inference pass, often generating pixel-aligned Gaussian primitives. While these feed-forward approaches have demonstrated efficacy in fast and generalizable novel view synthesis, their application to surface reconstruction, which demands higher precision in Gaussian primitive geometry, remains largely underexplored. Existing feed-forward methods often struggle to recover accurate surface orientations, with predicted surfels tending to align parallel to the image plane rather than with the actual surface.

SurfelSplat aims to bridge this gap by developing a feed-forward framework that generates efficient and generalizable pixel-aligned Gaussian surfel representations specifically tailored for sparse-view surface reconstruction. It addresses the geometric inaccuracy observed in prior feed-forward methods by incorporating principles from the Nyquist sampling theorem, thereby enabling the prediction of geometrically precise Gaussian surfels without costly per-scene optimization.

### 3. Key Objectives and Motivation

The primary objective of this research is to develop an efficient and generalizable feed-forward framework, named SurfelSplat, for high-fidelity 3D surface reconstruction from sparse multi-view images. This goal is motivated by several identified limitations in the existing research landscape:

1.  **High Computational Cost of Optimization-Based Methods:** Current state-of-the-art methods for precise and complete surface extraction, particularly those based on neural implicit representations (e.g., NeRF, SDFs) or optimization-driven 3D Gaussian Splatting, typically rely on per-scene optimization. This process is computationally intensive, requiring dense input views and often hours of training per scene (e.g., NeuS, NeuSurf taking 10-14 hours). This makes them impractical for applications requiring rapid reconstruction or deployment in resource-constrained environments.

2.  **Lack of Generalizability in Many High-Precision Methods:** Optimization-based methods often overfit to specific scenes and camera poses, necessitating retraining for each new scene. This limits their generalizability and usability in dynamic or large-scale applications.

3.  **Geometric Inaccuracy in Existing Feed-Forward Networks for Surface Reconstruction:** While feed-forward networks (e.g., pixelSplat, MVSplat) offer speed and generalizability for novel view synthesis by directly regressing 3D Gaussian parameters, they have not been effectively applied to precise surface reconstruction. A critical observation made by the authors is that these networks often fail to recover accurate geometric attributes, such as surface normal vectors, of pixel-aligned Gaussian surfels. Specifically, the predicted Gaussian surfels tend to orient parallel to the image plane rather than aligning with the true surface geometry.

4.  **Theoretical Explanation for Geometric Inaccuracy:** The authors hypothesize that this geometric inaccuracy stems from a fundamental signal processing principle: the Nyquist sampling theorem. They propose that the spatial frequency of pixel-aligned Gaussian surfels, as learned by conventional feed-forward structures, can exceed the Nyquist sampling rate. This violation of sampling principles means that the corresponding image regions do not provide sufficient supervisory information for the network to accurately infer the covariance and orientation of Gaussian surfels, leading to undersampling artifacts in the reconstructed geometry.

To address these motivations, SurfelSplat aims to:
*   Propose a feed-forward framework that directly regresses 2D Gaussian surfels from sparse-view images for surface reconstruction, bypassing per-scene optimization.
*   Conduct a detailed analysis using the Nyquist sampling theorem to explain why current feed-forward frameworks generate geometrically inaccurate Gaussian primitives.
*   Introduce novel mechanisms, specifically Nyquist theorem-guided Gaussian surfel adaptations and feature aggregations, to ensure that Gaussian primitives adhere to sampling rate constraints, thereby achieving superior geometric properties.
*   Demonstrate that this approach can generate surface-aligned Gaussian radiance fields with high efficiency and accurate geometry, comparable to state-of-the-art optimization-based methods, but with significantly faster inference times.

### 4. Methodology and Approach

SurfelSplat is a feed-forward framework designed to predict 2D Gaussian radiance fields with accurate geometry, guided by the Nyquist sampling theorem. The methodology can be broken down into several key components:

**4.1. Initial Feature Extraction and Gaussian Parameter Prediction:**
The process begins with N multi-view input images and their corresponding camera parameters. A backbone image encoder, incorporating epipolar transformers and DINO feature backbones, extracts initial image features (F). These features are then fed into two distinct regression networks:
*   $\Phi_{depth}$ predicts per-view depth maps ($d_i$). These depth maps are then unprojected ($\psi_{unproj}$) to obtain the 3D center positions ($\mu_i$) for each Gaussian primitive.
*   $\Phi_{attr}$ predicts initial Gaussian attributes ($f_i = [s_i, r_i, \sigma_i, c_i]$), which include scaling, rotation, opacity, and color.

**4.2. Sensitivity to Sampling Rates for Pixel-Aligned Gaussian Surfels (Nyquist Analysis):**
The core of SurfelSplat's innovation lies in its theoretical analysis of geometric inaccuracies.
*   **Nyquist Sampling Theorem:** The paper reiterates the Nyquist condition, stating that for precise reconstruction of a continuous signal, the spatial sampling rate ($\hat{\nu}$) must be at least twice the signal bandwidth ($\nu$).
*   **Spatial Sampling Rates in Multi-Camera Systems:** For a single camera, the sampling interval in the image plane corresponds to a 3D surface area. The spatial sampling rate ($\hat{\nu}_{sampling}$) at a given pixel is derived as $\frac{f_x f_y}{d^2}$, where $f_x, f_y$ are focal lengths and $d$ is the depth. For a multi-camera system, the authors define the overall sampling frequency for a Gaussian primitive $p_k$ as the maximum frequency observed across all visible cameras ($\hat{\nu}_k = \max_{i} \{V_i(p_k) \cdot |J_i|\}$). This ensures that the primitive is sufficiently sampled from at least one viewpoint.
*   **Spatial Frequency of 2D Gaussian Primitives:** The spatial frequency of a 2D Gaussian primitive is derived using its Spatial Fourier Transform. For a Gaussian with scaling parameters $s_u$ and $s_v$ along its tangent vectors, the spatial frequencies are $\nu_u = \frac{1}{\pi s_u}$ and $\nu_v = \frac{1}{\pi s_v}$.
*   **Problem Identification:** The analysis concludes that if $\nu_{surfel} > \frac{\hat{\nu}_{sampling}}{2}$, the Nyquist criterion is violated, leading to insufficient information for the network to accurately learn spatial parameters like covariance, resulting in geometrically misaligned surfels.

**4.3. Nyquist Theorem-Guided Gaussian Surfel Adaptation:**
To address the Nyquist violation, SurfelSplat introduces an adaptive surfel adaptation module operating in the frequency domain.
*   Each 2D Gaussian primitive ($G_k$) is convolved with an adaptive Gaussian low-pass filter ($G_{low_k}$). The filter's form is $G_{low_k}(x) = e^{-\frac{\hat{\nu}_k^2 u^2}{2s^2} - \frac{\hat{\nu}_k^2 v^2}{2s^2}}$, where $\hat{\nu}_k$ is the derived sampling rate for that primitive and $s$ is a hyperparameter.
*   This process effectively constrains the maximum frequency of $G_k$ according to the local spatial sampling rates, modifying the primitive's scaling matrix.
*   The adaptation ensures that the spatial frequency of the adapted surfel ($\hat{G}_{adapted_k}$) satisfies the Nyquist criterion (i.e., $\nu_k < \frac{\hat{\nu}_k}{2}$), regardless of variations in spatial sampling rates.

**4.4. Nyquist Theorem-Guided Gaussian Feature Aggregation:**
Following surfel adaptation, a feature aggregation module refines the Gaussian representations.
*   **Cross-view Projection:** The adapted 2D Gaussian primitives ($\hat{G}_{adapted_k}$) are projected back onto all input viewpoints.
*   **Region Identification:** For each primitive, image regions ($R^i_k$) are identified where the splatted Gaussian value exceeds a predefined threshold. These regions are deemed to contain geometrically relevant information for the primitive.
*   **Feature Collection:** Image features ($F_{geo_k}$) from these identified regions across all views are collected.
*   **Feature Refinement Network:** A cross-attention-based feature refinement network ($\Phi_{refine}$) takes the initial image feature ($F_k$) as a query and the collected geometric features ($F_{geo_k}$) as key and value. This enhances $F_k$ to produce refined features ($F_{refined_k}$).
*   **Final Prediction:** The refined features ($F_{refined_k}$) are then passed to the same Gaussian attribute prediction head ($\Phi_{attr}$) to regress geometry-aware pixel-aligned 2D Gaussian primitives ($\hat{f}_i$).

**4.5. Loss Design:**
The overall loss function ($L$) combines a rendering loss and a geometric loss:
*   **Rendering Loss ($L_{render}$):** Consists of RGB mean square error and LPIPS loss, ensuring high visual fidelity of rendered images.
*   **Geometric Loss ($L_{geo}$):** Includes a surface alignment term (based on normal consistency), depth mean square error ($L_d$), and normal mean square error ($L_n$). This loss component drives the Gaussian surfels to align accurately with the underlying 3D surface geometry.

**4.6. Training Strategy:**
The model employs a two-stage curriculum learning strategy:
1.  **Initial Phase:** Pre-training on large-scale diverse scene datasets, specifically RealEstate10K, for 300,000 iterations to learn rich generalizable priors.
2.  **Refinement Phase:** Fine-tuning on smaller datasets with ground truth depth and surface measurements, such as DTU, for 2,000 iterations to enhance precision in depth estimation and geometric detail.

### 5. Main Findings and Results

The research paper presents several findings demonstrating the efficacy and advantages of SurfelSplat:

**5.1. Sparse-View Surface Reconstruction Accuracy:**
*   **Quantitative Performance:** On the DTU dataset, SurfelSplat achieves a mean D2S Chamfer Distance (CD) of 1.12, which is the lowest among all compared state-of-the-art methods. This performance surpasses both neural implicit methods (e.g., NeuSurf (1.44), VolRecon (1.67), UFORecon (1.91)) and other neural explicit methods (e.g., 2DGS (3.02), GausSurf (4.36), FatesGS (1.18)).
*   **Qualitative Performance:** Visual comparisons on DTU benchmarks indicate that SurfelSplat generates superior global geometry with enhanced surface details. It exhibits improved global surface smoothness compared to UFORecon, which can produce coarse global geometry, and refines local details that methods like 2DGS might miss, leading to incomplete surfaces. Qualitative results on the BlendedMVS dataset further demonstrate consistent and stable performance.

**5.2. Efficiency:**
*   SurfelSplat demonstrates a significant advantage in inference speed. It predicts Gaussian surfels and performs surface reconstruction within approximately 1 second per scene on DTU benchmarks.
*   This represents a substantial speedup compared to other approaches: neural implicit methods typically require 10-14 hours (NeuS, NeuSurf), and even other neural explicit methods like 2DGS and FatesGS require 10-14 minutes. Even faster implicit methods like VolRecon and UFORecon take 60-100 seconds. This efficiency is achieved without costly per-scene training.

**5.3. Experimental Nyquist Theorem Verification:**
*   The empirical results support the theoretical analysis regarding the Nyquist sampling criterion.
*   **Before Adaptation:** The normalized frequency ratio ($\nu_{surfel} / \hat{\nu}_{Nyquist}$) for almost all Gaussian primitives exceeds 1, indicating that the Nyquist threshold is violated. This explains the observed geometric inaccuracies in standard feed-forward networks.
*   **After Adaptation:** Following the application of the surfel adaptation module, all Gaussian primitives fall within the Nyquist frequency boundary (ratio < 1).
*   **Visual Confirmation:** Rendered normal maps show significant differences and improvements before and after the surfel adaptation module, providing visual evidence of more precise geometry recovery.

**55.4. Ablation Studies:**
*   Experiments systematically evaluate the contribution of each proposed module.
*   **Without Surfel Adaptation:** Removing the surfel adaptation module results in a substantial degradation in performance, with Chamfer Distance increasing from 1.12 to 2.56 and Normal Mean Square Error (MSE) increasing from 0.060 to 0.135.
*   **Without Feature Aggregation:** Removing the feature aggregation module also leads to performance degradation, with Chamfer Distance increasing to 1.96 and Normal MSE to 0.115.
*   These results confirm the necessity and effectiveness of both the Nyquist theorem-guided surfel adaptation and feature aggregation modules for achieving accurate surface reconstruction.

**5.5. Novel View Synthesis:**
*   Experiments on novel view synthesis on the DTU dataset demonstrate that SurfelSplat achieves superior visual fidelity compared to existing methods like pixelSplat and MVSplat. This is attributed to the model's ability to capture fine-grained geometric details more effectively.

### 6. Significance and Potential Impact

The development of SurfelSplat represents a notable advancement in the field of 3D surface reconstruction, particularly for sparse-view scenarios.

**Technical Contributions:**
*   **Addressing Geometric Inaccuracy in Feed-Forward Networks:** The paper provides a theoretical explanation, grounded in the Nyquist sampling theorem, for the geometric inaccuracies encountered when applying feed-forward networks to surface reconstruction tasks. This analysis is a novel contribution that moves beyond empirical observation.
*   **Novel Methodology:** The introduction of Nyquist theorem-guided Gaussian surfel adaptation and feature aggregation modules provides a principled approach to constrain the spatial frequency of Gaussian primitives, ensuring they are adequately sampled and allowing for the learning of precise geometric attributes. This is a significant methodological innovation for generalizable 3D reconstruction.
*   **Efficiency and Generalizability:** By successfully integrating accurate surface reconstruction into a feed-forward architecture, SurfelSplat achieves a substantial improvement in efficiency, with inference times reduced to approximately 1 second. This speed, combined with its generalizable nature (no per-scene optimization), makes it suitable for real-time or near-real-time applications.

**Potential Impact:**
*   **Accelerated 3D Content Creation:** The rapid reconstruction capability could significantly accelerate workflows in various industries, including film production, game development, and digital archiving, by enabling quick generation of 3D models from limited photographic input.
*   **Robotics and Autonomous Systems:** Fast and accurate 3D surface reconstruction from sparse data is critical for robotic perception, navigation, and interaction with environments, especially in scenarios where computational resources are limited or real-time understanding is required.
*   **Augmented/Virtual Reality (AR/VR):** The method could facilitate faster scene understanding and environment mapping for AR/VR applications, improving immersion and interaction by enabling quick generation of coherent 3D representations.
*   **Reduced Computational Resources:** By eliminating the need for hours of per-scene optimization, SurfelSplat reduces the computational resources (and thus energy consumption) required for individual reconstruction tasks, which could be beneficial for accessibility and environmental impact if overall usage does not proportionally increase.
*   **Democratization of 3D Modeling:** The lower barrier to entry in terms of computational resources and technical expertise (due to the feed-forward nature) could broaden access to high-quality 3D modeling capabilities for researchers, hobbyists, and institutions with limited infrastructure.

**Limitations and Future Directions:**
The authors acknowledge several limitations that indicate avenues for future research:
*   **Resolution Sensitivity:** The pixel-aligned Gaussian representation leads to a rapid increase in the number of Gaussians (and thus inference/rendering time) with higher input resolutions (e.g., 1 million Gaussians for 1024x1024 inputs). Future work could explore adaptive Gaussian representations or hierarchical structures to manage this scaling.
*   **Redundancy in Representations:** Combining Gaussian groups from different viewpoints can lead to redundant representations in overlapping regions. Optimizing for non-redundant representations could further enhance efficiency.
*   **Limited Generalizability to Unseen Parts:** Like many reconstruction methods, performance can degrade for unseen parts of a scene. Integrating generative models, such as diffusion models, could potentially address this by hallucinating plausible geometry for occluded or unobserved regions.
*   **Camera Pose Configuration Sensitivity:** The current method may struggle with credible depth prediction when input views have small overlap regions, partly due to the scale of training data. Incorporating techniques from methods trained on vast datasets with explicit depth regularization could improve robustness across diverse camera configurations.
