---
title: "DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis"
date: 2026-04-15
arxiv: "2604.13416v1"
venue:
status: to-read

abstract: "Advances in radiance fields have enabled photorealistic novel view synthesis. In several domains, large-scale real-world datasets have been developed to support comprehensive benchmarking and to facilitate progress beyond scene-specific reconstruction. However, for distractor-free radiance fields, a large-scale dataset with clean and cluttered images per scene remains lacking, limiting the development. To address this gap, we introduce DF3DV-1K, a large-scale real-world dataset comprising 1,048 scenes, each providing clean and cluttered image sets for benchmarking. In total, the dataset contains 89,924 images captured using consumer cameras to mimic casual capture, spanning 128 distractor types and 161 scene themes across indoor and outdoor environments. A curated subset of 41 scenes, DF3DV-41, is systematically designed to evaluate the robustness of distractor-free radiance field methods under challenging scenarios. Using DF3DV-1K, we benchmark nine recent distractor-free radiance field methods and 3D Gaussian Splatting, identifying the most robust methods and the most challenging scenarios. Beyond benchmarking, we demonstrate an application of DF3DV-1K by fine-tuning a diffusion-based 2D enhancer to improve radiance field methods, achieving average improvements of 0.96 dB PSNR and 0.057 LPIPS on the held-out set (e.g., DF3DV-41) and the On-the-go dataset. We hope DF3DV-1K facilitates the development of distractor-free vision and promotes progress beyond scene-specific approaches."

website: 
code: 
openreview: 
issue: 47

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

# DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis

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

