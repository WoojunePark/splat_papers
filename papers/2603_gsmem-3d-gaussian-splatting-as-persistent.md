---
title: "GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning"
date: 2026-03-19
arxiv: "2603.19137"
venue:
status: to-read

abstract: "Effective embodied exploration requires agents to accumulate and retain spatial knowledge over time. However, existing scene representations, such as discrete scene graphs or static view-based snapshots, lack \textit{post-hoc re-observability}. If an initial observation misses a target, the resulting memory omission is often irrecoverable. To bridge this gap, we propose \textbf{GSMem}, a zero-shot embodied exploration and reasoning framework built upon 3D Gaussian Splatting (3DGS). By explicitly parameterizing continuous geometry and dense appearance, 3DGS serves as a persistent spatial memory that endows the agent with \textit{Spatial Recollection}: the ability to render photorealistic novel views from optimal, previously unoccupied viewpoints. To operationalize this, GSMem employs a retrieval mechanism that simultaneously leverages parallel object-level scene graphs and semantic-level language fields. This complementary design robustly localizes target regions, enabling the agent to ``hallucinate&#39;&#39; optimal views for high-fidelity Vision-Language Model (VLM) reasoning. Furthermore, we introduce a hybrid exploration strategy that combines VLM-driven semantic scoring with a 3DGS-based coverage objective, balancing task-aware exploration with geometric coverage. Extensive experiments on embodied question answering and lifelong navigation demonstrate the robustness and effectiveness of our framework"

website: https://vulab-ai.github.io/GSMem
code: 
openreview:
issue: 12

inputs:
  - posed-multi-view-images
outputs:
  - 3d-gaussians
methods:
  - 3dgs
  - memory
  - agent
benchmarks:
  - 

related:
  - 

compared:
  - 
---

# GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning

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

