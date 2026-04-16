---
title: "Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models"
date: 2026-03-18
arxiv: "2603.18002"
venue:
status: to-read

abstract: "Multimodal Large Language Models (MLLMs) have made impressive progress in connecting vision and language, but they still struggle with spatial understanding and viewpoint-aware reasoning. Recent efforts aim to augment the input representations with geometric cues rather than explicitly teaching models to reason in 3D space. We introduce Loc3R-VLM, a framework that equips 2D Vision-Language Models with advanced 3D understanding capabilities from monocular video input. Inspired by human spatial cognition, Loc3R-VLM relies on two joint objectives: global layout reconstruction to build a holistic representation of the scene structure, and explicit situation modeling to anchor egocentric perspective. These objectives provide direct spatial supervision that grounds both perception and language in a 3D context. To ensure geometric consistency and metric-scale alignment, we leverage lightweight camera pose priors extracted from a pre-trained 3D foundation model. Loc3R-VLM achieves state-of-the-art performance in language-based localization and outperforms existing 2D- and video-based approaches on situated and general 3D question-answering benchmarks, demonstrating that our spatial supervision framework enables strong 3D understanding. Project page: this https URL"

website: https://kevinqu7.github.io/loc3r-vlm
code: https://github.com/kevinqu7/Loc3R-VLM
openreview: 
issue: 18

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

# Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models

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

