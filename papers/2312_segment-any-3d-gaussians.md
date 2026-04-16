---
title: "Segment Any 3D Gaussians"
date: 2023-12-01
arxiv: "2312.00860"
venue:
status: read

abstract: "This paper presents SAGA (Segment Any 3D GAussians), a highly efficient 3D promptable segmentation method based on 3D Gaussian Splatting (3D-GS). Given 2D visual prompts as input, SAGA can segment the corresponding 3D target represented by 3D Gaussians within 4 ms. This is achieved by attaching an scale-gated affinity feature to each 3D Gaussian to endow it a new property towards multi-granularity segmentation. Specifically, a scale-aware contrastive training strategy is proposed for the scale-gated affinity feature learning. It 1) distills the segmentation capability of the Segment Anything Model (SAM) from 2D masks into the affinity features and 2) employs a soft scale gate mechanism to deal with multi-granularity ambiguity in 3D segmentation through adjusting the magnitude of each feature channel according to a specified 3D physical scale. Evaluations demonstrate that SAGA achieves real-time multi-granularity segmentation with quality comparable to state-of-the-art methods. As one of the first methods addressing promptable segmentation in 3D-GS, the simplicity and effectiveness of SAGA pave the way for future advancements in this field. Our code will be released."

website: https://jumpat.github.io/SAGA
code: https://github.com/Jumpat/SegAnyGAussians.git
issue: 

inputs:
  - posed-multi-view-images
  - 2d-pointing

outputs:
  - fast
  - 3d-segmentation
  - 3dgs

methods:
  - sam2d
  - feature-per-splat
  - scale-aware
  - clip

benchmarks:
  - 

related:
  - 

compared:
  - 
---

# Segment Any 3D Gaussians

## My Notes

**[Note from GitHub, 2026-04-15]**

1. 빠른 속도?
GS 복원하면서 splat 단위로 feature를 미리 만들어두었다면, 사실상 그때 segmentation 다 한 거 아닌가?
4ms의 빠른 inference 속도는, 씬 전체에 대한 이해하는 과정이 생략되어서 빠른 거 아닐까?

2. Trick들

    2-1. Scale 관련: Splat들이 크기가 튀는 경우가 빈번해서 크기가 큰 outlier들을 적절히 거르는 기법들 적용 (Scale-Gated Affinity Features, Local Feature Smoothing, Scale-Aware Contrastive Learning)

    2-2. Data imbalance

    2-3. Open set: CLIP 쓰면 가능

## Results

<!-- Optional: structured benchmark results for cross-paper comparison -->
<!-- Example:
| Benchmark | PSNR | SSIM | LPIPS |
|---|---|---|---|
| mipnerf360 | 27.21 | 0.815 | 0.214 |
| tanks-and-temples | 23.14 | 0.841 | 0.183 |
-->

## Figures

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-teaser.png)

*Figure 1: SAGA performs promptable multi-granularity segmentation within milliseconds. Prompts are marked by points.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-pipe-camera-ready.png)

*Figure 2: The architecture of SAGA. Left: SAGA attaches a Gaussian affinity feature to each 3D Gaussian. The magnitude of different affinity feature channels are adjusted by a soft scale gate to handle multi-granularity ambiguity. Right: SAGA distills segmentation ability of SAM into affinity features attached to 3D Gaussians in the 3D-GS model through scale-aware contrastive learning.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-vis-camera_ready_2.png)

*Figure 3: Qualitative results of SAGA across different scenes. We provide both the targets segmented via 2D point prompts and the “segment everything” results.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-fine-details-camera-ready.png)

*Figure 4: SAGA can maintain the high frequency texture details captured by 3D-GS. We reveal the inherent structure of these details by shrinking the Gaussians by 60%.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-ablation-camera-ready.png)

*Figure 5: Ablation study on effects of local feature smoothing (Smooth) and feature norm regularization (Feature Norm). Outliers are primarily eliminated through local feature smoothing. Feature norm regularization helps features of inner Gaussians align better with those of the surface.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-failure-case-camera-ready.png)

*Figure 6: Failure cases of SAGA. The targets of interest are labeled by red border.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-garfield-camera-ready.png)

*Figure A1: Adapting the scale gate mechanism with GARField achieves competitive results, demonstrating the potential of SAGA across different radiance fields.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-ngp-camera-ready.png)

*Figure A2: Applying SAGA to Instant-NGP achieves competitive segmentation performance, further demonstrating the generalizability and robustness of SAGA across different radiance field representations.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-comp-garfield-camera-ready.png)

