---
title: "DiffusionHarmonizer: Bridging Neural Reconstruction and Photorealistic Simulation with Online Diffusion Enhancer"
date: 2026-02-27
arxiv: "2602.24096"
venue:
status: to-read

abstract: "Simulation is essential to the development and evaluation of autonomous robots such as self-driving vehicles. Neural reconstruction is emerging as a promising solution as it enables simulating a wide variety of scenarios from real-world data alone in an automated and scalable way. However, while methods such as NeRF and 3D Gaussian Splatting can produce visually compelling results, they often exhibit artifacts particularly when rendering novel views, and fail to realistically integrate inserted dynamic objects, especially when they were captured from different scenes. To overcome these limitations, we introduce DiffusionHarmonizer, an online generative enhancement framework that transforms renderings from such imperfect scenes into temporally consistent outputs while improving their realism. At its core is a single-step temporally-conditioned enhancer that is converted from a pretrained multi-step image diffusion model, capable of running in online simulators on a single GPU. The key to training it effectively is a custom data curation pipeline that constructs synthetic-real pairs emphasizing appearance harmonization, artifact correction, and lighting realism. The result is a scalable system that significantly elevates simulation fidelity in both research and production environments."

website: https://research.nvidia.com/labs/sil/projects/diffusion-harmonizer
code: https://github.com/ZHKKKe/Harmonizer
openreview: 
issue: 28

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

# DiffusionHarmonizer: Bridging Neural Reconstruction and Photorealistic Simulation with Online Diffusion Enhancer

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

