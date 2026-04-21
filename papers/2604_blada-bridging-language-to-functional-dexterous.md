---
title: "BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields"
date: 2026-04-09
arxiv: "2604.08410v1"
venue:
status: to-read

abstract: "In unstructured environments, functional dexterous grasping calls for the tight integration of semantic understanding, precise 3D functional localization, and physically interpretable execution. Modular hierarchical methods are more controllable and interpretable than end-to-end VLA approaches, but existing ones still rely on predefined affordance labels and lack the tight semantic--pose coupling needed for functional dexterous manipulation. To address this, we propose BLaDA (Bridging Language to Dexterous Actions in 3DGS fields), an interpretable zero-shot framework that grounds open-vocabulary instructions as perceptual and control constraints for functional dexterous manipulation. BLaDA establishes an interpretable reasoning chain by first parsing natural language into a structured sextuple of manipulation constraints via a Knowledge-guided Language Parsing (KLP) module. To achieve pose-consistent spatial reasoning, we introduce the Triangular Functional Point Localization (TriLocation) module, which utilizes 3D Gaussian Splatting as a continuous scene representation and identifies functional regions under triangular geometric constraints. Finally, the 3D Keypoint Grasp Matrix Transformation Execution (KGT3D+) module decodes these semantic-geometric constraints into physically plausible wrist poses and finger-level commands. Extensive experiments on complex benchmarks demonstrate that BLaDA significantly outperforms existing methods in both affordance grounding precision and the success rate of functional manipulation across diverse categories and tasks. Code will be publicly available at this https URL."

website: 
code: https://github.com/PopeyePxx/BLaDA
openreview: 
issue: 19

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

# BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields

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

