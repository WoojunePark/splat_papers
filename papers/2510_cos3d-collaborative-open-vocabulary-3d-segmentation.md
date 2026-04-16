---
title: "COS3D: Collaborative Open-Vocabulary 3D Segmentation"
date: 2025-10-23
arxiv: "2510.20238"
venue:
status: to-read

abstract: "Open-vocabulary 3D segmentation is a fundamental yet challenging task, requiring a mutual understanding of both segmentation and language. However, existing Gaussian-splatting-based methods rely either on a single 3D language field, leading to inferior segmentation, or on pre-computed class-agnostic segmentations, suffering from error accumulation. To address these limitations, we present COS3D, a new collaborative prompt-segmentation framework that contributes to effectively integrating complementary language and segmentation cues throughout its entire pipeline. We first introduce the new concept of collaborative field, comprising an instance field and a language field, as the cornerstone for collaboration. During training, to effectively construct the collaborative field, our key idea is to capture the intrinsic relationship between the instance field and language field, through a novel instance-to-language feature mapping and designing an efficient two-stage training strategy. During inference, to bridge distinct characteristics of the two fields, we further design an adaptive language-to-instance prompt refinement, promoting high-quality prompt-segmentation inference. Extensive experiments not only demonstrate COS3D&#39;s leading performance over existing methods on two widely-used benchmarks but also show its high potential to various applications,~\ie, novel image-based 3D segmentation, hierarchical segmentation, and robotics. The code is publicly available at \href{this https URL}{this https URL}."

website: 
code: https://github.com/Runsong123/COS3D
openreview:
issue: 9

inputs:
  - posed-multi-view-images
  - text-prompt
outputs:
  - 3d-gaussians
  - semantic-segmentation
methods:
  - 3dgs
  - open-vocabulary
benchmarks:
  - 

related:
  - 

compared:
  - 
---

# COS3D: Collaborative Open-Vocabulary 3D Segmentation

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