![Figure](https://arxiv.org/html/2602.24096v2/x1.png)

*Figure 1: DiffusionHarmonizer on Driving Scenes. Our method transforms artifact-prone neural-rendered frames into temporally coherent simulations, improving their realism by jointly correcting shadows, lighting, appearance discrepancies and reconstruction artifacts.*

![Figure](https://arxiv.org/html/2602.24096v2/x2.png)

*Figure 2: Overview of the data curation pipeline (top) and model architecture (bottom) of DiffusionHarmonizer. We use a single-step temporally conditioned enhancement model, that is converted from a pretrained multi-step image diffusion model. To train it effectively, we develop a data curation pipeline to construct synthetic–real pairs emphasizing harmonization, artifact correction and lighting realism.*

![Figure](https://arxiv.org/html/2602.24096v2/x3.png)

*Figure 3: Comparison with Image and Video Editing Baselines on Out-of-Domain Testing Data. Our method harmonizes color tone and synthesizes realistic lighting and shadows, while editing baselines often fail to produce physically plausible shadowing. Although both can reduce reconstruction artifacts, baselines tend to hallucinate inconsistent content and over-edit well-reconstructed regions, whereas our method preserves scene geometry and input structure. Moreover, image-editing baselines introduce frame-to-frame jitter, whereas our model maintains strong temporal coherence.*

![Figure](https://arxiv.org/html/2602.24096v2/x4.png)

*Figure 4: Comparison with Harmonization Baselines Methods. While both our method and harmonization baselines adjust foreground appearance, the baselines fail to synthesize realistic shadows, resulting in less coherent composites.*

![Figure](https://arxiv.org/html/2602.24096v2/x5.png)

*Figure 5: Ablation on Loss Design. Removing perceptual supervision leads to oversmoothed outputs, while using a conventional LPIPS loss produces high-frequency artifacts. Our multi-scale formulation mitigates these artifacts and yields perceptually better results.*

![Figure](https://arxiv.org/html/2602.24096v2/x6.png)

*Figure 6: Ablation on Curated Data Sources. Removing any curated data source degrades performance: without artifact-correction data the model fails to fix reconstruction errors; without shadow data it cannot synthesize plausible shadows; and without appearance data it produces color-tone inconsistencies. Each data source provides complementary and essential supervision.*

![Figure](https://arxiv.org/html/2602.24096v2/x7.png)

*Figure 7: Visualization of Curated Training Dataset. We show representative paired samples from our curated training data: Relighting, ISP Modification, Asset Re-insertion, Artifacts Correction, and PBR Simulation.*

![Figure](https://arxiv.org/html/2602.24096v2/x8.png)

*Figure 8: User Study Interface. We show our study instructions and interface. Evaluators are shown the input image and two predictions (ours and a baseline) and asked to select the more realistic result, with prediction order randomized to avoid bias.*

![Figure](https://arxiv.org/html/2602.24096v2/x9.png)

*Figure 9: Additional Comparison with Image and Video Editing Baselines on Out-of-Domain Testing Data (Part 1 of 2). Our method harmonizes color tone and synthesizes realistic lighting and shadows, while editing baselines often fail to produce physically plausible shadowing. Although both can reduce reconstruction artifacts, baselines tend to hallucinate inconsistent content and over-edit well-reconstructed regions, whereas our method preserves scene geometry and input structure. Moreover, image-editing baselines introduce frame-to-frame jitter, whereas our model maintains strong temporal coherence.*

![Figure](https://arxiv.org/html/2602.24096v2/x10.png)

*Figure 10: Additional Comparison with Image and Video Editing Baselines on Out-of-Domain Testing Data (Part 2 of 2). Our method harmonizes color tone and synthesizes realistic lighting and shadows, while editing baselines often fail to produce physically plausible shadowing. Although both can reduce reconstruction artifacts, baselines tend to hallucinate inconsistent content and over-edit well-reconstructed regions, whereas our method preserves scene geometry and input structure. Moreover, image-editing baselines introduce frame-to-frame jitter, whereas our model maintains strong temporal coherence.*

![Figure](https://arxiv.org/html/2602.24096v2/x11.png)

*Figure 11: Additional Comparison with Video Harmonization Baselines on ISP modification held out test set.*

![Figure](https://arxiv.org/html/2602.24096v2/x12.png)

*Figure 12: Additional Comparison with Video Harmonization Baselines on ISP modification held out test set.*

![Figure](https://arxiv.org/html/2602.24096v2/x13.png)

*Figure 13: Comparison with Ground Truth on Holdout Datasets. Our model’s predictions closely match the ground-truth real-world captures, producing faithful, physically plausible results suitable for online simulation systems.*

## LLM Summary

The following report provides a detailed analysis of the research paper "DiffusionHarmonizer: Bridging Neural Reconstruction and Photorealistic Simulation with Online Diffusion Enhancer."

---

### **Research Report: DiffusionHarmonizer**

**1. Authors and Institution(s)**

The research was conducted by a team of authors primarily affiliated with NVIDIA. Several authors also hold joint affiliations with academic institutions:
*   Yuxuan Zhang (NVIDIA)
*   Katarína Tóthová (NVIDIA)
*   Zian Wang (NVIDIA, University of Toronto)
*   Kangxue Yin (NVIDIA)
*   Haithem Turki (NVIDIA)
*   Riccardo de Lutio (NVIDIA)
*   Yen-Yu Chang (NVIDIA, Cornell University)
*   Or Litany (NVIDIA, Technion)
*   Sanja Fidler (NVIDIA, University of Toronto)
*   Zan Gojcic (NVIDIA)

**2. How This Work Fits into the Broader Research Landscape**

The development and evaluation of autonomous robots, such as self-driving vehicles, critically rely on realistic simulation environments. Neural reconstruction methods, including Neural Radiance Fields (NeRF) and 3D Gaussian Splatting, have emerged as promising techniques to generate diverse simulation scenarios directly from real-world sensor data. These methods can decompose scenes into static backgrounds and dynamic foreground assets, allowing for manipulation of objects and trajectories within the simulated environment.

Despite advancements, current neural reconstruction approaches face two primary challenges:
1.  **Novel-view artifacts:** Renderings from viewpoints significantly different from the training data often exhibit visual defects such as spurious geometry, missing regions, blur, and ghosting. Similar issues arise when foreground assets are manipulated.
2.  **Object insertion artifacts:** When dynamic objects (either synthetic or reconstructed from separate captures) are inserted into neurally reconstructed scenes, the resulting composites frequently suffer from tone discrepancies, lighting mismatches, and absent or inaccurate shadows.

Existing research has explored various solutions for related problems:
*   **Image and Video Harmonization:** This field aims to adjust the appearance of inserted foreground objects to blend them naturally with the background. Early methods often relied on frame-to-frame regression using autoencoders or interpretable filters. More recent approaches leverage generative models, particularly diffusion models, through fine-tuning or training-free formulations. Extending harmonization to video introduces the challenge of temporal coherence, addressed by methods incorporating flow-based constraints or holistic video processing with latent diffusion models. However, most existing harmonization methods primarily focus on foreground appearance and generally do not address reconstruction artifacts or synthesize physically plausible shadows.
*   **Neural Reconstruction and Generative Priors:** Efforts to improve neural reconstruction quality, especially in sparse-view or novel-view scenarios, have incorporated geometric, photometric, and regularization priors. More recently, generative models like diffusion models and Generative Adversarial Networks (GANs) have been used to integrate appearance priors, leading to methods such as DiffusioNeRF, GANeRF, and Nerfbusters. Some works, like ReconFusion, 3DGS-Enhancer, and Cat3D, utilize diffusion models to generate novel views for reconstruction supervision. DIFIX3D+ proposed using image-to-image translation models specifically for artifact removal in 3D reconstructions.

The current work, DiffusionHarmonizer, positions itself at the intersection of these fields by addressing the combined limitations of existing neural reconstruction and generative enhancement techniques. It seeks to provide a unified, efficient solution that simultaneously corrects reconstruction artifacts, harmonizes appearance, and synthesizes realistic shadows, specifically tailored for online, real-time simulation environments. Current general image or video generative models are often too computationally expensive for online use or lack the necessary temporal consistency or fidelity in modeling physical phenomena like shadows, while specialized harmonization methods do not address reconstruction artifacts. This paper attempts to bridge this gap by offering an integrated framework.

**3. Key Objectives and Motivation**

The primary objective of this research is to enhance the photorealism of neurally reconstructed simulation environments by addressing common artifacts and inconsistencies, thereby making them suitable for online simulation applications in autonomous driving and robotics.

The motivation for this work stems from two fundamental challenges in current neural reconstruction methods that limit their utility for high-fidelity simulation:
1.  **Correction of Novel-View Artifacts:** Neural reconstruction models, while capable of high visual quality near training viewpoints, frequently produce visual discrepancies when rendered from unobserved, sparsely observed, or extrapolated viewpoints. These artifacts, including blurred details, spurious geometry, and missing regions, compromise the realism and reliability of simulated scenarios. The research aims to develop a system that can robustly correct these errors in rendered frames.
2.  **Harmonization and Realistic Integration of Inserted Objects:** When dynamic foreground objects (e.g., vehicles, pedestrians) are inserted into reconstructed scenes, they often appear visually inconsistent. This can manifest as tone mismatches, incorrect lighting interactions, or the absence of physically accurate cast shadows, making the composite scene unrealistic. A critical motivation is to ensure that inserted objects blend seamlessly with the scene, including the generation of plausible shadows.

To achieve these goals within the operational constraints of online simulation, the authors formulate the problem as an image-to-image translation task. This involves transforming artifact-prone or visually inconsistent frames rendered from a reconstructed scene into temporally consistent and harmonized video frames, while preserving the underlying scene structure. This formulation is driven by the need for a solution that:
*   **Computational Efficiency:** Can operate within the resource budget of online simulators, specifically on a single high-performance GPU (e.g., an H100). Existing video-based generative models are typically too computationally intensive.
*   **Temporal Coherence:** Produces output that is stable across consecutive frames, avoiding flickering or unstable dynamics often associated with frame-independent image-based models.
*   **Physical Plausibility:** Accurately models lighting conditions, including the synthesis of realistic cast shadows, without distorting existing scene geometry or appearance, which is crucial for physically grounded simulation.

The core motivation is to overcome the limitations of both general generative models (which lack efficiency and precise control for specific simulation needs) and specialized harmonization methods (which often neglect reconstruction artifacts and shadow synthesis), by creating a unified, efficient, and robust enhancement framework for neural simulation.

**4. Methodology and Approach**

The DiffusionHarmonizer framework is designed as an online generative enhancer, addressing both efficiency and temporal consistency through a specialized model architecture and a custom data curation strategy.

**4.1. Online Frame-to-Frame Enhancer**

The core of the model is an adaptation of a pretrained image diffusion model into a deterministic, single-step enhancer suitable for online simulation.

*   **Network Architecture:** The method formulates harmonization as an image-to-image translation. Given a degraded input frame $I_t$ at time $t$, the enhancer predicts an improved frame $\hat{I}_t$. This is achieved by feeding the input through a frozen pretrained latent encoder $E_{\eta}$, then processing the latent representation with a fine-tuned diffusion backbone $F_{\theta}$, and finally decoding the enhanced latent with a frozen pretrained latent decoder $D_{\phi}$. Only the diffusion backbone $F_{\theta}$ is fine-tuned for this task.
*   **Single-Step Deterministic Operation:** Unlike standard diffusion models that operate across multiple timesteps with stochastic noise, DiffusionHarmonizer feeds the clean latent from $E_{\eta}(I_t)$ directly into $F_{\theta}$ without injecting additional noise. The timestep and text-conditioning tokens are fixed to constant "null" values during both training and inference. This design yields a stable and deterministic mapping from the input latent to the enhanced latent, contributing to frame-wise structural consistency.
*   **Temporal Conditioning:** To ensure temporal stability in online simulation, the backbone $F_{\theta}$ is extended to incorporate a short temporal context of previous frames. At time $t$, the current degraded frame $I_t$ and up to $K=4$ previously *enhanced* frames ($\hat{I}_{t-1}, \dots, \hat{I}_{t-K}$) are encoded into latents. These latents are concatenated to form $Z_t$, which is then fed into the backbone. The backbone includes temporal attention layers interleaved with spatial attention, following standard video diffusion architectures. For initial frames where fewer than $K$ previous frames are available, the model conditions on the existing ones. This allows the enhancer to leverage historical context while maintaining structural fidelity and preventing temporal drift.

**4.2. Data Curation Strategy**

Training the model effectively requires a diverse dataset of paired artifact-prone renderings and high-quality photorealistic images, covering aspects like appearance harmonization, lighting realism, artifact correction, and shadow consistency. Since such paired data is scarce, the authors developed a scalable data curation pipeline with five complementary components:

*   **Novel-View Artifacts Correction:** To address reconstruction artifacts, the pipeline follows the strategy from DIFIX3D+. It generates degraded renderings using four procedures: sparse reconstruction, cycle reconstruction, cross-referencing, and deliberate model underfitting. Each degraded frame is paired with its clean rendering to provide supervision for artifact correction.
*   **ISP Modification:** To simulate appearance mismatches from varied camera signal processing (ISP), the method re-renders captured images with randomized ISP parameters (e.g., tone mapping, exposure, white balance). A foreground mask (obtained using SAM2) is used to create a composite where the foreground has altered ISP parameters, while the background remains original. This composite serves as input, with the original capture as the target, for learning foreground-background color and tone harmonization.
*   **Relighting:** An image relighting diffusion model is used to regenerate selected foreground regions under randomly sampled lighting conditions. This intentionally creates inputs where local illumination is inconsistent with the global scene lighting. These pairs supervise the model in resolving lighting discrepancies and synthesizing spatially consistent illumination.
*   **Physically Based Shadow Simulation:** For accurate shadow reasoning, a physically based renderer synthesizes cast shadows under controllable light configurations. By randomly varying environment maps and light sources in synthetic scenes, paired samples are generated with and without shadows. These pairs provide precise pixel-level cues for learning physically plausible shadow casting and attenuation.
*   **Asset Re-Insertion:** To bridge the domain gap with real-world statistics, dynamic scene reconstruction is employed. A static background is reconstructed (using 3DGUT), dynamic foreground objects are extracted, and then these objects are re-inserted into the background *without* casting shadows. These composites, intentionally lacking proper shadows and harmonization, are paired with original sequences that contain correct shadows and coherent appearance, providing rich supervision for realistic shadow synthesis and foreground-background harmonization.

**4.3. Training**

*   **Stabilizing Single-Step Training:** To mitigate high-frequency artifacts (e.g., checkerboard patterns) arising from the mismatch between the multi-step pretraining and single-step fine-tuning, a **multi-scale perceptual loss ($L_{perc}$)** is introduced. This loss is computed on randomly sampled square patches of varying sizes (from 128 to 512 pixels). It compares features from different layers of a VGG network on these patches, perturbing patch boundaries to emphasize high-frequency inconsistencies and suppress periodic aliasing.
*   **Temporal Warping Loss ($L_{temp}$):** To further promote temporal consistency, a warping-based temporal loss is incorporated. Optical flow ($F_{t \to t-1}$) is estimated between consecutive ground-truth frames ($I^{gt}_{t-1}, I^{gt}_t$) using RAFT. The enhanced frame at time $t-1$ ($\hat{I}_{t-1}$) is then warped into time $t$, and consistency is enforced with the current enhanced frame $\hat{I}_t$ in visible pixels. This loss is computationally tractable due to the single-step RGB output.
*   **Mixed Temporal Training:** The curated dataset includes both short video sequences and standalone images. To leverage all data and avoid overfitting to strong temporal cues, training uses mixed temporal and non-temporal batches. The overall objective combines a per-pixel $L_2$ loss, the multi-scale perceptual loss, and the temporal warping loss. The temporal loss is applied only to temporal batches. The training schedule involves initial pretraining on paired image data, followed by alternating between temporal and non-temporal batches, preventing over-reliance on nearby frames.

The model is built upon the Cosmos 0.6B text-to-image diffusion model, with its VAE tokenizer frozen and only the diffusion backbone fine-tuned. Training is performed at 1024x576 resolution with bf16 precision.

**5. Main Findings and Results**

The evaluation of DiffusionHarmonizer involved extensive experiments across multiple datasets and evaluation settings, focusing on perceptual realism, structural fidelity, and temporal consistency.

**5.1. Qualitative Comparisons**
*   **Vs. Image and Video Editing Baselines (e.g., SDEdit, InstructPix2Pix, Wan-Video V2V):** DiffusionHarmonizer demonstrated superior performance in harmonizing color tone and synthesizing realistic lighting and shadows, particularly for inserted objects. Baseline editing models frequently failed to produce physically plausible shadowing. While baselines could reduce reconstruction artifacts, they often hallucinated inconsistent content or over-edited well-reconstructed regions. DiffusionHarmonizer, in contrast, preserved scene geometry and input structure more faithfully. Furthermore, image-editing baselines showed notable frame-to-frame jitter, whereas DiffusionHarmonizer maintained strong temporal coherence comparable to video diffusion models.
*   **Vs. Specialized Harmonization Methods (e.g., Ke et al., VHTT):** These baselines effectively adjusted foreground appearance but did not synthesize realistic shadows and, by design, did not correct reconstruction artifacts, limiting their applicability for comprehensive simulation enhancement.

**5.2. Quantitative Evaluation**
*   **Against Image and Video Editing Baselines (Novel Trajectory Simulation and Dynamic Object Insertion):**
    *   **Perceptual Quality:** DiffusionHarmonizer consistently achieved lower FID and FVD scores, indicating higher perceptual realism.
    *   **Structural Preservation:** The method recorded lower DINO-Struct-Dist scores, signifying better preservation of scene structure.
    *   **Temporal Consistency:** It significantly outperformed image-editing baselines and achieved temporal coherence comparable to state-of-the-art video diffusion models (e.g., marginal difference to WAN V2V in VBench++ temporal score).
    *   **Ground-Truth Alignment (Holdout Datasets for Relighting, PBR Shadow, ISP Modification):** On datasets with available ground truth, DiffusionHarmonizer showed substantial improvements in PSNR, SSIM, and LPIPS, demonstrating closer alignment with real-world references.
    *   **Inference Speed:** Operating at 212ms per frame, DiffusionHarmonizer was at least 1.8x faster than image-editing baselines and 10x faster than video-editing baselines, enabling online deployment on a single H100 GPU.
*   **Against Video Harmonization Baselines (ISP Modification Dataset):** DiffusionHarmonizer consistently outperformed VHTT and Ke et al. across all image-quality metrics (PSNR, SSIM, LPIPS, FID, FVD), even though some baselines were evaluated at lower resolutions or on foreground-only regions.

**5.3. User Study and VLM Evaluation**
*   **Human Evaluation:** In a comparative user study, human evaluators consistently preferred DiffusionHarmonizer's outputs over all baselines. Preference rates for DiffusionHarmonizer were 84.28% against SDEdit, 90.10% against InstructPix2Pix, and 90.11% against Wan-Video V2V.
*   **VLM Evaluation:** An independent evaluation using a Vision-Language Model (LLaVA-1.5-7b) showed high agreement with human preferences, further supporting the perceived quality of the proposed method.

**5.4. Ablation Studies**
*   **Multi-Scale Perceptual Loss:** This loss was critical for stabilizing single-step training. Removing it led to over-smoothed outputs, while a conventional LPIPS loss resulted in high-frequency artifacts. The multi-scale formulation effectively mitigated these issues.
*   **Temporal Components (Conditioning and Loss):** The inclusion of temporal conditioning and the temporal warping loss significantly improved temporal consistency metrics, leading to reduced flickering and smoother transitions.
*   **Data Curation Strategy:** Ablations confirmed that all five components of the data curation pipeline (Novel-View Artifacts Correction, ISP Modification, Relighting, Physically Based Shadow Simulation, and Asset Re-Insertion) provided complementary and essential supervision signals, each contributing to the model's overall performance and generalization capabilities.

**6. Significance and Potential Impact**

DiffusionHarmonizer presents a significant contribution to the field of photorealistic simulation and neural rendering, particularly for applications in autonomous driving and robotics.

*   **Unified and Comprehensive Enhancement:** The work provides a single, integrated framework that simultaneously addresses multiple critical challenges in neural reconstruction: correcting novel-view artifacts, harmonizing foreground and background appearance, and synthesizing realistic cast shadows for inserted objects. This unified approach is more robust and practical than relying on separate, specialized models for each task.
*   **Enabling Online Simulation:** By converting a multi-step image diffusion model into an efficient, single-step, temporally conditioned enhancer, DiffusionHarmonizer achieves high performance while operating effectively on a single GPU. This efficiency, combined with strong temporal coherence, makes it a viable solution for real-time, online simulation pipelines, where computational budgets and consistency are paramount.
*   **Enhanced Realism and Fidelity:** The method substantially improves the perceptual realism and structural fidelity of neurally rendered frames. This is crucial for developing and evaluating autonomous systems, as realistic simulations can lead to more robust and generalizable models trained in virtual environments.
*   **Scalable Data Curation:** The introduction of a comprehensive and scalable data curation pipeline is a key enabler for the model's success. By synthetically generating diverse paired supervision data, the approach overcomes the scarcity of real-world annotated data for complex tasks like shadow synthesis and artifact correction, making the training process more efficient and robust.
*   **Broader Applicability:** While primarily demonstrated in autonomous driving scenarios, the domain-agnostic nature of the method suggests its potential applicability to other fields requiring high-fidelity, real-time scene synthesis and enhancement, such as virtual reality, gaming, or general robotics simulation.
*   **Advancement in Generative Models:** The method demonstrates an effective strategy for repurposing and fine-tuning pretrained multi-step diffusion models for deterministic, single-step inference, addressing inherent challenges like noise-trajectory mismatch. This approach, along with the tailored loss functions, can inform future developments in efficient generative model deployment.

In conclusion, DiffusionHarmonizer offers a practical, scalable, and high-quality solution that bridges the gap between imperfect neural reconstructions and the demanding requirements of photorealistic, online simulation, opening new avenues for integrating advanced generative priors into real-time applications.