![Figure](https://arxiv.org/html/2604.08410v1/x1.png)

*Figure 1: Comparison of existing pipelines: (a) end-to-end VLA is data-hungry, black-box, and poor generalization; (b) affordance-based methods rely on predefined labels, limited 2.5D localization, and primitive control; (c) BLaDA (ours) uses a structured intermediate SS with 3D executable constraints for zero-shot, intent-conditioned execution.*

![Figure](https://arxiv.org/html/2604.08410v1/x2.png)

*Figure 2: Overview of BLaDA. The top illustrates the construction of knowledge-guided functionality prompting and example demonstrations of “Handover me the drill” and “Use the drill”. The bottom shows the overall pipeline, which consists of three stages: (1) Language parsing (blue): the KLP module parses the input instruction LL into structured manipulation primitive elements 𝒮=(ga,gr,gt,gf,κ,τ)\mathcal{S}=(g^{a},g^{r},g^{t},g^{f},\kappa,\tau); (2) 3D Gaussian reconstruction and localization (green): TriLocation reconstructs a semantic 3D Gaussian field from multi-view RGB observations and localizes three functional keypoints Pi​(x,y,z)P_{i}(x,y,z), conditioned on (ga,gr,κ,τ)(g^{a},g^{r},\kappa,\tau); (3) Dexterous manipulation (yellow): FKGT3D(+) generates relative hand–object contact poses and produces fine-grained dexterous control actions under semantic constraints (gt,gf)(g^{t},g^{f}), which are finally executed in the real world.*

![Figure](https://arxiv.org/html/2604.08410v1/x3.png)

*Figure 3: Extract verbs, intent phrases, and tool types from human natural language instructions LL, and classify them into specific task-intent priors and tool-topology priors.*

![Figure](https://arxiv.org/html/2604.08410v1/x4.png)

*Figure 4: Overview of the TriLocation. a. We design the HSE module (highlighted in yellow), consisting of Select and Context-Aware Cropping units to decouple object/part regions and resolve semantic drift. This enables the construction of a clean, high-precision 3D Gaussian semantic field for keypoint localization. b. The module computes the CLIP [27] similarity between gag^{a} and each Gaussian feature fif_{i} to locate the semantic anchor p1p_{1}. c. A lightweight MLP predicts two relative offsets Δ​p2\Delta p_{2} and Δ​p3\Delta p_{3}, forming the graspable triangle structure {p1,p2,p3}\{p_{1},p_{2},p_{3}\}, which is supervised by structure-aware losses based on edge lengths and internal angles.*

![Figure](https://arxiv.org/html/2604.08410v1/x5.png)

*Figure 5: Real-world experiment setting and 6 typical scenarios demonstration.*

![Figure](https://arxiv.org/html/2604.08410v1/img/2Dlocation.png)

*Figure 6: Relevance maps of given language instructions. We project the language-activated 3D Gaussian semantic features onto 2D images for visualization. The orange panels denote object-level relevance maps, while the green panels denote part-level relevance maps. Red rectangles highlight the erroneous or ambiguous responses of GraspSplats, and yellow ellipses indicate that our method produces more compact and complete response regions for local semantic parts.*

![Figure](https://arxiv.org/html/2604.08410v1/x6.png)

*Figure 7: Visualization of the effect of the local coordinate system on 3D functional keypoint localization. Each example presents, in order: the input image, a 3D visualization of the local coordinate system (red/green/blue indicate the x/y/zx/y/z axes, where blue denotes the approach axis zz and green denotes the grasp axis yy), the predicted three-point structure under the local-coordinate constraint, and the results without this constraint (red boxes).*

![Figure](https://arxiv.org/html/2604.08410v1/x7.png)

*Figure 8: Dexterous grasping demonstration workflow based on 3D reconstructed points. Left of the dashed line: predicted reference points. Right of the dashed line, in sequence: initial state; pose alignment; coarse grasping based on gtg^{t}; tightening non-gfg^{f} fingers; and gfg^{f} fingers exerting grg^{r} force (Note that, except for the finger-force actuation, the post-grasp motions are completed by demonstration).*

![Figure](https://arxiv.org/html/2604.08410v1/x8.png)

*Figure 9: Hyperparameter analysis of α\alpha and γ\gamma. The optimal configuration is highlighted.*

## LLM Summary

### 1. Authors and Institution(s)

The research paper "BLaDA: Bridging Language to Functional Dexterous Actions within 3DGS Fields" was authored by Fan Yang, Wenrui Chen, Guorun Yan, Ruize Liao, Wanjun Jia, Dongsheng Luo, Kailun Yang, Zhiyong Li, and Yaonan Wang.

The primary affiliation for the authors is the School of Artificial Intelligence and Robotics, Hunan University, Changsha 410012, China. Additionally, Wenrui Chen, Kailun Yang, Zhiyong Li, and Yaonan Wang are affiliated with the National Engineering Research Center of Robot Visual Perception and Control Technology, Hunan University, Changsha 410082, China. Wenrui Chen is designated as the corresponding author.

### 2. How this Work Fits into the Broader Research Landscape

The work presented in this paper addresses the domain of functional dexterous grasping for robotic manipulation in unstructured environments. This field requires the integration of semantic understanding, precise 3D localization, and physically interpretable action execution.

Early research in functional grasping often relied on predefined task intentions or affordance semantics, typically assuming that functional regions were precisely segmented or localized. These methods often faced challenges in complex real-world environments due to their reliance on idealized perception systems. Some approaches sought to extract manipulation patterns directly from visual data, with affordance-based methods identifying key contact areas. However, these systems frequently utilized independent general-purpose grasping models, with affordance perception serving primarily to narrow down candidate regions rather than providing deterministic pose solutions for complex dexterous tasks. A key limitation was often the confinement of affordance perception to single-object localization in limited 2.5D scenes and insufficient consideration of subsequent intent execution.

More recent developments have seen the emergence of Large Language Models (LLMs) which have enabled new directions in robotic manipulation. End-to-end Vision-Language-Action (VLA) models, for instance, can directly map language and perception to actions. However, these models typically require extensive data, exhibit limited interpretability, and can be brittle when encountering distribution shifts. Hierarchical pipelines, which separate high-level planning from low-level control, offer improved modularity. Yet, these methods often focus on basic grasping and frequently lack the tight semantic-pose coupling and finger-level precision necessary for advanced functional dexterous grasping. Approaches attempting functionality-aware execution, such as SayFuncGrasp, have relied on learned planners for finger-level control, potentially leading to weakly constrained and training-distribution-sensitive semantics-to-action mappings.

BLaDA positions itself within this landscape by proposing a modular, zero-shot, language-driven framework. It seeks to bridge language understanding with functional dexterous actions in 3D Gaussian Splatting (3DGS) fields. By constructing a structured intermediate space that unifies language semantics, visual geometry, and motor control, the work aims to overcome the limitations of both data-hungry, black-box end-to-end VLA models and existing hierarchical approaches that lack the required precision and interpretability for functional dexterous manipulation in open-vocabulary, 3D environments. This approach specifically focuses on creating an interpretable reasoning chain, enabling object-part hierarchical localization in complex 3D scenes, and generating intent-conditioned finger-level actions.

### 3. Key Objectives and Motivation

The primary objective of this research is to enable robots to perform functional dexterous grasping in unstructured environments through a tight integration of semantic understanding, precise 3D functional localization, and physically interpretable execution. This goal is motivated by several challenges observed in the existing research landscape:

1.  **Limited Intent Understanding:** Current robotic manipulation systems often struggle with open-domain natural-language commands due to closed instruction vocabularies and rigid semantic representations. This limitation restricts their generalization capabilities to diverse and unforeseen tasks. The motivation here is to leverage the generalization and reasoning capabilities of foundation models to interpret open-vocabulary instructions more effectively.

2.  **Missing Perceptual Dimensionality:** Existing affordance perception methods are largely confined to single-object localization in limited 2.5D scenes. This restricts their applicability in complex, cluttered 3D environments where precise spatial reasoning for pose-consistent manipulation is required. The research aims to move beyond 2D or sparse-3D affordance prediction to support more robust and precise spatial reasoning in continuous 3D scene representations.

3.  **Limited Action Execution and Interpretability:** Many motion planning approaches terminate at basic "grasping" without sufficient consideration for subsequent task execution, or they rely on opaque, end-to-end mappings from semantics to actions. This lack of transparency can hinder debugging, control, and generalization. A core motivation is to avoid black-box mappings and instead enable physically interpretable and highly controllable execution, particularly for fine-grained, finger-level manipulation.

To address these motivations, the study defines specific objectives:
*   **Design a unified protocol:** Develop a framework that bridges language, geometry, and control for generalizable and executable grasp planning.
*   **Support pose-consistent, precise spatial reasoning:** Implement a method for functional region localization that operates within a continuous 3D scene representation (3D Gaussian Splatting) and can handle object-part hierarchies.
*   **Enable physically interpretable and highly controllable execution:** Create a mechanism that decodes semantic-geometric constraints into precise wrist poses and finger-level commands, ensuring physical plausibility and fine-grained control.
*   **Establish an interpretable reasoning chain:** From natural-language instructions to executable control, facilitating understanding and reliability.
*   **Zero-shot capability:** Achieve functional dexterous grasping without requiring task-specific policy training for semantic grounding.

### 4. Methodology and Approach

The proposed framework, BLaDA (Bridging Language to Dexterous Actions in 3DGS fields), is a modular, zero-shot, language-driven paradigm. It grounds open-vocabulary instructions into explicit perceptual and control constraints through a three-stage pipeline.

**Problem Formulation:** The framework takes a natural language instruction *L* and a collection of RGB-D images *Ω* as input. It aims to output a set of three 3D keypoint coordinates *P* = {p1, p2, p3} on the target object and a grasp configuration *G* = (R, T, J, F), which defines the relative pose, joint state of the robotic hand, and the force for execution.

**Pipeline Overview:**
1.  **Language Parsing (Knowledge-guided Language Parsing - KLP):** This module processes the input instruction *L* to extract a structured sextuple *S* = (g_a, g_r, g_t, g_f, κ, τ) of manipulation primitives.
2.  **3D Gaussian Field Reconstruction and Localization (TriLocation):** This module reconstructs a 3D Gaussian field from multi-view RGB observations, incorporating object-part hierarchical semantic information. It then localizes the three functional keypoints *P* within this field, conditioned on the semantic anchors (g_a, g_r, κ, τ) from the KLP module.
3.  **Dexterous Manipulation (3D Keypoint Grasp Matrix Transformation Execution - KGT3D+):** This module translates the semantic-geometric constraints into an optimal wrist pose and fine-grained finger-level commands, considering grasp type *g_t* and force parameter *g_f*.

**Detailed Breakdown of Modules:**

**A. Knowledge-guided Language Parsing (KLP):**
The KLP module leverages a large language model augmented with a structured knowledge graph to parse unstructured natural language instructions into a six-tuple *S*. This design aims to enhance semantic consistency and robustness in open-vocabulary settings.
*   **Core Primitives:** The parsing scaffold includes four core manipulation primitives:
    *   **g_a (Grasp Affordance):** Specifies spatial reachability of usable object regions.
    *   **g_r (Finger-Role Assignment):** Clarifies the functional logic of each finger during contact.
    *   **g_t (Grasp Type/Gesture):** Corresponds to coarse hand postures and associated joint-angle values.
    *   **g_f (Force Level):** Sets the interaction strength.
*   **Disambiguation Priors:** To resolve pose ambiguity, two additional priors are introduced:
    *   **τ (Tool-Topology Prior):** Categorizes the target object into four classes (axial-rod, lateral-handle, knob/wheel, slab/surface) based on geometric cues and human operation habits.
    *   **κ (Task-Intent Prior):** Normalizes verb phrases into four atomic task types (press, click, open, hold) to ensure physically unique and feasible grasp combinations.
*   **Prompt Design:** A carefully crafted prompt guides the LLM, comprising: (i) role specification (agent as embodied intelligence), (ii) structured injection of grasp, task, and tool-topology taxonomies from the F2F knowledge base, and (iii) in-context examples demonstrating the desired six-tuple output format and reasoning patterns.

**B. Triangular Functional Point Localization (TriLocation):**
This module is responsible for constructing a multi-level semantic 3D Gaussian field and precisely localizing three contact keypoints {p1, p2, p3} that form a triangular structure on the object, directly constraining the subsequent hand-object contact pose.
*   **Constructing 3D Gaussians with Object–Part Features (Hierarchical Semantic Extraction - HSE):**
    *   **Multi-granularity semantic mask generation:** YOLO detects bounding boxes, and SAM generates masks. A `select` module categorizes masks into object-level (M_o) and part-level (M_p) based on an area-ratio consistency hyperparameter *α*.
    *   **Context-aware part feature extraction:** For object-level features, a dense feature map is extracted from the full image. For part-level features, a `context-aware cropping` mechanism expands the bounding box by a padding ratio *γ* before feeding it to a CLIP encoder, mitigating semantic drift. Mask-guided projection then maps central features back to the specific SAM mask for purity.
    *   **Feature splatting and hierarchical distillation:** The scene is represented by 3D Gaussian primitives, each with a low-dimensional latent feature. Volumetric rendering obtains a rendered latent feature, which a shallow MLP decodes into object-level, part-level, and DINO-v2 branches.
    *   **Background consistency constraint:** A hard mask-guided constraint sets ground-truth feature vectors to zero for pixels not belonging to detected masks, suppressing background responses.
*   **Localization of Three Functional Keypoints:**
    *   **Semantic Anchor (p1):** The `grasp affordance` (g_a) from KLP is converted into a CLIP query vector. This vector is compared with the semantic feature of each Gaussian to compute similarity. Gaussian points with high similarity are clustered, and the centroid of the highest confidence cluster is selected as p1.
    *   **Lateral Support (p2) and Wrist Support (p3):** The `functional finger` (g_r) from KLP informs a `Hand three-point model`. A `Map` module then rigidly aligns this predefined hand template to the object space, using p1 as the reference. The `task-topology local coordinate frame` (defined below) guides the relative placement of p2 and p3 based on predefined edge lengths and angles.
*   **Constructing the Local Coordinate Frame:** This addresses pose ambiguity by providing a task-consistent geometric reference.
    *   **Coupling:** The task-intent prior *κ* and tool-topology prior *τ* are coupled to define a primary task axis (ˆz) and a hand orientation axis (ˆy) (e.g., for `Hold` and `axial-rod`, ˆz is the gravity direction and ˆy is the structural axis).
    *   **Geometric Primitive Estimation:** RANSAC is used to extract structural axes (rods, handles, knob rotation axes). PCA estimates surface normals and major in-plane axes for slab-like structures.
    *   **Frame Construction:** ˆy is projected onto the plane orthogonal to ˆz to ensure stability. The final right-handed frame (ˆx, ˆy, ˆz) is completed with ˆx = ˆy × ˆz. This frame provides a consistent reference for p1, p2, and p3.

**C. Keypoint-based Grasp Matrix Transformation in 3D for Dexterous Execution (KGT3D+):**
This module, an extension of the KGT method, generates physically executable 3D grasp control commands by converting the three localized keypoints into a precise wrist pose and finger-level actions.
*   **Palm Pose Construction:** Given {p1, p2, p3}, p3 is set as the palm reference point. A right-handed coordinate frame is constructed: ⃗z is defined along the vector from p3 to p1, ⃗y is derived from the cross product of (p2-p3) and ⃗z, and ⃗x is the cross product of ⃗y and ⃗z. This frame directly defines the wrist rotation matrix *R* and translation vector *T* (where T = p3).
*   **Finger Joint and Force Control:** The `grasp type` (g_t) and `force label` (g_f) from KLP are fed into a predefined functional grasp library (F2F). This library maps these semantic inputs to the joint configuration *J* (angles of the robotic hand) and per-finger force profile *F* for execution.

### 5. Main Findings and Results

The efficacy of BLaDA was evaluated through extensive experiments across three key components: language parsing, 3D keypoint localization, and real-world functional manipulation.

**A. KLP-Based Language Parsing Evaluation:**
The KLP module's ability to extract manipulation elements was assessed using Language Reasoning Accuracy (LRA) across three LLMs (ChatGPT4.0, DeepSeekv3, Gemini2.5), both with and without KLP.
*   **Consistent Improvement:** KLP significantly enhanced LRA for all LLMs, demonstrating an average relative gain of approximately +21.5%. For instance, ChatGPT4.0's average LRA increased from 0.508 to 0.753. This indicates KLP's role as a robust, plug-and-play reasoning module.
*   **Task- and Function-Related Gains:** The most substantial improvements were observed in `grasp type` (g_t) and `functional finger` (g_r) elements. ChatGPT4.0's g_t accuracy improved from 0.13 to 0.81, highlighting the importance of structured knowledge for precise functional reasoning.
*   **Overall Performance:** ChatGPT4.0 with KLP achieved the highest average LRA of 0.753, performing best in four out of six elements, suggesting its strength in leveraging structured knowledge for manipulation-oriented language understanding.

**B. Performance Evaluation of TriLocation:**

1.  **Qualitative Comparison of 2D Part-level Feature Extraction:**
    *   Compared to GraspSplats [28], BLaDA's Hierarchical Semantic Extraction (HSE) module demonstrated improved semantic feature rendering. GraspSplats often suffered from semantic "cross-talk" at the object level (activating irrelevant regions) and a "holistic override" effect at the part level (part queries diffusing to the entire object).
    *   BLaDA, in contrast, delineated clearer object and part contours with more compact and complete responses for fine-grained parts, attributed to HSE's explicit filtering and decoupling of object- and part-level features.

2.  **Qualitative Visualization of Local Coordinate System:**
    *   Visualization demonstrated that without the proposed local coordinate system, 3D functional keypoint localization often yielded disordered triangular structures and semantic misalignment among the three keypoints. This led to unreliable approach and interaction directions.
    *   With the local coordinate system, BLaDA consistently learned a structure-adaptive local coordinate system within the 3D Gaussian field, enabling the three keypoints to maintain a stable geometric triangle and a semantically consistent spatial configuration across varying viewpoints, object topologies, and task semantics.

3.  **Quantitative Evaluation of 2D Part Localization:**
    *   On metrics like Mean Absolute Error (MAE), Precision Energy (P_En), KL Divergence (KLD), Similarity (SIM), and Normalized Scanpath Saliency (NSS), BLaDA showed significant improvements over GraspSplats [28].
    *   For larger components (e.g., "Hammer Handle"), P_En increased by 113.1% and NSS by 110.7%, indicating highly focused part-level heatmaps. For fine-grained parts (e.g., "Pink Button"), BLaDA maintained superior MAE and KLD scores. These results confirm the HSE module's effectiveness in enhancing localization precision and spatial consistency.

4.  **Quantitative Evaluation of 3D Functional Keypoint Localization (LSR):**
    *   TriLocation achieved an overall Localization Success Rate (LSR) of 68.75% across 14 task-tool combinations in 6 real-world scenes.
    *   The baseline MKA [10], which requires manual point-clicking and lacks open-vocabulary semantic query, achieved an LSR of 22.5%, limited by susceptibility to depth errors.
    *   **Ablation Studies:**
        *   Removing the task-topology local coordinate frame constraint caused the mean LSR to drop sharply to 25%, with "Press" and "Open" tasks failing (0% success rate), highlighting its necessity for orientation resolution.
        *   Removing the HSE module decreased LSR to 53.13%, as fine-grained part features became blurred by global object context. These studies underscore the importance of hierarchical mask constraints and task-topology reasoning for precise 3D keypoint localization.

5.  **Hyperparameter Analysis:** The optimal configuration for the HSE module was found to be an area-ratio consistency *α* = 0.1 and padding ratio *γ* = 0.4. This configuration yielded the lowest MAE and highest P_En for fine-grained queries, indicating that moderate padding provides crucial context while overly restrictive or large ratios degrade performance.

**C. BLaDA Performance in Real-world Environments:**

1.  **Qualitative Demonstrations:** BLaDA successfully executed various natural-language tasks in real-world environments, ranging from simple object relocation ("Remove the spraybottle") to functional tool manipulation ("Use the spraybottle to water the flowers", "Pick up the hammer and hammer the nail", "Pick up the electric drill and handover it to me"). The system demonstrated stable extraction of "task-function-part-finger" elements and their grounding into topology/semantics-constrained grasps and functional actions.

2.  **Comparative Analysis of Functional Grasp Success Rate (FSR):**
    *   BLaDA was compared against MKA [10] and a Diffusion Policy extension (DP*) on two task-tool combinations ("hold the spray bottle" and "press the spray bottle").
    *   For "hold the spray bottle", BLaDA achieved 80% FSR, outperforming MKA (40%) and DP* (50%).
    *   For the more challenging "press the spray bottle", BLaDA achieved 30% FSR, while both MKA and DP* achieved 10%.
    *   MKA's limitations were attributed to its reliance on structured single-object scenes, leading to instability in complex environments. DP* demonstrated sensitivity in fine contact alignment and cross-scene generalization, requiring extensive task-specific demonstrations.
    *   These results validate BLaDA's robustness, precision, and generalization capability in real-world tasks, demonstrating its ability to map open-domain instructions into executable functional actions in a zero-shot manner, reducing data collection and training costs.

### 6. Significance and Potential Impact

This research presents a framework, BLaDA, that addresses several challenges in robotic functional dexterous manipulation, demonstrating a notable advancement in the field.

The primary significance lies in its **interpretable, zero-shot, language-driven approach** to bridging high-level semantic instructions with low-level dexterous actions. Unlike data-intensive, black-box end-to-end VLA models, BLaDA's modular architecture provides a clear reasoning chain, which can enhance robustness, facilitate debugging, and improve transparency in robotic systems. This interpretability is crucial for developing trustworthy and predictable robots that operate in human environments.

The use of **3D Gaussian Splatting as a continuous scene representation**, combined with a novel Hierarchical Semantic Extraction (HSE) strategy and Triangular Functional Point Localization (TriLocation), significantly improves the precision and spatial consistency of functional region localization. This capability to delineate fine-grained object parts and establish stable geometric constraints in 3D space is essential for complex manipulation tasks that require accurate contact points and orientations, moving beyond the limitations of 2.5D or sparse 3D representations.

Furthermore, the introduction of a **structured semantic-geometric-control intermediate representation** (the sextuple produced by KLP) serves as a universal interface, enabling cross-task transfer under open-vocabulary instructions. This generalized understanding of intent and object properties allows the system to adapt to new tasks and objects without specific retraining, significantly reducing the data collection and training overhead typically associated with robotic learning.

The **pose-level spatial constraints and physically interpretable execution mechanism** (KGT3D+) allow for mapping geometric cues into meaningful action transformations, including wrist poses and finger-level commands with specified forces. This fine-grained control is critical for executing functional interactions, such as pressing buttons, turning knobs, or operating tools, which go beyond basic grasping.

The **experimental validation** across complex benchmarks, demonstrating superior functional success rates and pose-consistency metrics in a zero-shot setting, indicates the practical viability and generalization capability of BLaDA. This represents a step towards robots that can operate more autonomously and effectively in diverse, unstructured human environments.

Potential impacts of this work include:
*   **Advancements in Humanoid Robotics:** Enabling humanoid robots to perform a wider range of dexterous tasks, similar to human capabilities, by better interpreting and executing functional grasps.
*   **Enhanced Robotic Assistants:** Developing more capable assistive robots for home and industrial settings, capable of manipulating everyday objects and tools based on natural language commands.
*   **Reduced Development Costs:** The zero-shot and data-efficient nature of the framework could substantially lower the costs and time associated with deploying robots for new tasks, fostering wider adoption of robotic manipulation.
*   **Foundation for Future Research:** Providing a robust framework for integrating language understanding, 3D vision, and dexterous control, which can be extended to incorporate more advanced sensory modalities and interaction paradigms.

Future research directions, as identified by the authors, include enhancing part-level semantic density in 3DGS fields to mitigate semantic ambiguities (e.g., misinterpreting tool parts as anatomical terms) and integrating tactile sensors for closed-loop adjustment. These advancements could further improve the system's robustness to unexpected object displacements or slippage during dynamic human-robot interaction.
