---
title: "You Only Gaussian Once: Controllable 3D Gaussian Splatting for Ultra-Densely Sampled Scenes"
date: 2026-04-23
arxiv: "2604.21400v1"
venue:
status: to-read

abstract: "3D Gaussian Splatting (3DGS) has revolutionized neural rendering, yet existing methods remain predominantly research prototypes ill-suited for production-level deployment. We identify a critical &#34;Industry-Academia Gap&#34; hindering real-world application: unpredictable resource consumption from heuristic Gaussian growth, the &#34;sparsity shield&#34; of current benchmarks that rewards hallucination over physical fidelity, and severe multi-sensor data pollution. To bridge this gap, we propose YOGO (You Only Gaussian Once), a system-level framework that reformulates the stochastic growth process into a deterministic, budget-aware equilibrium. YOGO integrates a novel budget controller for hardware-constrained resource allocation and an availability-registration protocol for robust multi-sensor fusion. To push the boundaries of reconstruction fidelity, we introduce Immersion v1.0, the first ultra-dense indoor dataset specifically designed to break the &#34;sparsity shield.&#34; By providing saturated viewpoint coverage, Immersion v1.0 forces algorithms to focus on extreme physical fidelity rather than viewpoint interpolation, and enables the community to focus on the upper limits of high-fidelity reconstruction. Extensive experiments demonstrate that YOGO achieves state-of-the-art visual quality while maintaining a strictly deterministic profile, establishing a new standard for production-grade 3DGS. To facilitate reproducibility, part scenes of Immersion v1.0 dataset and source code of YOGO has been publicly released. The project link is this https URL."

website: https://jjrcn.github.io/YOGO
code: 
openreview: 
issue: 32

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

# You Only Gaussian Once: Controllable 3D Gaussian Splatting for Ultra-Densely Sampled Scenes

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

