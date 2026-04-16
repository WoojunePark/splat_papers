---
title: "GaussianVLM: Scene-centric 3D Vision-Language Models using Language-aligned Gaussian Splats for Embodied Reasoning and Beyond"
date: 2025-07-01
arxiv: "2507.00886"
venue:
status: to-read

abstract: "As multimodal language models advance, their application to 3D scene understanding is a fast-growing frontier, driving the development of 3D Vision-Language Models (VLMs). Current methods show strong dependence on object detectors, introducing processing bottlenecks and limitations in taxonomic flexibility. To address these limitations, we propose a scene-centric 3D VLM for 3D Gaussian splat scenes that employs language- and task-aware scene representations. Our approach directly embeds rich linguistic features into the 3D scene representation by associating language with each Gaussian primitive, achieving early modality alignment. To process the resulting dense representations, we introduce a dual sparsifier that distills them into compact, task-relevant tokens via task-guided and location-guided pathways, producing sparse, task-aware global and local scene tokens. Notably, we present the first Gaussian splatting-based VLM, leveraging photorealistic 3D representations derived from standard RGB images, demonstrating strong generalization: it improves performance of prior 3D VLM five folds, in out-of-the-domain settings."

website: https://insait-institute.github.io/gaussianvlm.github.io
code: https://github.com/amhalacheva/GaussianVLM/tree/main
openreview:
issue: 7

inputs:
  - posed-multi-view-images
  - text-prompt
outputs:
  - 3d-gaussians
  - semantic-segmentation
methods:
  - 3dgs
  - vlm
benchmarks:
  - 

related:
  - 

compared:
  - 
---

# GaussianVLM: Scene-centric 3D Vision-Language Models using Language-aligned Gaussian Splats for Embodied Reasoning and Beyond

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

![Figure](https://arxiv.org/html/2507.00886/x2.png)

*Figure 2: The GaussianVLM architecture processes a user task prompt (query and optional location) and a 3D scene (Gaussian Splat representation). A 3D vision module (SceneSplat Transformer) predicts per-Gaussian language features. These dense features are then sparsified by a dual sparsifier module. The decoder’s hidden states also inform the task-guided sparsifier. The dual sparsifier comprises: 1) a location-guided pathway that selects language features from Gaussians within a ROI around the task location, producing ROI tokens; and 2) a task-guided pathway that attends to dense scene tokens and SceneSplat decoder hidden states using task tokens (via cross-attention) to produce 128 task-selected scene tokens. The resulting sparse scene representation (ROI tokens + task-selected tokens), along with the task tokens, is input to an LLM for response generation.*

![Figure](https://arxiv.org/html/2507.00886/x3.png)

*Figure 3: Qualitative results on scene-centric tasks.*

![Figure](https://arxiv.org/html/2507.00886/x4.png)

*Figure 4: Qualitative results on object-centric tasks.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/GaussianVLM_v3_labels_dist_correct.png)

*Figure 5: Distribution of the questions on object counts, answered correctly by GaussianVLM. The distribution is according to object class labels. Overall, 254 questions answered correctly.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/LL3DA_v3_labels_dist_correct.png)

*Figure 6: Distribution of the questions on object counts, answered correctly by LL3DA. The distribution is according to object class labels. Overall, 44 questions answered correctly.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/GaussianVLMv3_labels_overlayed.png)

*Figure 7: Distribution of object count questions (correcly answered by GaussianVLM, vs all questions) according to object class labels.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/LL3DAv3_labels_overlayed.png)

*Figure 8: Distribution of object count questions (correcly answered by LL3DA, vs all questions) according to object class labels.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/v3_labels_dist_on_counts_True.png)

*Figure 9: Distribution of object count questions according to object count labels.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/GaussianVLMv3_labels_overlayed_on_counts_True.png)

*Figure 10: Distribution of object count questions (correcly answered by GaussianVLM, vs all questions) according to object count labels. Overall, 254 questions answered correctly. Logarithmic scaling for the distribution.*

