---
title: "Vision-Language Memory for Spatial Reasoning"
date: 2025-11-25
arxiv: "2511.20644"
venue:
status: to-read

abstract: "Spatial reasoning is a critical capability for intelligent robots, yet current vision-language models (VLMs) still fall short of human-level performance in video-based spatial reasoning. This gap mainly stems from two challenges: a semantic-geometric misalignment that prevents consistent 3D understanding, and the absence of persistent memory to retain 3D representation and understanding over time. To address these limitations, we present VLM$^2$, a Vision-Language Model with persistent Memory for spatial reasoning with a view-consistent, 3D-aware representation purely from 2D video. Specifically, to enhance long-horizon reasoning, we incorporate a dual-memory module, consisting of a working memory that operates as a sliding window to focus on immediate context, and an episodic memory that consolidates and stores critical long-term information. This design enables efficient and long-horizon spatial reasoning with a fixed computational cost. Extensive experiments on multiple benchmarks show that VLM$^2$ achieves state-of-the-art performance among video-only models, significantly advancing the frontier of visual-spatial intelligence."

website: https://sairlab.org/vlm2
code: https://github.com/chrisrhymes/bulma-clean-theme
openreview:
issue: 11

inputs:
  - posed-multi-view-images
  - text-prompt
outputs:
  - 3d-gaussians
  - semantic-segmentation
methods:
  - 3dgs
  - vlm
  - memory
benchmarks:
  - 

related:
  - 

compared:
  - 
---

# Vision-Language Memory for Spatial Reasoning

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

## LLM Summary

This report provides a detailed analysis of the research paper "Vision-Language Memory for Spatial Reasoning," outlining its contributions, methodology, and significance within the broader field of artificial intelligence and robotics.

---

### 1. Authors, Institution(s), and Notable Context

The paper "Vision-Language Memory for Spatial Reasoning" is primarily authored by researchers from the **Spatial AI & Robotics (SAIR) Lab at the University at Buffalo**, namely Zuntao Liu, Yi Du, Taimeng Fu, Shaoshu Su, and Chen Wang. An additional author, Cherie Ho, is affiliated with **Stanford University**.

The SAIR Lab, led by Assistant Professor Chen Wang, appears to be a dynamic research group focused on the intersection of artificial intelligence, computer vision, and robotics. Their work, as indicated by the project website (sairlab.org/vlm2/), often emphasizes developing intelligent systems capable of perceiving, understanding, and interacting with the physical world in a spatially aware manner. The lab's explicit focus on "Spatial AI & Robotics" aligns perfectly with the core themes of this paper, which seeks to enhance spatial reasoning in intelligent robots. The publication of this work, focusing on video-based spatial reasoning, reinforces the lab's commitment to advancing capabilities critical for embodied AI agents operating in real-world, dynamic environments. The inclusion of Cherie Ho from Stanford University suggests a collaborative effort, possibly bringing expertise from a leading institution in AI research, thereby enriching the project with diverse perspectives and potentially broader impact. This collaboration further highlights the interdisciplinary nature and high-profile ambition of the research.

### 2. How This Work Fits into the Broader Research Landscape

This research directly addresses critical limitations within the rapidly evolving field of Vision-Language Models (VLMs) and their application to spatial reasoning, particularly for intelligent robots. VLMs have shown remarkable progress in interpreting and generating content across visual and textual modalities. However, their performance in sophisticated 3D spatial reasoning, especially from dynamic 2D video inputs, still lags significantly behind human capabilities.

The broader research landscape for spatial reasoning in AI can be segmented into several key areas:

