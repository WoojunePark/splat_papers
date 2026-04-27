---
title: "Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training"
date: 2026-04-21
arxiv: "2604.20046v1"
venue:
status: read

abstract: "3D Gaussian Splatting (3DGS) has revolutionized novel view synthesis with high-quality rendering through continuous aggregations of millions of 3D Gaussian primitives. However, it suffers from a substantial memory footprint, particularly during training due to uncontrolled densification, posing a critical bottleneck for deployment on memory-constrained edge devices. While existing methods prune redundant Gaussians post-training, they fail to address the peak memory spikes caused by the abrupt growth of Gaussians early in the training process. To solve the training memory consumption problem, we propose a systematic memory-bounded training framework that dynamically optimizes Gaussians through iterative growth and pruning. In other words, the proposed framework alternates between incremental pruning of low-impact Gaussians and strategic growing of new primitives with an adaptive Gaussian compensation, maintaining a near-constant low memory usage while progressively refining rendering fidelity. We comprehensively evaluate the proposed training framework on various real-world datasets under strict memory constraints, showing significant improvements over existing state-of-the-art methods. Particularly, our proposed method practically enables memory-efficient 3DGS training on NVIDIA Jetson AGX Xavier, achieving similar visual quality with up to 80% lower peak training memory consumption than the original 3DGS."

website: 
code: 
openreview: 
issue: 

inputs:
  - posed-multi-view-images

outputs:
  - 3dgs

methods:
  - efficient-training

benchmarks:
  - 

related:
  - 

compared:
  - 
---

# Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training

## My Notes



**[Note from GitHub, 2026-04-27]**

----
최소한의 결과 손실로 training 도중 RAM 사용량을 줄이고자 함. (최종 용량은 목적이 아님)

Table 1. 비교해보면 정량적으로는 Taming 3DGS보다 엄청 크게 개선된 건 아님.
다만 Fig 8.의 (cherry-picking된) 정성적인 결과물을 보면 Taming 3DGS가 아예 실패한 영역도 자기네 기법으로는 살려낸다고 주장.
## Results

<!-- Optional: structured benchmark results for cross-paper comparison -->
<!-- Example:
| Benchmark | PSNR | SSIM | LPIPS |
|---|---|---|---|
| mipnerf360 | 27.21 | 0.815 | 0.214 |
| tanks-and-temples | 23.14 | 0.841 | 0.183 |
-->

## Figures