![Figure](https://arxiv.org/html/2507.00886/extracted/6586298/supp_fig/LL3DAv3_labels_overlayed_on_counts_True.png)

*Figure 11: Distribution of object count questions (correcly answered by LL3DA, vs all questions) according to object count labels. Overall, 44 questions answered correctly. Logarithmic scaling for the distribution.*

## LLM Summary

The following report provides a detailed analysis of the research paper "GaussianVLM: Scene-centric 3D Vision-Language Models using Language-aligned Gaussian Splats for Embodied Reasoning and Beyond," arXiv:2507.00886v1.

### 1. Authors, Institution(s), and Notable Context about the Research Group

The paper is authored by Anna-Maria Halacheva, Jan-Nico Zaech, Xi Wang, Danda Pani Paudel, and Luc Van Gool. The primary affiliation for all authors is INSAIT, Sofia University “St. Kliment Ohridski.” Xi Wang also holds affiliations with ETH Zurich and TU Munich.

INSAIT (Institute for Computer Science, Artificial Intelligence and Technology) is a cutting-edge research institute located in Sofia, Bulgaria, established with the vision of becoming a global leader in AI research. It benefits from strong academic partnerships, notably with ETH Zurich and EPFL, attracting top-tier talent and fostering advanced research environments. The presence of Luc Van Gool as a co-author is particularly significant. Professor Van Gool is a highly distinguished and influential figure in the field of computer vision, renowned for his foundational contributions and extensive research impact. His involvement typically signifies a project at the forefront of the field, backed by deep expertise and rigorous methodology. Xi Wang's dual affiliations with ETH Zurich and TU Munich, two of Europe's leading technical universities, further underscore the collaborative and high-caliber nature of the research group. This institutional backing and the prominent researchers involved position this work as a substantial contribution from a well-resourced and highly capable team.

### 2. How This Work Fits into the Broader Research Landscape

The development of 3D Vision-Language Models (VLMs) is a rapidly expanding area within multimodal AI, aiming to equip embodied agents with a comprehensive understanding of physical 3D environments. This work by Halacheva et al. is positioned as a significant advancement that addresses several critical limitations of existing 3D VLM approaches.

Historically, 3D scene understanding for embodied agents began with tasks like Embodied Question Answering (EQA), which focused on situated, navigation-oriented challenges. This evolved to include more complex multi-hop, commonsense reasoning, and embodied planning and dialogue tasks, culminating in the emergence of generalist 3D VLMs. However, the majority of these prior methods are predominantly "object-centric." This means they rely heavily on pre-trained object detectors to identify and categorize individual objects within a 3D scene, which are then used as the primary tokens for language interaction. While intuitive, this approach introduces several fundamental limitations:
*   **Processing Bottlenecks:** The dependency on object detectors creates a sequential processing bottleneck and limits scalability.
*   **Taxonomic Rigidity:** Models are constrained by predefined object categories and cannot flexibly adapt to novel objects or fine-grained distinctions not present in the detector's training data.
*   **Neglect of Global Context:** By focusing on discrete objects, object-centric methods often struggle to capture overarching scene layout, spatial relationships, and global semantic context, which are crucial for true scene understanding and embodied reasoning.
*   **Inefficient Tokenization:** Existing 3D scene tokenization strategies either suffer from detector dependence (object-level) or over-smoothing and fixed granularity (region-based), risking the loss of fine-grained details or introducing irrelevant data.
*   **Weak Cross-Modal Alignment:** Many methods align 3D visual features with language by projecting them into a shared embedding space or using learnable query tokens, often resulting in shallow alignment where language has limited impact on the initial visual encoding.

GaussianVLM proposes a fundamental "paradigm shift" by moving from an object-centric to a "scene-centric" approach. It aims to overcome detector dependency, improve taxonomic flexibility, and enable a more holistic understanding by directly embedding rich linguistic features into the fine-grained spatial structure of the 3D scene. Furthermore, it introduces the novel use of 3D Gaussian Splatting (3DGS) as the underlying 3D representation, a recent innovation in neural rendering that offers photorealistic quality and rich geometric/appearance information derived from standard RGB images. This integration positions GaussianVLM as a pioneering work in language-grounded 3D VLMs leveraging 3DGS, addressing both the conceptual limitations of prior models and the practical challenges of dense 3D representations.

### 3. Key Objectives and Motivation

The primary motivation behind GaussianVLM stems from the recognized limitations of existing 3D Vision-Language Models (VLMs) in achieving truly comprehensive 3D scene understanding for embodied agents. The authors highlight several key problems:

1.  **Over-reliance on Object Detectors:** Current 3D VLMs are heavily "object-centric," meaning they depend on pre-trained object detectors. This dependency introduces several issues:
    *   **Bottlenecks:** Object detection is a computational bottleneck.
    *   **Limited Flexibility:** It restricts the model to predefined object categories and taxonomies, hindering understanding of novel or fine-grained objects.
    *   **Neglect of Global Context:** Focusing solely on discrete objects often ignores crucial global scene context and intricate spatial relationships.
2.  **Dense Representation Challenge:** Embedding rich language features directly into fine-grained 3D scene elements (like points or Gaussians) results in extremely dense representations (tens of thousands of tokens per scene). Processing such high-dimensional, dense data efficiently with Large Language Models (LLMs) is computationally challenging and prone to semantic dilution.
3.  **Suboptimal 3D Scene Representation:** Many 3D VLMs rely on point clouds, which, while providing geometry, often lack detailed textural and appearance information crucial for nuanced scene understanding. The use of more expressive representations like Gaussian Splats, which capture photorealistic 3D textures, has not yet been explored in the context of language-grounded 3D VLMs.

To address these challenges, GaussianVLM sets out with the following key objectives:

*   **Shift to Scene-Centric Understanding:** The core objective is to move away from object-centric paradigms to a holistic, "scene-centric" approach that understands the entire 3D environment, including objects, spatial context, relationships, and global semantics, without relying on explicit object detection.
*   **Direct Language-Feature Embedding:** To achieve scene-centrism, the model aims to directly embed rich linguistic features (e.g., from CLIP or SigLIP) into each primitive element (Gaussian splat) of the 3D scene, facilitating early modality alignment.
*   **Efficient Dense Representation Processing:** Introduce a mechanism, specifically a "dual sparsifier," to efficiently distill these dense, language-augmented scene representations into compact, task-relevant tokens that are manageable for LLMs while preserving semantic fidelity.
*   **Pioneer Gaussian Splatting in 3D VLMs:** Leverage the photorealistic and richly detailed 3D representations offered by Gaussian Splats, derived from standard RGB images, as the foundational visual input for a language-grounded VLM.
*   **Enable Advanced Embodied Reasoning:** Develop a model capable of handling complex scene- and object-level tasks requiring multi-object reasoning, spatial understanding, global context, and fine-grained analysis, suitable for embodied agents and beyond.

### 4. Methodology and Approach

GaussianVLM introduces a novel, fully scene-centric 3D Vision-Language Model that leverages language-aligned Gaussian Splats. The methodology is built upon three key innovations: a language-aware 3D backbone, a dual sparsification module, and the use of Gaussian Splats as the primary 3D scene representation.

**4.1. GaussianVLM Architecture Overview**
GaussianVLM operates by taking a 3D scene (represented as Gaussian Splats) and a natural language prompt as input. It then fuses language and 3D vision features to generate a textual response. The model functions entirely in the language embedding space and is notably detector-free. The architecture comprises:

1.  **Language-Aware Gaussian Splatting Backbone:** The model adopts **SceneSplat** [27] as its 3D vision module. SceneSplat is designed to process 3D scenes represented as Gaussian splats and predict a **SigLIP2** [43] language feature for each Gaussian end-to-end. This crucial step directly embeds rich linguistic features into the spatial structure of the 3D scene, establishing early and strong language-visual alignment at a fine-grained level. The output is a dense sequence of language features, one for each Gaussian (e.g., 40,000 Gaussians yield 40,000 tokens).

2.  **Dual Sparsifier Module:** To address the challenge of processing the extremely dense language features from the SceneSplat backbone, GaussianVLM introduces a dual sparsifier module. This module distills the dense representation into a compact, task-relevant sparse set of tokens, making it manageable for LLMs. The dual nature consists of two pathways:

    *   **Task-Guided Sparsification:**
        *   This pathway re-tokenizes the dense scene representation into a compact set of 128 task-selected scene tokens.
        *   It employs **depth-wise cross-attention** [5] where queries are derived from the user's natural language prompt (tokenized using SigLIP2).
        *   This sparsification is applied iteratively to the output of *each* SceneSplat decoder layer, allowing dynamic and context-aware reduction of visual information. This "depth-wise" approach integrates global scene understanding from earlier layers with instance-level awareness from per-Gaussian features.
        *   To manage computational overhead, an initial uniform downsampling reduces features to 512 tokens per decoder layer, followed by cross-attention to further sparsify to 128 tokens.
        *   For prompts containing spatial locations (`loc_xyz`), learnable **Fourier embeddings** [9] encode this positional information, which is injected into the final sparsifier layer.

    *   **Location-Guided Sparsification (ROI Magnifier):**
        *   For tasks that provide a specific location (e.g., object captioning with a click point or bounding box), this module extracts fine-grained features from a **Region-of-Interest (ROI)**.
        *   It selects Gaussians within a spherical radius (default 15cm, iteratively expandable if empty) around the specified location.
        *   Attention pooling is then applied to the language features of these selected Gaussians to generate 4 compact ROI tokens that summarize the region. This acts as a detector-free mechanism to focus on local context.

3.  **Language Model Integration:**
    *   The sparse scene tokens (128 task-selected tokens + 4 ROI tokens) are linearly projected from the SigLIP2 space into the LLM's embedding space.
    *   These vision tokens are concatenated with the user's task tokens (tokenized by the LLM's tokenizer).
    *   The combined sequence is fed into a frozen Large Language Model (LLM), either **OPT-1.3B** [52] for LL3DA settings or **Vicuna-7B** [13] for LEO settings, augmented with **Low-Rank Adaptation (LoRA)** [21] for efficient fine-tuning.
    *   The LLM then autoregressively generates the response, conditioned jointly on both visual and textual context.