*   **3D Large Language Models (LLMs):** Initial efforts in this domain focused on integrating explicit 3D modalities, such as point clouds or depth maps, with LLMs to enable 3D scene understanding. While these models demonstrated improved 3D awareness, their reliance on specialized 3D sensors limits their applicability in many real-world scenarios where only 2D video feeds are available. More recent works have attempted to recover 3D cues from multi-view images or inject 3D position information into visual representations, but often still necessitate additional 3D data or complex reconstruction processes.
*   **Spatial Reasoning in VLMs:** Much of the existing VLM research on spatial reasoning has concentrated on static 2D images. Extending this to video, where viewpoint changes, object occlusions, and temporal relationships are paramount, presents unique challenges. Recent advancements have sought to enhance VLM spatial reasoning by incorporating geometric priors, often derived from 3D Visual Geometry Foundation Models (VGFMs). However, a common critique highlighted by this paper is that many approaches rely on "simple feature fusion," which frequently fails to resolve the inherent misalignment between semantic features (from 2D vision encoders) and geometric features (from 3D priors). This misalignment leads to inconsistent 3D understanding, particularly under camera motion.
*   **Memory Mechanisms in Computer Vision:** The necessity of memory for processing long sequences of information has been acknowledged across various vision tasks, including video understanding, generation, and 3D reconstruction. Within the context of embodied AI and spatial reasoning, specialized memory modules have been explored to build spatial maps or track objects over time. For instance, models like 3DLLM-Mem have introduced long-term memory for embodied 3D LLMs. However, current memory solutions often suffer from drawbacks such as requiring explicit 3D inputs, accumulating redundant information, or incurring unbounded computational costs when processing long video sequences.

VLM$^2$ positions itself at the forefront of this landscape by tackling the two most significant challenges for video-based spatial reasoning in VLMs: **semantic-geometric misalignment** and the **absence of persistent memory**. Unlike many existing 3D LLMs, VLM$^2$ learns 3D-aware representations *purely from 2D video*, thereby removing the dependency on costly or unavailable 3D sensor data during inference. It innovates beyond simple feature fusion methods by introducing explicit alignment mechanisms for semantic and geometric cues. Furthermore, its dual-memory architecture offers a bounded and efficient solution to the problem of long-horizon reasoning, contrasting with approaches that face issues of redundancy and scalability. By addressing these core limitations, VLM$^2$ significantly advances the frontier of visual-spatial intelligence, making a substantial contribution to the development of more capable and versatile intelligent robots.

### 3. Key Objectives and Motivation

The overarching goal of the "Vision-Language Memory for Spatial Reasoning" paper is to equip intelligent robots with human-level spatial reasoning capabilities, specifically when operating solely on 2D video input. This ambitious objective is driven by two fundamental limitations observed in current Vision-Language Models (VLMs) regarding video-based spatial reasoning:

1.  **Semantic-Geometric Misalignment:**
    *   **Motivation:** Existing VLMs, while adept at extracting semantic information from 2D video (e.g., identifying objects like "chairs"), often lack precise metric grounding and positional awareness. This makes it difficult to maintain consistent spatial understanding across different viewpoints or over time. For example, a model might incorrectly identify two different chairs as the same instance when the camera moves. Conversely, geometric features derived from 3D models provide structural cues but can be view-dependent and unstable when naively combined with semantic features, leading to global spatial inconsistencies. The inability to consistently align these two crucial information streams (semantic meaning and geometric structure) prevents VLMs from building a coherent and stable 3D understanding of a scene from varying 2D perspectives.
    *   **Objective:** The authors aim to develop a method that constructs a **view-consistent, 3D-aware representation** from 2D video inputs. This representation must effectively resolve the semantic-geometric misalignment, ensuring that both visual semantics and geometric structure are coherently integrated and remain stable under camera motion.

2.  **Absence of Persistent Memory:**
    *   **Motivation:** Intelligent robots operating in dynamic environments frequently encounter situations with continuous viewpoint changes, partial observability, and transient occlusions. Objects may disappear and reappear as the robot navigates. Traditional VLMs typically rely on short-term, token-based context windows, which are inherently transient. This design causes them to "forget" previously observed information, making it challenging to maintain a long-term, coherent spatial map. For tasks requiring long-horizon reasoning (e.g., counting objects across an entire room after moving through it), this lack of persistent memory is a critical impediment.
    *   **Objective:** The authors seek to introduce a **persistent memory mechanism** into VLMs. This mechanism must be capable of retaining and updating 3D-aware representations over extended periods and across various viewpoints, thereby enabling efficient and robust long-horizon spatial reasoning with a fixed computational cost.

By addressing these two core challenges simultaneously, VLM$^2$ aims to significantly enhance the ability of VLMs to perform sophisticated spatial reasoning tasks, moving them closer to human-level performance in complex, dynamic, real-world environments.

### 4. Methodology and Approach

