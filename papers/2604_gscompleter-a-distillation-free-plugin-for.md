---
title: "GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds"
date: 2026-04-22
arxiv: "2604.20155v1"
venue:
status: to-read

abstract: "While 3D Gaussian Splatting (3DGS) has revolutionized real-time rendering, its performance degrades significantly under sparse-view extrapolation, manifesting as severe geometric voids and artifacts. Existing solutions primarily rely on an iterative &#34;Repair-then-Distill&#34; paradigm, which is inherently unstable and prone to overfitting. In this work, we propose GSCompleter, a distillation-free plugin that shifts scene completion to a stable &#34;Generate-then-Register&#34; workflow. Our approach first synthesizes plausible 2D reference images and explicitly lifts them into metric-scale 3D primitives via a robust Stereo-Anchor mechanism. These primitives are then seamlessly integrated into the global context through a novel Ray-Constrained Registration strategy. This shift to a rapid registration paradigm delivers superior 3DGS completion performance across three distinct benchmarks, enhancing the quality and efficiency of various baselines and achieving new SOTA results."

website: 
code: 
openreview: 
issue: 34

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

# GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds

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

![Figure](https://arxiv.org/html/2604.20155v1/x1.png)

*Figure 1: Overview of GSCompleter. We propose a “Generate-then-Register” paradigm for rapid and robust 3DGS scene completion. (a) Given a 3DGS scene exhibiting geometric voids, (b) we first synthesize a high-fidelity 2D reference image via a generative prior and explicitly lift it into metric-scale 3D Gaussian primitives guided by a stereo anchor view. (c) Instead of global optimization, we seamlessly register these primitives into the scene via a strictly ray-constrained integration strategy. (d) This process yields a completed scene with fidelity comparable to the Ground Truth, achieved within seconds.*

![Figure](https://arxiv.org/html/2604.20155v1/x2.png)

*Figure 2: Overview of the GSCompleter. Addressing the geometric holes in the novel view, we adopt a “Generate-then-Register” paradigm to complete the scene via four stages: (1) Feed-Forward Metric Context Initialization: We first reconstruct the observed regions using a scale-aware feed-forward 3DGS model, establishing a foundational context with metric scale; (2) Anchor-Guided Gaussian Initialization: To fill the voids, we generatively synthesize the novel view in 2D space, subsequently employing a Stereo-Anchor Selection strategy to pair the view with an optimal stereo anchor view, enabling it to be lifted into 3D Gaussians with accurate depth; (3) Ray-Constrained Gaussian Registration: To align these new primitives, we apply a coarse-to-fine mechanism that first rectifies global drift via RANSAC, followed by a strict 1-DoF ray-space optimization to lock primitives along their camera rays for for local refinement; and (4) Multi-View Gaussian Integration &amp; Refinement: Finally, redundant primitives are pruned, followed by an opacity-only refinement to seamlessly integrate newly generated Gaussians while preventing catastrophic forgetting of the initial scene.*

![Figure](https://arxiv.org/html/2604.20155v1/img/stereo_anchor.png)

*Figure 3: Stereo-Anchor Selection Strategy. We identify the optimal reference for 3D lifting through a prioritized process: (1) Filtering: Context views with relative rotation Δ​θ&gt;45∘\Delta\theta&gt;45^{\circ} are discarded to ensure sufficient overlap. (2) Selection: Among valid candidates (Left), we select the one with the maximum baseline to stabilize metric scale. (3) Fallback: In extreme cases where no candidates satisfy the angular constraint (Right), we default to the view with the minimum relative rotation to prevent tracking failure.*

![Figure](https://arxiv.org/html/2604.20155v1/x3.png)

*Figure 4: Ray-Constrained Gaussian Registration. (a) Coarse Global Alignment: We employ RANSAC to estimate the global affine parameters (s,ts,t), which are used to explicitly re-initialize the depth of the target Gaussians. (b) Fine-grained Ray-Constrained Optimization: We optimize the Gaussian depth solely by adjusting the distance along the camera ray. Concurrently, we reproject these primitives into the stereo anchor view to enforce precise geometric structural accuracy.*

![Figure](https://arxiv.org/html/2604.20155v1/x4.png)

*Figure 5: Qualitative Comparison on RealEstate10K. While baselines exhibit significant geometric collapses or “black holes” in unobserved regions, our method achieves high fidelity consistent with the Ground Truth (GT). GSCompleter accurately recovers complex geometric structures and scene details while maintaining robustness across diverse baseline architectures (e.g., pixel-aligned and voxel-aligned).*

![Figure](https://arxiv.org/html/2604.20155v1/x5.png)

*Figure 6: Comparison between our method and the densification strategy. While densification tends to overfit the reference view, our method effectively mitigates this issue.*

![Figure](https://arxiv.org/html/2604.20155v1/img/RegGS_Compare.jpg)

*Figure 7: Visual comparison with RegGS. RegGS suffers from severe geometric distortions (highlighted in red) arising from scale-agnostic optimization. In contrast, our method leverages metric priors to achieve precise alignment while strictly preserving structural fidelity. Given the same input views, our geometric pipeline accelerates the process by over 170×\times compared to RegGS (1.43s vs. ∼\sim4 min).*

![Figure](https://arxiv.org/html/2604.20155v1/img/evaluation_strategy_update.png)

*Figure 8: Visual illustration of the 2-view input and 1-view target extrapolation setting.*

![Figure](https://arxiv.org/html/2604.20155v1/img/comparison_reggs_ours.png)

*Figure 9: Visual comparison: RegGS exhibits artifacts and blur due to error accumulation, while ours preserves high-frequency details and structural integrity.*

![Figure](https://arxiv.org/html/2604.20155v1/x6.png)

*Figure 10: Qualitative comparison on long sequences. RegGS suffers from progressive blurring and structural drift due to metric scale instability. In contrast, GSCompleter maintains sharp details and global consistency, effectively rectifying artifacts in challenging frames.*

![Figure](https://arxiv.org/html/2604.20155v1/x7.png)

*Figure 11: More results on the RealEstate10K dataset.*

![Figure](https://arxiv.org/html/2604.20155v1/x8.png)

*Figure 12: More results on the ACID dataset.*

![Figure](https://arxiv.org/html/2604.20155v1/x9.png)

*Figure 13: More results on the DL3DV dataset.*

## LLM Summary

The following report details the research paper titled "GSCompleter: A Distillation-Free Plugin for Metric-Aware 3D Gaussian Splatting Completion in Seconds."

---

### Research Report: GSCompleter

#### 1. Authors and Institution(s)

The authors of this paper are Ao Gao, Jingyu Gong, Xin Tan, Zhizhong Zhang, and Yuan Xie. Their affiliations include:
*   School of Computer Science and Technology, East China Normal University, Shanghai, China
*   Shanghai Innovation Institute, Shanghai, China
*   Chongqing Key Laboratory of Precision Optics, Chongqing Institute of East China Normal University, Chongqing, China
*   Shanghai Key Laboratory of Computer Software Evaluating and Testing, Shanghai, China

Jingyu Gong is listed as the correspondence author, and Yuan Xie is identified as the Project Leader.

#### 2. How This Work Fits into the Broader Research Landscape

The field of 3D scene representation and novel view synthesis has advanced significantly with methods like Neural Radiance Fields (NeRF) and, more recently, 3D Gaussian Splatting (3DGS). 3DGS, introduced by Kerbl et al. (2023), has demonstrated capabilities in real-time, photorealistic rendering using explicit primitives, distinguishing it from implicit ray-marching methods. However, a known limitation of 3DGS is its performance degradation when input views are sparse, leading to geometric voids and rendering artifacts in extrapolated views.

Existing approaches to address these missing regions generally fall into two categories. The first, and prevalent, is an iterative "Repair-then-Distill" or "Render-Repair-Reoptimize" paradigm. This strategy involves attempting to distill 2D inpainted content back into a 3D representation via optimization. Methods like those by Paliwal et al. (2025) and Wu et al. (2025a) exemplify this. However, this approach is often unstable, prone to overfitting, and can produce near-camera artifacts due to under-constrained optimization, especially in empty regions where gradient-based densification is ineffective. While external depth priors can offer guidance, they frequently encounter depth alignment issues, potentially causing geometric inconsistencies.

The second category involves registration-based approaches, which aim to align independent sets of Gaussians. These methods, such as RegGS (Cheng et al., 2025), can struggle with generalization or efficiency. For instance, RegGS involves a complex iterative registration process that can be computationally intensive, requiring minutes per scene, partly because it often operates on unscaled primitives, necessitating complex Sim(3) optimizations.

More recent advancements in feed-forward models (e.g., Chen et al., 2024; Xu et al., 2025) have shown the ability to directly predict Gaussians with an inherent metric scale, typically by leveraging stereo-depth estimation. This development introduces the possibility of transforming scene completion into a more rapid registration task by eliminating the need for expensive scale optimization.

GSCompleter positions itself within this landscape by proposing a "Generate-then-Register" paradigm. It aims to circumvent the instability and inefficiency of existing methods by explicitly synthesizing plausible 2D content, lifting it into metric-scale 3D Gaussians, and then rapidly registering these new primitives into the existing scene context. This approach seeks to provide a distillation-free, rapid, and robust solution to the sparse-view completion problem in 3DGS, functioning as a plugin to enhance various baseline architectures.

#### 3. Key Objectives and Motivation

The primary objective of this research is to develop a novel, efficient, and robust method for completing 3D Gaussian Splatting (3DGS) scenes, specifically addressing the geometric voids and rendering artifacts that occur when input views are sparse.

The motivation for this work arises from several limitations identified in the current state of 3DGS and existing completion techniques:

*   **Degradation of 3DGS with Sparse Views:** While 3DGS has demonstrated high-quality real-time rendering, its performance significantly degrades in extrapolated views derived from sparse input data. This results in observable geometric holes and structural artifacts that compromise rendering fidelity.
*   **Instability and Inefficiency of Optimization-Based Completion:** The dominant "Repair-then-Distill" paradigm, which relies on iteratively optimizing manually initialized points under sparse 2D supervision, is inherently unstable. This process is prone to overfitting, leading to geometric distortions and artifacts, particularly near the camera. The gradient-based densification integral to 3DGS struggles in empty regions, making implicit optimization an insufficient strategy for robust scene completion. Even with external depth priors, challenges with depth alignment can cause geometric collisions with the global scene.
*   **Limitations of Existing Registration-Based Methods:** While registration offers an alternative, current methods either lack generalizability across diverse scenes or are computationally expensive. Some approaches require complex iterative processes, solving for optimal transport distances or similar metrics, which can consume minutes per scene. This computational burden renders them impractical for applications requiring rapid processing.
*   **Leveraging Metric Priors for Efficiency:** Recent advances in feed-forward models for 3D reconstruction can directly predict metric-scale Gaussians from stereo inputs. This capability suggests a potential to bypass the expensive scale optimization step inherent in methods that operate on unscaled primitives. The motivation is to capitalize on these metric priors to transform the complex scene completion problem into a faster, more direct registration task.
*   **Developing a Plugin for Broad Applicability:** The aim is to create a "distillation-free plugin" that can seamlessly integrate with and enhance various existing 3DGS baselines. This approach seeks to improve both the quality and efficiency of scene completion without requiring fundamental modifications or re-training of the underlying 3DGS models.

In summary, the research is motivated by the need for a more stable, rapid, and geometrically accurate solution to 3DGS scene completion that can effectively hallucinate and integrate missing content in sparse-view scenarios, thereby overcoming the drawbacks of existing optimization- and registration-based techniques.

#### 4. Methodology and Approach

GSCompleter proposes a "Generate-then-Register" workflow designed to address the challenges of 3DGS scene completion in sparse-view settings. The pipeline consists of four main stages:

**3.1. Preliminaries**
The scene representation utilizes 3D Gaussian Splatting (3DGS), where each Gaussian is parameterized by its mean position (μ), covariance matrix (Σ), opacity (α), and spherical harmonic (SH) coefficients (c). The covariance matrix is decomposed into a scaling vector (s) and a rotation quaternion (q). The method also leverages the Positional-Encoding Field (PE-Field), a 3D-aware generative prior that extends positional encodings into a structured 3D volumetric field, enabling geometry-aware view synthesis with strict perspective consistency.

**3.2. Overview of the Pipeline**
Given a context scene G_ctx reconstructed from sparse observations I_obs, the objective is to integrate missing geometry from a target viewpoint P_t.
1.  **Feed-Forward Metric Context Initialization:** A pre-trained feed-forward 3DGS estimator Ψ is used to reconstruct the global context G_ctx from the observed images I_obs. This step establishes an absolute metric scale for the scene, framing the subsequent completion as a direct registration task.
2.  **Anchor-Guided Gaussian Initialization:** To fill geometric voids, a high-fidelity 2D reference image Ĩ_t for the novel view is synthesized using the PE-Field generator. To lift this 2D image into metric-scale 3D Gaussians G_tgt, a Stereo-Anchor Selection strategy is introduced. This mechanism identifies an optimal stereo view P_s from the context views to serve as a robust geometric baseline. The target hypothesis Ĩ_t is paired with the selected anchor view I_s, and this pair (V_pair = (Ĩ_t, I_s)) is fed into the stereo-based Gaussian estimator Ψ to produce G_tgt with accurate depth. This strategy facilitates implicit alignment between the coordinate systems of the new and context Gaussians.
3.  **Ray-Constrained Gaussian Registration:** This stage mitigates minor misalignments through a coarse-to-fine registration strategy.
    *   **Coarse Global Alignment:** The feed-forward model Ψ provides paired depth maps for both the anchor view (D_anc_pred) and the target view (D_tgt_pred). The anchor view's predicted depth (D_anc_pred) is used as a bridge to align with the established context depth (D_anc_ctx). This is done by estimating a global affine transformation (scale 's' and translation 't') via RANSAC, minimizing the difference between D_anc_ctx and the transformed D_anc_pred. These parameters (s, t) are then applied to the target view's predicted depth to initialize the new primitives (D_init_tgt = s ⋅ D_tgt_pred + t).
    *   **Fine-Grained Ray-Constrained Optimization:** To correct local non-linear residuals, a 1-DoF Ray-Space Optimization is performed. First, the planar Z-depth D_init_tgt is unprojected into Euclidean ray space to derive an initial Euclidean distance d_init_i along each viewing ray. The 3D position μ_i of each Gaussian is then parameterized solely by a learnable scalar distance d_i along its viewing ray, freezing other Gaussian attributes (rotation, scaling, opacity, SH coefficients). The set of distances D = {d_i} is optimized by minimizing a joint objective function L_total. This loss includes an L1 depth loss (L_depth) anchoring rendered target depth ˆD_tgt to the sparse context depth D_tgt_ctx, an L1 stereo loss (L_stereo) enforcing multi-view consistency by minimizing error between rendered anchor depth ˆD_anc and established anchor depth D_anc_ctx, and an L1 photometric regularizer (L_rgb) preserving visual fidelity.
4.  **Multi-View Gaussian Integration & Refinement:**
    *   **Hole-Aware Filtering & Integration:** Before integration, the aligned target Gaussians G_tgt are filtered to retain only those that fall within the unobserved regions (holes) of the context scene. A binary hole mask M_hole is derived by thresholding the opacity map A_ctx rendered from G_ctx. The filtered primitives G'_tgt are then merged into the global context G_ctx.
    *   **Opacity-Only Multi-View Refinement:** To prevent catastrophic forgetting and ensure seamless integration, a lightweight multi-view optimization is performed. This involves freezing the existing context G_ctx and optimizing only the opacity (α) of the newly integrated primitives G'_tgt. The objective function L_mv minimizes a combination of L1 loss between the rendered target image ˆI_tgt and the synthesized reference image Ĩ_t, and L1 losses between rendered context views ˆI_k and their ground-truth counterparts I_k.

**Implementation Details:** The system is implemented in PyTorch. Experiments use 256x256 or 256x448 resolutions. During inference, Ray-Constrained Registration is performed for 50 iterations, followed by 30 iterations of Opacity-Only Refinement. The PE-Field generative prior uses 4 inference steps. All baseline models maintain frozen pre-trained weights.

#### 5. Main Findings and Results

The evaluation of GSCompleter involved qualitative and quantitative analyses across three distinct benchmarks: RealEstate10K, ACID, and DL3DV. A 2-view extrapolation setting (n-k configuration) was specifically designed to test the model's ability to synthesize large-scale unobserved regions.

**5.1. Qualitative Results**
*   **Completion Fidelity:** As illustrated in Fig. 5, baseline methods consistently exhibited significant geometric voids and "black holes" in unobserved regions due to sparse view coverage. GSCompleter effectively completed these regions, generating physically plausible geometry and coherent textures that were consistent with the ground truth (GT).
*   **Robustness Across Architectures:** The method demonstrated robustness across diverse baseline architectures, including pixel-aligned (MVSplat, DepthSplat) and voxel-aligned (VolSplat) models. For VolSplat, which showed extensive black voids and artifacts under sparse 2-view settings, GSCompleter not only filled the voids but also resolved existing artifacts, indicating its versatility.

**5.2. Quantitative Results**
*   **Overall Performance:** Tables 1, 2, and 3 demonstrate that GSCompleter consistently outperformed all baselines across RealEstate10K, ACID, and DL3DV datasets, achieving state-of-the-art results in the tested extrapolation setting. For instance, on RealEstate10K, the module provided a +2.41 dB PSNR gain for MVSplat.
*   **Performance with Pixel-Aligned Baselines (MVSplat, DepthSplat):** GSCompleter yielded comprehensive improvements across all metrics (PSNR, SSIM, LPIPS). This enhancement was attributed to the Ray-Constrained Registration strategy, which aligns with the pixel-aligned geometric nature of these methods, ensuring high-fidelity reconstruction and precise texture alignment.
*   **Performance with Voxel-Aligned Baselines (VolSplat):** The method achieved substantial gains by filling geometric voids (e.g., +2.00 dB PSNR on ACID). A slight increase in LPIPS was noted, attributed to a structural conflict between the ray-based registration (continuous Gaussians) and VolSplat's quantized voxel grid, which can introduce minor misalignment at boundaries.

**5.3. Ablation Study**
*   **Geometric Registration Accuracy (Table 4):**
    *   **Stereo-Anchor Selection (SA):** Removing SA resulted in the most significant performance drop (increased CD, decreased F-Score), confirming its critical role in resolving scale ambiguity by providing robust stereo parallax.
    *   **Depth-Alignment (DA):** Disabling the global alignment (RANSAC) degraded the F-Score, indicating the necessity of explicit global rectification for correcting residual geometric drift.
    *   **Ray-Constrained Optimization (RC):** The RC module improved geometric fidelity (reduced CD) compared to unconstrained optimization, maintaining rendering quality by restricting Gaussian movements along camera rays.
*   **Multi-View Consistency (Table 5):** The Multi-View Gaussian Refinement (MV) module enhanced target-view performance and preserved the quality of the original context views. Its removal led to a decline in both target-view and context-view quality, confirming its effectiveness in preventing catastrophic forgetting and maintaining global scene consistency.

**5.4. Efficiency Analysis**
*   **Runtime (Table 6):** GSCompleter achieved a total inference time of 3.16 seconds on a single NVIDIA H200 GPU. The generative prior (PE-Field) accounted for 1.73s, while the entire registration stage (alignment, registration, refinement) was completed in 1.43s.
*   **Speedup:** When isolating the geometric pipeline, GSCompleter delivered a 170x speedup compared to the registration-based baseline RegGS (1.43s vs. approximately 4 minutes).

**5.5. Analysis of Depth Alignment Strategy**
*   **Anchor-based vs. Target-based (Table 7, Fig. 6):** Directly aligning at the target pose was found to be unstable due to insufficient geometric constraints from unobserved voids. The proposed anchor-based strategy, which leverages the anchor view's dense depth for spatial constraints, yielded a 16.8% F-Score improvement (0.398 → 0.465), demonstrating its superior stability and effectiveness.

**5.6. Comparison with Alternative Strategies**
*   **vs. Densification (Fig. 6):** Naive 3DGS densification faced a dilemma: insufficient optimization left voids, while intensive optimization led to severe overfitting and near-camera artifacts. GSCompleter avoided these issues, producing robust, high-fidelity reconstructions.
*   **vs. Registration Baselines (RegGS, Fig. 7):** RegGS suffered from scale drift and high computational cost (minutes) due to optimizing unscaled primitives with an expensive M_W2 distance. GSCompleter, by contrast, utilized stereo priors to directly estimate metric-scale Gaussians, enabling precise and rapid registration in seconds.
*   **Robustness on Extrapolation Span (Table 8):** GSCompleter consistently outperformed the DepthSplat baseline across increasing extrapolation spans (sparser input), with the performance margin widening in more challenging scenarios. This indicated robustness in handling large-baseline inputs and preventing geometric collapse.
*   **Long Sequence Completion (Fig. 9, 10):** In long sequence completion tasks, RegGS exhibited severe temporal error accumulation, resulting in blurred textures and catastrophic geometric drift. GSCompleter, using its Stereo-Anchor Selection strategy, maintained structural consistency and sharp details throughout the trajectory, preventing cumulative drift and achieving significantly higher efficiency with consistent processing times (averaging approx. 1.8s per view, representing over 200x speedup compared to RegGS's peak latency).

#### 6. Significance and Potential Impact

The work presented in this paper introduces GSCompleter, a novel approach to 3D Gaussian Splatting (3DGS) scene completion that represents a paradigm shift from conventional "Repair-then-Distill" methods to a "Generate-then-Register" workflow. This research holds several significant implications and potential impacts:

*   **Enhanced 3DGS Robustness and Fidelity:** GSCompleter directly addresses a critical limitation of 3DGS: its performance degradation under sparse-view conditions. By effectively filling geometric voids and resolving rendering artifacts, the method significantly enhances the robustness and visual fidelity of 3DGS scenes, particularly in extrapolation scenarios. This capability allows 3DGS to be more reliably deployed in contexts with limited input data.
*   **Improved Efficiency for 3D Scene Completion:** The proposed "Generate-then-Register" paradigm, combined with metric-aware Gaussian initialization, enables scene completion in seconds. This speed represents a substantial improvement over existing optimization-based or computationally intensive registration methods, which can take minutes. Such efficiency makes the approach suitable for real-time applications, large-scale scene reconstruction, and scenarios requiring rapid iteration.
*   **Distillation-Free and Plugin-Based Integration:** The design as a distillation-free plugin allows GSCompleter to integrate seamlessly with various existing 3DGS baselines (e.g., MVSplat, DepthSplat, VolSplat) without requiring extensive re-training or modification of the underlying models. This broad compatibility increases its practical utility and accessibility for researchers and developers working with different 3DGS implementations.
*   **Novel Technical Contributions:** The introduction of specific mechanisms such as the Stereo-Anchor Selection strategy for robust metric depth estimation and the Ray-Constrained Registration for rapid, precise alignment without texture drift contributes new techniques to the field of 3D reconstruction and novel view synthesis. The 1-DoF ray-space optimization effectively resolves local geometric distortions while preserving visual integrity.
*   **Advancement in Generalizable 3D Reconstruction:** By leveraging a 3D-aware generative prior (PE-Field) for plausible content synthesis and integrating it through metric-aware registration, the work contributes to the development of more generalizable and robust 3D reconstruction techniques, especially for unobserved regions.
*   **Potential for Practical Applications:** The ability to rapidly and accurately complete 3D scenes from sparse inputs has implications for various real-world applications, including:
    *   **Augmented/Virtual Reality (AR/VR):** Enabling more immersive and geometrically consistent virtual environments from real-world captures.
    *   **Robotics:** Improving environmental mapping and perception in scenarios with limited sensor data.
    *   **Content Creation:** Facilitating the generation of high-quality 3D assets and environments from fewer input images.
    *   **Digital Twins:** Contributing to the creation and maintenance of accurate digital representations of physical spaces.

In conclusion, GSCompleter offers a robust and highly efficient solution to a critical problem in 3DGS, pushing the boundaries of real-time 3D scene completion and paving the way for broader adoption of 3DGS in various applications.