**4.2. Training Objective and Strategy**
The model follows a two-stage training protocol, common in VLM training:
1.  **Alignment Phase:** The 3D backbone and LLM tokenizer are frozen. The sparsifier modules and a small transformer for textual alignment of vision tokens are trained. The LLM is adapted using LoRA.
2.  **Fine-tuning (Instruction Tuning) Phase:** The model is further trained on diverse tasks to follow natural language instructions.

Both stages share a unified **prefix language modeling** objective [6, 23, 35], where the model is trained to autoregressively generate a target continuation given an input prefix (task prompt and vision tokens).

**4.3. Sparsifier Pre-training**
To enhance spatial grounding, the task-guided sparsifier undergoes an initial pre-training phase on an object captioning task. Given the 3D coordinates of an object instance, the model is trained to generate a visual token embedding similar to the embeddings of its corresponding label token, using a one-sided contrastive objective [34]. This encourages the sparsifier to learn meaningful spatial-semantic associations before full VLM training.

### 5. Main Findings and Results

GaussianVLM demonstrates significant advancements across a comprehensive suite of 3D vision-language tasks, consistently outperforming state-of-the-art baselines.

**5.1. State-of-the-Art Performance Across Benchmarks**
The model was evaluated under two established training protocols: LL3DA and LEO, across both scene-centric and object-centric tasks.