VLM$^2$ is designed as a vision-language model with persistent memory for spatial reasoning, building upon a view-consistent, 3D-aware representation derived purely from 2D video. The architecture is implemented on top of LLaVA-Video [72] and utilizes π$_3$ [52] as its 3D foundation model. The methodology comprises two primary innovations: a module for view-consistent 3D-aware representation and a dual-memory module.

**4.1. View-Consistent 3D-Aware Representation**

To resolve the semantic-geometric misalignment, VLM$^2$ processes uniformly sampled frames from an input video to produce a coherent 3D-aware representation for each frame. This involves three interconnected modules:

1.  **Adaptive 3D Position Injection:**
    *   **Purpose:** To ground 2D visual tokens in 3D space while mitigating noise from predicted 3D coordinates.
    *   **Mechanism:** The model first extracts visual tokens (F$_t$) from a pretrained vision encoder and predicts per-pixel 3D point maps (X$_t$) from a 3D foundation model (π$_3$). These point maps are pooled to get per-patch 3D coordinates (C$_t$). Unlike previous methods that uniformly inject 3D information, VLM$^2$ introduces a **learnable gating mechanism ($\alpha_t$)**. This gate adaptively modulates the injection of encoded 3D position embeddings ($\phi(C_t)$) into the visual tokens. This selective injection ensures that only reliable and useful 3D cues are incorporated, preventing performance degradation from noisy or irrelevant predictions. The output is position-aware visual tokens (F$^{pa}_t$).

2.  **Viewpoint-Aware Geometry Alignment:**
    *   **Purpose:** To disambiguate viewpoint-ambiguous geometric features, ensuring spatial coherence across different camera perspectives.
    *   **Mechanism:** From the 3D foundation model, geometry tokens (G$_t$) and view tokens (Z$_t$) are extracted. To make geometric features viewpoint-aware, VLM$^2$ infuses them with both local and global perspective cues.
        *   **Patch-level:** View tokens (Z$_t$) are projected and concatenated with geometry tokens (G$_t$) and passed through an MLP to produce features (G$^{va}_t$) that disambiguate local geometric patterns (e.g., distinguishing the front from the back of a chair).
        *   **Frame-level:** A global view descriptor ($\bar{Z}_t$), obtained by pooling view tokens and projecting them, is appended to G$^{va}_t$. This provides a frame-level signal of the camera's overall viewpoint direction, resulting in viewpoint-consistent geometry tokens (G$^{vc}_t$).

3.  **Semantic-Geometric Fusion:**
    *   **Purpose:** To integrate the enhanced visual and geometric features into a unified, coherent 3D-aware representation.
    *   **Mechanism:** The position-aware visual tokens (F$^{pa}_t$) serve as queries, and the viewpoint-aware geometry tokens (G$^{vc}_t$) act as keys and values in a **cross-attention mechanism**. This fusion process binds visual semantics to consistent geometric structure, generating powerful 3D-aware tokens (H$_t$) for each frame that are consistent across varying camera motions.

**4.2. Dual-Memory Module**

To achieve persistent memory for long-horizon reasoning, VLM$^2$ introduces a dual-memory module that operates on the generated 3D-aware representations (H$_t$).

1.  **Working Memory for Immediate Retrieval (W$_t$):**
    *   **Purpose:** To capture and dynamically focus on the most relevant short-term context.
    *   **Mechanism:** This module functions as a **sliding window** that stores the $L_w$ most recent 3D-aware representations (H$_t$). The current representation H$_t$ is used as a query to perform cross-attention over the working memory's contents. This selective retrieval generates an immediate-context-enhanced representation (M$^{w}_t$). The working memory is updated by adding the current H$_t$ and removing the oldest entry if capacity is reached.

2.  **Episodic Memory for Long-Horizon Recall (E$_t$):**
    *   **Purpose:** To retain crucial information over long horizons, supporting tasks requiring long-term recall.
    *   **Mechanism:** This is a **fixed-capacity bank** of $L_e$ salient observations. The model implicitly learns what information is "task-relevant" through end-to-end training. Similar to working memory, the current H$_t$ queries the episodic memory via cross-attention, producing an episodic-enhanced representation (M$^{e}_t$).