![Figure](https://arxiv.org/html/2604.13416v1/x1.png)

*Figure 1: Features of the DF3DV-1K dataset and benchmark. (a) DF3DV-1K Dataset. We introduce DF3DV-1K, a large-scale distractor-free dataset comprising 1,048 manually captured indoor and outdoor scenes, with clean and cluttered images per scene spanning 128 distractor types. (b) Distractor-Free Dataset Comparison. * denotes log scale in the normalized radar chart. We compare DF3DV-1K with public datasets [sabour2023robustnerf, Ren2024NeRF], showing a larger scale (e.g., ∼\sim100×\times more scenes), broader scene diversity (e.g., ∼\sim10×\times more distractor types), and increased difficulty, reflected by higher 3DGS [kerbl20233d] LPIPS. (c) DF3DV-1K Benchmark. A comprehensive benchmark across nine recent distractor-free radiance field methods [sabour2025spotlesssplats, 2025RobustSplat, ling2025ocsplats, markin2024t, kulhanek2024wildgaussians, wang2025desplat, wang2025degauss, li2025asymgs] and 3DGS [kerbl20233d] reveals varying levels of robustness to distractors.*

![Figure](https://arxiv.org/html/2604.13416v1/x2.png)

*Figure 2: Comparison of radiance fields. (a) Distractor-free tasks [Ren2024NeRF] use casually captured images within a short period. (b) In-the-wild tasks [martin2021nerf, jin2021image], with large temporal gaps, often target images collected across seasons. (c) Dynamic tasks [wu2022d] target 4D scene synthesis and assume densely captured sequential data.*

![Figure](https://arxiv.org/html/2604.13416v1/x3.png)

*Figure 3: Number of distractor-free radiance field papers. The first distractor-free radiance field method [sabour2023robustnerf], targeting images captured over short time spans, was introduced in 2023 together with a benchmark. The research area rapidly gained attention in 2024 with the release of the On-the-go benchmark [Ren2024NeRF]. Although the number of works doubled in 2025, a public, large-scale, challenging dataset and benchmark systematically designed for this area are still lacking.*

![Figure](https://arxiv.org/html/2604.13416v1/x4.png)

*Figure 4: Samples of systematically designed scenarios in DF3DV-41. Each example, where green and red boxes denote clean and cluttered images, respectively, illustrates a carefully designed scenario with curated distractor types or scene conditions, highlighting the benchmark’s diversity. These 17 scenarios systematically evaluate the robustness of distractor-free 3D reconstruction methods under challenging conditions.*

![Figure](https://arxiv.org/html/2604.13416v1/x5.png)

*Figure 5: Dataset difficulty analysis via per-image performance distributions. DF3DV-1K shows wider LPIPS and SSIM distributions, indicating greater diversity and increased difficulty. In contrast, RobustNeRF [sabour2023robustnerf] is relatively clean, where a vanilla 3DGS [kerbl20233d] frequently achieves PSNR values exceeding 30 dB.*

![Figure](https://arxiv.org/html/2604.13416v1/x6.png)

*Figure 6: Overview of the data collection and curation pipeline. (a) Scene design and capture. We design scenes with predefined themes, distractor types, coverage (e.g., 180∘180^{\circ}-360∘360^{\circ}), viewpoint orientation (e.g., landscape or portrait), and the number of images per scene. Images are captured using consumer cameras (e.g., iPhone). Camera settings such as exposure and focus are set to automatic by default and adjusted only when necessary. Anti-shake settings are disabled to ensure consistent image resolution within each scene. For controllable setups, clean and cluttered scenes are captured separately. Otherwise, they are captured simultaneously and later separated by operators. (b) Data curation. Low-quality images (e.g., defocused samples) are removed through manual inspection by two experts per scene. Then, camera poses are jointly estimated using COLMAP [schoenberger2016mvs, schoenberger2016sfm], followed by image undistortion. Next, scenes are reconstructed with instant-ngp [muller2022instant] for verification. Failed cases are reprocessed with adjusted COLMAP [schoenberger2016mvs, schoenberger2016sfm] parameters and discarded if reconstruction remains unsuccessful. Finally, metadata are manually annotated.*

![Figure](https://arxiv.org/html/2604.13416v1/x7.png)

*Figure 7: Distribution of DF3DV-1K by capture device, resolution, and month of data collection. The distributions highlight the diversity of acquisition settings.*

![Figure](https://arxiv.org/html/2604.13416v1/x10.png)

*Figure 8: Scene count distribution. Clean images per scene skew slightly toward lower bins for efficient novel-view benchmarking, whereas cluttered images extend toward higher bins to capture diverse distractor conditions. Total images per scene remain comparable to typical non-sparse radiance field settings.*

![Figure](https://arxiv.org/html/2604.13416v1/x11.png)

*Figure 9: Qualitative results of the radiance field methods on DF3DV-41. The benchmark introduces systematically challenging conditions that enable clear visual comparison across methods and support the evaluation of robustness differences. For instance, WildGaussian [kulhanek2024wildgaussians] is less robust to color-similar distractors and tends to blend the black distractors with the background, while DeSplat [wang2025desplat] produces a noisier background in the chess scene.*

![Figure](https://arxiv.org/html/2604.13416v1/x12.png)

*Figure 10: Qualitative results of enhancers. Leveraging DF3DV-1K*, a large-scale and diverse dataset, DI2FIX effectively removes distractor artifacts (e.g., dynamic chess pieces and vegetable artifacts) while inpainting occluded regions in target views.*

![Figure](https://arxiv.org/html/2604.13416v1/x13.png)

*Figure 11: Qualitative results of DI2FIX trained with different data scales. Increasing the amount and diversity of training data improves robustness. In particular, DI2FIX progressively removes distractor artifacts (e.g., the chess pieces) while avoiding incorrect modifications to static scene content (e.g., the animal toy).*

![Figure](https://arxiv.org/html/2604.13416v1/x14.png)

*Figure 12: Qualitative results of DI2FIX trained using different LPIPS filtering thresholds. Overly strict thresholds (e.g., 0.1) exclude many challenging image pairs, making artifacts difficult to remove (e.g., floaters around the cutting board). Overly loose thresholds (e.g., 0.9) introduce excessive noisy training samples, which may lead to undesired modifications of scene content (e.g., disappearing game cards). A moderate threshold provides a better balance between data quality and diversity.*

## LLM Summary

## Research Paper Report: DF3DV-1K: A Large-Scale Dataset and Benchmark for Distractor-Free Novel View Synthesis

### 1. Authors and Institution(s)

The research paper was authored by:
*   Cheng-You Lu, Charlie Li-Ting Tsai, Yu-Cheng Chang, Thomas Do, and Chin-Teng Lin from the University of Technology Sydney.
*   Yi-Shan Hung from the University of Sydney.
*   Wei-Ling Chi and Hao-Ping Wang (equal contribution), and Yu-Lun Liu from National Yang Ming Chiao Tung University.

### 2. How this work fits into the broader research landscape

Novel view synthesis, particularly through radiance fields such as Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3DGS), has achieved photorealistic rendering capabilities. The broader research landscape in this area is characterized by several specialized sub-fields. These include:

*   **Scene-specific reconstruction:** Focusing on optimizing a radiance field for a single static scene.
*   **Generalizable models:** Aiming to reconstruct new scenes from a few input images without extensive per-scene optimization.
*   **Dynamic radiance fields:** Addressing the challenge of synthesizing novel views of scenes with moving objects or temporal changes (4D scenes).
*   **"In-the-wild" radiance fields with large temporal gaps:** Dealing with images captured over extended periods, often across different seasons or lighting conditions, where appearance changes are significant.

Within this landscape, a distinct and rapidly growing area is **distractor-free radiance fields**. These methods aim to synthesize clean, static novel views from casually captured image collections that frequently contain visual distractors (e.g., transient objects, moving people, or unwanted items) present during a short-span capture.

Prior to this work, the development of distractor-free radiance fields was primarily supported by smaller-scale datasets like RobustNeRF and On-the-go. RobustNeRF offered five indoor tabletop scenes with clean and cluttered images, while On-the-go extended this to twelve scenes, including outdoor environments, and introduced more distractor types. However, as distractor-free methods have advanced, these existing datasets have become less challenging, making it difficult to differentiate the performance of state-of-the-art approaches. This limitation often necessitated qualitative evaluations based on subtle background differences visible only upon zooming, and hindered the transition from scene-specific optimization to generalizable solutions.

This paper addresses this gap by introducing a significantly larger and more diverse dataset and benchmark specifically designed for distractor-free novel view synthesis. By providing a comprehensive and challenging evaluation platform, it aims to accelerate the development of more robust and generalizable methods in this specialized domain.

### 3. Key objectives and motivation

The primary objective of this research is to advance the field of distractor-free novel view synthesis by introducing a large-scale, real-world dataset and a comprehensive benchmark. This aims to overcome identified limitations in existing resources and facilitate future research.

The motivation for this work stems from two main issues observed in the current state of distractor-free radiance field research:

1.  **Saturation of existing benchmarks and difficulty in performance differentiation:** Current public datasets (e.g., RobustNeRF, On-the-go) for distractor-free radiance fields are limited in scale and diversity. While these datasets have supported initial progress, the rapid advancement of methods has led to a point where many state-of-the-art approaches achieve similar performance metrics on these benchmarks. This makes it challenging for researchers to precisely identify the strengths, limitations, and marginal improvements of new methods. Qualitative comparisons often rely on minute background differences, which can be ambiguous or only discernible under specific viewing conditions (e.g., zoomed-in views). The rapid increase in the number of distractor-free papers, particularly in 2025, further underscored the urgent need for a more challenging and systematic evaluation platform to keep pace with methodological innovation.

2.  **Hindrance to developing generalizable solutions:** The relatively small scale and limited diversity of existing distractor-free datasets restrict the training of models that can generalize across different scenes. Most contemporary distractor-free radiance field methods still require per-scene optimization, which is computationally intensive and not scalable for widespread application. The lack of a large-scale, real-world dataset with paired clean and cluttered images prevents researchers from leveraging extensive data for training generalizable models, thereby delaying the shift from scene-specific approaches towards more practical, generalizable solutions that do not require extensive test-time optimization.

To address these motivations, the authors established the following key objectives:

*   To create **DF3DV-1K**, a large-scale, real-world, and diverse dataset comprising 1,048 scenes, each featuring both clean and cluttered image sets, covering a broad range of indoor and outdoor environments, distractor types, and scene themes.
*   To design **DF3DV-41**, a curated subset of 41 scenes, specifically tailored to systematically evaluate the robustness of distractor-free methods under challenging scenarios.
*   To establish a **comprehensive benchmark** across DF3DV-1K and DF3DV-41, evaluating ten representative distractor-free radiance field methods and 3DGS, enabling systematic analysis of method robustness and identification of challenging scenarios.
*   To demonstrate the utility of DF3DV-1K in enabling progress beyond scene-specific methods, specifically by **fine-tuning a diffusion-based 2D enhancer (DI2FIX)** to improve the rendering quality of distractor-free radiance fields without per-scene model modifications. This serves as a proof-of-concept for developing generalizable solutions.

### 4. Methodology and approach

The methodology encompasses the design, acquisition, and curation of the DF3DV-1K dataset, its application in a comprehensive benchmark, and a demonstration of its utility for developing generalizable solutions.

**4.1 DF3DV-1K Dataset Design and Acquisition**

The dataset, named DF3DV-1K (Distractor-Free 3D Vision 1K), is constructed to be a large-scale, real-world, and diverse resource for distractor-free novel view synthesis.

*   **Scale and Diversity:** DF3DV-1K contains 1,048 scenes, comprising 726 indoor and 322 outdoor environments. In total, 89,924 images were collected. The dataset covers 128 distinct distractor types and 161 scene themes, reflecting a wide range of real-world conditions. Each scene includes both a "clean" set of images (without distractors) and a "cluttered" set (with distractors), which is crucial for evaluating distractor-free methods.
*   **DF3DV-41 Subset:** A curated subset of 41 scenes, DF3DV-41, was systematically designed to challenge methods with 17 specific distractor and scene scenarios. These include color-similar distractors, frontal occlusion, fluid distractors, slow-motion distractors, semi-transient distractors, shadow distractors, highly reflective distractors, large-scale distractors, local air distractors, semantically similar distractors, local appearance distractors, semi-transparent distractors, various distractors, daily scenes, common distractors as static parts, and nighttime scenes.
*   **Capture Conditions:** Data was collected over a period of nine months using 12 different consumer-grade cameras (e.g., iPhone 12, 13, 14, 15, Samsung Galaxy A15, S22+, S7, iPad Air, XREAL Beam Pro, DJI Mini 3 Pro). This mimics casual, real-world image capture scenarios. Images are typically 4K JPEG resolution. Camera settings (exposure, focus) were set to automatic by default but adjusted manually when necessary, and anti-shake was disabled to maintain consistent image resolution.

**4.2 Data Acquisition and Curation Pipeline**

A systematic pipeline was followed to ensure data quality and consistency:

1.  **Scene Design:** Operators predefined each scene by specifying themes, potential distractor types, viewpoint coverage (180° to 360°), viewpoint orientation (landscape/portrait), and target numbers of clean and cluttered images. For indoor scenes, distractors were manually introduced; for outdoor scenes, existing natural distractors were primarily leveraged.
2.  **Capture:** For controllable scenes, clean and cluttered images were captured separately. For uncontrollable outdoor scenes, they were captured simultaneously and later manually separated. Operators were instructed to avoid capturing during windy conditions.
3.  **Data Review:** Two experts per scene manually inspected and removed low-quality images (e.g., motion blur in static regions). Crucially, the clean image set was verified to be free of distractors. Distractors themselves were permitted to exhibit lower visual quality (e.g., motion blur) as this is common in casual capture.
4.  **Pose Estimation and Undistortion:** COLMAP was used to jointly estimate camera poses from both clean and cluttered images, leveraging reliable correspondences from clean views to enhance robustness and establish a shared camera coordinate system. All images were then undistorted using these parameters.
5.  **Tool-Assisted Data Verification:** Each scene was reconstructed using instant-ngp to verify data quality. Failed reconstructions (e.g., missing geometry, degenerate solutions) prompted adjustments to COLMAP parameters (e.g., minimum inlier threshold, registration trials, minimum model size). Scenes that consistently failed reconstruction were discarded.
6.  **Annotation:** Manual metadata annotation was performed for each passed scene, including its theme, specific distractor types, and environment type (indoor/outdoor).

**4.3 Benchmarking Methodology**

*   **Methods Evaluated:** Ten representative methods were benchmarked: the baseline 3D Gaussian Splatting (3DGS) and nine recent open-source distractor-free radiance field methods. These include AsymGS, RobustSplat, OCSplats, DeGauss, SLS, DeSplat, WildGaussians, T-3DGS, and T-3DGS-TMR.
*   **Evaluation Metrics:** Standard image quality metrics were used: Peak Signal-to-Noise Ratio (PSNR), Structural Similarity Index Measure (SSIM), and Learned Perceptual Image Patch Similarity (LPIPS). Higher PSNR and SSIM values indicate better quality, while lower LPIPS values indicate better perceptual similarity.
*   **Evaluation Scenarios:** Benchmarking was conducted on the full DF3DV-1K dataset and the challenging DF3DV-41 subset to assess general robustness and performance in specific challenging scenarios.

**4.4 DI2FIX (Enhancer Demonstration) Methodology**

To demonstrate the potential for generalizable solutions, the authors developed DI2FIX, a plug-and-play 2D enhancer.

*   **Base Model:** DIFIX, a diffusion-based 2D enhancement framework for sparse-view radiance fields, was used as the foundation.
*   **Adaptation for Distractor-Free Tasks:** For distractor-free enhancement, the clean reference view input to DIFIX was replaced with a radiance field rendering.
*   **Training Data Generation:** Paired training data was generated from DF3DV-1K* (DF3DV-1K excluding DF3DV-41). Scenes were reconstructed from cluttered images using various radiance field methods (3DGS and the nine distractor-free methods). Novel views were then rendered at the clean-image camera poses. This generated 316,890 candidate pairs.
*   **Data Filtering:** Pairs were filtered based on an LPIPS threshold (γ=0.5) to select data with moderate degradation for training.
*   **Fine-tuning:** DIFIX was fine-tuned on this generated dataset to create DI2FIX.
*   **Evaluation:** DI2FIX was evaluated on the held-out DF3DV-41 subset and the external On-the-go dataset.
*   **Ablation Studies:** Experiments explored the impact of training data scale (250, 500, 750, 1,007 scenes) and the LPIPS degradation threshold (0.1 to 0.9) on DI2FIX's performance. An out-of-distribution test was also performed by training on a subset of radiance field methods and evaluating on an unseen method.

### 5. Main findings and results

The research yielded several findings regarding the dataset characteristics, method performance, challenging scenarios, and the efficacy of a generalizable enhancer.

**5.1 DF3DV-1K Dataset Characteristics and Challenge Level**

*   **Scale and Diversity:** DF3DV-1K is significantly larger and more diverse than previous distractor-free datasets. It comprises 1,048 scenes (compared to 5 for RobustNeRF and 12 for On-the-go) and 128 distractor types (compared to 4 and 14, respectively). This represents a substantial increase in scale and variability.
*   **Increased Difficulty:** Quantitative analysis (e.g., PSNR, SSIM, LPIPS values for 3DGS) consistently demonstrated that DF3DV-1K and its subset DF3DV-41 are more challenging than RobustNeRF and On-the-go. Baseline 3DGS achieved notably lower PSNR and SSIM, and higher LPIPS on DF3DV-1K, indicating a greater inherent difficulty in reconstruction and distractor removal. The dataset also showed wider LPIPS and SSIM distributions, reflecting greater scene diversity and varied reconstruction challenges.

**5.2 Benchmark Performance of Distractor-Free Radiance Field Methods**

*   **Most Robust Methods:** On the large-scale DF3DV-1K and the challenging DF3DV-41 subsets, AsymGS and RobustSplat demonstrated the highest robustness, consistently outperforming other methods across various metrics (PSNR, SSIM, LPIPS). OCSplats and DeGauss followed as the next most robust methods.
*   **Performance Progression:** The ranking of methods on DF3DV-1K largely correlated with their publication timelines, particularly for PSNR and SSIM. This suggests a consistent and observable progression in performance as methods evolve, which was less evident on older, less challenging benchmarks.
*   **Benchmarking Efficacy:** The dataset enabled clear visual differentiation between methods ("zoom-in no more" comparisons) which was difficult on prior datasets where differences were subtle. Methods that showed promising performance on older datasets often exhibited noticeable degradation under the more challenging conditions of DF3DV-1K.

**5.3 Limitations of Current Methods and Challenging Scenarios**

*   **Challenging Distractor Types:** Semantically similar distractors and fluid distractors were identified as the most challenging categories. Methods relying on semantic features struggled when distractors shared similar meanings with static scene objects. For fluid distractors (e.g., splashes, smoke), online masking strategies often failed due to their spatially scattered and semi-transparent nature, leading to accidental removal of valid scene content or incomplete distractor suppression.
*   **Challenging Scene Types:** Nighttime scenes posed the greatest difficulty. Methods that use fixed thresholds for distractor filtering (typically tuned for daytime) became unreliable under low illumination, where distinguishing distractors from static scene components was harder.
*   **Degradation:** While AsymGS, RobustSplat, and OCSplats showed comparative robustness, other methods exhibited greater performance degradation under specific challenging scenarios, indicating limitations in their generalizability to diverse conditions.

**5.4 DI2FIX Performance and Impact of Dataset Characteristics**

*   **Enhancer Effectiveness:** DI2FIX, fine-tuned on DF3DV-1K*, achieved an average improvement of 0.96 dB PSNR and a 0.057 reduction in LPIPS on the held-out DF3DV-41 and On-the-go datasets. This demonstrated its ability to effectively remove distractor artifacts and restore visual structures.
*   **Comparison to Baselines:** In contrast, the original DIFIX (without domain-specific fine-tuning) generally degraded performance, and DIFIX fine-tuned on the smaller RobustNeRF dataset still resulted in notable performance drops, highlighting the importance of large-scale, diverse training data from the target domain.
*   **Impact of Dataset Scale:** Ablation studies showed a consistent improvement in DI2FIX's performance (PSNR, SSIM, LPIPS) as the number of training scenes from DF3DV-1K* increased (from 250 to 1,007 scenes). This quantitatively confirmed the benefit of a large-scale dataset for training generalizable models.
*   **Impact of Data Degradation Level:** A moderate LPIPS threshold (γ=0.5) for selecting training pairs yielded optimal performance. Overly strict thresholds limited the diversity and challenging nature of the training data, while overly loose thresholds introduced excessive noise, leading to undesired modifications of static scene content.
*   **Generalizability to Unseen Methods:** DI2FIX demonstrated stable out-of-distribution performance in leave-one-method-out evaluations, with minimal changes in metrics for unseen radiance field methods, suggesting good generalizability beyond the specific methods used for training data generation.

### 6. Significance and potential impact

This research makes several contributions that have potential implications for the field of 3D vision, particularly for distractor-free novel view synthesis:

*   **Addressing a Critical Gap:** The introduction of DF3DV-1K directly addresses the lack of a large-scale, diverse, and challenging real-world dataset for distractor-free radiance fields. This resource is designed to keep pace with the rapid methodological advancements in the field, moving beyond the saturation of previous benchmarks.
*   **Enabling Robust Method Development:** DF3DV-1K and its systematically designed subset, DF3DV-41, provide a robust platform for comprehensive benchmarking. This allows researchers to systematically evaluate and compare distractor-free methods, clearly identify their strengths and limitations, and pinpoint challenging scenarios (e.g., semantically similar distractors, fluid phenomena, nighttime scenes). This clarity can guide future research towards developing more robust algorithms.
*   **Facilitating Generalizable Solutions:** The scale and diversity of DF3DV-1K are instrumental in enabling the transition from scene-specific, per-scene optimized methods to generalizable solutions. The demonstration with DI2FIX illustrates how a large, high-quality dataset can be used to fine-tune existing models or train new ones that can generalize across various scenes and distractor types without requiring extensive test-time optimization. This has the potential to significantly improve the practical applicability and scalability of distractor-free 3D reconstruction.
*   **Advancing Real-World Applicability:** By mimicking casual capture conditions and including a wide array of real-world distractors and scene types, DF3DV-1K contributes to making 3D reconstruction technology more robust and practical for use in uncontrolled, everyday environments. This aligns the capabilities of novel view synthesis with the demands of real-world applications where perfect, distractor-free inputs are rarely available.
*   **Guiding Future Research:** The identified challenging scenarios highlight specific areas where current distractor-free methods fall short. This information can serve as a roadmap for future research, encouraging the development of more sophisticated techniques for semantic distractor differentiation, robust masking of complex fluid dynamics, and adaptive handling of varied illumination conditions. The success of DI2FIX also suggests a promising avenue for integrating 2D image enhancement techniques with 3D reconstruction, potentially leading to multi-reference or cascaded approaches.

The limitations, such as the dataset being smaller than general 3D datasets, potential minimal cloud movement in clean images despite short capture times, and DI2FIX's susceptibility to severely corrupted inputs or confirmation bias, also provide valuable insights for subsequent work. Overall, DF3DV-1K is positioned to be a foundational resource that accelerates the development of more robust, scalable, and generalizable distractor-free vision methods.