![Figure](https://arxiv.org/html/2604.20046v1/x2.png)

*Figure 1: We present a memory-bounded 3D Gaussian Splatting training framework, enabling lower peak training memory and higher rendering quality, compared to existing state-of-the-art methods.*

![Figure](https://arxiv.org/html/2604.20046v1/x3.png)

*Figure 2: The variation curves for the numbers of Gaussians over iteration. Our method iteratively grows and prunes Gaussians under the memory constraint, while 3DGS [17] and Mini-Splatting [9] densify Gaussians to millions and remove them afterwards.*

![Figure](https://arxiv.org/html/2604.20046v1/x4.png)

*Figure 3: The “error” information (grass behind the bicycle) cannot be corrected after long-term iterations by Taming 3DGS [25], while our proposed solution can effectively optimize those areas.*

![Figure](https://arxiv.org/html/2604.20046v1/x5.png)

*Figure 4: Illustration of Gaussian compensation. (left) Color gradient per pixel. (Right) Compensated Gaussians in yellow color. Our compensation step recovers the high-frequency region that is hard to capture by the original densification (e.g., rubble under the train).*

![Figure](https://arxiv.org/html/2604.20046v1/x6.png)

*Figure 5: Rendered images with our growing strategy. (Left) Our proposed hybrid gradient-based method recovers the texture of the floor more accurately. (Right) Existing approaches based on position-only gradient lose details.*

![Figure](https://arxiv.org/html/2604.20046v1/x7.png)

*Figure 6: Overall workflow of our proposed memory-bounded 3DGS training framework, which iteratively performs growing, compensation, and pruning, progressively refining the representation capability.*

![Figure](https://arxiv.org/html/2604.20046v1/x8.png)

*Figure 7: Rendered image example. Our method presents significantly higher perceptual quality with high-frequency details, while Taming 3DGS [25] shows blurry background trees and land.*

![Figure](https://arxiv.org/html/2604.20046v1/figs/rendered_images_diff_iter_c.jpg)

*Figure 8: Visualized results on flowers at the 8K-th iteration and kitchen at the 2K-th iteration. Our method shows significantly improved rendering quality after the same training iterations compared to Taming 3DGS [25].*

![Figure](https://arxiv.org/html/2604.20046v1/figs/rendered_images_all_p1_c.jpg)

*Figure 9: Visualized results. Our method achieves superior rendering quality compared against original 3DGS and Taming 3DGS [25].*

![Figure](https://arxiv.org/html/2604.20046v1/figs/rendered_images_all_p2_c.jpg)

*Figure 10: Visualized results. Our method achieves superior rendering quality compared against original 3DGS and Taming 3DGS [25].*

![Figure](https://arxiv.org/html/2604.20046v1/figs/ellipsoid_compare_c.jpg)

*Figure 11: Visualized ellipsoid results. Our position adjustment reduces overlapped Gaussians (middle image), dynamically allocating more Gaussians to texture-rich regions (right image, texture of blanket), leading to a superior rendering quality.*

## LLM Summary

The following report provides a detailed analysis of the research paper "Gaussians on a Diet: High-Quality Memory-Bounded 3D Gaussian Splatting Training."

---

### 1. Authors and Institution(s)

The authors of this research paper are:
*   Yangming Zhang, Jian Xu, and Miao Yin (affiliated with the Department of Computer Science, University of Texas at Arlington).
*   Kunxiong Zhu and Wei Niu (affiliated with the School of Computing, University of Georgia).

### 2. How This Work Fits into the Broader Research Landscape

Novel View Synthesis (NVS) is a fundamental problem in computer vision and graphics that aims to generate photorealistic images of a scene from arbitrary viewpoints given a set of input images. Recent advancements in neural rendering, particularly Neural Radiance Fields (NeRF) and its derivatives, have significantly improved NVS fidelity. These methods represent scenes as continuous volumetric functions, achieving high visual quality but often requiring extensive sampling and long training times, which limits their practicality for real-time or resource-constrained applications.

More recently, 3D Gaussian Splatting (3DGS) has emerged as an explicit point-based rendering approach, providing an alternative to NeRF by offering a better balance between rendering quality, speed, and memory efficiency. 3DGS represents a scene using a collection of anisotropic 3D Gaussians, each defined by spatial position, scale, opacity, rotation, and spherical harmonic (SH) coefficients for view-dependent color. This differentiable rendering approach has demonstrated state-of-the-art performance in terms of rendering speed and quality, enabling real-time immersive view synthesis at high resolutions.

However, the advantages of 3DGS come with a substantial memory cost. 3DGS models frequently utilize millions of Gaussians for a single scene, leading to significant memory consumption during both training and inference. This large memory footprint restricts the deployment of 3DGS-based applications on memory-constrained platforms, such as edge devices.

Existing efforts to address this memory issue have primarily focused on pruning redundant Gaussians *post-training* to achieve a more compact scene representation for inference. Examples include LightGaussian and RadSplat, which reduce final storage. However, these post-training pruning strategies do not mitigate the high *peak memory consumption* that occurs during the training phase. The original 3DGS framework involves an uncontrolled densification process where the number of Gaussian primitives can rapidly increase to several million, causing substantial memory spikes early in training. This peak memory usage often exceeds the capacity of edge systems, thereby hindering real-time 3D applications in practical settings.

Previous work, such as Taming 3DGS, attempted to manage memory spikes during training by regulating Gaussian growth through a predictable curve and selectively cloning/splitting primitives based on an importance score. While Taming 3DGS reduced peak Gaussian counts, it introduced its own limitations: strict growth restrictions in early training could limit representational capacity, leading to persistent rendering errors; cloned Gaussians often inherited identical initial positions, resulting in redundant gradient updates; and the absence of an active Gaussian removal mechanism allowed poorly optimized Gaussians to persist.

This current work directly addresses the problem of high peak training memory consumption in 3DGS. It aims to develop a systematic memory-bounded training framework that actively manages Gaussian primitives throughout the training process, rather than relying solely on post-training optimizations or constrained growth, to enable high-quality 3DGS applications on memory-constrained devices.

### 3. Key Objectives and Motivation

The primary objective of this research is to develop a systematic memory-bounded 3D Gaussian Splatting (3DGS) training framework that addresses the issue of high peak training memory consumption while maintaining or improving rendering quality. This framework aims to enable the practical deployment of 3DGS on memory-constrained devices, such as NVIDIA Jetson AGX Xavier.

The motivation for this work stems from several limitations observed in existing 3DGS training approaches:

1.  **Uncontrolled Gaussian Densification and High Peak Training Memory:** The original 3DGS framework suffers from a substantial memory footprint, particularly during training, due to the uncontrolled growth of Gaussian primitives. Gaussians can abruptly expand to millions early in the training process, leading to significant peak memory spikes (e.g., 18.29 GB for 3DGS compared to 8.86 GB for the proposed method in Figure 1). Although many existing methods focus on pruning redundant Gaussians *after* training to reduce inference memory, they fail to address these critical peak memory demands during the training phase. This high peak memory consumption is a bottleneck for deploying 3DGS on edge devices.

2.  **Limitations of Existing Memory-Aware Training Strategies:** Prior attempts to mitigate training memory spikes, such as Taming 3DGS, regulate Gaussian growth but exhibit shortcomings:
    *   **Accumulated Errors due to Restricted Growth:** Taming 3DGS's strict growth restrictions in early training stages limit the model's representational capacity. The slow growth speed means that the model operates with a limited number of Gaussians for an extended period, potentially leading to accumulated rendering errors that are difficult to correct later (as shown in Figure 3, where Taming 3DGS fails to correct errors even after 10K iterations).
    *   **Ineffective Gaussian Refinement:** In existing methods, cloned Gaussians often inherit identical initial positions. This similarity in parameters results in them receiving similar gradient updates, hindering their ability to diverge spatially and effectively capture missing scene details. Consequently, a significant number of low-opacity Gaussians can persist, increasing redundancy and computational overhead.
    *   **Lack of Active Gaussian Removal:** Previous approaches often prune infrequently (e.g., every 500 iterations) or lack an effective mechanism to actively remove poorly optimized or "ill" Gaussians throughout training. Infrequent pruning makes it challenging to identify and remove true redundancies, as "error" information can become mixed among Gaussians over long intervals.

3.  **Incomplete Densification Criteria:** The densification process in 3DGS primarily relies on view-space positional gradients. While useful, these gradients are influenced by the magnitude of overlapped Gaussians' colors and may not accurately detect underfit areas, especially in blurred or low-contrast regions. This limitation can lead to permanently low-quality rendering results in such areas.

Inspired by the Lottery Ticket Hypothesis, which suggests that a sparse subnetwork can achieve performance comparable to a dense one, the authors hypothesize that an optimal sparse Gaussian model can be trained from scratch under strict memory limitations. The objective is to develop a systematic training framework that dynamically grows and removes Gaussian primitives based on more effective criteria, ensuring consistently low memory usage while progressively refining rendering fidelity to match or surpass the quality of original 3DGS.

### 4. Methodology and Approach

The proposed method, "Gaussians on a Diet," introduces a systematic memory-bounded training framework for 3D Gaussian Splatting that dynamically optimizes Gaussians through iterative growth and pruning. The framework alternates between incremental pruning of low-impact Gaussians and strategic growing of new primitives with an adaptive Gaussian compensation mechanism. This approach aims to maintain near-constant low memory usage while progressively refining rendering fidelity.

The overall workflow of the proposed framework, as illustrated in Figure 6, involves iteratively performing growing, compensation, and pruning steps within predefined intervals (e.g., every 50 or 100 iterations).

#### 4.1. Iterative Growing and Pruning

This core principle involves dynamically adding informative Gaussians and removing redundant ones at frequent intervals.

*   **Growing Step:**
    *   **Hybrid Gradient Criterion:** The paper identifies limitations in existing densification methods that primarily use view-space positional gradients (∇_p). These gradients are influenced by overlapping Gaussians' colors and may not accurately reflect rendering errors in underfit or blurry regions. To address this, the proposed method incorporates the color gradient (∇_c), which more accurately reflects rendering error in the actual rendering space and is not influenced by other Gaussians' colors. A mixed criterion, ∇_mix = ∇_p + ∇_c, is used to identify regions requiring densification for cloning and splitting Gaussians. This hybrid metric aims to provide a more informative cue for densifying under-structured geometric regions (Figure 5).
    *   **Dynamical Position Adjustment:** To mitigate the problem of cloned Gaussians overlapping and receiving similar gradient updates, an adaptive position adjustment method is introduced. When new Gaussians are cloned or split, their positions (μ_new) are shifted by a small distance based on the accumulated positional gradients from N views: μ_new = μ_old + Σ∇_μi. This slight shift helps new Gaussians diverge spatially and adaptively move to correct locations, thereby improving rendering quality and robustness.

*   **Pruning Step:**
    *   **Importance-Based Removal:** As new Gaussians are added, an equal number of the least important Gaussians are subsequently removed to ensure the total peak training memory remains under a predefined constraint (F). Instead of computationally expensive comprehensive importance scores, the method utilizes a light calculation by aggregating the ray contribution of Gaussians (G_i) along all rays of N views (R_f). The importance score R_i = max_r∈R_f α_r_i τ_r_i (where τ_i is the ray transmittance) reflects each Gaussian's blending contribution to the final pixel color. This metric can be computed efficiently within the existing rendering pipeline, incurring negligible overhead when performed, for example, every 100 iterations.
    *   **Benefits:** This iterative growing and pruning strategy enables consistent training on devices with strict memory constraints and allows the model to recover and re-optimize after each pruning, leading to a more balanced and high-quality sparse representation.

#### 4.2. Adaptive Gaussian Compensation

This step is designed to refine poorly reconstructed and sparsely covered areas, particularly those where positional gradients might remain stable but reconstruction errors persist.

*   **Identification of Underfitting Regions:** Gaussian compensation is performed before the pruning step. It identifies pixels with the highest per-pixel error, which is directly derived from the color gradient for each pixel during the backward pass, without additional computational cost.
*   **3D Gaussian Generation:**
    *   For the top-K pixels identified with the highest color gradient magnitude, their corresponding 3D positions are estimated. This is achieved by first approximating the depth (D) for each pixel using an alpha-blended depth calculation (D = Σ d_i α_i Π (1 - α_j)).
    *   Then, selected high-error pixels are projected back into 3D space, replacing d_i with d_mid (the Gaussian midpoints contributing most to the pixel).
    *   New Gaussians are generated at these computed 3D positions, and their colors are initialized with the ground truth pixel values of the corresponding high-error pixels (Figure 4).
*   **Timing:** This compensation process is performed at specified intervals (e.g., starting at 10K iterations and ending at 15K iterations in experiments), ensuring that new Gaussians are introduced in areas that are hard to capture by the original growth method.

#### 4.3. Memory Management

The framework includes a mechanism to strictly adhere to memory constraints:
*   **Threshold-based Pruning:** If the total number of Gaussians (|G|) exceeds the predefined target peak number (F), a specific number of Gaussians (K = F - |G|) identified as least important are pruned.
*   **Parallel Dataloader:** For practical deployment on extremely memory-constrained edge devices (like NVIDIA Jetson AGX Xavier), a parallel dataloader dynamically prefetches and moves data between storage and memory. This engineering optimization further reduces peak training memory usage.

In summary, the proposed framework iteratively refines the Gaussian representation by strategically growing new primitives based on hybrid gradients and dynamic position adjustment, compensating for underfitting regions with new Gaussians derived from pixel-wise errors, and consistently pruning low-impact Gaussians to stay within strict memory bounds. This dynamic process aims to discover and optimize a compact subset of Gaussians that preserves rendering fidelity while ensuring memory efficiency throughout training.

### 5. Main Findings and Results

The research evaluates the proposed memory-bounded 3DGS training framework on Mip-NeRF 360, Tank&Temple, and Deep-Blending datasets, comparing it against the original 3DGS, Taming 3DGS, and other state-of-the-art pruning methods like Mini-Splatting, Reducing-3DGS, Compact-3DGS, and EAGLES.

#### 5.1. Quantitative Results

*   **Rendering Quality vs. Peak Gaussians (Table 1):** The proposed method consistently outperforms Taming 3DGS in rendering quality, achieving an average improvement of 0.15 dB PSNR and a reduction of 0.03 LPIPS across all scenes, while maintaining a comparable or slightly lower peak number of Gaussians during training.
    *   For example, on Mip-NeRF 360, the method achieves 27.30 PSNR, 0.809 SSIM, 0.234 LPIPS with 0.628M Gaussians, compared to Taming 3DGS's 27.22 PSNR, 0.795 SSIM, 0.260 LPIPS with 0.632M Gaussians.
    *   Compared to Mini-Splatting and the vanilla 3DGS, the proposed method improves PSNR by 0.5 dB on the Tank&Temple dataset while significantly reducing the peak number of Gaussians by more than 6x (0.318M vs 4.320M for Mini-Splatting and 1.840M for 3DGS).

*   **Peak Training Memory Usage on Edge Devices (Table 2b):** The method practically enables on-device training on memory-constrained platforms.
    *   On an NVIDIA Jetson AGX Xavier, the proposed method reduces peak memory usage to 8.55 GB, nearly 2x lower than the original 3DGS (18.59 GB).
    *   With an additional parallel dataloader optimization, which dynamically prefetches and moves data, peak training memory is further reduced to 2.98 GB, representing an 80% reduction compared to the original 3DGS.

*   **Training Speed:** The framework also exhibits improved training speed. On the bicycle scene, the proposed approach reduces training time from 10 minutes to 7 minutes, achieving a 30% speedup compared to the per-splat parallelized backpropagation used in Taming 3DGS. This is attributed to more efficient memory usage and fewer redundant primitives.

#### 5.2. Visual Quality Results

*   **Perceptual Fidelity (Figures 7, 9, 10):** Rendered images demonstrate that the proposed method yields significantly higher visual quality, preserving high-frequency details and textural fidelity. For instance, in Figure 7, it captures fine details in grass, tree bark, and gravel surfaces, which appear blurry or indistinct in Taming 3DGS. This superior quality is consistently observed across multiple scenes and iterations.
*   **Gaussian Distribution (Figure 11):** Visualizations of Gaussian ellipsoids on the playroom scene indicate that the proposed method effectively reduces redundancy by minimizing excessive overlap among Gaussians. It dynamically allocates a higher density of Gaussians to texture-rich regions (e.g., patterns on a blanket), thereby better capturing complex scene content.
*   **Early Iteration Performance (Figure 8):** The actual rendering quality of the proposed method is shown to be superior to Taming 3DGS at earlier training iterations (e.g., 8K iterations for flowers, 2K iterations for kitchen), demonstrating the effectiveness of its iterative growing and pruning strategy over existing slower densification approaches.

#### 5.3. Ablation Study (Table 2a)

Ablation studies conducted on the Deep-Blending dataset (specifically "Playroom" and "Drjohnson" scenes, reporting LPIPS scores) quantify the contribution of each proposed component:

*   **Iterative Pruning (I.P.):** The iterative pruning strategy, which includes hybrid gradients for growing new Gaussians and position adjustment after cloning, contributes to continuous model refinement. Implementing this component improves LPIPS by approximately 0.015 (e.g., from 0.279 to 0.264 for "Playroom" compared to the baseline).
*   **Gaussian Compensation (G.C.):** The adaptive Gaussian compensation mechanism, which generates new Gaussians in high-error pixel areas, further improves perceptual fidelity. Its addition results in an additional LPIPS improvement of approximately 0.005 (e.g., from 0.264 to 0.259 for "Playroom").
*   **Mixed Gradients:** The use of mixed gradients (positional + color) for densification yields a modest improvement of +0.04 dB PSNR on the test dataset but shows a more significant gain of +0.87 dB PSNR on the training dataset for the 'kitchen' scene, indicating improved ability to capture details in underfit areas.

### 6. Significance and Potential Impact

This research presents a significant advancement in the field of 3D Gaussian Splatting by directly addressing a critical limitation: the substantial peak memory consumption during training. The development of a memory-bounded training framework holds several key significances and potential impacts:

1.  **Enabling Deployment on Memory-Constrained Devices:** The most direct impact is the practical enablement of high-quality 3DGS training on hardware with limited memory resources, such as embedded systems, mobile devices, and edge AI platforms (e.g., NVIDIA Jetson AGX Xavier). By achieving up to 80% lower peak training memory usage compared to the original 3DGS, the proposed framework removes a significant bottleneck for real-world deployment in resource-limited settings. This allows 3DGS to move beyond high-end GPUs into a wider range of applications.

2.  **Improved Training Efficiency and Quality:** The iterative growing and pruning mechanism, coupled with adaptive Gaussian compensation, leads to a more efficient and effective training process. The framework refines the Gaussian representation dynamically, identifying and optimizing "healthy" Gaussians while removing "ill" or redundant ones. This results in superior rendering quality, particularly in complex, high-frequency, or blurry regions, often achieved with fewer training iterations and a more compact model. The observed 30% speedup in training time further contributes to overall efficiency.

3.  **Enhanced Robustness and Representation:** The introduction of hybrid gradients for densification and dynamic position adjustment for new Gaussians allows the model to better capture underfit geometric and textural details. By reducing redundant overlapping Gaussians and enabling more distinct gradient updates, the scene representation becomes more robust and accurate. The adaptive Gaussian compensation mechanism acts as a fine-grained refinement step, specifically targeting and correcting errors in challenging areas that might otherwise persist.

4.  **Advancement in Sparse Learning for 3DGS:** The work extends concepts from sparse training in neural networks (like the Lottery Ticket Hypothesis) to 3DGS. It demonstrates that it is possible to train an optimal sparse Gaussian model from scratch under strict memory limitations, progressively discovering an effective set of primitives that matches or surpasses the fidelity of denser models. This could inspire further research into intrinsically sparse and memory-efficient 3D representations.

5.  **Broadened Application Scope:** By making 3DGS more accessible and efficient, this work expands its potential application in areas such as:
    *   **Augmented Reality (AR) and Virtual Reality (VR):** Enabling real-time 3D scene reconstruction and rendering on mobile AR/VR devices.
    *   **Robotics and Autonomous Navigation:** Facilitating efficient 3D environment mapping and perception for resource-constrained robotic systems.
    *   **Digital Content Creation:** Providing artists and developers with more accessible tools for high-fidelity 3D asset generation and scene editing.
    *   **Real-time 3D Sensing and Reconstruction:** Enhancing the capability of systems that capture and render 3D environments on-the-fly.

In conclusion, this research provides a scalable and practical solution for training high-quality 3DGS models under hardware constraints, overcoming a major hurdle for its widespread adoption in resource-limited environments while maintaining or improving visual fidelity and training efficiency.