3.  **Memory Fusion and Update:**
    *   **Purpose:** To combine immediate and long-term memory streams and maintain an efficient, diverse episodic memory.
    *   **Mechanism:** A **learnable gate ($\gamma_t$)** combines M$^{w}_t$ and M$^{e}_t$ to yield the final memory-enhanced representation (M$_t$). For updating episodic memory, a **similarity-based mechanism** is employed: the most similar existing entry in E$_t$ (based on cosine similarity with M$_t$) is replaced by the current M$_t$. This strategy ensures that episodic memory remains bounded, non-redundant, and stores diverse, salient information, which is crucial for efficient and persistent long-horizon spatial reasoning.

This comprehensive methodology allows VLM$^2$ to not only understand the 3D world from 2D video but also to retain and update that understanding over extended periods, providing a robust foundation for complex spatial reasoning tasks.

### 5. Main Findings and Results

The experiments conducted by the authors demonstrate VLM$^2$'s superior performance across a range of spatial reasoning and 3D understanding benchmarks, particularly when compared to other video-only models and even some models requiring explicit 3D inputs.

1.  **State-of-the-Art Performance on Spatial Reasoning Benchmarks:**
    *   **VSI-Bench [60] (3D Spatial Reasoning):** VLM$^2$ consistently outperforms proprietary models (GPT-4o, Gemini-1.5 Pro/Flash) and numerous open-source VLMs (e.g., LLaVA-NeXT-Video-72B, InternVL2-40B). It also surpasses specialized spatial-enhanced models like VLM-3R-7B, achieving an overall average accuracy of 68.8% compared to VLM-3R's 60.9%. The gains are particularly significant in tasks like Absolute Distance, Relative Direction, Route Plan, and Appearance Order, indicating strong, fine-grained 3D awareness and the ability to integrate spatial understanding over time.
    *   **VSTI-Bench [16] (3D Spatial-Temporal Reasoning):** For tasks assessing persistent spatial reasoning over time, VLM$^2$ achieves an overall accuracy of 65.3%, marking an 11.1% relative improvement over the previous best method, VLM-3R (58.8%). This includes SOTA performance across all task categories, affirming its robust capabilities in understanding evolving spatial relationships.

2.  **Enhanced Long-Horizon Reasoning Abilities:**
    *   When videos were categorized by length (Short: <1 min, Mid: 1-2 min, Long: >2 min), VLM$^2$ demonstrated consistent performance across all durations. Crucially, it showed the largest gains on *long videos* compared to baselines. For instance, on VSI-Bench, VLM$^2$ improved by +8.1 points over VLM-3R for long videos, and by +8.2 points on VSTI-Bench. This explicitly validates the effectiveness of the dual-memory module in preserving spatial understanding and supporting reasoning over extended temporal horizons, where other models typically degrade.

3.  **Strong Performance on 3D Scene Understanding Benchmarks:**
    *   **ScanQA [1] and SQA3D [40] (3D Question Answering):** VLM$^2$ achieves SOTA performance among video-only models on both benchmarks. It also significantly outperforms all task-specific models (e.g., ScanQA, SQA3D, 3D-VisTA). Furthermore, VLM$^2$ surpasses several models that require explicit 3D or 2.5D inputs (e.g., Video-3D LLM, 3DRS), demonstrating that its 3D-aware representation, learned solely from video, can effectively compete with and often exceed methods using richer 3D modalities. While Ross3D, which uses point clouds for reconstructive supervision, achieved slightly higher on some metrics, VLM$^2$'s video-only approach remains highly competitive.

4.  **Ablation Studies Confirm Component Contributions:**
    *   **Overall Component Analysis:** Ablations on VSI-Bench showed that the 3D-aware representation module alone significantly improved the baseline (+8.6% accuracy). Adding the working memory yielded further gains (+2.1%), and incorporating the episodic memory provided additional improvements (+2.3%). The full VLM$^2$ model, combining all components, achieved the best performance, boosting the baseline by +12.6%, particularly on tasks like Route Plan.
    *   **Effectiveness of 3D-Aware Representation:** Experiments confirmed that the proposed Viewpoint-Aware Geometry Alignment (VAGA) and Adaptive 3D Position Injection (A3PI) are crucial. Cross-attention as a semantic-geometric fusion strategy outperformed simpler concatenation or addition. The adaptive gating mechanism in A3PI was vital, with its removal leading to degraded performance due to noise from uniform 3D position injection. π$_3$ was identified as the most effective 3D backbone among those tested.
    *   **Dual-Memory Length:** Studies on memory length revealed an optimal configuration of a working memory window size ($L_w$) of 8 and an episodic memory capacity ($L_e$) of 32. This balance allowed effective capture of immediate context and long-term salient information, maximizing spatial reasoning performance.