![Figure](https://arxiv.org/html/2510.20238/Image/Prompt-propagation.png)

*Figure 3: Visual comparisons on LeRF [9].*

## LLM Summary

## Research Paper Analysis: COS3D: Collaborative Open-Vocabulary 3D Segmentation

### 1. Authors, Institution(s), and Notable Context About the Research Group

The paper "COS3D: Collaborative Open-Vocabulary 3D Segmentation" features a diverse author team from several prominent academic and industrial institutions. The primary affiliation for most authors, including Runsong Zhu, Weiliang Tang, Shi Qiu, Pheng-Ann Heng, and Chi-Wing Fu, is **The Chinese University of Hong Kong (CUHK)**. This suggests a strong research group in computer vision, computer graphics, or robotics based at CUHK, likely led by senior academics like Professor Pheng-Ann Heng and Professor Chi-Wing Fu, given their numerous co-authors. The acknowledgement section further reinforces this, mentioning funding from the InnoHK initiative via the Hong Kong Centre for Logistics Robotics and the Hong Kong Innovation and Technology Fund, indicating a strategic research focus on practical applications in robotics and intelligent systems.

The author list also includes **Ka-Hei Hui from Autodesk AI Lab**. Autodesk is a leading software company specializing in 3D design, engineering, and entertainment. The involvement of the Autodesk AI Lab signifies a strong industrial interest in advanced 3D understanding, suggesting a drive towards integrating cutting-edge AI research into practical software solutions. This collaboration likely brings a valuable perspective on real-world applicability and scalability to the research.

Further academic contributions come from **Zhengzhe Liu of Lingnan University** and **Qianyi Wu of Monash University**. The inclusion of researchers from other universities, both local (Lingnan) and international (Monash), highlights the collaborative nature of this research, benefiting from a broader range of expertise and perspectives. This multi-institutional collaboration, with a strong academic core and significant industrial input, positions the work to bridge fundamental research with practical, high-impact applications, particularly in areas like 3D modeling, AR/VR, and robotics.

### 2. How This Work Fits into the Broader Research Landscape

Open-vocabulary 3D segmentation (OV3DS) represents a critical frontier in 3D scene understanding, aiming to accurately segment 3D objects and regions based on flexible natural language queries rather than predefined, fixed categories. This capability is paramount for advancing applications in augmented reality (AR), virtual reality (VR), and robotics, where dynamic and context-aware understanding of 3D environments is essential.

Recent advancements in OV3DS have largely leveraged 2D vision-language models (VLMs) like CLIP, transferring their capabilities to 3D scenes often represented by learned radiance fields, particularly 3D Gaussian Splatting (3D-GS) due to its efficiency. The existing research landscape can be broadly categorized into two main paradigms:

*   **Language-based methods:** Approaches such as LERF, LangSplat, LEGaussians, and Dr.Splat directly distill language features from 2D image space into a 3D language field. While innovative, these methods often struggle with limited distinctiveness in the learned language features, leading to inferior segmentation quality, especially around object boundaries, and the presence of artifacts.
*   **Segmentation-based methods:** Works like OpenGaussian, InstanceGaussian, and Gaussian Grouping tackle OV3DS sequentially. They first perform class-agnostic 3D segmentation (often leveraging models like SAM for 2D instance masks) and then use 2D VLMs for post-selection of the best-matched 3D segments. This sequential approach, however, suffers from inherent limitations. Accurately segmenting all objects without semantic guidance is challenging, frequently resulting in under- or over-segmentation errors. Moreover, the reliance on hand-crafted matching strategies for post-selection can introduce additional inaccuracies, collectively leading to error accumulation and constrained overall performance.

COS3D emerges as a direct response to these limitations by proposing a novel "collaborative prompt-segmentation framework." Unlike prior works that prioritize either language or segmentation features, or process them sequentially, COS3D argues for and implements a deep integration of both complementary information types throughout its entire pipeline. It fundamentally acknowledges that effective OV3DS requires a "mutual understanding of both language and segmentation," with segmentation providing discriminative, boundary-aware cues, and language facilitating high-level semantic understanding. By adopting 3D-GS as its underlying representation, COS3D also capitalizes on the efficiency benefits of this explicit representation for real-time applications.

### 3. Key Objectives and Motivation

The primary objective of COS3D is to achieve **high-quality and efficient open-vocabulary 3D segmentation (OV3DS)** that overcomes the inherent shortcomings of existing Gaussian-splatting-based methods.

The key motivations driving this research are:
*   **Addressing the limitations of current OV3DS paradigms:** Existing language-based methods suffer from blurry or inaccurate segmentations due to the weak expressiveness of directly distilled language features. Segmentation-based methods, on the other hand, struggle with error accumulation stemming from imperfect class-agnostic segmentation and unreliable post-selection strategies.
*   **Leveraging complementary information:** The authors identify that segmentation information is crucial for accurate boundaries and discriminative features, while language information provides high-level semantic understanding. The core motivation is to develop a framework that effectively integrates these two complementary types of information, which prior works largely failed to do.
*   **Enhancing practical applicability:** By enabling flexible text queries for diverse semantic categories, physical properties, and affordances, OV3DS is a vital tool for real-world applications in AR, VR, and robotics. COS3D aims to provide a more robust and precise solution for these domains.
*   **Improving efficiency:** Beyond accuracy, the work is motivated by the need for an efficient solution, both in terms of training and inference, especially given the computational demands of 3D scene representation and understanding.

In essence, COS3D aims to build a system where language and segmentation cues collaboratively inform and refine each other, leading to segmentations that are both semantically accurate and spatially precise, making 3D scene understanding more robust and usable.

### 4. Methodology and Approach

COS3D introduces a novel collaborative prompt-segmentation framework designed to effectively integrate complementary language and segmentation cues throughout its pipeline. The methodology is built upon three core technical components: the collaborative field, a two-stage collaborative field learning strategy, and an adaptive prompt-segmentation inference mechanism.

**4.1. Collaborative Field**
At its foundation, COS3D utilizes **3D Gaussian Splatting (3D-GS)** as the explicit 3D scene representation, known for its efficiency in rendering. Each 3D Gaussian in the scene is augmented with two distinct feature vectors:
*   **Instance Field (Θ_I):** A feature vector `I` (e.g., 16-dimensional) encoding discriminative, boundary-aware instance-level information for each Gaussian.
*   **Language Field (Θ_L):** A high-dimensional language feature vector `L` (e.g., 512-dimensional, like CLIP embeddings) for each Gaussian, representing its semantic content.
These two fields are designed to interact and "collaborate" during both training and inference.

**4.2. Collaborative Field Learning (Two-Stage Training Strategy)**
The key innovation in training is the **instance-to-language (Ins2Lang) mapping**, which models the intrinsic relationship between instance-level segmentation and language semantics. This is achieved through a two-stage strategy:

1.  **Stage 1: Instance Field Learning:**
    *   The instance field (Θ_I) is optimized to encode segmentation-aware information.
    *   **Supervision:** 2D instance segmentation masks (`K_I`) are automatically generated from multi-view images using the Segment Anything Model (SAM).
    *   **Mechanism:** Differentiable rasterization renders 3D instance features to 2D image space. A widely-used InfoNCE loss is applied, encouraging features within the same instance segment to be similar while being distinct from other segments. This process ensures the instance field learns view-consistent and discriminative 3D instance-level features.

2.  **Stage 2: Instance-to-Language (Ins2Lang) Mapping Learning:**
    *   After the instance field is learned, a mapping function `Φ` is trained to transfer features from the instance domain to the language domain.
    *   **Training Pairs:** Rendered 3D instance feature maps (from Θ_I) are grouped by SAM masks, and their mean features (`I_m`) are paired with corresponding 2D CLIP language feature maps (`F_L`), also averaged segment-wise (`L_m`). This creates segment-level (I_m, L_m) training pairs.
    *   **Mapping Function Implementations:**
        *   **Shallow MLPs (Φ_network):** A neural network is trained to learn the mapping `L = Φ_network(I)` using an L1 loss. This approach is highly efficient, taking only minutes to train.
        *   **Kernel Regression (Φ_kernel):** A non-parametric Nadaraya-Watson estimator is used, offering a learning-free, traditional approach. This method computes `L` as a weighted average of `L_m` based on the similarity of `I` to `I_m` in the training set.
    *   **Language Field Construction:** Once `Φ` is learned, it is applied to the instance feature `I` of every Gaussian to generate its corresponding language feature `L`, thereby constructing the entire language field (Θ_L).

This two-stage approach ensures effectiveness by building upon already discriminative instance features and efficiency by using a shared mapping function and segment-level supervision.

**4.3. Collaborative Prompt-Segmentation Inference**
During inference, COS3D employs an adaptive strategy to leverage both fields for high-quality segmentation:

1.  **3D Relevance Map in Language Field:**
    *   Given a text query `q_text`, its CLIP embedding `L_text` is obtained.
    *   A 3D relevance map `R` is computed for each Gaussian by comparing its language feature `L` with `L_text` and a canonical phrase embedding `L_canon`. This map indicates the correspondence between the text query and 3D regions.
    *   An initial segmentation `S` is formed by selecting Gaussians with relevance `R` above a predefined threshold `τ`.

2.  **Adaptive Language-to-Instance (Lang2Ins) Prompt Refinement:**
    *   To address the potential inferior segmentation from the language field alone (due to limited expressivity), the initial relevance map `S` acts as a prompt to guide the instance field.
    *   For each Gaussian `g'` in the initial set `S`, a local neighborhood `S_g'` is identified using the learned instance field (i.e., points with instance features similar to `g'`).
    *   An adaptive filtering operation is performed based on region-level relevance (opacity-weighted average of relevance scores within `S_g'`). Regions are processed in descending order of their center point's relevance, and only those exceeding `τ` are included in the final refined segmentation `S_t`.
    *   This refinement leverages the instance field's boundary awareness to aggregate spatially and semantically coherent neighboring points, while adaptively filtering out noisy points, significantly improving segmentation quality with minimal overhead.

### 5. Main Findings and Results

COS3D demonstrates leading performance across standard benchmarks, showcasing its effectiveness, efficiency, and robustness.

**5.1. State-of-the-Art Performance:**
*   **LeRF Dataset (2D Rendered Metrics from 3D Segmentation):** COS3D significantly outperforms all existing language-based (LangSplat, LEGaussians, Dr.Splat) and segmentation-based (OpenGaussian, InstanceGaussian) baselines. For instance, on the "mean" category, the kernel regression version of COS3D achieves an mIoU of 50.76 and mAcc of 72.08, surpassing Dr.Splat (43.58 mIoU, 63.87 mAcc) and InstanceGaussian (45.30 mIoU, 58.44 mAcc). Qualitatively, COS3D yields rendered objects with more complete boundaries and significantly fewer artifacts, validating its superior segmentation quality.
*   **ScanNetv2 Dataset (Direct 3D Evaluation):** For direct 3D Gaussian point-level segmentation, COS3D consistently achieves superior mIoU and mAcc compared to LangSplat, LEGaussians, and OpenGaussian across various class subsets (10, 15, and 19 categories). For the 19-class evaluation, COS3D (kernel regression) achieves 32.47 mIoU and 49.05 mAcc, considerably better than OpenGaussian (24.73 mIoU, 41.54 mAcc). Visualizations confirm accurate and complete 3D segmentations, particularly for challenging, dense queries like "chair."

**5.2. Ablation Studies:**
The ablation studies rigorously validate the efficacy of COS3D's key design choices:
*   **Learning Designs for Collaborative Field:** The proposed two-stage instance-to-language mapping (both MLP and kernel regression implementations) significantly outperforms alternative training solutions like one-stage joint learning or parallel learning. This is evidenced by higher performance and substantially reduced training times. Notably, the kernel regression implementation consistently yields the best performance, attributed to its suitability for mapping discriminative instance features to language features.
*   **Collaborative Prompt-Segmentation Inference:** The adaptive language-to-instance prompt refinement mechanism markedly improves mIoU and mAcc compared to inference solely based on the instance branch or language branch. This enhancement is achieved with only a slight increase in query inference time (0.22s vs. 0.12s-0.13s for alternatives), confirming its efficiency.
*   **Training Efficiency:** COS3D demonstrates rapid convergence and excellent performance even with significantly reduced training times. For example, using only 8 minutes for instance field training (compared to 45 minutes default), COS3D still achieves superior performance (50.16 mIoU) than baselines like LangSplat (9.66 mIoU, 240 min) or OpenGaussian (38.36 mIoU, 60 min).
*   **VLM Compatibility:** The framework is shown to be compatible with various 2D foundation vision-language models (e.g., CLIP vs. SigLIP for language, SAM vs. SAM2 vs. Semantic SAM for segmentation). Using more advanced VLMs like SigLIP or SAM2 can further boost performance, demonstrating the modularity and future-proof nature of COS3D.

### 6. Significance and Potential Impact

COS3D represents a significant advancement in open-vocabulary 3D segmentation, offering a robust and efficient solution that effectively addresses the limitations of prior methods. Its contributions hold substantial significance and potential impact across various domains:

*   **Elevating 3D Scene Understanding:** By pioneering a truly collaborative framework that integrates complementary segmentation and language cues, COS3D sets a new state-of-the-art for OV3DS. This moves beyond merely transferring 2D VLM features to 3D or performing sequential operations, achieving a more holistic and accurate understanding of 3D scenes. The resulting boundary-aware and semantically meaningful segmentations are crucial for complex 3D tasks.

*   **Enhanced Practicality and Efficiency:** The novel two-stage training strategy, particularly with the instance-to-language mapping, not only improves segmentation quality but also significantly boosts training efficiency. The adaptive prompt refinement during inference further refines results with minimal computational overhead. This combination of high quality and efficiency makes COS3D highly practical for real-world deployments where resources or time might be constrained.

*   **Broadening Applications of 3D Perception:** COS3D's versatility extends its utility beyond pure text-based queries:
    *   **Novel Image-based 3D Segmentation:** The ability to perform 3D segmentation using novel images as queries expands its applicability, allowing users to "segment anything in 3D" from a visual example, which is intuitive and powerful.
    *   **Explicit Hierarchical OV3DS:** The demonstrated capability for hierarchical segmentation (both coarse and fine-grained queries) enables more nuanced and flexible 3D scene interaction and analysis, crucial for detailed inspection or multi-level task planning.
    *   **Robotics:** Its successful application in robotic grasping tasks underscores its immediate relevance for autonomous systems. Accurate 3D object perception, guided by open-vocabulary queries, can significantly enhance a robot's ability to interact with unstructured environments, paving the way for more intelligent and adaptable robotic agents in logistics, manufacturing, and service industries.

*   **Foundational Research Contribution:** The introduction of the "collaborative field" and the "instance-to-language mapping" as core concepts provides a novel architectural paradigm for multimodal 3D understanding. This could serve as a foundational building block for future research into more advanced 3D perception systems that require deep integration of various data modalities.

While the authors acknowledge limitations such as the lack of reasoning for relational or multi-object queries and its current offline setting, COS3D lays a strong groundwork for future work to overcome these challenges, potentially leading to more sophisticated online, real-time, and cognitively aware 3D systems. The public release of the code further promotes research and development in this exciting field.