*Figure A3: Qualitative comparison with GARField. We conduct feature clustering across the whole scene (LERF-figurines). Compared to GARField, which employs an additional feature field to model affinity features, SAGA demonstrates greater stability by utilizing explicit affinity features. At larger scales, SAGA effectively preserves the perception of small objects without merging them with other targets.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-supp-vis-1.png)

*Figure A4: More qualitative results of SAGA.*

## LLM Summary

This report provides a detailed analysis of the research paper "Segment Any 3D Gaussians" (SAGA), focusing on its core contributions, methodological advancements, and positioning within the broader landscape of 3D computer vision.

### 1. Authors, Institution(s), and Notable Context about the Research Group

The paper "Segment Any 3D Gaussians" is a collaborative effort between researchers from academia and industry:

* **Jiazhong Cen, Chen Yang, and Wei Shen (Corresponding Author):** Are affiliated with the MoE Key Lab of Artificial Intelligence, AI Institute, Shanghai Jiao Tong University (SJTU). SJTU is one of China's most prestigious universities, particularly renowned for its engineering, computer science, and artificial intelligence programs. The MoE Key Lab of Artificial Intelligence is a leading research center, suggesting a strong focus on fundamental and applied AI research. Wei Shen, as the corresponding author, likely leads the academic component of this research, specializing in areas such as medical image analysis, computer vision, and machine learning. Their involvement indicates a strong theoretical foundation and rigorous experimental methodology.
* **Jiemin Fang, Lingxi Xie, Xiaopeng Zhang, and Qi Tian:** Are from Huawei Technologies Co., Ltd. Huawei is a global leader in information and communications technology (ICT) infrastructure and smart devices, with substantial investments in AI research and development. Their collaboration with SJTU reflects a common trend in cutting-edge AI research, where industry partners provide significant computational resources, data, and practical application insights, while academic partners contribute theoretical breakthroughs and novel algorithms. Lingxi Xie and Qi Tian are notable researchers in the computer vision community, with extensive publication records, especially in areas like image recognition, segmentation, and neural networks. This strong academic-industry partnership is crucial for developing efficient and robust AI solutions, bridging the gap between theoretical advancements and real-world applicability.

The combined expertise suggests a group highly capable of tackling complex computer vision challenges, with both deep theoretical understanding and practical engineering considerations. The work builds on their previous research in 3D segmentation with radiance fields, such as "Segment Anything in 3D with NeRFs" (Cen et al. 2023) and "Segment Anything in 3D with Radiance Fields" (Cen et al. 2024), indicating a sustained research direction in extending 2D foundation models to 3D.

### 2. How This Work Fits into the Broader Research Landscape

SAGA operates at the intersection of several rapidly evolving fields within computer vision: 3D scene representation, promptable segmentation, and foundation models.

**2.1. Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3D-GS):**
The field of novel view synthesis has been revolutionized by Neural Radiance Fields (NeRFs), which represent scenes implicitly using neural networks to encode color and density. However, NeRFs often suffer from slow rendering and training times. 3D Gaussian Splatting (3D-GS) emerged as a significant advancement, offering superior rendering quality and real-time performance by explicitly representing scenes as a collection of 3D Gaussians. SAGA specifically targets 3D-GS, recognizing its explicit structure as an "ideal carrier for 3D segmentation" due to its efficiency and direct manipulability.

**2.2. Promptable Segmentation and Foundation Models:**
The advent of foundation models like the Segment Anything Model (SAM) (Kirillov et al. 2023) has dramatically simplified 2D image segmentation, enabling promptable and highly flexible mask generation. A major research direction has been to "lift" these powerful 2D capabilities into the 3D domain. Prior works have attempted this using various radiance field approaches (e.g., SA3D, OmniSeg3D, GARField), often by distilling 2D segmentation knowledge into 3D representations.

**2.3. 3D Segmentation in Radiance Fields:**
Before SAM, several methods explored 3D segmentation in NeRFs, either through unsupervised feature distillation (N3F, DFF, ISRF), interactive object selection (NVOS), or semantic propagation (Semantic-NeRF). With the rise of SAM, a new wave of methods (Kim et al. 2024; Ying et al. 2024; Cen et al. 2023; Lyu et al. 2024) aimed to transfer SAM's capabilities to 3D. Some, like SA3D and SA-GS, adopt iterative 2D mask refinement. Others, like OmniSeg3D and GaussianGrouping, use contrastive learning or video tracking to learn 3D features.