![Figure](https://arxiv.org/html/2603.18002v1/x1.png)

*Figure 1: Loc3R-VLM equips 2D VLMs with advanced 3D spatial understanding capabilities from video. Inspired by human cognition, it builds an internal cognitive map of the global environment while explicitly modeling an agent’s position and orientation. By jointly capturing global layout and egocentric state, the model excels at two core tasks: language-driven localization and viewpoint-aware 3D reasoning.*

![Figure](https://arxiv.org/html/2603.18002v1/x2.png)

*Figure 2: Overview of Loc3R-VLM. Our framework takes a monocular video as input and augments the vision token sequence with per-frame latent camera pose priors extracted from the 3D foundation model CUT3R [wang2025cut3r]. The model is jointly trained using two spatial objectives: (1) layout reconstruction, which grounds vision patch tokens into a bird’s-eye-view (BEV) space to capture global scene structure, and (2) situation modeling, which utilizes dedicated localization query tokens to localize an agent from a situation description. During answer generation, the model leverages the inferred layout and location to perform viewpoint-aware 3D reasoning.*

![Figure](https://arxiv.org/html/2603.18002v1/x3.png)

*Figure 3: Spatial Supervision Framework introduces complementary training signals. For the layout reconstruction objective, the model learns to ground each vision patch token onto its corresponding BEV coordinate in a cognitive map to capture global scene structure. For localization, dedicated localization tokens explicitly model the agent’s position and orientation. The framework is trained end-to-end using a joint objective of layout, localization, and language losses.*

![Figure](https://arxiv.org/html/2603.18002v1/x4.png)

*Figure 4: Qualitative Results for language-based localization and situated QA on SQA3D [ma2022sqa3d]. Loc3R-VLM accurately grounds the described situations (blue: prediction, green: ground truth) and provides the correct viewpoint-dependent answer. Meshes are shown for visualization only and are not used by the model.*

![Figure](https://arxiv.org/html/2603.18002v1/x5.png)

*Figure 0.D.1: Correlation Between Localization Accuracy, QA Performance, and Predicted Uncertainty in Loc3R-VLM on SQA3D [ma2022sqa3d]. Localization is considered accurate for a position error ≤1.0\leq 1.0m and an orientation error ≤45∘\leq 45^{\circ}. Left: QA accuracy (EM-R) is substantially higher when Loc3R-VLM correctly localizes the agent, demonstrating that its learned situation representation enables effective viewpoint-aware reasoning. Right: The predicted positional uncertainty σpos\sigma_{\text{pos}} is notably higher for instances where localization is inaccurate, demonstrating that the model’s uncertainty estimates can reflect the reliability of the predicted situation.*

![Figure](https://arxiv.org/html/2603.18002v1/x6.png)

*Figure 0.J.1: Qualitative Examples of language-based localization and situated question answering on SQA3D [ma2022sqa3d] (blue: predicted situation, green: ground-truth situation).*

![Figure](https://arxiv.org/html/2603.18002v1/x9.png)

*Figure 0.J.2: Additional Qualitative Examples of localization and situated question answering on SQA3D [ma2022sqa3d] (blue: predicted situation, green: ground-truth situation).*

![Figure](https://arxiv.org/html/2603.18002v1/x12.png)

*Figure 0.J.3: Visualization of Failure Cases. We show three different types of failure cases. Left: correct localization but wrong answer. Middle: wrong localization but correct answer. Right: wrong localization and wrong answer (blue: predicted situation, green: ground-truth situation).*

## LLM Summary

The following report provides a detailed analysis of the research paper "Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models."

---

## Detailed Report: Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Models

### 1. Authors and Institution(s)

The research was conducted by Kevin Qu, Haozhe Qi, Mihai Dusmanu, Mahdi Rad, Rui Wang, and Marc Pollefeys. Their affiliations are as follows:
*   **Kevin Qu**: Microsoft Spatial AI Lab and ETH Zurich
*   **Haozhe Qi**: EPFL
*   **Mihai Dusmanu**: Microsoft Spatial AI Lab
*   **Mahdi Rad**: Microsoft Spatial AI Lab
*   **Rui Wang**: Microsoft Spatial AI Lab
*   **Marc Pollefeys**: Microsoft Spatial AI Lab and ETH Zurich

### 2. How This Work Fits into the Broader Research Landscape

Multimodal Large Language Models (MLLMs) have demonstrated progress in linking vision and language in two-dimensional contexts. However, a significant challenge persists in endowing these models with robust three-dimensional (3D) spatial understanding and viewpoint-aware reasoning capabilities. Existing MLLMs frequently process information locally, struggling to integrate observations across multiple frames into a persistent, unified global context, a capability often observed in human cognition for forming mental representations of environments.

Current approaches to enhance the spatial awareness of MLLMs typically fall into two categories: (i) integrating point cloud representations directly into the model, or (ii) augmenting 2D image inputs with 3D positional encodings derived from depth maps and camera poses. Both strategies exhibit limitations. First, they often necessitate precise 3D ground-truth data during inference, which is not consistently available in real-world scenarios. Second, the supervision provided to these models primarily targets language-based or object-centric objectives, treating global scene understanding and situational awareness as secondary outcomes rather than explicitly learned capacities. Consequently, these models may struggle with reasoning about viewpoint-dependent spatial relationships or inferring perspectives beyond the immediate egocentric view. Furthermore, methods relying on dense point-cloud representations face scalability and generalization constraints due to the limited availability of large-scale paired 3D-text datasets. More recent efforts have explored leveraging internal representations from 3D foundation models to provide implicit geometric cues; however, these are often utilized as passive input augmentations rather than for explicitly teaching 3D spatial awareness.

Loc3R-VLM addresses these limitations by introducing a framework designed to explicitly equip 2D Vision-Language Models (VLMs) with advanced 3D understanding and situational awareness directly from monocular video input. It aims to circumvent the reliance on ground-truth 3D annotations during inference by providing direct spatial supervision. This work positions itself by emphasizing a joint learning approach that integrates global scene structure and egocentric state modeling, drawing inspiration from human spatial cognition to bridge the gap between visual perception, spatial understanding, and embodied reasoning in artificial systems.

### 3. Key Objectives and Motivation

The primary objective of this research is to augment 2D Vision-Language Models (VLMs) with advanced 3D spatial understanding capabilities and explicit situational awareness, operating solely on monocular video input. This overarching goal is motivated by the observation that while MLLMs have achieved proficiency in connecting vision with language in 2D, they largely lack a coherent grasp of 3D space, which is essential for complex spatial reasoning.

The motivation for Loc3R-VLM is fundamentally inspired by human spatial cognition. Humans naturally construct an internal "cognitive map" of their surroundings from visual observations, enabling them to recall and manipulate this mental representation to answer diverse spatial queries, such as locating objects, determining directions, or mentally simulating alternative viewpoints. Replicating this capacity for visual-spatial intelligence in artificial systems remains a substantial challenge for current MLLMs, which tend to operate in a localized manner without integrating observations into a persistent global context.

To bridge this gap and imbue VLMs with human-like spatial reasoning, the paper outlines several key objectives:
*   **Global Layout Reconstruction**: To enable the model to build a holistic, internal representation of the scene structure, akin to a cognitive map. This objective aims to facilitate an internal memory of the environment and capture its spatial organization, allowing the model to ground observations across multiple frames into a unified global context.
*   **Explicit Situation Modeling**: To enable the model to precisely localize itself within the scene by explicitly modeling an agent’s position and orientation. This objective aims to allow the model to reason from a grounded, egocentric perspective, essential for viewpoint-aware inference from natural language descriptions.
*   **Geometric Consistency and Metric-Scale Alignment**: To ensure that the learned spatial representations are geometrically consistent and aligned to metric scale. This is achieved by leveraging lightweight camera pose priors extracted from a pre-trained 3D foundation model, mitigating the inherent scale ambiguity of monocular video.
*   **Reduced Reliance on 3D Ground Truth**: To develop a framework that enables robust 3D understanding and spatial reasoning directly from monocular video input, thereby eliminating the need for precise 3D ground-truth data during inference, which is often unavailable in real-world applications.
*   **Improved Performance**: To achieve state-of-the-art performance in language-based localization and to surpass existing 2D- and video-based approaches on situated and general 3D question-answering benchmarks, demonstrating the efficacy of the proposed spatial supervision framework.

These objectives collectively aim to advance MLLMs beyond passive input augmentation of 3D cues, instead teaching them to actively reason about and represent 3D space.

### 4. Methodology and Approach

Loc3R-VLM is a framework designed to equip a 2D Vision-Language Model (VLM) with 3D spatial understanding and situational awareness capabilities using monocular video input. The architecture is built upon LLaVA-Video-7B [69] and incorporates three complementary components, optimized through a joint training objective.

**4.1. Integration of Camera Pose Priors**
To provide geometric grounding for the input video, Loc3R-VLM integrates per-frame latent camera tokens. This is achieved by leveraging a pre-trained, feed-forward geometry model, CUT3R [55]. For each input video frame $I_t$, CUT3R processes the image through a vision transformer to produce feature tokens $F_t$. A learnable camera query token $z$ is prepended to $F_t$ and then processed alongside the previous recurrent state $s_{t-1}$ by a transformer decoder, yielding an updated camera token $z'_t$ and geometry tokens $F'_t$.

Loc3R-VLM exclusively utilizes the camera token $z'_t$ as a geometric prior. This token is projected into the VLM's language embedding space using a two-layer MLP, $f_{cam}$, resulting in a projected camera token $c_t$. For each frame, $c_t$ is prepended to the vision tokens obtained from a SigLIP [64] encoder, forming an augmented vision sequence $X_{aug,t} = [c_t, v_{t,1}, v_{t,2}, \dots, v_{t,n}]$. This strategy aims to embed latent metric pose information directly into the visual stream, grounding each frame within a broader scene context while preserving the integrity of the VLM's pre-trained vision-language feature space.

**4.2. Global Layout Reconstruction**
Global Layout Reconstruction is introduced as an auxiliary training objective to enhance the model’s understanding of cross-view spatial relationships and the global structure of the scene. This component trains the model to associate vision patch tokens with their corresponding two-dimensional coordinates within a unified Bird’s-Eye-View (BEV) representation. The BEV space is defined in a gravity-aligned world coordinate frame, consistently shared across all camera views from the same video and anchored to the first video frame, aligning with the CUT3R convention.

From a sequence of $M$ vision tokens $(v_i)_{i=1}^M$ extracted from the LLM’s output layer, a learnable projection head $f_{proj}$ estimates each token’s BEV position $\hat{p}_i = [\hat{x}_i, \hat{y}_i]^\top \in \mathbb{R}^2$ and its associated predictive uncertainty $\hat{\sigma}_i = [\hat{\sigma}_{x,i}, \hat{\sigma}_{y,i}]^\top \in \mathbb{R}^2$. The ground-truth BEV coordinates $p_i = [x_i, y_i]^\top$ are modeled as samples from a Gaussian distribution centered at $\hat{p}_i$ with diagonal covariance matrix $diag(\hat{\sigma}^2_{x,i}, \hat{\sigma}^2_{y,i})$. The training objective minimizes the Gaussian Negative Log-Likelihood (GNLL) loss, $L_{BEV}$, which encourages the model to construct a coherent global representation and enrich vision token hidden states with spatial information. During training, ground-truth BEV coordinates are computed from the depth maps and camera poses provided by the datasets.

**4.3. Situation Modeling**
To enable explicit localization and situation-aware reasoning, Loc3R-VLM introduces two new tokens to its vocabulary: `<Pos>` for position and `<Ori>` for orientation. Given a textual situation description $txt_{sit}$ and a question $txt_q$, these tokens are inserted between the text segments before tokenization: $X_{in} = concat(txt_{sit}, \text{<Pos>}, \text{<Ori>}, txt_q)$.

At the LLM’s output layer, the final hidden state of these tokens is decoded via lightweight, task-specific heads:
*   **Position Estimation**: A position head, $f_{pos}$, estimates the agent’s 2D location $\hat{p} = [\hat{x}, \hat{y}]^\top$ and its uncertainty $\sigma_{pos} = [\sigma_x, \sigma_y]^\top$ in the global BEV frame. This is supervised using the GNLL loss, $L_{pos}$. This probabilistic formulation aims to down-weight ambiguous samples during training and enable the model to output higher uncertainty for challenging cases.
*   **Orientation Estimation**: An orientation head, $f_{ori}$, predicts discretized angle logits $\hat{y}_{ori} \in \mathbb{R}^B$ over $B$ uniform bins (where $B=36$). A smooth training signal is generated using a wrapped Gaussian target distribution centered at the ground-truth angle, from which normalized probabilities $y^{(b)}_{ori}$ are derived. The loss, $L_{ori}$, is calculated using KL-divergence between the predicted logits and this target distribution. During inference, a continuous orientation $\hat{\theta}$ is recovered using a circular soft-argmax.

The final situation modeling objective, $L_{sit}$, combines both components: $L_{sit} = L_{pos} + \lambda_{ori} L_{ori}$, with $\lambda_{ori} = 3.5$ for balancing loss magnitudes. The explicit `<Pos>` and `<Ori>` tokens are designed to provide a dedicated representation for the agent’s situational state, allowing the model to attend to them for internal viewpoint transformations during answer generation.

**4.4. Overall Training Objective**
Loc3R-VLM is trained end-to-end using a joint objective that integrates standard language modeling with the proposed spatial objectives. This allows for shared multimodal representation across language, reconstruction, and situation tasks. The total loss, $L_{total}$, is defined as:
$L_{total} = L_{CE} + \lambda_{BEV} L_{BEV} + \lambda_{sit} L_{sit}$
where $L_{CE}$ is the autoregressive cross-entropy language modeling loss, and $\lambda_{BEV} = 0.05$ and $\lambda_{sit} = 0.075$ are weighting coefficients. During training, the parameters of the LLM, spatial and situation heads, and projection layers are updated, while the vision and CUT3R encoders are frozen. Each scene is processed with 32 uniformly sampled video frames at an input resolution of 384x384. For inference, the model requires only raw monocular video, without any 3D annotations.

### 5. Main Findings and Results

Loc3R-VLM's performance was evaluated across language-based localization, situated 3D question answering, and general 3D question answering tasks, demonstrating its spatial understanding capabilities.

**Language-based Localization Benchmarks:**
Evaluations on the SQA3D [34] benchmark, which comprises textual scenarios describing an embodied agent's situation in indoor scenes, show that Loc3R-VLM achieves notable performance improvements.
*   **Performance Comparison**: Loc3R-VLM significantly outperforms all prior methods, including those that rely on dense 3D point-cloud representations (e.g., SQA3D, 3D-VisTA, SIG3D, View2Cap). Specifically, it surpasses the strongest baseline, View2Cap, by +25.2% in Acc@0.5m and +39.0% in Acc@1.0m for position estimation. For orientation prediction, it achieves gains of +14.3% in Acc@15° and +34.5% in Acc@30°.
*   **Attribution**: These gains are attributed to the global layout reconstruction objective, which facilitates a coherent internal map of the scene, and the camera pose prior, which provides metric-scale cues for stable absolute position estimation. The situation modeling module also contributes to robust viewpoint understanding.

**3D Question Answering Benchmarks:**
Loc3R-VLM was assessed on VSI-Bench [61], SQA3D [34], MSQA [32] (ScanNet portion), ScanQA [2], and Beacon3D [21].
*   **VSI-Bench**: Among generalist baselines, Loc3R-VLM achieves the strongest overall performance. It demonstrates particular proficiency in tasks requiring viewpoint understanding, exhibiting substantial gains in Relative Direction (+36.1%), Relative Distance (+10.8%), and Route Planning (+8.8%) compared to the second-best generalist baseline. For numerical tasks, it obtains the best results in Absolute Distance and Object Size, attributed to the metric-scale cues provided by the camera-pose prior.
*   **ScanQA and SQA3D**: On SQA3D, Loc3R-VLM achieves an EM score of 62.8, outperforming all 2D MLLMs and most 3D-based approaches. This highlights the efficacy of explicit situation modeling for robust viewpoint grounding. For general QA on ScanQA, the model surpasses other 2D methods across most metrics. Loc3R-VLM exhibits the best performance among all methods capable of situation localization across both benchmarks.
*   **MSQA and Beacon3D**: The model attains the highest overall scores, with 58.6% on MSQA and 62.4% on Beacon3D. Significant gains are observed in the spatial subcategories of both benchmarks, outperforming the second-best methods by +11.1% on MSQA and +9.4% on Beacon3D.

**Ablation Studies:**
Ablation studies were conducted to assess the impact of individual components:
*   **Localization**: Explicit situation modeling provides a strong baseline. The addition of the layout reconstruction objective further improves localization accuracy by consolidating multi-view observations into a global map. Incorporating the camera pose prior leads to additional substantial improvements, particularly for position estimation, by aligning the internal map in metric space.
*   **3D QA**: Situation modeling consistently improves QA performance on SQA3D and MSQA, indicating that explicitly encoding the agent's pose helps resolve viewpoint-dependent references. Improvements are also observed on ScanQA, suggesting that the situation module enhances general spatial understanding. Global layout reconstruction also contributes to performance gains. The combination of these two components yields greater improvements than either alone. The integration of camera pose priors provides further, though comparatively modest, gains in QA, suggesting that 3D QA relies primarily on relational and global scene understanding established by the spatial training objectives.
*   **3D Foundation Model Feature Selection**: Evaluating the choice of features from the 3D foundation model, using only the CUT3R camera token as a spatial prior demonstrated superior performance compared to including both camera and geometry tokens. This suggests the camera token is sufficient for geometric grounding, and additional geometry tokens may introduce redundant signals that interfere with pre-trained representations.

**Correlation of Localization Accuracy with QA Performance and Uncertainty:**
Analysis on SQA3D revealed a correlation between localization accuracy and situated QA performance. When Loc3R-VLM accurately localizes the agent, it achieves higher QA accuracy. Conversely, QA performance declines when localization fails, indicating that the internal situation representation effectively grounds viewpoint-aware reasoning. Furthermore, localization accuracy is reflected in the predicted positional uncertainty, with inaccurate position estimates correlating with higher predicted uncertainty.

### 6. Significance and Potential Impact

Loc3R-VLM presents a framework that equips 2D Vision-Language Models with advanced 3D understanding capabilities from monocular video input. A key aspect of this work is its ability to perform language-based localization and spatial reasoning without requiring explicit 3D ground-truth data during inference, which expands the practical applicability of 3D-aware models to real-world scenarios where such data is often unavailable.

The framework's significance lies in its dual approach, inspired by human cognition, which jointly enhances global scene understanding through a global layout reconstruction objective and situational awareness via an explicit situation modeling module. The integration of lightweight camera pose priors from a pre-trained 3D foundation model further ensures metric-scale consistency, which is crucial for accurate spatial reasoning.

The demonstrated results indicate substantial gains across multiple benchmarks:
*   **Language-based Localization**: Loc3R-VLM achieves state-of-the-art performance, outperforming previous methods that often rely on dense 3D point-cloud inputs. This suggests a more efficient and accessible approach to grounding agents in 3D environments from linguistic descriptions.
*   **Situated and General 3D Question Answering**: The model shows superior performance on various 3D QA benchmarks, particularly excelling in viewpoint-dependent tasks. This indicates an improved capacity for models to interpret and respond to queries that require understanding of relative positions, directions, and routes within a 3D space, anchored to an agent's perspective.

The work contributes to the development of MLLMs that can perceive and reason about the world with greater spatial intelligence. By enabling robust 3D understanding directly from video input through explicit spatial supervision, Loc3R-VLM offers a pathway toward more capable and generalized embodied AI systems. Such advancements could have implications for domains like robotics, where precise situational understanding is fundamental for safe navigation and decision-making, and autonomous driving, where environmental awareness underpins operational safety.

While advancing the field, the authors also identify certain limitations:
*   **Vertical Granularity**: The use of a 2D Bird's-Eye-View (BEV) representation inherently discards vertical detail, potentially limiting reasoning in multi-floor environments or tasks requiring precise height-based distinctions. Future work could explore layered BEV architectures or object-centric tokens to reintroduce vertical information.
*   **Scene Coverage**: The fixed-length frame sampling (e.g., 32 frames) for constructing the cognitive map might lead to "blind spots" in expansive scenes with low viewpoint overlap. Spatially adaptive or coverage-aware frame selection strategies are suggested as potential solutions.
*   **Domain Scope**: The current approach focuses on static indoor scenes, leaving the adaptation to dynamic scenes and outdoor environments as a direction for future research.

Overall, Loc3R-VLM represents a step towards creating 3D-aware VLMs with stronger spatial and embodied understanding, by demonstrating that robust 3D reasoning can emerge from video input when models are guided to organize visual information into comprehensive global and viewpoint-aware representations.
