---
title: "WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images"
date: 2026-04-23
arxiv: "2604.21182v1"
venue:
status: to-read

abstract: "We propose WildSplatter, a feed-forward 3D Gaussian Splatting (3DGS) model for unconstrained images with unknown camera parameters and varying lighting conditions. 3DGS is an effective scene representation that enables high-quality, real-time rendering; however, it typically requires iterative optimization and multi-view images captured under consistent lighting with known camera parameters. WildSplatter is trained on unconstrained photo collections and jointly learns 3D Gaussians and appearance embeddings conditioned on input images. This design enables flexible modulation of Gaussian colors to represent significant variations in lighting and appearance. Our method reconstructs 3D Gaussians from sparse input views in under one second, while also enabling appearance control under diverse lighting conditions. Experimental results demonstrate that our approach outperforms existing pose-free 3DGS methods on challenging real-world datasets with varying illumination."

website: 
code: https://github.com/yfujimura/WildSplatter
openreview: 
issue: 33

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

# WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images

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

![Figure](https://arxiv.org/html/2604.21182v1/x1.png)

*Figure 1: We propose WildSplatter, a feed-forward 3DGS model for unconstrained images with unknown camera parameters and varying lighting conditions. Our method reconstructs 3D Gaussians and appearance embeddings from sparse input views in under one second, while also enabling appearance control under diverse lighting conditions.*

![Figure](https://arxiv.org/html/2604.21182v1/x2.png)

*Figure 2: Overview of the proposed method. Given sparse-view context images captured under inconsistent lighting, the model first estimates colorless 3D Gaussian geometry and local scene features. During training, target images are additionally used to extract global appearance embeddings, which are combined with local features to predict Gaussian colors. This design enables disentangled modeling of geometry and appearance for robust rendering under varying lighting conditions.*

![Figure](https://arxiv.org/html/2604.21182v1/x3.png)

*Figure 3: Examples of training samples. The first two rows show context images captured under different lighting conditions, while the third row shows the corresponding target images. The last row shows visibility masks computed by warping depth maps from the target views to the context views.*

![Figure](https://arxiv.org/html/2604.21182v1/x4.png)

*Figure 4: Qualitative comparison for novel-view synthesis on the NeRF-OSR dataset [22].*

![Figure](https://arxiv.org/html/2604.21182v1/x5.png)

*Figure 5: Appearance interpolation. The first and third rows show rendered images from novel views with fixed appearance embeddings from the two input views, respectively. The second row shows rendered images with linearly interpolated appearance embeddings.*

![Figure](https://arxiv.org/html/2604.21182v1/x6.png)

*Figure 6: (a) t-SNE visualization [28] of learned appearance embeddings, where each point corresponds to an image and colors indicate K-means clusters. (b) Representative images for each cluster, showing that images within the same cluster share similar appearance characteristics.*

![Figure](https://arxiv.org/html/2604.21182v1/x7.png)

*Figure 7: Cross-dataset appearance control. The geometry of 3D Gaussians estimated from context views is kept fixed, while their colors are modulated using appearance embeddings extracted from reference images of different scenes.*

![Figure](https://arxiv.org/html/2604.21182v1/x8.png)

*Figure 8: From left to right: context images, estimated opacity maps for the context views, target image, rendered target image, and the visibility mask at the target view. The model suppresses transient objects by assigning low opacity values.*

## LLM Summary

### 1. Authors and Institution(s)

The research paper "WildSplatter: Feed-forward 3D Gaussian Splatting with Appearance Control from Unconstrained Images" was authored by:

*   **Yuki Fujimura:** NAIST
*   **Takahiro Kushida:** Ritsumeikan University
*   **Kazuya Kitano:** NAIST
*   **Takuya Funatomi:** Kyoto University
*   **Yasuhiro Mukaigawa:** NAIST

### 2. How This Work Fits into the Broader Research Landscape

The field of 3D scene representation and novel view synthesis has advanced significantly with the emergence of Neural Radiance Fields (NeRFs) and, more recently, 3D Gaussian Splatting (3DGS). The original 3DGS framework [14] offers high-quality, real-time rendering of complex 3D scenes by optimizing volumetric Gaussian primitives from multi-view images. However, its practical application is limited by several requirements: it necessitates iterative optimization for each scene, requires images captured under consistent lighting conditions, and depends on known camera parameters for the input views.

To address the computational expense of iterative optimization, a line of research has focused on **feed-forward 3DGS models** [2, 4, 5]. These models take sparse input views and directly predict pixel-aligned 3D Gaussians, enabling faster inference. Further enhancing real-world applicability, **pose-free feed-forward 3DGS models** [12, 25, 35, 38] have emerged, eliminating the need for known extrinsic or intrinsic camera parameters. These often build upon 3D vision foundation models like DUSt3R [31], MASt3R [29], or Depth Anything 3 [16].

Another significant challenge is handling **unconstrained images** with varying lighting conditions, common in real-world photo collections (e.g., outdoor scenes captured at different times or weather). While the original 3DGS uses spherical harmonics for view-dependent effects, it struggles with large appearance variations. NeRF-based methods like NeRF-W [18] and Ha-NeRF [3] introduced per-image appearance embeddings to model such variations. Similarly, 3DGS has been extended to unconstrained images through methods like SWAG [6], WildGaussians [15], Wild-GS [32], and GS-W [36], which typically use learnable appearance embeddings or reference image features. However, these appearance-aware 3DGS approaches still rely on iterative optimization and generally assume known camera parameters.

WildSplatter positions itself at the intersection of these advancements, aiming to bridge the gap between efficient, pose-free 3DGS and robust appearance modeling for unconstrained, variable-lighting images. Existing pose-free feed-forward 3DGS methods often struggle with significant appearance changes across inputs, while existing appearance-aware 3DGS methods are typically optimization-based and require known camera poses. WildSplatter seeks to integrate the benefits of feed-forward and pose-free reconstruction with a flexible appearance control mechanism, providing a comprehensive solution for unconstrained real-world image datasets.

### 3. Key Objectives and Motivation

The primary objective of this research is to develop a feed-forward 3D Gaussian Splatting (3DGS) model, named WildSplatter, that can generate high-quality novel views from unconstrained image collections. This model specifically aims to address the challenges posed by unknown camera parameters and varying lighting conditions in real-world datasets.

The motivation behind WildSplatter stems from several limitations of existing 3DGS frameworks:

1.  **Computational Efficiency and Real-time Performance:** The original 3DGS framework, while producing high-quality renders, necessitates iterative optimization for each new scene. This process is computationally intensive and time-consuming, hindering its use in applications requiring rapid scene reconstruction or dynamic updates. The authors are motivated to achieve fast inference, ideally under one second, by employing a feed-forward approach.

2.  **Broader Applicability in Real-World Scenarios (Pose-Free):** Many real-world image collections, particularly those gathered from the internet or consumer-grade cameras, lack precise camera parameters (intrinsics and extrinsics). This absence restricts the direct application of standard 3DGS. The research aims to overcome this by designing a "pose-free" model, making 3DGS accessible to a wider array of uncalibrated image datasets.

3.  **Robustness to Appearance Variations (Unconstrained Lighting):** Traditional 3DGS models are generally optimized from images captured under consistent lighting conditions. However, "in-the-wild" datasets, especially outdoor scenes, often exhibit significant appearance variations due to changes in time of day, weather, or camera settings. While some prior works have extended 3DGS to handle appearance variations, these typically rely on iterative optimization and known camera parameters, making them inefficient for large-scale, unconstrained data. WildSplatter is motivated to effectively model and control these large appearance shifts, providing photorealistic novel views despite inconsistent input illumination.

To achieve these goals, the specific objectives of WildSplatter are:

*   To propose a novel feed-forward, pose-free 3DGS model capable of reconstructing 3D Gaussians from sparse input views.
*   To introduce a joint learning framework that estimates both 3D Gaussian geometry and appearance embeddings, conditioned on the input images. This framework is intended to allow flexible modulation of Gaussian colors to account for diverse lighting and appearance conditions.
*   To validate that the learned appearance embeddings can generalize across different scenes, enabling capabilities such as appearance interpolation and cross-dataset appearance control.
*   To quantitatively and qualitatively demonstrate that the proposed method outperforms existing pose-free 3DGS approaches on challenging real-world datasets that feature varying illumination.

### 4. Methodology and Approach

WildSplatter is a pose-free, feed-forward 3D Gaussian Splatting model designed to operate on unconstrained image collections with unknown camera parameters and varying lighting. The core methodology involves explicitly disentangling the estimation of 3D Gaussian geometry from their appearance.

**Architecture Overview:**
The model's architecture is built upon the framework of Depth Anything 3 [16], incorporating a Vision Transformer (ViT) encoder (based on DINOv2 [20]) and DPT heads [21]. The ViT encoder is partitioned into two components:
*   **ViT_1:** Handles local (intra-frame) attention to extract frame-level features from individual input images.
*   **ViT_2:** Incorporates global (inter-frame) attention to aggregate features across multiple frames.

**Input Processing:**
The model accepts sparse-view *context images* ($\{I^c_i\}$) and, during training, also *target images* ($\{I^t_j\}$). All images are initially processed by ViT_1 independently to generate context and target feature tokens. The context feature tokens are then passed through ViT_2 for cross-frame feature aggregation.

**Geometry Estimation of 3D Gaussians:**
The geometry of 3D Gaussians (centers, opacities, rotations, and scales) is estimated exclusively from the context images, operating on the assumption that scene geometry remains largely invariant to lighting changes.
1.  **Depth and Ray Estimation:** Feature tokens from the context images (output of ViT_2) are fed into a dual-DPT head [16] to estimate depth maps ($\{D_i\}$) and ray origins/directions ($\{[o_i, d_i]\}$) for each context image.
2.  **Gaussian Parameter Prediction:** Another DPT head processes the same context feature tokens to predict Gaussian parameters: opacity ($\alpha_i$), rotation ($r_i$), scale ($s_i$), and depth offsets ($\Delta D_i$).
3.  **Gaussian Center Computation:** The Gaussian centers ($\mu_i$) are calculated by extending ray origins along their directions, using the estimated depth maps and depth offsets: $\mu_i = o_i + (D_i + \Delta D_i)d_i$.
4.  **Local Scene Features:** Feature maps ($\{f_i\}$) encoding local scene information are also extracted from an intermediate layer of this DPT head, which are later used for appearance estimation.

**Appearance Estimation of 3D Gaussians:**
To address the challenge of varying lighting, WildSplatter estimates a global appearance embedding for each target image, which then modulates the Gaussian colors.
1.  **Global Appearance Embedding:** A learnable "appearance token" is concatenated with the feature tokens of each target image (output of ViT_1). These are then processed by shallow Transformer blocks, and the resulting token is passed through a shallow Multi-Layer Perceptron (MLP) to produce a global appearance embedding ($e_j$) for image $I^t_j$. This embedding represents the global appearance characteristics of the target image.
2.  **Gaussian Color Prediction:** The global appearance embedding ($e_j$) is spatially broadcast to match the resolution of the local feature maps. It is then concatenated channel-wise with the local scene feature maps ($\{f_i\}$) obtained during geometry estimation. These combined features are fed into two convolutional layers to estimate the spherical harmonics coefficients ($\{c^j_i\}$) for Gaussian colors.
3.  **Final 3D Gaussians:** The complete 3D Gaussians for each target image are thus represented as $\{\mu_i, \alpha_i, r_i, s_i, c^j_i\}$.

**Training Details:**
*   **Dataset:** The model is trained on the MegaScenes dataset [27], a collection of unconstrained internet photos of landmarks.
*   **Training Sample Construction:** Monocular depth maps (from Depth Anything 3) are first estimated for all images and aligned with COLMAP sparse depth. Images are then selected based on sufficient overlap (computed by warping depth maps between views) to form training samples, each consisting of two context views ($\text{N}_\text{c}=2$) and one target view ($\text{N}_\text{t}=1$). Context views are chosen from different dates/lighting conditions, and target views are interpolated between context views.
*   **Visibility Masks:** To handle unobserved regions and transient objects, visibility masks ($M_j$) are computed for target views based on depth consistency. These masks are extended to include sky regions ($M^s_j$). The masks are applied to target views during loss computation, while the model implicitly learns to suppress transient objects in context views by adjusting their opacities.
*   **Training Loss:** The training loss is a combination of pixel-wise Mean Squared Error (MSE) and LPIPS perceptual loss [37], applied to the masked regions of the rendered target images ($\hat{I}^t_j$) compared to the ground-truth target images ($I^t_j$):
    $L = \sum_{j=1}^{N_t} \text{MSE}(M^s_j \odot I^t_j, M^s_j \odot \hat{I}^t_j) + \lambda \text{LPIPS}(M^s_j \odot I^t_j, M^s_j \odot \hat{I}^t_j)$.
*   **3D Gaussian Alignment:** During training, a scale factor and translation vector are estimated using a weighted least-squares formulation to align the scale of the model's output 3D Gaussians with the dataset's ground-truth scale. Weights are derived from multi-view consistency of dataset depths.
*   **Implementation:** The model is initialized with a pretrained Depth Anything 3. The ViT backbone and depth/ray estimation dual-DPT head are frozen. Only the DPT head for Gaussian parameter prediction and the appearance estimation module are trained. Input image resolution is 504x504. The appearance embedding dimension ($d_g$) is set to 32. Training uses AdamW optimizer for 15K iterations on multiple GPUs.

### 5. Main Findings and Results

The evaluation of WildSplatter primarily focused on its ability to perform novel view synthesis from unconstrained images with varying lighting and unknown camera parameters, comparing its performance against current state-of-the-art methods.

**Quantitative Performance for Novel-View Synthesis:**
The method was evaluated on the NeRF-OSR dataset [22], which consists of outdoor image sequences with varying lighting conditions. WildSplatter's performance was measured using PSNR (higher is better) and LPIPS (lower is better) metrics for novel view synthesis, with 2, 3, or 4 context images.
*   WildSplatter consistently demonstrated superior performance over competing state-of-the-art pose-free feed-forward 3DGS models, including SPFSplat [11], AnySplat [12], and Depth Anything 3 [16], across most scenes and input view counts.
*   The model also outperformed WildGaussians [15], an optimization-based 3DGS method with appearance modeling, particularly benefiting from its feed-forward nature and pose-free capabilities when dealing with sparse inputs.
*   The results indicated that while increasing context views generally aids reconstruction, the performance gain was not always strictly monotonic for all methods, which the authors attribute to the challenging nature of the dataset (varying lighting conditions across context images and target image selection protocol).

**Qualitative Performance for Novel-View Synthesis:**
Qualitative comparisons (Figure 4) highlighted WildSplatter's ability to accurately model appearance variations. While other feed-forward 3DGS baselines tended to produce rendered novel views with "mixed appearance" due to inconsistent lighting in the input, WildSplatter generated outputs that correctly reflected the desired appearance, matching the specific target lighting conditions.

**Appearance Control Capabilities:**
*   **Appearance Interpolation:** The learned appearance embeddings enabled flexible appearance control. By linearly interpolating between appearance embeddings derived from two different context views, WildSplatter successfully generated a smooth transition of appearance in novel views (Figure 5). This demonstrates the interpretability and continuity of the learned latent space for appearance.
*   **Cross-dataset Appearance Control:** The learned embeddings exhibited generalization capabilities across scenes. WildSplatter could take 3D Gaussian geometry estimated from one set of context views and modulate its colors using appearance embeddings extracted from reference images of entirely different scenes (Figure 7). This suggests that the appearance embeddings capture generic lighting and stylistic attributes.

**Analysis of Learned Appearance Embeddings:**
*   A t-SNE visualization [28] of appearance embeddings showed that images with similar visual characteristics (e.g., specific lighting, time of day) clustered together in the embedding space (Figure 6). This provides empirical evidence that the model learns meaningful and discriminative representations of appearance.
*   An ablation study confirmed that a relatively low-dimensional appearance embedding (d_g = 32) was sufficient to capture global appearance variations effectively, yielding comparable performance to a higher-dimensional embedding (d_g = 256) without significant computational overhead.

**Runtime Efficiency:**
*   WildSplatter reconstructed 3D Gaussians and enabled rendering in approximately 0.375 seconds when provided with two input views on a single NVIDIA RTX 6000 Ada GPU.
*   This represents a significant speed-up compared to optimization-based methods like WildGaussians (which took 1.5 minutes for reconstruction).
*   The runtime was comparable to that of Depth Anything 3, indicating that the added appearance estimation module does not introduce substantial computational overhead.

**Implicit Handling of Transient Objects:**
The study noted an implicit capability of the model: despite not explicitly modeling transient objects in context views, WildSplatter learned to assign low opacity values to such regions during training. This effectively suppressed them in the final rendered images, improving robustness in challenging real-world scenarios (Figure 8).

**Limitations:**
The authors identified a limitation where the use of a single global appearance embedding can sometimes lead to slight color drift or a limited ability to represent complex, localized lighting effects, such as detailed shadows.

### 6. Significance and Potential Impact

WildSplatter represents a significant contribution to the field of 3D vision and novel view synthesis by effectively addressing several key limitations of existing 3D Gaussian Splatting (3DGS) methods. Its introduction of a feed-forward, pose-free 3DGS model with explicit appearance control from unconstrained images marks a notable advancement, particularly in its combined capabilities.

The primary significance lies in its ability to **democratize 3D scene reconstruction and novel view synthesis**. By eliminating the need for known camera parameters and consistent lighting conditions, WildSplatter makes the process accessible from a wide variety of readily available, unconstrained image sources, such as casual photo collections or internet datasets. This broadens the applicability of 3DGS technology beyond controlled laboratory settings to real-world "in-the-wild" scenarios.

The **feed-forward nature** of WildSplatter, enabling 3D Gaussian reconstruction in under one second, is crucial for applications requiring rapid processing and real-time performance. This speed, combined with the high visual quality inherent to 3DGS, opens up new possibilities for:
*   **Virtual and Augmented Reality (VR/AR):** Rapidly digitizing environments and objects with dynamic appearance control is essential for immersive and interactive experiences.
*   **Robotics:** Real-time 3D scene understanding and dynamic environment modeling in unstructured settings.
*   **3D Content Creation:** Accelerating the generation of realistic 3D assets and environments from photographs, benefiting industries like gaming, film, and digital art.

The novel approach of **disentangling geometry and appearance** through jointly learned 3D Gaussians and appearance embeddings is a core innovation. This disentanglement allows for flexible manipulation of scene properties, enabling:
*   **Appearance Control and Editing:** Users can modify the lighting and style of a reconstructed scene post-capture, or interpolate between different appearances, as demonstrated by the appearance interpolation and cross-dataset control features. This could lead to advanced 3D photo editing tools.
*   **Generalization of Appearance:** The finding that appearance embeddings generalize across scenes is impactful, suggesting that a model trained on diverse datasets can transfer lighting and atmospheric conditions to new geometries, fostering capabilities akin to 3D style transfer.

The fact that WildSplatter outperforms existing pose-free 3DGS methods on challenging real-world datasets, particularly those with varying illumination, establishes a new benchmark for performance in this complex domain. While the identified limitations regarding complex local lighting effects (like shadows) and slight color drift suggest avenues for future research, this work provides a robust foundation. Future efforts could explore more localized appearance models or integrate inverse rendering techniques to overcome these challenges.

In conclusion, WildSplatter pushes the boundaries of efficient, robust 3D scene representation from unconstrained data. Its capabilities have the potential to significantly impact practical applications requiring fast, high-quality 3D reconstruction and flexible appearance control, making advanced 3D vision more accessible and versatile.
