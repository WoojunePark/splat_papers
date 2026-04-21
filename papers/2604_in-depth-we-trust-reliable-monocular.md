---
title: "In Depth We Trust: Reliable Monocular Depth Supervision for Gaussian Splatting"
date: 2026-04-07
arxiv: "2604.05715v1"
venue:
status: read

abstract: "Using accurate depth priors in 3D Gaussian Splatting helps mitigate artifacts caused by sparse training data and textureless surfaces. However, acquiring accurate depth maps requires specialized acquisition systems. Foundation monocular depth estimation models offer a cost-effective alternative, but they suffer from scale ambiguity, multi-view inconsistency, and local geometric inaccuracies, which can degrade rendering performance when applied naively. This paper addresses the challenge of reliably leveraging monocular depth priors for Gaussian Splatting (GS) rendering enhancement. To this end, we introduce a training framework integrating scale-ambiguous and noisy depth priors into geometric supervision. We highlight the importance of learning from weakly aligned depth variations. We introduce a method to isolate ill-posed geometry for selective monocular depth regularization, restricting the propagation of depth inaccuracies into well-reconstructed 3D structures. Extensive experiments across diverse datasets show consistent improvements in geometric accuracy, leading to more faithful depth estimation and higher rendering quality across different GS variants and monocular depth backbones tested."

website: 
code: https://github.com/graphdeco-inria/gaussian-splatting.git
openreview: 
issue: 

inputs:
  - posed-multi-view-images
  - depth

outputs:
  - 3dgs

methods:
  - depth-align

benchmarks:
  - 

related:
  - 

compared:
  - 
---

# In Depth We Trust: Reliable Monocular Depth Supervision for Gaussian Splatting

## My Notes



**[Note from GitHub, 2026-04-21]**

`모노 뎁스를 쓸 때 더 잘 쓰자`는 논문
그런데 결과 보면 weak baseline인 3DGS 보다 depth를 쓰고 + 자기네가 제안한 더 나은 방식을 썼어도 그다지 향상이 없음..
## Results

<!-- Optional: structured benchmark results for cross-paper comparison -->
<!-- Example:
| Benchmark | PSNR | SSIM | LPIPS |
|---|---|---|---|
| mipnerf360 | 27.21 | 0.815 | 0.214 |
| tanks-and-temples | 23.14 | 0.841 | 0.183 |
-->

## Figures