*   **Scene-Centric Tasks (Table I):**
    *   **SQA3D (LEO Protocol):** GaussianVLM achieved a top-1 exact match accuracy of **49.4%**, surpassing LEO's [23] 47.0% by 2.4 percentage points. This indicates superior situated question answering capabilities.
    *   **LL3DA Protocol (Embodied Dialogue, Planning, Scene Captioning):** GaussianVLM showed substantial improvements over LL3DA* [9]. For Embodied Dialogue, CIDEr increased from 145.9 to **270.1** (+124.2), and for Embodied Planning, CIDEr increased from 65.1 to **220.4** (+155.3). Similar significant gains were observed in Sentence Similarity, BLEU-4, METEOR, and ROUGE across these tasks. These results highlight GaussianVLM's enhanced multi-object reasoning, global context understanding, and ability to generate more coherent and relevant responses for complex scene-centric tasks.

*   **Object-Centric Tasks (Table II):**
    *   Despite being detector-free, GaussianVLM achieved comparable or superior results on object-centric benchmarks.
    *   **ScanQA:** Performance was comparable to LL3DA* [9].
    *   **Nr3D (Object Captioning):** GaussianVLM achieved a METEOR score of **20.8**, significantly outperforming LL3DA*'s 5.8 (+15.0). ROUGE also saw a substantial improvement from 9.9 to **19.2** (+9.3). This demonstrates that the model's scene-centric approach, combined with the location-guided sparsifier, can effectively handle fine-grained object understanding tasks without explicit object detection.

**5.2. Real-World Generalization (Table III)**
To assess robustness in realistic, out-of-domain (OOD) settings, GaussianVLM and LL3DA were evaluated on ScanNet++ [49] scenes (validation split), which are derived from RGB images and represent an OOD distribution for models typically trained on laser-scanned data like ScanNet. A novel object counting question-answering dataset (1,000 QA pairs) was created for this evaluation.
*   GaussianVLM, leveraging Gaussian Splats for its 3D representation, dramatically outperformed the point cloud-based LL3DA. It achieved an accuracy of **24.1%** compared to LL3DA's 4.2%, representing a **474% improvement** in accuracy. Significant gains were also observed in Exact Match (+520%), CIDEr (+120.6%), METEOR (+38.0%), and ROUGE (+76.5%). This finding underscores the strong generalization capabilities of GaussianVLM to real-world data obtainable with readily available RGB cameras.

**5.3. Ablation Study (Table IV)**
The ablation study provided crucial insights into the contribution of key components:

*   **Dual Sparsifier's Necessity:** Removing either the task-guided scene tokens or the location-guided ROI tokens resulted in substantial performance drops across both scene- and object-centric tasks, confirming their critical roles.
*   **Task Guidance Effectiveness:** Replacing text-prompt-based queries with task-unaware learnable queries significantly degraded performance, especially for scene-centric tasks, validating the importance of dynamic, language-guided selection of visual cues.
*   **Depth-Wise Sparsification:** Utilizing intermediate SceneSplat decoder hidden states for sparsification (depth-wise CA) was more effective than using only the final decoder output, particularly for scene-centric tasks requiring global context.
*   **Efficiency of Uniform Downsampling:** The simpler uniform downsampling strategy for initial sparsification proved as effective as more complex language-unaware alternatives like kNN and attention pooling, confirming its efficiency without compromising performance.
*   **ROI Radius:** An ROI radius of 15cm provided better performance for object-centric tasks with only a negligible drop for scene-centric tasks, indicating the fine-grained nature of its contribution.

In summary, GaussianVLM not only achieves state-of-the-art performance but also introduces a more flexible, efficient, and generalizable approach to 3D VLM by fundamentally shifting to a scene-centric, detector-free paradigm based on language-aligned Gaussian Splats.

### 6. Significance and Potential Impact

GaussianVLM represents a pivotal advancement in the field of 3D Vision-Language Models, offering several significant contributions and potential impacts:

*   **Paradigm Shift to Scene-Centric 3D Understanding:** The most significant contribution is the successful implementation of a fully scene-centric 3D VLM. By moving away from the prevailing object-centric and detector-dependent approaches, GaussianVLM enables a more natural, holistic, and flexible understanding of 3D environments. This bypasses the limitations of predefined taxonomies, improves adaptability to novel objects, and fosters a richer comprehension of spatial relationships and global context—aspects crucial for true intelligence in physical spaces.

*   **Empowered Embodied Agents:** The comprehensive scene understanding capabilities of GaussianVLM are highly beneficial for embodied agents (e.g., robots, virtual assistants). It allows for advanced tasks such as more accurate embodied reasoning, multi-object spatial reasoning, robust planning, and nuanced dialogue, directly improving an agent's ability to act intelligently and interact effectively within complex real-world environments.

*   **Pioneering Gaussian Splatting in 3D VLMs:** GaussianVLM is the first language-grounded 3D VLM to directly operate on 3D Gaussian Splat representations. This leverages the inherent advantages of Gaussian splats, such as their photorealistic quality, ability to capture rich geometric and appearance information, and reconstructibility from standard RGB images. This integration not only enhances the quality of visual features but also significantly improves the model's generalization capabilities to real-world, less structured inputs, as demonstrated by the dramatic performance increase on out-of-domain ScanNet++ data. This opens new avenues for deploying 3D VLMs with more accessible data collection methods.

*   **Efficient Processing of Dense 3D Data:** The novel dual sparsification module (task-guided and location-guided) is a critical methodological contribution. It effectively tackles the challenge of extremely dense, language-augmented 3D representations, distilling them into compact, task-relevant tokens that can be efficiently processed by LLMs. This addresses a major computational bottleneck and ensures that the fine-grained semantic information embedded in each Gaussian is meaningfully utilized without overwhelming the language model.

*   **Broader Applications:** Beyond embodied AI, the advancements brought by GaussianVLM have implications for various fields:
    *   **Robotics:** Enhanced environmental perception, task planning, and human-robot interaction.
    *   **Augmented/Virtual Reality (AR/VR):** More context-aware and interactive virtual environments.
    *   **Accessibility Technologies:** Better understanding of surroundings for assistive devices.
    *   **General 3D Content Understanding:** Improved capabilities for querying and summarizing complex 3D scenes using natural language.

Despite its significant strengths, the authors also acknowledge important limitations. The training of such large-scale VLMs remains computationally intensive, requiring substantial GPU resources and training hours, contributing to environmental concerns. Current evaluations are primarily focused on static 3D indoor scenes, suggesting future work for dynamic or outdoor environments. The quality of Gaussian Splat reconstructions can vary, which might impact performance in less-than-ideal scenarios. Furthermore, a broader range of out-of-domain benchmarks is needed for a more comprehensive assessment of generalization.

In conclusion, GaussianVLM represents a substantial leap forward by providing a robust, flexible, and efficient framework for holistic 3D scene understanding. Its scene-centric, detector-free approach, coupled with the innovative use of Gaussian Splats and dual sparsification, sets a new benchmark for 3D VLMs and paves the way for more capable and adaptable intelligent agents operating in the physical world.