**2.4. SAGA's Position and Differentiation:**
SAGA distinguishes itself by being one of the first methods to specifically address **promptable segmentation directly within the 3D-GS framework** in a highly efficient manner.

* **Efficiency:** Unlike NeRF-based methods that rely on implicit feature fields requiring repeated queries (e.g., GARField), SAGA integrates segmentation capabilities directly into the explicit 3D Gaussians, preserving 3D-GS's real-time performance.
* **Multi-Granularity:** SAGA tackles the critical challenge of multi-granularity ambiguity in 3D segmentation, inspired by GARField's use of 3D physical scales. However, SAGA implements this with a "scale-gate mechanism" that is significantly more efficient due to its direct integration with 3D-GS and a streamlined design.
* **Direct Feature Integration:** By attaching "affinity features" to each 3D Gaussian, SAGA avoids the need for additional bulky segmentation modules, making it a lean and efficient solution.

In essence, SAGA represents a natural and highly optimized evolution of 3D promptable segmentation, leveraging the strengths of 3D-GS to achieve real-time, multi-granularity results that are superior or comparable to state-of-the-art methods while being significantly faster during inference.

### 3. Key Objectives and Motivation

The primary objectives and motivations behind the development of SAGA are:

* **Achieve Real-time 3D Promptable Segmentation:** The significant advancements in 2D promptable segmentation (e.g., SAM) have created a demand for similar capabilities in 3D. However, existing 3D methods often suffer from high computational costs, especially during inference. SAGA aims to address this by leveraging the efficiency of 3D-GS to enable segmenting 3D targets represented by 3D Gaussians within milliseconds (specifically, 4ms).
* **Endow 3D Gaussians with Segmentation Capability:** The core idea is to integrate segmentation as an intrinsic property of the 3D Gaussians themselves, rather than relying on external, computationally heavy modules or iterative refinement processes. This involves designing an efficient way to attach and learn segmentation-specific features for each Gaussian.
* **Handle Multi-Granularity Ambiguity:** A key challenge in 3D segmentation is that objects or parts can exist at various scales of granularity (e.g., a "table" vs. a "cup on the table"). A robust promptable segmentation method must be able to handle these different levels without conflict. SAGA aims to effectively address this ambiguity.
* **Distill SAM's 2D Segmentation Prowess to 3D:** The paper seeks to transfer the powerful and flexible segmentation capabilities of 2D foundation models like SAM into the 3D domain. This distillation process should be efficient and effective, leveraging existing 2D masks as supervision.
* **Pave the Way for Future Advancements:** By demonstrating a simple, effective, and highly efficient approach to 3D promptable segmentation in 3D-GS, SAGA intends to lay a foundational stone for further research and practical applications in this emerging field.

In summary, SAGA is motivated by the need for fast, flexible, and accurate 3D segmentation that can handle user prompts and multi-granularity objects, all within the efficient framework of 3D Gaussian Splatting.

### 4. Methodology and Approach

SAGA's methodology is built upon extending 3D Gaussian Splatting (3D-GS) by integrating segmentation-specific features directly into the Gaussian representation.

**4.1. Gaussian Affinity Feature:**
The core idea is to attach a *Gaussian affinity feature* (f_g ∈ R^D) to each 3D Gaussian (g) in a pre-trained 3D-GS model. The similarity between these affinity features indicates whether corresponding Gaussians belong to the same 3D target. To handle multi-granularity ambiguity, a *scale-gate mechanism* is introduced.

**4.2. Scale-Gated Affinity Features:**
Inspired by GARField, SAGA employs a soft scale-gate, S: [0,1] → [0,1]^D, which is a single linear layer followed by a sigmoid function. For a given 3D physical scale 's', this gate adjusts the magnitude of each channel of the base affinity feature (f_g) via Hadamard product: f_g^s = S(s) ⊙ f_g. This projects the features into different sub-spaces for various scales, allowing a single Gaussian to belong to different targets at different granularities. During training, the scale gate is applied to the 2D rendered features (F_s(p) = S(s) ⊙ F(p)) for efficiency, while during inference, it directly operates on 3D Gaussian features.

**4.3. Local Feature Smoothing (LFS):**
To mitigate noisy Gaussians that might exhibit spurious feature similarities (e.g., due to poor geometry or insufficient training weight), SAGA applies a spatial locality prior. During training, a Gaussian's feature is replaced by the average of its K-nearest neighbors' features. After training, the smoothed features are saved.