![Figure](https://arxiv.org/html/2604.21400v1/img1.jpg)

*Figure 1: (A) Vanilla 3DGS suffers from uncontrollable growth and OOM risks on our challenging Immersion dataset. (B) YOGO ensures high-fidelity reconstruction under a deterministic budget (e.g., 1.5M points) via robust multi-sensor fusion. (C) Unlike sparse conventional benchmarks (left), Immersion provides ultra-dense saturation (right), breaking the sparsity shield to force true physical fidelity.*

![Figure](https://arxiv.org/html/2604.21400v1/img2.jpg)

*Figure 2: Overview of the YOGO Framework. The pipeline begins with multi-sensor data undergoing Availability-Registration Multi-Sensor Fusion (Sec. 3.2) to filter polluted inputs. Under the deterministic budget controller (Sec. 3.1), the number of Gaussian points at each stage is strictly controlled, which regulates growth based on preset constraints and Polygon regions. The process is enhanced by the Solid Optimization Suite (Sec. 3.3) for robust handling of complex textures.*

![Figure](https://arxiv.org/html/2604.21400v1/img3.jpg)

*Figure 3: Characteristics of the Immersion Dataset. (A) Heterogeneous multi-sensor capture rigs. (B) Ultra-dense capture that breaks the "sparsity shield." (C) Example frames showing challenging real-world attributes: weak texture, complex texture, high specularity &amp; transmission, complex lighting, over exposure, and narrow space.*

![Figure](https://arxiv.org/html/2604.21400v1/img5.jpg)

*Figure 4: Qalign correlation with PSNR, SSIM, and LPIPS (95% confidence intervals, p&lt;0.001) alongside example renderings sorted by increasing Qalign. Higher Qalign values consistently correspond to improved perceptual quality, demonstrating its reliability as a no-reference 3DGS metric.*

![Figure](https://arxiv.org/html/2604.21400v1/img4.jpg)

*Figure 5: Qualitative comparison across Immersion v1.0 dataset.*

## LLM Summary

This report provides a detailed analysis of the research paper "You Only Gaussian Once: Controllable 3D Gaussian Splatting for Ultra-Densely Sampled Scenes," referred to as YOGO. The paper introduces a system-level framework for deterministic and robust 3D Gaussian Splatting, alongside a novel ultra-dense dataset.

---

### 1. Authors and Institution(s)

The authors of this research are Jinrang Jia, Zhenjia Li, and Yifeng Shi. Jinrang Jia and Zhenjia Li are noted as having contributed equally to the work, while Yifeng Shi is designated as the corresponding author. All authors are affiliated with Ke Holdings Inc., located in Beijing, China.

### 2. How This Work Fits into the Broader Research Landscape

The development of 3D Gaussian Splatting (3DGS) by Kerbl et al. [13] marked a significant advancement in neural rendering, enabling real-time radiance field reconstruction with an explicit, point-based geometry. Prior to 3DGS, Neural Radiance Fields (NeRF) [26] and its accelerations like Instant-NGP [27] offered high-fidelity view synthesis but were computationally intensive and implicit, posing challenges for real-time rendering in complex scenes. 3DGS addressed these limitations by combining an explicit representation with an optimized rasterizer, leading to rapid real-time rendering.

Following the introduction of 3DGS, the research community has focused on enhancing its capabilities and addressing its initial constraints. Efforts have been directed towards improving geometric accuracy and surface modeling (e.g., SuGaR [9], 2DGS [10]), mitigating aliasing artifacts (e.g., Mip-Splatting [38]), and optimizing structural efficiency and densification logic (e.g., Scaffold-GS [24], absGS [36], pixelGS [41]). These works have primarily focused on improving visual quality, efficiency, or specific aspects of the Gaussian representation.

Despite these advancements, the authors identify a critical "Industry-Academia Gap" that restricts 3DGS from widespread production-level deployment. Existing 3DGS methods often function as academic prototypes, struggling with the high-frequency textures, complex occlusions, and stringent resource constraints characteristic of real-world applications such as digital twins and autonomous driving. A central issue highlighted is the reliance on heuristic densification, which results in unpredictable primitive counts and memory footprints, complicating deployment on hardware with fixed budgets. Furthermore, conventional benchmarks, characterized by sparse viewpoint sampling (e.g., Mip-NeRF 360 [2], Tanks & Temples [15]), inadvertently incentivize algorithms to interpolate or "hallucinate" missing scene information rather than achieving absolute physical fidelity. Real-world data acquisition also introduces "data pollution" from heterogeneous sensors, with varying radiometric properties and noise profiles.

YOGO distinguishes itself by directly confronting these limitations. Unlike prior research that predominantly focuses on post-hoc optimization or incremental improvements to rendering quality, YOGO fundamentally re-engineers the 3DGS pipeline to achieve deterministic resource consumption and robust multi-sensor fusion. It moves beyond the "uncontrollable one-way causal" densification process by introducing explicit budget control, which is a departure from the heuristic approaches common in existing explicit rendering frameworks. Concurrently, the introduction of the Immersion v1.0 dataset aims to establish a new evaluation paradigm, challenging algorithms to demonstrate true physical fidelity under ultra-dense sampling conditions, thereby breaking the "sparsity shield" of traditional benchmarks. This work positions itself as a step towards making 3DGS a more reliable and deployable technology for industrial applications.

### 3. Key Objectives and Motivation

The overarching objective of this research is to bridge what the authors term the "Industry-Academia Gap" in 3D Gaussian Splatting (3DGS), with the goal of enabling the transition of 3DGS from a research prototype to a deployable, production-ready technology. This primary objective is driven by several specific motivations and addresses identified limitations of existing 3DGS methodologies:

1.  **Addressing Unpredictable Resource Consumption:** Current 3DGS pipelines utilize heuristic densification strategies, which lead to an unpredictable final number of Gaussian primitives and, consequently, an uncontrolled memory footprint. For real-world applications, particularly on edge hardware with strict memory and computational budgets, this non-deterministic behavior necessitates extensive trial-and-error parameter tuning. The motivation is to reformulate this stochastic growth into a deterministic, budget-aware process to ensure strict adherence to hardware constraints and enable predictable resource allocation.

2.  **Overcoming the "Sparsity Shield" in Benchmarks:** Existing 3D reconstruction benchmarks, characterized by sparse viewpoint sampling, often compel algorithms to perform significant interpolation or "hallucination" of missing geometric and textural information. This evaluation paradigm can obscure an algorithm's true capacity for physical fidelity, as success is measured by plausible view synthesis rather than precise reconstruction of reality. A key motivation is to shift this paradigm by creating a dataset with saturated viewpoint coverage, thereby forcing algorithms to prioritize extreme physical fidelity and robust reconstruction over imaginative infilling.

3.  **Mitigating Multi-Sensor Data Pollution:** Real-world data acquisition frequently involves heterogeneous sensors, which introduces inconsistencies such as varying exposures, color profiles, and noise characteristics. Naive fusion of such "polluted" data can degrade reconstruction quality. The motivation is to develop a robust multi-sensor fusion protocol that can identify, register, and filter out non-compliant data, ensuring a high-quality, consistent input for 3DGS training.

4.  **Enhancing Reconstruction Fidelity and Efficiency:** Beyond the system-level concerns, there is a motivation to improve the intrinsic rendering quality and structural efficiency of 3DGS. This includes preserving high-frequency details, preventing blurring in texture-dense regions, effectively pruning redundant primitives, and efficiently recovering thin structures and anisotropic textures, all while compressing the model size.

To address these motivations, the key objectives of the YOGO framework are:
*   To implement a Deterministic Budget Controller that can enforce strict, hardware-defined primitive budgets and allow for localized resource allocation.
*   To establish an Availability-Registration Multi-Sensor Fusion protocol for robust integration of heterogeneous data by quantitatively assessing and filtering data quality.
*   To integrate a Solid Optimization Suite encompassing techniques like Area-Normalized Gradient Accumulation, Maximum Effective Opacity Pruning, and Principal Axis Densification to improve detail recovery and model compression.
*   To introduce Immersion v1.0, an ultra-dense, multi-sensor indoor dataset designed to serve as a new benchmark for evaluating absolute physical fidelity and robustness to heterogeneous data.

Through these objectives, the research aims to establish a new standard for resource-controllable, high-fidelity 3DGS that is suitable for real-world deployment.

### 4. Methodology and Approach

The YOGO framework proposes a system-level approach to controllable 3D Gaussian Splatting, integrating novel components to address determinism, multi-sensor fusion, and reconstruction fidelity.

**4.1 Deterministic Budget Controller (DBC)**
The DBC replaces heuristic Gaussian growth with a budget-driven mechanism.
*   **Spatial Partitioning:** The scene is divided into `M` disjoint spatial polygons `P = {P1, ..., PM}`. Each polygon is assigned a target Gaussian budget (`N_target_m`), which can be defined by users or hardware constraints.
*   **Budget-Aware Regulation:** During densification steps (scheduled between start `S` and end `E` iterations with interval `D`), a "prune-then-densify" sequence is applied. After pruning, the current Gaussian count (`N_cur_m(k)`) in each polygon `P_m` is noted. The remaining budget gap (`∆N_m(k) = N_target_m − N_cur_m(k)`) informs the densification quota (`N_densify_m(k) = max(0, ∆N_m(k) / (K − k + 1))`), ensuring stable convergence towards the target budget. `K` represents the total number of densification events.
*   **Importance-Driven Selection:** Instead of fixed gradient thresholds, YOGO selects the top `Q` Gaussians (where `Q` is the allocated densification quota) with the highest accumulated gradient magnitudes (`∥∇μ∥`) within each polygon `P_m`. This approach provides deterministic control over the final primitive count and allows for multi-granular, localized resource allocation.

**4.2 Availability-Registration Multi-Sensor Fusion**
This protocol addresses data pollution from heterogeneous sensors through a hierarchical training pipeline.
*   **Foundation Training:** An initial 3DGS anchor model is trained using data exclusively from a designated primary sensor (`D_pri`).
*   **Radiometric Registration:** With the anchor model frozen, auxiliary sensor data (`D_aux`) is introduced. For each auxiliary image `I_j`, a per-view affine transformation (`C_trans = G_j C_rend + b_j`) is optimized. This transformation, represented by `A_j = [G_j |b_j]`, decouples exposure and sensor-specific biases.
*   **Hybrid Training:** Auxiliary frames are filtered based on an "Availability Score" before joint optimization with `D_pri`.
*   **Availability Scoring and Outlier Rejection:** The Availability Score `S_j` quantifies the deviation of `A_j` from an identity transformation. It is calculated as `S_j = ∥diag(G_j) − 1∥∞ + avg(|offdiag(G_j)|) + avg(|b_j|)`. Samples exceeding a threshold (`S_j > τ`) are rejected. This process aims to ensure that only radiometrically consistent and geometrically aligned auxiliary data contributes to the final model.

**4.3 The Solid Optimization Suite**
A collection of targeted enhancements for fidelity and robustness:
*   **Area-Normalized Gradient Accumulation:** To mitigate blurring in texture-dense areas, an Area-Normalized Absolute Gradient (`¯G_accum`) is computed. This metric averages per-pixel absolute gradients over visible views, normalized by the total pixel footprint across those views. This prevents directional cancellation and footprint bias, targeting regions with high reconstruction error.
*   **Pruning via Maximum Effective Opacity:** Standard pruning based on intrinsic opacity (`α < ϵ`) can retain Gaussians that are effectively occluded. YOGO introduces "Effective Opacity" (`ˆα = α · T`, where `T` is accumulated transmittance). Primitives are pruned if their Maximum Per-View Effective Opacity (`ˆα_max`, computed as the maximum average `ˆα` over any visible view's pixel footprint) falls below a threshold (`τ_opacity`). This aims to remove visually redundant Gaussians without quality loss.
*   **Principal Axis Densification:** To recover thin structures and anisotropic textures, "split" and "clone" operations are unified. For a Gaussian exceeding a gradient threshold, three new Gaussians are generated along its major scaling axis. New world-space positions are `x_new = {x + R∆l, x, x − R∆l}` where `∆l` is a perturbation along the principal axis. Scaling and opacity are attenuated for energy conservation.

**4.4 The Immersion v1.0 Dataset**
Immersion v1.0 is designed to break the "sparsity shield" of existing benchmarks.
*   **Heterogeneous Multi-Sensor Acquisition:** The dataset uses an Insta360 X5 Engine (panoramic video), an Osmo High-Dynamic Array (four synchronized units), and a SHARE SLAM S20 (hybrid LiDAR-Visual system) for diverse data capture. The LiDAR provides geometric "ground truth."
*   **Saturated Acquisition Protocol:** A "Six-Loop Trajectory Strategy" is employed, involving multi-level coverage (High, Medium, Low heights), bi-directional sampling (clockwise and counter-clockwise loops), and supplementary close-up shots. This ensures comprehensive scene observation from numerous overlapping angles.
*   **Dataset Characteristics:** Quantitative metrics include Image Density per Square Meter (IDSM) and Scene Coverage (ratio of "effectively occupied" 0.2m x 0.2m grid cells with >6 camera poses). Immersion v1.0 offers significantly higher image counts (∼30K vs. ∼2K for ScanNet++), initial points (∼2.55M vs. ∼161K), IDSM (500 vs. 130), and coverage (72% vs. 16%) compared to conventional benchmarks. It also includes multi-sensor and LiDAR data support across multi-room environments.
*   **Evaluation Metrics:** Standard metrics (PSNR, SSIM, LPIPS) are complemented by Qalign [31], a perceptual-level metric driven by large multi-modality models, used for no-reference evaluation on out-of-distribution "roaming" test sets.
*   **Evaluation Tracks:** Three tracks are defined: Single-Sensor Sparse (SSS), Single-Sensor Dense (SSD), and Multi-Sensor Dense (MSD) to assess performance under varying data density and fusion conditions.

### 5. Main Findings and Results

The research presents several findings regarding the YOGO framework's performance, the utility of its components, and the characteristics of the Immersion v1.0 dataset.

**5.1 Reliability of the Qalign Metric**
The Qalign [31] metric demonstrated a strong positive correlation with PSNR (r=0.95, p < 0.001) and SSIM (r=0.94, p < 0.001), and a strong negative correlation with LPIPS (r=-0.95, p < 0.001). This consistency with established perceptual metrics supported its use as a primary evaluator for scenarios where ground truth is unavailable, such as the Roaming Test Set.

**5.2 Deterministic Budget Controller Analysis**
The Deterministic Budget Controller (DBC) enabled explicit control over the number of Gaussians, facilitating a performance-memory trade-off analysis. Benchmarking three budget variants (YOGO1, YOGO2, YOGO3) revealed distinct performance saturation points. For instance, on the Single-Sensor Sparse (SSS) track, increasing the budget from YOGO1 to YOGO2 (an addition of approximately 2 million points) yielded a 0.13 improvement in Qalign. However, a subsequent increase to YOGO3 (another approximately 2 million points) resulted in a marginal 0.04 Qalign gain. This observation indicates that the DBC allows for identifying an optimal balance between visual fidelity and computational cost, preventing unnecessary memory allocation.

**5.3 State-of-the-Art Comparison on Immersion v1.0**
YOGO was benchmarked against leading explicit 3DGS frameworks: 3DGS [13], AbsGS [36], Mip-Splatting [38], Scaffold-GS [24], and Perceptual-GS [42]. Evaluation on the ultra-dense Immersion v1.0 dataset presented computational challenges for some baselines, leading to Out-Of-Memory (OOM) failures or excessive overhead on the Single-Sensor Dense (SSD) and Multi-Sensor Dense (MSD) tracks.

Quantitative results (Table 2) showed YOGO consistently outperforming these existing architectures across various metrics (PSNR, SSIM, LPIPS, Qalign). Notably, on both SSD and MSD tracks, the most resource-constrained YOGO variant (YOGO1, with approximately 1.5 million points) achieved superior rendering quality compared to AbsGS, which utilized a larger model (approximately 4.28 million points). This indicates enhanced structural efficiency of the YOGO framework.

A significant observation emerged from the multi-modal fusion evaluation: on the Validation Set, MSD metrics slightly lagged behind SSD metrics. However, on the Roaming Test Set (which features out-of-distribution viewpoints), MSD consistently yielded higher Qalign scores. This inversion suggests that while single-sensor models (SSD) may overfit to the specific capture trajectory, the integration of auxiliary sensor data (MSD) compels the model to construct a more robust and geometrically complete scene representation, thereby improving generalization to novel viewpoints.

**5.4 Ablation Studies**
*   **Multi-Sensor Fusion Strategies (Table 3):** An ablation study on multi-sensor fusion strategies demonstrated the effectiveness of the Availability-Registration Protocol. Direct fusion of multi-sensor data without quality control resulted in degraded performance due to radiometric "data pollution." In contrast, the Availability-Registration Protocol, particularly with a strictness threshold of `τ = 0.15`, successfully filtered severe sensor inconsistencies. This selective fusion leveraged compliant auxiliary data to enhance generalization on the Test Set.
*   **The Solid Optimization Suite (Table 4):** A component-wise analysis of the Solid Optimization Suite revealed compounding gains from each module. Starting from the DBC baseline, progressively enabling Area-Normalized Gradient Accumulation, Maximum Effective Opacity Pruning, and Principal Axis Densification led to incremental improvements in reconstruction quality. The combination of Area-Normalized Gradient and Principal Axis Densification was observed to be particularly effective in preventing blurring in texture-dense regions and accurately recovering anisotropic structures prevalent in complex indoor environments.

### 6. Significance and Potential Impact

The YOGO framework and the Immersion v1.0 dataset collectively address several limitations in 3D Gaussian Splatting (3DGS), signifying a step towards more practical and robust real-world applications.

**Bridging the Industry-Academia Gap:** The primary significance of this work lies in its explicit aim to bridge the "Industry-Academia Gap." By introducing deterministic resource control, YOGO directly tackles the challenge of unpredictable memory and computational demands of 3DGS, which has been a barrier to its adoption in production environments with strict hardware constraints. This deterministic profile can streamline deployment and reduce development costs in industrial settings.

**Establishing a New Standard for Production-Grade 3DGS:** YOGO's ability to maintain state-of-the-art visual quality under strictly controlled resource budgets, as demonstrated by its performance against existing methods, suggests a new standard for production-grade 3DGS. The framework's components, such as the Deterministic Budget Controller and the Solid Optimization Suite, contribute to both efficiency and fidelity, which are critical for industrial applications like digital twins and autonomous driving.

**Advancing Reconstruction Fidelity and Generalization:** The Immersion v1.0 dataset facilitates a shift in the evaluation paradigm. By providing ultra-dense viewpoint coverage, it moves beyond assessing an algorithm's ability to interpolate sparse views and instead measures its capacity for absolute physical fidelity. This new benchmark encourages the development of algorithms that prioritize accurate reconstruction over "hallucination," leading to more trustworthy 3D models. The observed improvement in out-of-distribution generalization on the Roaming Test Set when using Multi-Sensor Dense data highlights the framework's ability to learn more robust and complete scene representations, which is crucial for dynamic and varied real-world scenarios.

**Robust Multi-Sensor Data Fusion:** The Availability-Registration Protocol offers a practical solution to the challenge of "data pollution" from heterogeneous sensors. By intelligently filtering inconsistent auxiliary data, YOGO can leverage multi-modal inputs to enhance model robustness without degrading quality, which is highly relevant for large-scale data acquisition pipelines that often combine diverse sensor types.

**Efficient Resource Utilization:** The Deterministic Budget Controller's ability to allow for precise control over Gaussian counts, even at a localized polygon level, enables targeted allocation of computational resources. This can lead to more efficient use of memory and processing power, focusing fidelity where it is most needed while maintaining overall model compression.

**Facilitating Future Research:** The public release of partial Immersion v1.0 scenes and YOGO's source code promotes reproducibility and provides a robust foundation for future research. This allows the community to build upon the work, focusing on areas such as semantic-aware budget allocation or extending the framework to dynamic, unbounded environments, as suggested by the authors for future work.

In conclusion, this research offers a practical and technically rigorous advancement in the field of neural rendering, making 3DGS a more viable technology for high-fidelity, resource-constrained real-world applications.