![Figure](https://arxiv.org/html/2604.05715v1/x1.png)

*Figure 1: The quality of monocular depth priors directly impacts the rendering performance of 3D Gaussian Splatting (3DGS) [19]. (a) Existing foundation monocular depth estimation models suffer from scale ambiguity and may fail to recover fine-grained details. (b) The rendering performance of 3DGS is correlated with the quality of the monocular depth priors used; naively applying monocular depth supervision in already well-reconstructed regions can even degrade performance. Our proposed framework provides a more versatile and reliable way to leverage monocular depth priors compared to previous scale-invariant depth supervision used in [20].*

![Figure](https://arxiv.org/html/2604.05715v1/x2.png)

*Figure 2: Impact of SfM point count in scale alignment on GS rendering quality for identical training images and point clouds. When using only ℒsid\mathcal{L}_{\text{sid}}, fewer observed points lead to degraded performance compared to the baseline (without using monocular depth supervision), highlighting the limitation of scale-invariant depth supervision in aligning monocular depth cues.*

![Figure](https://arxiv.org/html/2604.05715v1/x3.png)

*Figure 3: Overview of our proposed framework. During GS optimization, depth-inconsistent Gaussians are identified using a virtual stereo setup (Sec. 4.1). These regions guide the learning of absolute depth corrections from monocular depth priors aligned with sparse SfM point clouds. Additionally, a relative depth loss (Sec. 4.2) is applied to learn geometric cues under ambiguous scene scales.*

![Figure](https://arxiv.org/html/2604.05715v1/x4.png)

*Figure 4: Comparison of different relative depth supervision losses, shown on two zoomed-in scene crops. Gradient-based loss (GAL) achieves sharper rendering with fewer smearing artifacts compared to the patch-based Pearson correlation loss, as seen in the reduced distortion on photo-frame edges in the top row and a clearer shape around the orange triangular region in the bottom.*

![Figure](https://arxiv.org/html/2604.05715v1/x5.png)

*Figure 5: Qualitative results on 3DGS. (Top): low-data setting; (Bottom): moderate-data setting.*

![Figure](https://arxiv.org/html/2604.05715v1/x6.png)

*Figure 6: Qualitative comparisons of rendered images and depth maps on the ScanNet++ dataset for the baseline (without depth supervision), ℒsid\mathcal{L}_{\text{sid}}, and our method using MoGe-2 monocular depth supervision. Our method produces clearer, more accurate depth maps and yields sharper, less artifact-prone renderings than the baseline and ℒsid\mathcal{L}_{\text{sid}}. We encourage readers to zoom in for a clearer visual comparison.*

## LLM Summary

### 1. Authors and Institution(s)

The research paper "In Depth We Trust: Reliable Monocular Depth Supervision for Gaussian Splatting" was authored by:
*   Wenhui Xiao (Queensland University of Technology, CSRIO Data61)
*   Ethan Goan (Queensland University of Technology)
*   Rodrigo Santa Cruz (Queensland University of Technology)
*   David Ahmedt-Aristizabal (Queensland University of Technology, CSRIO Data61)
*   Olivier Salvado (Queensland University of Technology)
*   Clinton Fookes (Queensland University of Technology)
*   Leo Lebrat (Queensland University of Technology)

### 2. How this work fits into the broader research landscape

The field of 3D vision has seen advancements in novel view synthesis techniques, such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), which aim to generate photorealistic images from various viewpoints. A critical component for improving both scene reconstruction and rendering quality in these methods is accurate geometric information, often provided in the form of depth maps. Traditionally, these depth maps are obtained using specialized and costly hardware like RGB-D cameras.

More recently, foundation monocular depth estimation (MDE) models have emerged, offering a cost-effective alternative by predicting depth from single RGB images. While these MDE models have demonstrated notable accuracy, their direct application to 3DGS training presents challenges. These include inconsistent depth scales across different views, multi-view inconsistencies, and localized geometric inaccuracies, particularly on out-of-distribution data. Blindly incorporating these potentially unreliable monocular depth priors can degrade the multi-view geometry learning process in 3DGS, sometimes leading to poorer rendering performance than if no depth supervision were used. Consequently, some 3DGS software implementations disable monocular depth priors by default due to their unreliability.

Previous research has explored using monocular depth priors as auxiliary geometric supervision in scenarios where sufficient geometric constraints are lacking, such as sparse-view 3DGS reconstruction. Approaches include scale-invariant depth loss after aligning MDE maps with sparse Structure-from-Motion (SfM) point clouds (e.g., DRGS) or focusing on depth changes rather than absolute values (e.g., DNGaussian, SparseGS, FSGS). However, these methods often face limitations. Coarse scale alignment can be inadequate, and they may not generalize well to denser view regimes, potentially underperforming baseline methods and introducing unreliable cues that can propagate errors into the scene geometry.

This work contributes to the landscape by addressing the problem of reliably integrating monocular depth priors into Gaussian Splatting, moving beyond extreme sparsity conditions and focusing on selective application and robust learning of geometric cues, thereby mitigating the negative impacts of MDE inaccuracies and scale ambiguity.

### 3. Key objectives and motivation

The primary objective of this research is to develop a training framework that reliably leverages monocular depth priors to enhance the rendering performance and geometric accuracy of Gaussian Splatting (GS). This framework aims to integrate readily available, yet potentially imperfect, monocular depth cues into the GS optimization process.

The motivation for this work stems from several challenges in current 3D scene reconstruction and view synthesis:

1.  **Enhancing GS with Geometric Priors:** Accurate depth information is known to significantly improve 3DGS rendering, especially in mitigating artifacts that arise from sparse training data or textureless surfaces. This geometric prior can regularize density distributions and resolve ambiguities in radiance field formation.
2.  **Addressing Limitations of Monocular Depth Estimation (MDE):** While foundation MDE models offer a cost-effective alternative to specialized depth acquisition systems, they possess inherent limitations. These include scale ambiguity (depth predictions are often relative, not absolute metric scales), multi-view inconsistency (depth predictions for the same 3D point can vary across different camera views), and local geometric inaccuracies (failure to recover fine-grained details or introduction of noise). These issues prevent direct, naive application of MDE outputs as supervision for GS.
3.  **Mitigating Degradation from Unreliable Priors:** When monocular depth priors are used without careful consideration of their inaccuracies, they can propagate errors into the multi-view geometry learning of GS. This can lead to a degradation in rendering performance, as observed in some existing 3DGS implementations that disable monocular depth priors by default due to their unreliability.
4.  **Improving Upon Existing Integration Methods:** Current methods for incorporating monocular depth supervision, particularly in sparse-view scenarios, often rely on coarse scale alignment or focus solely on relative depth changes. These approaches can struggle with maintaining performance in denser view configurations, risk oversmoothing geometry, or indiscriminately propagate unreliable depth cues, leading to suboptimal or even inferior rendering quality compared to baselines without depth supervision.
5.  **Developing a Versatile and Forward-Compatible Solution:** The objective is to create a framework that is versatile, compatible with various GS backbones and MDE models, and robust enough to benefit from future advances in monocular depth estimation while maintaining consistent enhancements across different training data densities and scene types. The motivation is to safely harness 2D foundation priors without compromising established geometric constraints from multi-view supervision.

In summary, the motivation is to bridge the gap between the availability of cost-effective MDE and the need for reliable, performance-enhancing depth supervision in GS, by intelligently integrating these priors to improve reconstruction and rendering quality without introducing adverse effects.

### 4. Methodology and approach

The proposed training framework aims to reliably leverage monocular depth priors for Gaussian Splatting (GS) enhancement by integrating scale-ambiguous and noisy depth information into geometric supervision. The approach focuses on selectively applying depth regularization and extracting reliable geometric cues, even from imperfect monocular depth estimates.

The framework is composed of three main components: a scale-invariant depth loss ($L_{sid}$), a Depth-Inconsistency Mask (DIM), and a Gradient-Alignment Loss (GAL). The overall depth supervision regularization ($R$) is defined as a weighted sum of an absolute depth loss ($L_{abs}$) and a relative depth loss ($L_{rel}$), represented by the equation $R = \alpha L_{abs} + \beta L_{rel}$.

**Scale Alignment for Monocular Depth:**
Before applying monocular depth supervision, the output of MDE models, which often predict depth at an arbitrary scale, must be aligned with the scene's metric scale. This is achieved by solving a least-squares problem (Equation 4 in the paper) that matches the monocular depth map ($D_m$) to a sparse target scene depth map ($D_s$) derived from Structure-from-Motion (SfM) point clouds. This process computes an optimal scale ($s^*$) and shift ($t^*$) to obtain an aligned monocular depth map ($D = s^* \cdot D_m + t^*$). This aligned map is then used for supervision.

**Depth-Inconsistency Mask (DIM):**
The DIM is designed to identify and isolate multi-view inconsistent regions within the GS rendering. This ensures that monocular depth supervision is primarily applied to areas where the GS reconstruction is geometrically ambiguous or poorly constrained by multi-view observations, preventing the propagation of erroneous MDE predictions into already well-reconstructed 3D structures.

1.  **Virtual Stereo Setup:** A virtual stereo setup is emulated during training. The current training camera acts as the "left eye" with pose $P_l$, and a pseudo-camera, offset by a baseline $b$ along the x-axis, acts as the "right eye" with pose $P_r$. Both share the same camera intrinsics.
2.  **Stereo Depth Rendering and Reprojection:** At each training iteration, stereo depth maps ($ \hat{D}_l $, $ \hat{D}_r $) are rendered from the GS model using these virtual cameras. The depth map from the pseudo-right view ($ \hat{D}_r $) is then back-projected into 3D world coordinates and subsequently re-projected onto the left training view to obtain a re-projected depth map ($ \hat{D}_{l \leftarrow r} $).
3.  **Mask Construction:** The DIM ($M$) is constructed by performing a pixel-wise comparison between the rendered left depth map ($ \hat{D}_l $) and the re-projected depth map ($ \hat{D}_{l \leftarrow r} $). A pixel is marked as inconsistent (mask value 1) if the absolute difference between these two depth values exceeds a predefined threshold ($\epsilon$), or if no re-projected depth is available (indicating self-occlusion or floaters in the depth rendering).
4.  **Selective Absolute Depth Supervision:** The absolute depth loss ($L_{abs}$) is then calculated as an L1 loss between the aligned monocular depth map ($D$) and the rendered depth map ($ \hat{D} $), but only applied to the regions identified by the DIM: $L_{abs} = L_1(M \odot D, M \odot \hat{D})$. This means supervision on absolute depth values is restricted to inconsistent regions.

**Gradient-Alignment Loss (GAL):**
The GAL is introduced to capture fine-grained geometric cues from monocular depth priors while mitigating scale ambiguity. It addresses the limitations of patch-based correlation losses, which can be computationally expensive and lead to oversmoothed geometry.

1.  **Multi-scale Gradient Matching Principle:** Inspired by multi-scale gradient matching in MDE, GAL encourages consistent local depth variations between the rendered depth and the monocular depth prior.
2.  **First-order Spatial Derivatives:** GAL computes the L1 difference between the first-order spatial derivatives of the rendered depth map ($ \hat{D} $) and the aligned monocular depth map ($D$) along both the horizontal (x) and vertical (y) directions.
3.  **Formula:** $L_{rel} = L_1(\partial_x D, \partial_x \hat{D}) + L_1(\partial_y D, \partial_y \hat{D})$. This loss promotes the reconstruction of detailed geometric structures by aligning high-frequency depth variations.

**Experimental Setup:**
The framework was evaluated on three real-world datasets: ScanNet++, MipNeRF 360, and TanksAndTemples. Experiments were conducted under varying training-view densities: a low-data setting (sparse views) and a moderate-data setting. Two GS backbones, 3DGS and 2DGS, were used to assess generality. For monocular depth priors, DepthAnything V2 (DAV2) was primarily used, with additional evaluations using MoGe-2, UniDepth V2, and Marigold to demonstrate robustness across MDE variants. Performance was measured using standard metrics for novel view synthesis (PSNR, SSIM, LPIPS, AVGE) and rendered depth accuracy (Abs. Rel., $\delta_1$). Ablation studies were performed to quantify the individual contributions of DIM and GAL, and to compare GAL with other relative depth loss formulations (e.g., NCC, cosine similarity of gradients).

### 5. Main findings and results

The experiments conducted demonstrated that the proposed framework consistently enhances both geometric accuracy and rendering quality across various configurations of Gaussian Splatting (GS) and monocular depth estimation (MDE) models.

**5.1. Results on ScanNet++ Dataset:**
On the ScanNet++ dataset, the framework was compared against using only the scale-invariant depth loss ($L_{sid}$) with different MDE variants.
*   The baseline 3DGS (without depth supervision) achieved a PSNR of 24.20 dB and a rendered depth $\delta_1$ of 0.678.
*   Using $L_{sid}$ alone often resulted in marginal improvements or even performance degradation. For instance, with Marigold (a weaker MDE model), $L_{sid}$ led to a 0.52 dB reduction in PSNR (23.68 dB) compared to the baseline, indicating that naive depth supervision can hinder geometry learning when priors are noisy.
*   In contrast, the proposed method consistently improved performance, even with noisy priors. With Marigold, it achieved a PSNR of 24.31 dB (a 0.11 dB gain over the baseline) and a rendered depth $\delta_1$ of 0.723 (a 0.045 gain).
*   With stronger MDE priors, such as MoGe-2, the improvements were more pronounced, yielding a PSNR of 24.50 dB (a 0.3 dB gain over the baseline) and a rendered depth $\delta_1$ of 0.839.
*   These results indicated that the framework is robust to varying qualities of MDE backbones and can effectively leverage depth priors without compromising the reconstruction.

**5.2. Rendering Comparisons on MipNeRF 360 and TanksAndTemples:**
The framework’s novel view synthesis performance was evaluated against the 3DGS baseline and state-of-the-art methods (SparseGS, DNGaussian, FSGS) under low-data (sparse views) and moderate-data (denser views) settings, using DAV2 as the MDE prior.

*   **Low-data Setting:**
    *   On TanksAndTemples, the 3DGS baseline achieved 19.916 dB PSNR. The proposed method yielded 20.578 dB PSNR, demonstrating a gain of approximately 0.66 dB. It also surpassed SparseGS (20.152 dB) and DNGaussian (19.740 dB).
    *   On MipNeRF 360, the 3DGS baseline achieved 21.785 dB PSNR. The proposed method reached 22.253 dB PSNR, a gain of about 0.47 dB, outperforming other methods.
    *   These results highlighted the framework's effectiveness even when scale alignment is challenging due to insufficient SfM points.

*   **Moderate-data Setting:**
    *   In denser view regimes, existing methods frequently showed performance degradation. For example, on TanksAndTemples, SparseGS decreased PSNR by 0.1 dB (23.146 dB) and DNGaussian by 1.05 dB (22.190 dB) compared to the 3DGS baseline (23.240 dB).
    *   In contrast, the proposed method consistently improved rendering quality, achieving 23.414 dB PSNR on TanksAndTemples (a 0.17 dB gain over the baseline) and 25.716 dB PSNR on MipNeRF 360 (a 0.125 dB gain over the baseline). This demonstrated strong generalization across view densities.

*   **Generalization across GS Backbones:** The framework was also applied to the 2DGS backbone and consistently improved its performance across both datasets and data regimes, confirming its versatility.

*   **LPIPS Metric:** While showing consistent improvements in other metrics, the method yielded more modest improvements in LPIPS. This was attributed to the nature of artifacts corrected by the approach potentially differing from those used to train the LPIPS metric.

**5.3. Ablation Studies:**
Ablation studies using the 2DGS backbone on MipNeRF 360 (low-data setting) investigated the contribution of each module:
*   **DIM Contribution:** Incorporating the Depth-Inconsistency Mask (DIM) with $L_{sid}$ yielded a 0.24 dB PSNR improvement over $L_{sid}$ alone (21.66 dB vs. 21.42 dB). This supported the role of DIM in preventing inaccurate monocular depth cues from corrupting geometry learning.
*   **GAL Contribution:** Adding the Gradient-Alignment Loss (GAL) further enhanced rendering quality by an additional 0.43 dB PSNR, leading to the full method's 22.09 dB PSNR. This indicated the effectiveness of GAL in learning fine-grained geometry from relative depth variations.
*   **Relative Depth Loss Choices:** Comparisons with other relative depth losses showed that GAL achieved superior rendering quality and maintained computational efficiency. Patch-based NCC loss (e.g., NCC$_{w63}$, NCC$_{w127}$) struggled in scenes with high-frequency structures and introduced significant computational overhead. Cosine similarity loss of gradients was less effective than GAL, suggesting that both gradient magnitude and orientation are important.

**5.4. Qualitative Results:**
Qualitative comparisons visually supported the quantitative findings. The proposed monocular depth supervision led to sharper details and reduced noisy artifacts (e.g., "floaters") in 3DGS renderings. The method also imposed stronger geometric constraints, resulting in spatially coherent depth maps with better-preserved structural details, which translated into higher-fidelity novel view renderings.

### 6. Significance and potential impact

The research presents a significant advancement in the reliable integration of monocular depth priors into 3D Gaussian Splatting (3DGS), addressing critical limitations that have hindered the widespread use of such priors. The significance and potential impact of this work are multi-faceted:

1.  **Enhanced 3D Scene Reconstruction and Rendering Quality:** By introducing a reliable framework for leveraging monocular depth, the research directly contributes to improving the geometric accuracy and visual fidelity of 3D scene reconstructions. This leads to higher quality novel view synthesis, particularly in challenging scenarios characterized by sparse training data or textureless surfaces where multi-view constraints are weak.
2.  **Mitigation of Monocular Depth Estimation (MDE) Limitations:** The framework explicitly addresses core issues of MDE, such as scale ambiguity, multi-view inconsistencies, and local geometric inaccuracies. The Depth-Inconsistency Mask (DIM) selectively applies supervision to ambiguous regions, preventing error propagation into well-reconstructed geometry. The Gradient-Alignment Loss (GAL) effectively captures fine-grained geometric details from relative depth variations, even with imperfect scale alignment. This robust handling of MDE imperfections makes the priors more practically usable.
3.  **Increased Accessibility and Cost-Effectiveness of 3D Content Creation:** By enabling the reliable use of readily available monocular depth cues, the framework reduces the reliance on expensive and specialized depth acquisition hardware (e.g., RGB-D cameras). This lowers the barrier to entry for high-quality 3D scene reconstruction, potentially democratizing the creation of 3D content for various applications.
4.  **Versatility and Generalization:** The demonstrated compatibility of the framework with different GS variants (3DGS, 2DGS) and various MDE backbones (e.g., DepthAnything V2, MoGe-2, UniDepth V2, Marigold) highlights its broad applicability. This versatility ensures that the method is not tied to a specific technology stack and can benefit from future advances in both MDE and GS research.
5.  **Robustness Across Data Regimes:** Unlike some previous methods that perform optimally only under extreme data sparsity, this framework demonstrates consistent improvements across both low-data (sparse view) and moderate-data regimes. Its robustness to varying view densities enhances its practical utility in diverse real-world scenarios.
6.  **Foundation for Future Research:** The work establishes a robust methodology for incorporating 2D foundation priors into 3D reconstruction. This provides a strong foundation for future research in areas such as sparse-view reconstruction, real-time 3D mapping, and the integration of other 2D vision priors (e.g., surface normals, semantics) to further enhance 3D models.
7.  **Contribution to Computer Vision and Graphics:** This research advances the state of the art in novel view synthesis and 3D reconstruction, offering a scalable solution for generating high-fidelity 3D scenes from readily available image data. Its impact could extend to applications in virtual reality, augmented reality, robotics, and digital content creation, where accurate and photorealistic 3D environments are crucial.
