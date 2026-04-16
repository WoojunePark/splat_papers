---
title: "ReLaGS: Relational Language Gaussian Splatting"
date: 2026-03-18
arxiv: "2603.17605"
venue:
status: to-read

abstract: "Achieving unified 3D perception and reasoning across tasks such as segmentation, retrieval, and relation understanding remains challenging, as existing methods are either object-centric or rely on costly training for inter-object reasoning. We present a novel framework that constructs a hierarchical language-distilled Gaussian scene and its 3D semantic scene graph without scene-specific training. A Gaussian pruning mechanism refines scene geometry, while a robust multi-view language alignment strategy aggregates noisy 2D features into accurate 3D object embeddings. On top of this hierarchy, we build an open-vocabulary 3D scene graph with Vision Language derived annotations and Graph Neural Network-based relational reasoning. Our approach enables efficient and scalable open-vocabulary 3D reasoning by jointly modeling hierarchical semantics and inter/intra-object relationships, validated across tasks including open-vocabulary segmentation, scene graph generation, and relation-guided retrieval. Project page: this https URL"

website: https://dfki-av.github.io/ReLaGS
code: https://github.com/dfki-av/ReLaGS
openreview:
issue: 13

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

# ReLaGS: Relational Language Gaussian Splatting

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

![Figure](https://arxiv.org/html/2603.17605v1/x1.png)

*Figure 1: Relational Language Gaussian Splatting. We build a platform with multi-hierarchical language Gaussian field and open-vocabulary 3D scene graph, to support various tasks such as object selection via click, open vocabulary 3D object segmentation across semantic granularity, spatial relationship reasoning between objects and querying object with relation-guidance.*

![Figure](https://arxiv.org/html/2603.17605v1/x2.png)

*Figure 2: ReLaGS Overview. Given a reconstructed Gaussian scene, redundant primitives are first pruned to improve geometric accuracy. Heuristic clustering under multi-level SAM supervision then forms a hierarchical scene structure, where each cluster is assigned a CLIP-based language feature with outlier rejection. Finally, open-vocabulary inter- and intra-object scene graphs are obtained either by lifting LLM-derived relations for semantic diversity or by using a pretrained graph network for efficient offline inference.*

![Figure](https://arxiv.org/html/2603.17605v1/x3.png)

*Figure 3: Illustration of proposed two improvement methods for hierarchical scene construction and two example scene graphs. (a): Low contribution Gaussian points (red) are removed to improve scene geometry. (b): Outlier features (e.g., due to occluded or inconsistent masks) are filtered before aggregation, producing a more coherent and consistent embedding for the target. (c): The spatial relationships are predicted by our GNN. (d): The more semantic-enriched relationship lifted with LLM, the root object is marked as -1.*

![Figure](https://arxiv.org/html/2603.17605v1/x4.png)

*Figure 4: Qualitative results of open vocabulary object segmentation. We show results on LERF dataset for segmentation mask on 2D view. With multi-hierarchy querying search and 3D scene graph for relation guidance, our method shows strong improvement against THGS.*

![Figure](https://arxiv.org/html/2603.17605v1/x5.png)

*Figure 5: Qualitative results on LERF, ScanNet++, ScanNet and 3D-OVS.*

![Figure](https://arxiv.org/html/2603.17605v1/x6.png)

*Figure 6: Visualization of multi-hierarchy scene reconstruction on LERF and 3D-OVS datasets.*

![Figure](https://arxiv.org/html/2603.17605v1/x7.png)

*Figure 7: Examples of our SoM+LLM scene graph annotation on 2D images from 3DSSG dataset.*

## LLM Summary

## Report on "ReLaGS: Relational Language Gaussian Splatting"

### 1. Authors and Institution(s)
The authors of this paper are Yaxu Xie, Abdalla Arafa, Alireza Javanmardi, Christen Millerdurai, Shaoxiang Wang, Alain Pagani, and Didier Stricker from the German Research Center for Artificial Intelligence (DFKI), with affiliations also at RPTU University Kaiserslautern-Landau for Yaxu Xie, Abdalla Arafa, Shaoxiang Wang, and Didier Stricker. Jia Cheng Hu is affiliated with the University of Modena and Reggio Emilia. Yaxu Xie and Abdalla Arafa contributed equally to this work.

### 2. How this work fits into the broader research landscape
The research presented in "ReLaGS: Relational Language Gaussian Splatting" operates within the domain of 3D scene understanding, specifically building upon recent advancements in neural radiance fields (NeRF) and 3D Gaussian Splatting. These representations have enabled high-fidelity 3D reconstruction but traditionally lack semantic information, hindering high-level reasoning.

A significant development in this area is "language field distillation," which injects vision-language priors from 2D foundation models (e.g., CLIP, SAM) into 3D representations. This transformation allows for open-vocabulary 3D querying and tasks such as segmentation and language-guided navigation. However, prior language field distillation methods often suffer from limitations:
*   **Single Semantic Granularity**: They typically operate at an object-centric level, failing to represent finer part-level details or broader scene context.
*   **Lack of Relational Context**: They do not inherently model inter-object spatial or semantic relationships, making queries like "cup next to the laptop" challenging or impossible.
*   **Computational Cost**: Some approaches that attempt to embed relational context (e.g., RelationField, SplatTalk) are computationally intensive, involving per-scene training or expensive tokenization and fine-tuning.

Concurrently, the field of 3D Scene Graphs (3DSSG) aims to represent 3D scenes as structured graphs, linking objects, their attributes, and relationships. While many 3DSSG methods are limited to closed-set categories or rely on pre-segmented point clouds, recent efforts have moved towards open-vocabulary 3DSSG by integrating vision-language models. However, existing open-vocabulary 3DSSG methods also face challenges, such as reliance on costly LLM inference (ConceptGraphs), scene-specific training (GaussianGraph), or high computational overhead for learning relation fields (RelationField).

ReLaGS positions itself at the intersection of these two areas by seeking to overcome the limitations of both language-distilled 3D fields and current 3DSSG approaches. It aims to achieve multi-level scene representations (part-object-scene hierarchy) and explicit relational 3D scene graphs within a unified, computationally efficient, and training-free framework based on Gaussian Splatting. The work contributes to developing 3D representations that support more comprehensive and structured reasoning in open-vocabulary settings.

### 3. Key objectives and motivation
The primary objective of ReLaGS is to develop a unified framework that enables both multi-hierarchical semantic understanding and relational reasoning within 3D Gaussian fields, without requiring scene-specific training. This objective is motivated by several identified limitations in existing 3D scene understanding methods:

**1. Limited Semantic Expressiveness in Existing Language Fields:**
Current language field distillation methods, while enabling open-vocabulary querying, often operate with a "flat" semantic representation. This means they can identify objects but struggle with:
*   **Multi-granularity Queries:** They cannot differentiate between an entire object (e.g., "laptop") and its constituent parts (e.g., "keyboard of the laptop"). Queries for parts often result in the segmentation of the whole object.
*   **Relational Queries:** They lack the capability to understand or process queries involving spatial or functional relationships between objects (e.g., "select the cup next to the laptop"). Their features are typically confined within individual entities, providing no context on inter-entity relationships.

**2. Lack of Hierarchical Organization:**
Existing methods typically assign semantic features to individual Gaussians or object-level clusters without a structured hierarchy. This absence of a nested abstraction (from sub-part to part to object) limits their ability to provide comprehensive and structured 3D scene understanding, making it difficult to link fine-grained details to broader contextual relationships.

**3. Computational and Memory Costs of Prior Relational Methods:**
Attempts to embed relational context into radiance fields, such as RelationField, often involve computationally heavy volumetric rendering pipelines or scene-specific training. These approaches can be time-consuming (e.g., hours of training) and memory-intensive, making them impractical for large-scale deployment or real-time applications.

**4. Weak Language Registration and Geometric Inconsistencies:**
Methods that group Gaussians and register 2D language features often suffer from inconsistent Segment Anything Model (SAM) masks and noisy CLIP features across different views. This leads to unreliable language embeddings for 3D objects and fragmented or inaccurate object-level clusters, which in turn compromises the quality of any subsequent relational reasoning.

To address these motivations, ReLaGS aims to:
*   Construct a **hierarchical language-distilled Gaussian scene** that captures semantics at multiple granularities, from sub-parts to full objects.
*   Build an **explicit open-vocabulary 3D scene graph** on top of this hierarchy, representing inter- and intra-object relationships.
*   Achieve this in an **optimization-free framework** that is efficient and scalable, avoiding costly per-scene training.
*   Improve the robustness of language feature lifting and geometric integrity through novel mechanisms to ensure **accurate object segmentation and language registration**.
*   Enable **structured causal reasoning** in 3D by jointly modeling hierarchical semantics and inter/intra-object relationships.

### 4. Methodology and approach
ReLaGS integrates multi-hierarchical scene representation and relational reasoning within a 3D Gaussian field, employing a training-free pipeline. The approach is organized into three main stages: multi-hierarchy Gaussian representation construction, enhanced language lifting, and explicit 3D scene graph generation.

**4.1. Multi-Hierarchy Gaussian Representation**
The framework starts with a reconstructed 3D Gaussian field, where each Gaussian $G_i$ encodes spatial and radiance attributes. A hierarchical representation is constructed with $L$ abstraction levels, $S^{(1)}, \ldots, S^{(L)}$, where $S^{(l)}$ is a set of clusters at level $l$. Each Gaussian is assigned to a cluster at each level, forming a nested hierarchy where lower levels (e.g., $S^{(2)}$ for parts) are nested within higher levels (e.g., $S^{(3)}$ for complete objects). Each cluster $S^{(l)}_k$ is assigned a language-aligned embedding $f^{(l)}_k \in \mathbb{R}^d$.

To establish consistent pixel-to-Gaussian correspondence for tasks like instance segmentation and lifting 2D annotations, a rasterization process is used. For each pixel, the dominant Gaussian $G^*_{(u,v)}$ (the one with maximum contribution weight) is identified, providing a reliable 2D-3D mapping that extends to clusters.

**4.2. Improving Construction and Language Lifting of Hierarchical Scene**
ReLaGS builds upon the THGS method for hierarchical Gaussian field organization but introduces two enhancements to improve geometric and semantic quality:

*   **Maximum Weight Pruning (MWP)**: The initial Gaussian field often contains "floaters" – Gaussians with negligible visual impact across views, which can lead to noisy object clusters and inaccurate boundaries. MWP addresses this by removing Gaussians whose maximum contribution weight across all camera views, $\omega^{max}_i$, falls below a small threshold $\tau_{contrib}$. This step refines scene geometry, improves boundary integrity, and enhances the stability of the semantic hierarchy before clustering.

*   **Robust Outlier-Aware Feature Aggregation (ROFA)**: Multi-view language feature aggregation (e.g., CLIP features) can be compromised by inconsistencies arising from erroneous SAM masks or extreme viewpoints. Directly averaging features makes object embeddings sensitive to these outliers. ROFA mitigates this by filtering inconsistent features. For each object, the semantic consistency of its CLIP features from different views is measured by their mean cosine similarity $s_i$. These scores are then Z-score normalized ($z_i$), and features with $z_i < -\tau_{lang}$ (low-similarity outliers) are removed. The final object-level embedding is computed by averaging the remaining filtered features, yielding more reliable language-aligned representations.

**4.3. Relation Lifting and Prediction**
An explicit 3D scene graph is constructed on top of the hierarchical Gaussian scene. At the highest level $L$, an inter-object graph $H^{(L)}_{3D}$ captures relationships between complete objects. At lower levels $l < L$, intra-object graphs $H^{(l)}_{3D,intra}$ describe relationships among parts within the same object. Two complementary methods are proposed for building these relational edges:

*   **3D Consistent Relation Lifting from LLM Annotation**: This method leverages multimodal Large Language Models (LLMs) for open-vocabulary relational annotations. Instead of relying on potentially inconsistent per-frame SAM masks, ReLaGS renders view-consistent cluster ID maps from its hierarchical Gaussian scene. These cluster masks are then overlaid with numeric marks for Set-of-Mark (SoM) prompting, allowing a Multimodal LLM (e.g., GPT-4V, GPT-4o) to infer textual predicates ⟨subject, predicate, object⟩ between marked object pairs in 2D. Since masks correspond to 3D-consistent cluster IDs, these 2D annotations are directly lifted into 3D. The top-$k_p$ frequent predicates for each edge are encoded using Jina-Embedding-V3 and averaged to form the lifted relational embedding.

*   **Relation Prediction with GNN**: To provide broader coverage and efficiency, a lightweight pretrained residual Graph Neural Network (GNN) is employed. A neighboring graph $H'$ is first constructed by connecting object nodes within a fixed distance threshold. The GNN $F_\theta$ then predicts relation embeddings $\hat{f}_{ij}$ for these edges, taking as input geometry-language fused node embeddings of source and destination objects, along with an initial edge feature. Node features are 19-dimensional geometric descriptors (center, orientation, scale, mass center) concatenated with CLIP features. Edge features are built from relative displacement, distance, direction, and OBB overlap cues. The GNN uses an edge-aware graph transformer design, where edge features modulate attention and are iteratively refined. The GNN is pretrained on the 3RScan dataset using a multi-positive contrastive learning objective, aligning predicted embeddings with Jina-Embedding-V3. This pretrained model generalizes to Gaussian scenes without fine-tuning due to representation-independent geometric descriptors and modality-agnostic language embeddings.

**4.4. Applications: Hierarchical and Relational Reasoning in 3D**
ReLaGS enables two primary forms of structured reasoning:

*   **Language-based Multi-hierarchy Querying**: This allows users to query for either entire objects or their parts using natural language. A tree-searching method computes cosine similarity between a text query's CLIP embedding and per-cluster features across hierarchy levels. The search descends to child clusters only if they exhibit higher similarity, adaptively matching query granularity. It also identifies multiple relevant matches by detecting significant drops in similarity scores among ranked candidates. The resulting union of Gaussians forms an adaptive segmentation mask.

*   **Language-Triplet Querying on 3D Scene Graph**: This extends querying to handle relationship-based queries in the form of ⟨subject, predicate, object⟩. Subject and object candidates are identified using the multi-hierarchy querying procedure. Their relationships are then evaluated by comparing the corresponding scene graph edge embeddings to the predicate embedding from the query in the Jina embedding space. Candidate pairs are ranked based on subject-text alignment, object-text alignment, and predicate-relation alignment. The Gaussians associated with the highest-ranked subject candidates are returned.

### 5. Main findings and results
The experimental evaluation of ReLaGS focused on 3D scene graph prediction, relationship-guided 3D object segmentation, and open-vocabulary object segmentation.

**5.1. 3D Scene Graph Prediction**
On the RIO10 subset of the 3DSSG dataset, ReLaGS demonstrates performance in 3D scene graph prediction. As shown in Table 1, ReLaGS (pred.), which uses the pretrained GNN, achieves a Recall@3 of 0.79 and Recall@5 of 0.87 for relationship prediction. This represents an improvement of 0.03 for R@3 and 0.05 for R@5 over RelationField, the previous baseline in the "scene agnostic" category. While its object Recall@5 and R@10 are slightly lower (0.68 and 0.79) compared to RelationField (0.69 and 0.80), ReLaGS maintains comparable object recognition. The VLM-based relation lifting (Ours VLM) shows lower performance (0.10 R@3, 0.35 R@5) due to limitations in spatial reasoning from 2D images. ReLaGS also demonstrates efficiency, constructing a scene graph in under 15 minutes and rendering at over 200 fps, compared to RelationField's hours of training and below 10 fps rendering, and is 4.7x faster and 7.6x more memory efficient (Table 7).

**5.2. Open Vocabulary Instance Segmentation with Relationship Guidance**
On the ScanNet++ dataset for relationship-guided 3D instance segmentation, ReLaGS achieved a mean IoU (mIoU) of 0.56 (Table 2). This performance exceeds all compared methods, including the training-based RelationField (0.53) and other language field distillation methods. The results indicate that ReLaGS’s multi-hierarchical scene representation and graph-based relational reasoning facilitate effective inference of spatial relationships from 3D structure. The ablation study revealed that removing the multi-hierarchy (w/o MH) degraded performance to 0.54 mIoU, underscoring the contribution of hierarchical search to resolving complex spatial relationships.

**5.3. Open Vocabulary Object Querying**
*   **LERF-OVS Dataset**: For open-vocabulary object segmentation on LERF-OVS, ReLaGS obtained a mean mIoU of 64.4% (Table 3), which is the highest among both training-based and training-free approaches. The most notable improvements were observed in the Figurines (64.7%) and Teatime (81.0%) scenes, which are characterized by cluttered and occluded setups. The study also showed particularly strong gains (over 15%) on part-level queries compared to a baseline, highlighting the effectiveness of the hierarchical scene representation in capturing fine-grained semantic structure (Table 8).

*   **ScanNet Dataset**: On the ScanNet dataset for open-vocabulary semantic segmentation, ReLaGS achieved an mIoU of 47.17% for the 10-class subset and 40.04% for the 15-class subset (Table 4). This represents a slight improvement over the previous state-of-the-art training-free method, THGS (46.38% and 39.61% respectively).

**5.4. Ablation Studies**
*   **Impact of Proposed Components (Table 5)**: Maximum Weight Pruning (MWP) yielded the largest improvement in open-vocabulary 2D segmentation mIoU on LERF-OVS, increasing it from 55.88% (Base) to 62.04% (Base+MWP). Robust Outlier-Aware Feature Aggregation (ROFA) provided additional gains, bringing the mIoU to 64.36% (Base+MWP+ROFA). This suggests that refining scene geometry by removing low-contribution Gaussians and filtering inconsistent language features are crucial for semantic coherence.
*   **Sensitivity to $\tau_{lang}$ (Table 6)**: The Z-score threshold $\tau_{lang}$ for ROFA affects performance. An optimal value of 3 resulted in the highest mIoU of 64.36%.
*   **MWP and ROFA on Scene Graph Prediction (Table 10)**: Both MWP and ROFA contributed to improving 3D scene graph prediction results on 3DSSG. MWP notably improved object R@5 from 0.57 to 0.65 and relationship R@3 from 0.75 to 0.77. The addition of ROFA further improved object R@5 to 0.68 and relationship R@3 to 0.79.
*   **GNN Architecture (Table 11)**: An ablation on the GNN design indicated that a single transformer layer (L=1) with node-feature-initialized edge features yielded the best performance. Adding more layers did not improve results, suggesting the importance of local information.
*   **Pruning on Rendering Quality (Table 12)**: Lightweight pruning ($\tau_{contrib} = 5 \times 10^{-4}$) improved segmentation mIoU from 57.84 to 64.36 without affecting rendering metrics (SSIM, PSNR, LPIPS). Aggressive pruning, however, degraded both rendering quality and segmentation performance.

### 6. Significance and potential impact
ReLaGS introduces a novel framework that unifies hierarchical 3D Gaussian fields and open-vocabulary 3D scene graphs within a single language-grounded representation. This approach represents a step in structured 3D understanding, particularly for applications requiring complex reasoning capabilities.

The significance of ReLaGS stems from several key contributions:
*   **Unified Hierarchical and Relational Reasoning**: By integrating multi-level semantic abstraction (part-object-scene) with explicit scene graph formulation, ReLaGS addresses a long-standing limitation of existing language-distilled 3D representations, which were often flat and lacked relational context. This allows for more granular and contextual understanding of 3D scenes.
*   **Enhanced Robustness and Accuracy**: The introduction of Maximum Weight Pruning (MWP) and Robust Outlier-Aware Feature Aggregation (ROFA) improves both geometric fidelity and the accuracy of multi-view language registration. MWP refines the underlying Gaussian geometry by removing redundant primitives, while ROFA filters inconsistent language features, leading to more coherent and reliable object representations.
*   **Efficiency and Scalability**: ReLaGS provides an optimization-free and training-free pipeline for constructing structured 3D scenes and scene graphs. This design choice, particularly the use of a lightweight, pretrained Graph Neural Network (GNN) for relation prediction, results in significantly lower computational and memory costs compared to prior scene-specific training methods like RelationField. This efficiency makes it suitable for larger-scale applications and real-time scenarios.
*   **Open-Vocabulary Capabilities**: The framework supports open-vocabulary querying at multiple semantic granularities and through relational triplets, leveraging advancements in vision-language models. This enables more natural and flexible human-computer interaction with 3D environments.

The potential impact of ReLaGS is broad, particularly in fields such as:
*   **Robotics and Autonomous Systems**: Enhanced 3D scene understanding, including hierarchical object decomposition and relational reasoning, could improve robot navigation, object manipulation, and human-robot interaction in complex environments.
*   **Virtual and Augmented Reality (VR/AR)**: More semantically rich and structured 3D scene representations can lead to more immersive and interactive VR/AR experiences, enabling content creation, editing, and querying based on natural language and semantic relationships.
*   **Digital Twins**: The ability to generate detailed, semantically enriched digital twins at low computational cost could facilitate better analysis, simulation, and management of physical assets and environments.
*   **3D Content Creation and Editing**: Designers and creators could leverage language-guided hierarchical and relational understanding to manipulate 3D scenes more intuitively, for example, by querying for "the handle of the blue cabinet" or "the object on top of the table."

Overall, ReLaGS advances open-vocabulary 3D understanding by establishing a foundation for causal and compositional reasoning within 3D Gaussian fields, potentially paving the way for more sophisticated and intuitive interactions with 3D digital content.