**4.4. Scale-Aware Contrastive Learning:**
This is the training strategy used to distill SAM's segmentation capability into the scale-gated affinity features.

* **Scale-Aware Pixel Identity Vector:** For each training image, multi-granularity 2D masks are automatically extracted using SAM. For every pixel 'p', a scale-aware pixel identity vector V(s, p) is constructed. This vector indicates which 2D masks the pixel belongs to at a specific scale 's', following a rule that if a pixel belongs to a mask at a given scale, it also belongs to it at larger scales, unless smaller masks at the current scale block it. This provides the ground-truth "mask correspondence."
* **Correspondence Distillation Loss (L_corr):** This loss function (adapted from Hamilton et al. 2022) encourages consistency between pixel-wise mask correspondence and feature correspondence. For two pixels p1, p2 at scale 's', their mask correspondence (Corr_m) is 1 if they share at least one mask, 0 otherwise. Their feature correspondence (Corr_f) is the cosine similarity between their scale-gated rendered features. The loss pulls features together if pixels are in the same mask and pushes them apart otherwise.
* **Feature Norm Regularization (L_norm):** A regularization term is added (1 - ||F(p)||_2) to encourage the 2D rendered features to have a norm close to 1 when their constituent 3D features along a ray are well-aligned. This helps to ensure that good 2D segmentation performance translates to good 3D feature alignment, preventing 3D features from deviating from their 2D projections.

**4.5. Additional Training Strategies (Appendix A.1):**
To address data imbalance issues inherent in contrastive learning (scale-sensitivity, positive-negative sample, and target-size imbalances):

* **Resampling:** Pixel pairs are categorized into "inconsistent" (sensitive to scale), "consistent positive," and "consistent negative." All inconsistent pairs are used, and a balanced subset of consistent positive/negative pairs are sampled, prioritizing "hard" samples (e.g., negative pairs with high feature similarity).
* **Re-weighting:** A pixel-wise re-weighting scheme is applied to the loss, giving less weight to pairs from larger masks, ensuring that small targets also contribute sufficiently to the optimization.

**4.6. Inference:**
Once trained, SAGA performs 3D promptable segmentation by converting 2D visual prompts (points with scales) into 3D scale-gated query features. It then segments the 3D target by comparing these query features with the 3D Gaussian affinity features. For automatic scene decomposition, HDBSCAN clustering is applied to a subset of the 3D Gaussian affinity features. SAGA also supports vote-based open-vocabulary segmentation by clustering multi-view 2D masks based on their segmented 3D Gaussians and then using CLIP to assign language labels to these clusters.

### 5. Main Findings and Results

SAGA demonstrates strong quantitative and qualitative performance, particularly highlighting its efficiency.

**5.1. Quantitative Results:**

* **Promptable Segmentation (NVOS Dataset):** SAGA achieved 92.6% mIoU and 98.6% mAcc, outperforming previous state-of-the-art methods, including those based on 3D-GS (SA3D-GS: 92.2% mIoU). This confirms its superior accuracy in fine-grained 3D segmentation.
* **Promptable Segmentation (SPIn-NeRF Dataset):** SAGA maintained competitive performance with 93.4% mIoU and 99.2% mAcc, slightly outperforming SA3D-GS (93.2% mIoU). The paper notes minor performance degradation compared to some NeRF-based methods due to 3D-GS's modeling of reflection effects with outlier Gaussians, but asserts its accuracy is sufficient for most applications.
* **Open-Vocabulary Semantic Segmentation (3D-OVS Dataset):** SAGA demonstrated superior results (96.0% mIoU mean) across all tested scenes compared to other language-conditioned radiance field methods like LERF, 3D-OVS, LangSplat, and N2F2, showcasing its adaptability beyond point-based prompts.

**5.2. Time Consumption Analysis:**
This is a major highlight for SAGA:

* **Inference Speed:** SAGA achieves remarkable real-time inference, requiring only 2-5 milliseconds (ms) for segmentation. This is significantly faster than other promptable segmentation methods in radiance fields (e.g., OmniSeg3D: 50-100ms, GARField: 30-70ms, SA3D: 45 seconds). This efficiency makes SAGA highly practical for interactive applications.
* **Training Speed:** SAGA's training time (10-40 minutes) is comparable to or faster than other SAM-distillation methods like OmniSeg3D (15-40 minutes) and GARField (20-60 minutes).

**5.3. Qualitative Results:**