![Figure](https://arxiv.org/html/2603.19137v1/x1.png)

*Figure 1: With GS-Mem, previously explored regions can be retrieved and re-observed directly from the 3DGS memory without physically navigating to them.*

![Figure](https://arxiv.org/html/2603.19137v1/x2.png)

*Figure 2: Demonstration of Multi-level Retrieval-Rendering. Given a task-related target, the agent retrieves ROIs based on object-level and semantic-level cues. Subsequent viewpoint selection and rendering enable the agent to re-observe these regions for further reasoning.*

![Figure](https://arxiv.org/html/2603.19137v1/x3.png)

*Figure 3: Demonstration of our Hybrid Exploration Strategy. When frontier observations do not contain sufficient task-related cues for the VLM to make a decision, we incorporate an information gain-based score to select the most informative frontier for further exploration.*

![Figure](https://arxiv.org/html/2603.19137v1/x4.png)

*Figure 4: Case analysis. We analyze several cases where scene-graph and view-based representations fail, and demonstrate the advantages of 3DGS-based memory. The images shown correspond to the views selected by the VLM for answering the questions. The examples (a-c) illustrate failures of the scene-graph detector, while the last example (d) highlights how optimal viewpoint rendering benefits the VLM’s reasoning.*

![Figure](https://arxiv.org/html/2603.19137v1/x5.png)

*Figure 5: Runtime analysis for real-world multi-process setup.*

## LLM Summary

## Research Paper Report: GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning

### 1. Authors and Institution(s)

The research paper "GSMem: 3D Gaussian Splatting as Persistent Spatial Memory for Zero-Shot Embodied Exploration and Reasoning" was authored by:

*   Yiren Lu (Case Western Reserve University)
*   Yi Du (Spatial AI & Robotics (SAIR) Lab, University at Buffalo)
*   Disheng Liu (Case Western Reserve University)
*   Yunlai Zhou (Case Western Reserve University)
*   Chen Wang (Spatial AI & Robotics (SAIR) Lab, University at Buffalo)
*   Yu Yin (Case Western Reserve University)

Yiren Lu and Yi Du are designated as equal contributors.

### 2. How This Work Fits into the Broader Research Landscape

Embodied artificial intelligence, particularly embodied navigation, concerns the development of agents capable of interacting with and understanding complex 3D environments. A central challenge in this field involves enabling agents to effectively acquire, store, and utilize spatial knowledge over time to support tasks such as exploration, reasoning, and navigation.

Existing approaches to scene representation for embodied agents generally fall into two categories: object-centric abstractions and view-based representations. Object-centric methods, such as 3D scene graphs (e.g., ConceptGraphs, Hydra), model environments as discrete collections of objects and their relationships. While providing high-level semantic understanding, these methods are susceptible to perception module failures, where undetected or misidentified objects lead to irrecoverable memory omissions. They also discard raw visual data, limiting their ability to reason about fine-grained visual details.

View-based representations, including 2D top-down maps or collections of egocentric image snapshots (e.g., 3D-Mem, GOAT), aim to preserve visual fidelity. However, these memories are inherently sparse and view-dependent. If an initial observation is suboptimal, such as from an unfavorable angle or due to occlusion, the static nature of these memories prevents the agent from synthesizing alternative views to resolve ambiguities or extract missed information.

The limitation identified across both paradigms is the absence of "post-hoc re-observability." Current agents are restricted to their initial observations and cannot mentally revisit a previously explored scene from a new perspective to discover details that were initially overlooked.

The paper positions GSMem as addressing this fundamental gap by introducing a continuous, dense, and re-renderable spatial memory based on 3D Gaussian Splatting (3DGS). This approach differentiates itself from previous offline semantic 3DGS methods by integrating an online, optimization-free language field for real-time semantic retrieval.

In the context of embodied exploration and navigation, the field has evolved from traditional reinforcement learning (RL) policies to zero-shot Vision-Language Model (VLM) agents. While VLM-based methods (e.g., Explore-EQA, VLMNav, TANGO, MTU3D, 3D-Mem) leverage VLMs for semantic reasoning and subgoal generation, many still rely on discrete observations or sparse graph representations. GSMem extends these VLM-driven approaches by providing a richer, continuous memory structure and introducing a hybrid exploration strategy that combines VLM-driven semantic relevance with an information-theoretic coverage objective. This work seeks to advance the generalization capabilities of agents to open-vocabulary queries in unseen environments by enabling more robust spatial recollection and efficient exploration.

### 3. Key Objectives and Motivation

The primary motivation behind GSMem stems from a recognized limitation in current embodied AI systems: their inability to perform "post-hoc re-observability." Unlike human cognitive processes, where past scenes can be mentally revisited from different perspectives to uncover previously missed details or clarify ambiguities, existing embodied agents are constrained by the specific viewpoints and resolutions of their initial observations or by the discrete nature of their stored object information. This limitation leads to irrecoverable memory omissions when objects are not detected or are observed from suboptimal angles, directly impacting downstream reasoning and navigation tasks.

To address this, the work sets forth several key objectives:

1.  **Develop a Persistent, Re-renderable Spatial Memory:** The central objective is to move beyond discrete scene graphs and static view-based snapshots by constructing a dense, continuous radiance field that can serve as a persistent spatial memory. This memory needs to explicitly parameterize both scene geometry and appearance to support high-fidelity novel view synthesis in real time. The chosen technology for this purpose is 3D Gaussian Splatting (3DGS).
2.  **Enable Spatial Recollection:** By leveraging the novel view synthesis capability of 3DGS, the framework aims to endow the agent with "Spatial Recollection." This means the agent should be able to virtually "re-visit" previously explored regions by rendering photorealistic views from arbitrary, optimal viewpoints, including those it has never physically occupied. This capability is intended to overcome the view-dependency and sparsity limitations of existing memory systems.
3.  **Implement a Multi-level Retrieval-Rendering Mechanism:** To effectively utilize the persistent spatial memory, the objective is to design a robust mechanism for localizing task-relevant regions. This mechanism needs to be resilient to common perception failures, such as missing or incorrect object detections. It is proposed to achieve this through a complementary design that leverages both object-level cues from a 3D scene graph and semantic-level features from a continuously updated language field.
4.  **Support High-Fidelity VLM Reasoning:** Following the retrieval of relevant regions, a critical objective is to determine the optimal viewpoint from which to render these regions. The rendered, high-fidelity observations would then be fed to a Vision-Language Model (VLM) to perform more accurate and nuanced reasoning, thereby improving the agent's ability to answer questions or fulfill task queries.
5.  **Design a Hybrid Exploration Strategy:** To ensure efficient and comprehensive accumulation of spatial knowledge during active exploration, the work aims to develop an exploration strategy that balances task-aware objectives with geometric coverage. This strategy is intended to prevent premature focus on semantically relevant but under-observed areas, ensuring the constructed 3DGS memory is both rich in semantic information and geometrically complete.

In summary, the motivation is to equip embodied agents with a more human-like capacity for spatial memory and reasoning, allowing them to overcome the rigidity of current representations and perform more robustly in complex, open-vocabulary tasks.

### 4. Methodology and Approach

The GSMem framework integrates 3D Gaussian Splatting (3DGS) as a continuous spatial memory, a multi-level retrieval-rendering mechanism, and a hybrid exploration strategy to facilitate zero-shot embodied exploration and reasoning.

#### 4.1 3DGS Mapping

The core of GSMem's spatial memory is built upon 3D Gaussian Splatting. A scene is represented by a set of anisotropic 3D Gaussians, each defined by its position, covariance, opacity, and color. Novel view rendering is achieved by projecting these Gaussians onto a target camera's image plane and compositing them via alpha blending.

*   **Keyframe Selection & Optimization:** The system ingests RGB-D images from an agent's sensors. Keyframes are selected when the average optical flow magnitude between the current frame and the last keyframe exceeds a threshold. A sliding window approach, typically of 10 keyframes, is used for incremental map updates. The Gaussian parameters are optimized by minimizing L1 losses on rendered RGB and depth images against observed data, using a sampled subset of keyframes from the window and the broader keyframe set.
*   **Online Language Field Generation:** To support semantic grounding, each 3D Gaussian is associated with a language embedding. Instead of iterative optimization, GSMem employs an optimization-free approach: dense 2D features are extracted from keyframes using a pixel-wise CLIP encoder and a super-resolution decoder. These compressed 2D features are then "reverse aggregated" onto the 3D Gaussians using the same alpha-blending weights derived during forward rendering. This weight-consistent process generates a dense 3D language field without additional optimization overhead.
*   **Auxiliary Maps:** In addition to the 3DGS map and language field, the system maintains an object-level scene graph (via object detection, matching, and merging) for structured region retrieval. A frontier map and a Truncated Signed Distance Function (TSDF) map are also maintained for navigation and obstacle avoidance.

#### 4.2 Multi-level Retrieval-Rendering

This mechanism aims to localize task-relevant regions and render optimal views for VLM reasoning.

*   **Object-level Region Retrieval:** Given an input question, the VLM interacts with the scene graph to rank detected objects based on semantic relevance. The top-K objects define object-level regions of interest (ROIs).
*   **Semantic-level Region Retrieval:** The VLM identifies target semantic entities from the query, converting them into CLIP embeddings. These embeddings query the 3D language field to retrieve Gaussians with high cosine similarity. These retrieved Gaussians are then spatially clustered into coherent groups (e.g., using KD-Tree and connected components), forming semantic-level ROIs. This dual approach provides robustness, as semantic-level retrieval can compensate for object detection failures.
*   **Optimal Rendering Viewpoint for Visual Recall:** For each ROI, GSMem samples candidate camera poses around its 3D bounding box (e.g., 108 poses at various azimuths and elevations). A two-phase scoring process selects the optimal viewpoint:
    *   **Phase 1 (Coarse Filtering):** Candidate poses inside obstacles (checked via TSDF map) are discarded. Remaining poses are scored based on ray visibility (S_vis) from the ROI's bounding box and projected 2D area (S_A), which penalizes views that are too close or too far. The top-10 candidates proceed.
    *   **Phase 2 (Fine-grained Quality):** For the top candidates, an opacity map is rendered using 3DGS. The average opacity within the projected 2D ROI (S_opa) indicates surface presence and visual observability. The viewpoint with the highest combined score (S_final = S_vis + S_A + S_opa) is selected.

#### 4.3 ROI Rendering & Vision-Language Reasoning

From the selected optimal viewpoint, the ROI is rendered. To further enhance visual quality for VLM input, a single-step diffusion model is applied to the rendered images. These enhanced images, along with views from the object's highest-confidence detection pose, are then fed into a VLM (e.g., GPT-4o) to determine if the task query can be answered. If not, the agent proceeds to exploration.

#### 4.4 Hybrid Exploration Strategy

This strategy guides the agent's exploration based on frontier-based navigation, balancing semantic relevance and geometric coverage.

*   **Semantic Relevance:** For each candidate frontier (boundary between known and unknown space), an observation is fed to a VLM with the task query. The VLM outputs a relevance score (s_sem) indicating the likelihood of the frontier revealing task-relevant information.
*   **Geometric Coverage:** This metric quantifies the expected information gain from exploring a frontier. It approximates the reduction in differential entropy of the 3DGS parameters. Using a T-optimality surrogate, it's calculated as the trace of the incremental Fisher Information Matrix (Tr(I_i)), derived from the gradients of the 3DGS rendering function. This acts as a proxy for geometric uncertainty and is efficiently computed without ground-truth supervision.
*   **Exploration Decision:** The agent prioritizes frontiers based on a hybrid criterion. If the maximum semantic score among all frontiers (max s_sem_i) exceeds a threshold (τ_s), the frontier with the highest semantic score is chosen. Otherwise, if the VLM lacks sufficient task-related cues, the frontier maximizing the geometric coverage score (max s_geo_i) is selected to gain new information about under-observed regions.

### 5. Main Findings and Results

The efficacy of GSMem was evaluated through extensive experiments on two distinct benchmarks: Active Embodied Question Answering (A-EQA) and Multimodal Lifelong Navigation (GOAT-Bench).

#### 5.1 Active Embodied Question Answering (A-EQA)

*   **Performance:** GSMem achieved state-of-the-art performance on the A-EQA benchmark, which involves agents actively exploring unseen environments to answer queries. It demonstrated improvements over existing baselines, including Blind LLMs, LLMs with frame captions, standalone VLMs, and other VLM exploration methods such as Explore-EQA, ConceptGraphs (CG) with frontier snapshots, and 3D-Mem.
*   **Metrics:** GSMem attained an LLM-Match score of 55.4 and an LLM-Match SPL (Success weighted by Path Length) of 43.8, surpassing the closest VLM exploration baseline (3D-Mem) which scored 52.6 and 42.0 respectively.
*   **Analysis:** The performance gain was attributed to GSMem's dense geometric and visual representations, which provide richer visual evidence for reasoning. The ability to select optimal viewpoints for retrieved regions and the hybrid exploration strategy further contributed to improved visual coverage and higher-quality VLM inputs, leading to enhanced reasoning and efficiency.

#### 5.2 Multi-modal Lifelong Navigation (GOAT-Bench)

*   **Performance:** In the GOAT-Bench benchmark, which tests sequential target localization across multiple episodes in unseen scenes, GSMem exhibited substantial performance gains.
*   **Metrics:** GSMem achieved a Success Rate (SR) of 67.2 and a Success weighted by Path Length (SPL) of 46.9. This outperformed all tested baselines, including reinforcement learning-based methods (e.g., Modular GOAT, Modular CLIP on Wheels, SenseAct-NN) and VLM-based exploration methods (e.g., VLMnav, DyNaVLM, TANGO, MTU3D, 3D-Mem). The closest VLM exploration baseline, 3D-Mem, achieved 62.9 SR and 44.7 SPL.
*   **Analysis:** The larger performance improvement observed in lifelong navigation compared to A-EQA suggests that GSMem's persistent memory representation, which allows for robust retrieval and re-observation over extended interactions, is particularly beneficial for long-horizon tasks. The hybrid exploration strategy was noted for enabling more efficient exploration, as evidenced by the improved SPL metric.

#### 5.3 Case Analysis

Qualitative analysis demonstrated GSMem's robustness against limitations of discrete and view-dependent memories:

*   **Missing and Incorrect Detections:** Unlike baselines that failed due to missed object detections (e.g., "white robe," "ficus tree") or incorrect semantic identification (e.g., "white door" mistaken for "refrigerator"), GSMem successfully localized targets by querying its continuous language field based on semantic similarity, even when explicit object detections were absent or erroneous.
*   **View-Dependency and Resolution Limits:** In cases where static egocentric snapshots provided by baselines suffered from limited resolution or suboptimal perspective, hindering VLM reasoning, GSMem's optimal viewpoint selection and rendering capability provided VLMs with clearer visual evidence, enabling correct identification (e.g., "hanging clothes").

#### 5.4 Ablation Study

Ablation experiments confirmed the contribution of key components:

*   **CLIP Language Field:** Removal of the language field resulted in a notable drop in success rate, confirming its crucial role in open-vocabulary retrieval as a complement to object detection.
*   **Hybrid Exploration Strategy:** Disabling the hybrid strategy and relying solely on VLM-driven exploration significantly reduced SPL, indicating the importance of the coverage-aware component for exploration efficiency.
*   **Viewpoint Selection and Diffusion Enhancement:** Both optimal viewpoint selection and the single-step diffusion model for rendering enhancement contributed to improved success rates, by providing better-aligned and higher-quality visual inputs to the VLM.
*   **Hyperparameter Sensitivity:** The study investigated the impact of the semantic threshold (τ_s) for hybrid exploration and the number of top-K objects (K_obj) selected for rendering, identifying optimal ranges for these parameters to balance exploration and reasoning.

#### 5.5 Real-world Practicality

Runtime analysis of a multi-process setup, utilizing an offline Qwen3-VL-8B model and without single-step diffusion during rendering, indicated an average processing time of approximately 1.2 seconds per step on an RTX 4090 and H100 GPU combination. This suggests the framework's practical feasibility for deployment.

### 6. Significance and Potential Impact

The GSMem framework addresses a core challenge in embodied AI: the limitation of current spatial memory representations that lack post-hoc re-observability. By implementing 3D Gaussian Splatting (3DGS) as a persistent, continuous, and re-renderable spatial memory, the work equips embodied agents with a capability analogous to human mental recall, allowing them to synthesize novel views from previously explored regions without physical re-navigation.

This approach offers several significant contributions and potential impacts:

*   **Enhanced Spatial Reasoning and Recall:** The ability to render photorealistic novel views from optimal, previously unoccupied viewpoints provides VLMs with more precise and comprehensive visual evidence. This is expected to lead to more robust and accurate reasoning, especially in situations where initial observations were suboptimal or ambiguous.
*   **Robustness to Perception Failures:** The multi-level retrieval-rendering mechanism, which integrates both object-level scene graphs and semantic-level language fields, improves the agent's resilience to common perception system limitations. By allowing semantic querying of the continuous 3D language field, the agent can localize target regions even when explicit object detections are missed or incorrect, a frequent failure mode in real-world scenarios.
*   **Improved Exploration Efficiency:** The proposed hybrid exploration strategy, which intelligently combines VLM-driven semantic relevance with a 3DGS-based information gain objective, promotes a more balanced and efficient exploration process. This ensures that the agent not only prioritizes task-relevant areas but also comprehensively covers the environment, leading to a richer and more complete spatial memory. This efficiency is reflected in the improved SPL metrics.
*   **Advancement in Zero-Shot Embodied Tasks:** The framework demonstrates notable performance gains in both active embodied question answering and lifelong navigation, particularly in open-vocabulary and long-horizon tasks. This indicates progress towards more generalized and adaptive embodied agents that can operate effectively in unseen environments without extensive prior training.
*   **Foundation for Future Embodied AI Systems:** GSMem establishes a foundation for future embodied AI systems that require sophisticated spatial understanding, long-term memory, and adaptability. The continuous and re-renderable nature of the 3DGS memory could support more complex tasks beyond navigation, such as dexterous manipulation, human-robot interaction, and detailed scene understanding, where the precise context and appearance from arbitrary viewpoints are critical.
*   **Practical Applicability:** The runtime analysis suggests that, with suitable hardware and optimized VLM deployment, GSMem can operate at a practical speed, moving towards real-world deployment of such advanced embodied agents.

Overall, GSMem represents a step towards embodied agents that possess a more flexible and robust understanding of their environment, capable of addressing the challenges of complex 3D world interaction more effectively.