In summary, the results unequivocally establish VLM$^2$ as a leading model for spatial reasoning from video, showcasing the critical importance and effectiveness of its novel approach to 3D-aware representation and persistent dual-memory.

### 6. Significance and Potential Impact

The development of VLM$^2$ represents a significant leap forward in the field of Vision-Language Models for spatial reasoning, with profound implications for intelligent robotics and broader AI research. Its significance and potential impact can be summarized as follows:

1.  **Advancing Visual-Spatial Intelligence to Human Levels:** VLM$^2$ directly addresses the long-standing challenge of achieving human-level spatial reasoning from video inputs in AI systems. By demonstrating state-of-the-art performance across diverse benchmarks, the paper pushes the boundaries of what is achievable in visual-spatial intelligence, bringing AI systems closer to a more intuitive and comprehensive understanding of the physical world.

2.  **Bridging the 2D-to-3D Gap without Explicit 3D Sensors:** A major contribution is its ability to construct a view-consistent, 3D-aware representation *purely from 2D video*. This eliminates the need for expensive, specialized 3D sensors (like LiDAR or depth cameras) or complex 3D reconstruction pipelines during inference. This fundamental shift makes sophisticated spatial reasoning far more accessible and practical for deployment in real-world scenarios where only conventional 2D cameras are available (e.g., security cameras, mobile phone cameras, or basic robot vision systems).

3.  **Resolving Fundamental Challenges in VLMs:** VLM$^2$ effectively tackles two core limitations that have hindered video-based VLMs:
    *   **Semantic-Geometric Misalignment:** The innovative adaptive 3D position injection and viewpoint-aware geometry alignment mechanisms provide a robust solution for integrating semantic and geometric cues coherently, ensuring stable 3D understanding despite varying viewpoints.
    *   **Absence of Persistent Memory:** The dual-memory module (working and episodic memory) offers an elegant and efficient solution for long-horizon reasoning. By maintaining a bounded yet persistent memory of salient 3D-aware representations, it overcomes the "forgetting" problem inherent in transient context windows, which is crucial for tasks requiring continuous environmental awareness.

4.  **Enabling More Capable and Autonomous Robots:** The enhanced spatial reasoning and persistent memory capabilities endowed by VLM$^2$ are critical for intelligent robots. They will enable robots to:
    *   **Navigate more intelligently:** Reason about unobserved areas, plan complex routes, and avoid re-visiting previously explored spaces efficiently.
    *   **Interact with objects more effectively:** Understand object positions, sizes, and relationships consistently across different views and over time, facilitating precise manipulation and interaction.
    *   **Perform complex tasks:** Execute long-horizon tasks requiring cumulative spatial knowledge, such as inventory management, multi-room exploration, or sophisticated human-robot collaboration in dynamic environments.
    *   **Improve safety and reliability:** A more consistent understanding of the environment leads to more reliable decision-making and safer operation.

5.  **Setting New Benchmarks and Directions for Future Research:** By achieving SOTA on multiple established benchmarks and performing particularly well on long-horizon tasks, VLM$^2$ sets a new high bar for video-based spatial reasoning. This will undoubtedly inspire further research in several directions, including:
    *   Developing more sophisticated memory update mechanisms.
    *   Exploring adaptive gating strategies for various modalities.
    *   Integrating VLM$^2$'s capabilities into full embodied AI agents for end-to-end task performance.
    *   Applying the principles of view-consistent representation and dual-memory to other spatio-temporal AI problems.

In conclusion, VLM$^2$ not only presents a technically sound and empirically validated solution to pressing challenges in VLM research but also significantly contributes to the foundational capabilities required for the next generation of truly intelligent and autonomous robotic systems.