* **Fine-Grained and Multi-Granularity Segmentation:** SAGA successfully segments objects at various scales across diverse indoor and outdoor scenes, demonstrating its multi-granularity capability.
* **High-Frequency Detail Preservation:** The method can segment thin and fine-grained structures effectively, leveraging 3D-GS's ability to capture high-frequency texture details. Shrinking Gaussians further reveals the completeness of the underlying structural modeling.
* **Scene Decomposition:** The compact Gaussian affinity features enable straightforward scene decomposition through simple clustering in 3D space.
* **Comparison with GARField:** Qualitative comparisons indicate SAGA's affinity features exhibit better stability, especially in preserving small objects at larger scales during clustering, unlike GARField which tends to merge them. This highlights the advantage of SAGA's explicit Gaussian features and simpler scale-gate mechanism over implicit feature fields.

**5.4. Ablation Study:**

* **Local Feature Smoothing (LFS):** Demonstrates that LFS is crucial for eliminating "false positives" (noisy Gaussians) around the segmentation target, making the results cleaner and more accurate.
* **Feature Norm Regularization (FNR):** Shows that FNR helps align features of inner Gaussians with those on the surface. Without FNR, objects can appear "translucent" or incomplete when a stricter similarity threshold is applied, indicating that 3D features are not perfectly aligned with 2D features. FNR ensures better consistency between 2D and 3D feature spaces.

### 6. Significance and Potential Impact

SAGA represents a significant advancement in 3D computer vision, particularly for interactive and real-time applications. Its contributions and potential impact are multifold:

**6.1. Real-time 3D Promptable Segmentation:** The most impactful contribution is SAGA's ability to perform high-quality, multi-granularity 3D segmentation in real-time (2-5ms). This speed is unprecedented for such a task in radiance fields, moving 3D segmentation from offline processing to interactive applications.

**6.2. Efficient Integration with 3D-GS:** By embedding segmentation capabilities directly into the explicit 3D Gaussian representation via lightweight affinity features and a simple scale-gate, SAGA fully leverages the inherent efficiency of 3D-GS. This avoids the computational overhead of implicit feature fields or iterative refinement pipelines, making the solution elegant and practical.

**6.3. Effective Multi-Granularity Handling:** The soft scale-gate mechanism is a clever and efficient way to address the inherent multi-granularity ambiguity in 3D scenes. It allows Gaussians to belong to different parts or objects at varying levels of detail without conflicts, enhancing the flexibility and robustness of the segmentation.

**6.4. Foundation for 3D Scene Understanding and Editing:** SAGA's ability to segment fine-grained structures and decompose scenes into objects in real-time has profound implications for various applications:

* **Interactive 3D Editing:** Users can easily select and manipulate specific objects or parts within a 3D scene reconstructed from images, opening doors for advanced 3D content creation and editing tools.
* **Augmented Reality (AR) and Virtual Reality (VR):** Real-time object segmentation is crucial for AR/VR applications, enabling realistic object placement, interaction, and occlusion handling.
* **Robotics and Autonomous Systems:** Faster and more accurate 3D scene understanding can benefit robots in navigation, object manipulation, and human-robot interaction.
* **Digital Twins and Reconstruction:** Enhances the ability to create semantically rich 3D models from real-world captures.

**6.5. Paving the Way for Future Research:** As one of the first methods to achieve truly real-time promptable segmentation in 3D-GS, SAGA sets a new benchmark and provides a strong baseline. It encourages further research into optimizing feature representations, enhancing generalization to unseen objects, and integrating other modalities (e.g., language for more nuanced prompts). The simplicity and effectiveness of its core design (Gaussian affinity features + scale-gate) can inspire similar integrations of attributes into explicit 3D representations.

**6.6. Limitations and Future Directions:**
The paper acknowledges a key limitation: SAGA's reliance on SAM-extracted 2D masks means it struggles with objects not well-represented in those masks. This points to a future direction of enhancing generalization to unrecognized targets, perhaps through more robust self-supervised learning or incorporating broader foundational models. Another limitation noted in open-vocabulary segmentation is the inherent multi-granularity ambiguity in semantics and the context dependence of CLIP's visual encoder, which could lead to misclassifications. Addressing these aspects will be crucial for the next generation of 3D scene understanding models.

In conclusion, SAGA delivers a high-performance, real-time solution for promptable 3D segmentation, establishing 3D-GS as a highly suitable representation for such tasks and opening exciting possibilities for interactive 3D applications.
