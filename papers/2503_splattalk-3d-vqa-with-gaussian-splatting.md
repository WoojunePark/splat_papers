---
title: "SplatTalk: 3D VQA with Gaussian Splatting"
date: 2025-03-08
arxiv: "2503.06271"
venue:
status: to-read

abstract: "Language-guided 3D scene understanding is important for advancing applications in robotics, AR/VR, and human-computer interaction, enabling models to comprehend and interact with 3D environments through natural language. While 2D vision-language models (VLMs) have achieved remarkable success in 2D VQA tasks, progress in the 3D domain has been significantly slower due to the complexity of 3D data and the high cost of manual annotations. In this work, we introduce SplatTalk, a novel method that uses a generalizable 3D Gaussian Splatting (3DGS) framework to produce 3D tokens suitable for direct input into a pretrained LLM, enabling effective zero-shot 3D visual question answering (3D VQA) for scenes with only posed images. During experiments on multiple benchmarks, our approach outperforms both 3D models trained specifically for the task and previous 2D-LMM-based models utilizing only images (our setting), while achieving competitive performance with state-of-the-art 3D LMMs that additionally utilize 3D inputs. Project website: this https URL"

website: https://splat-talk.github.io
code: https://github.com/ngailapdi/SplatTalk
openreview:
issue: 

inputs:
  - posed-multi-view-images
  - text-prompt
outputs:
  - 3d-gaussians
  - vqa
methods:
  - 3dgs
  - vlm
  - llm
benchmarks:
  - 

related:
  - 

compared:
  - 
---

# SplatTalk: 3D VQA with Gaussian Splatting

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

![Figure](https://arxiv.org/html/2503.06271/x2.png)

*Figure 2: Overview. Left: During the self-supervised 3D-language Gaussian Splatting training phase, multiple RGB input views are first encoded into Gaussian latent features (Gaussian triplets). These latent features are then decoded into Gaussian parameters for rendering, along with a low-dimensional visual-language feature ffitalic_f. To ensure proper supervision of this low-dimensional feature, we train an autoencoder that maps the high-dimensional, unbounded features obtained from LLaVA-OV, specifically, the visual tokens serving as direct inputs to the LLM, onto a low-dimensional hypersphere space. Right: During 3D VQA inference, visual-language features are directly extracted from the 3D Gaussians. These features are then mapped back to the original high-dimensional space using the pretrained decoder and subsequently used as direct visual token inputs to the LLM. LoRA fine-tuning of the LLM is optional.*

![Figure](https://arxiv.org/html/2503.06271/x3.png)

*Figure 3: Qualitative results on ScanQA, scene0030_00 and scene0084_00. We compare responses from LLaVA-OV, our model (Ours), and the ground truth (GT) for spatial reasoning questions in 3D VQA. Each scene highlights the referenced objects with red circles, and key relative objects are marked in blue. The answers from each model are displayed in color-coded speech bubbles: LLaVA-OV (brown), Ours (blue), and GT (green). With its 3D-aware representation, our model exhibits improved spatial reasoning capabilities, accurately identifying relationships between objects that are far apart and may never co-occur in the same image (e.g., door and window). More examples in Supp.*

![Figure](https://arxiv.org/html/2503.06271/x4.png)

*Figure 4: Qualitative results on ScanQA, scene0389_00 and scene0222_00. We compare responses from LLaVA-OV, our model (Ours), and the ground truth (GT) for spatial reasoning questions in 3D VQA. Each scene highlights the referenced objects with red circles, and key relative objects are marked in blue. The answers from each model are displayed in color-coded speech bubbles: LLaVA-OV (brown), Ours (blue), and GT (green). With its 3D-aware representation, our model exhibits improved spatial reasoning capabilities.*

![Figure](https://arxiv.org/html/2503.06271/x5.png)

*Figure 5: Qualitative results on ScanQA, scene0100_00, scene0193_00, and scene0426_00. We compare responses from LLaVA-OV, our model (Ours), and the ground truth (GT) for spatial reasoning questions in 3D VQA. Each scene highlights the referenced objects with red circles, and key relative objects are marked in blue. The answers from each model are displayed in color-coded speech bubbles: LLaVA-OV (brown), Ours (blue), and GT (green). With its 3D-aware representation, our model exhibits improved spatial reasoning capabilities.*

## LLM Summary

This report provides a detailed analysis of the paper "SplatTalk: 3D VQA with Gaussian Splatting," focusing on its authors, institutional context, placement within the broader research landscape, key objectives, methodology, main findings, and overall significance.

### 1. Authors, Institution(s), and Notable Context about the Research Group

The paper "SplatTalk: 3D VQA with Gaussian Splatting" is authored by Anh Thai, Songyou Peng, Kyle Genova, Leonidas Guibas, and Thomas Funkhouser. The primary author, Anh Thai, is affiliated with the Georgia Institute of Technology, with the work explicitly stated as being done as a student researcher at Google DeepMind. The remaining authors are all affiliated with Google DeepMind.

**Google DeepMind** is a globally renowned artificial intelligence research laboratory owned by Alphabet (Google's parent company). It is at the forefront of AI research, consistently pushing boundaries in areas like deep reinforcement learning, large language models, computer vision, and multimodal AI. DeepMind is known for its ambitious projects and significant contributions to the field, often characterized by tackling complex problems with novel architectures and large-scale computational resources. Their involvement in a project like SplatTalk underscores the strategic importance of 3D understanding and multimodal integration within Google's broader AI vision, particularly for applications in robotics, augmented reality (AR), and virtual reality (VR). The expertise of authors like Leonidas Guibas (a prominent figure in computational geometry and computer graphics) and Thomas Funkhouser (known for contributions to 3D vision and shape analysis) further emphasizes the strong foundational research underpinning this work.

**Georgia Institute of Technology** is a leading public research university and a highly respected institution for computer science and engineering. Anh Thai's affiliation with Georgia Tech while conducting research at DeepMind highlights a common and beneficial collaboration model, where academic talent contributes to and benefits from industry-leading research environments. This synergy often leads to high-impact publications that blend rigorous academic inquiry with practical application and scalability.

The context of this collaboration is particularly notable. A student researcher working within DeepMind implies access to significant computational resources, specialized datasets, and mentorship from leading experts in AI. This environment is conducive to developing sophisticated models that can address grand challenges in AI, such as robust 3D scene understanding.

### 2. How This Work Fits into the Broader Research Landscape

SplatTalk operates at the intersection of 3D computer vision, natural language processing, and multimodal AI, specifically addressing the challenge of 3D Visual Question Answering (3D VQA). The broader research landscape for 3D VQA is characterized by efforts to enable AI models to understand and interact with 3D environments using natural language, a crucial step for applications in robotics, AR/VR, and human-computer interaction.

**Challenges in 3D VQA:** The paper clearly outlines the primary hurdles in 3D VQA: the inherent complexity of 3D data, its scarcity compared to abundant 2D datasets, and the prohibitively high cost and difficulty of manually annotating 3D scenes with language. This contrasts sharply with the rapid advancements seen in 2D Vision-Language Models (VLMs) and Large Multimodal Models (LMMs) for 2D VQA, where vast amounts of image-text pairs are readily available.

**Evolution of 3D LMMs:** Previous approaches to 3D multimodal learning have largely relied on explicit 3D inputs such as meshes, point clouds, or voxels, often combined with multi-view RGB images. While these methods have shown promise, they are constrained by the availability and quality of detailed 3D reconstructions. Models like LEO, 3D-LLM, and Scene-LLM (referenced in the paper) fall into this category, requiring dense 3D representations that are not always available or easily acquired.

**Neural Radiance Fields (NeRFs) and 3D Gaussian Splatting (3DGS):** A more recent wave of research has explored implicit 3D representations, such as NeRFs, or explicit representations like 3DGS, which can reconstruct 3D scenes from only multi-view RGB images. Works like LangSplat [38] integrated semantic features into 3DGS, but often required per-scene optimization, limiting scalability and generalization. SplatTalk builds on this line of work but crucially addresses the generalization problem and self-supervised learning of language features.

**Generalizable 3DGS:** SplatTalk specifically leverages advancements in generalizable 3D Gaussian Splatting, drawing inspiration from FreeSplat [46]. Generalizable 3DGS aims to create models that can infer 3D representations of novel, unseen scenes without per-scene optimization, typically focusing on novel view synthesis. SplatTalk extends this concept to embed language features, shifting the focus from photorealistic reconstruction to semantic 3D scene understanding.

**Comparison to 2D LMMs for 3D Tasks:** The paper notes that even advanced 2D LMMs (e.g., LLaVA-OV, GPT-4V) struggle with 3D spatial reasoning tasks when presented with multiple 2D images of a 3D scene. This is because these models lack an explicit 3D understanding, instead relying on the LLM to infer 3D relationships from a collection of 2D tokens. This often leads to failures in queries requiring holistic scene understanding or precise spatial reasoning across widely separated objects. SplatTalk directly addresses this by consolidating language tokens in 3D space, thus providing a 3D-aware representation to the LLM.

**Distinction from Concurrent Work:** The paper positions SplatTalk against concurrent works like ChatSplat [6], which also explores language interaction with 3DGS. SplatTalk differentiates itself by being fully self-supervised, not requiring per-scene optimization for language feature integration, and producing tokens directly compatible with an LLM for easier language-based reasoning. It also performs joint optimization of RGB and semantic features, a departure from methods that train them sequentially.

In summary, SplatTalk advances the field by offering a **self-supervised, generalizable, and 3D-aware solution for 3D VQA that relies solely on multi-view RGB images**, sidestepping the need for explicit 3D geometry inputs or expensive 3D language annotations. It effectively bridges the gap between powerful 2D VLMs and the requirements of 3D understanding by embedding rich language semantics directly into a compact and efficient 3D Gaussian representation.

### 3. Key Objectives and Motivation

The overarching objective of SplatTalk is to significantly advance language-guided 3D scene understanding, particularly for 3D Visual Question Answering (3D VQA), thereby enabling more sophisticated applications in robotics, AR/VR, and human-computer interaction.

The core motivations behind this work stem from several critical challenges and observations in the current landscape of multimodal AI:

1.  **Bridging the 2D-3D Gap in Multimodal Understanding:** While 2D Vision-Language Models (VLMs) have achieved remarkable success in interpreting and responding to language queries about 2D images, their ability to reason about complex 3D scenes from multiple 2D views remains limited. They struggle with queries requiring deep spatial understanding or relationships between objects not simultaneously visible in a single image. SplatTalk aims to fill this gap by explicitly modeling 3D spatial and semantic information.
2.  **Addressing Data Scarcity and Annotation Costs in 3D:** The development of 3D LMMs has been hampered by the scarcity of 3D datasets and the high cost of language annotations in 3D space. Unlike 2D images, acquiring and labeling 3D data is significantly more complex and expensive. SplatTalk seeks to overcome this by operating solely on readily available multi-view RGB images, which are easier to capture, and by employing a self-supervised training paradigm that requires no explicit 3D-language annotations.
3.  **Leveraging Efficient 3D Representations:** Existing 3D LMMs often rely on explicit 3D inputs like point clouds, meshes, or voxels, which can be computationally intensive and not always available. SplatTalk is motivated by the efficiency and representational power of 3D Gaussian Splatting (3DGS) as a sparse, explicit, and differentiable 3D representation that can be learned from images alone. The goal is to integrate rich semantic features into this efficient framework.
4.  **Enabling Zero-Shot 3D VQA:** A key objective is to achieve effective zero-shot 3D VQA performance, meaning the model can answer questions about unseen 3D scenes without specific fine-tuning on those scenes or explicit 3D language supervision during its core training. This enhances the model's generalizability and practical utility.
5.  **Producing LLM-Compatible 3D Tokens:** The paper aims to develop a method that generates "3D tokens" directly suitable as input for a pre-trained Large Language Model (LLM). This approach allows SplatTalk to harness the powerful reasoning capabilities of LLMs for complex 3D VQA tasks without requiring extensive retraining of the LLM itself, thereby providing a more efficient and powerful framework than prior methods.

In summary, SplatTalk's key objectives are to develop a novel, self-supervised 3D Gaussian-based framework that can learn spatially-aware semantic representations from only multi-view RGB images, generate LLM-compatible 3D tokens, and achieve state-of-the-art or competitive zero-shot performance in 3D VQA benchmarks, thereby fostering broader adoption of language-guided 3D reasoning.

### 4. Methodology and Approach

SplatTalk proposes a novel, self-supervised 3D-Language Gaussian Splatting model designed to perform zero-shot 3D Visual Question Answering (3D VQA) using only multi-view RGB images. The methodology can be broken down into three main stages: Feature Autoencoder Training, Self-supervised 3D-Language Gaussian Splatting Training, and 3D VQA Inference. An optional fine-tuning step is also detailed.

**4.1. Training the Feature Autoencoder**

The first critical step addresses the challenge of integrating high-dimensional, sparse, and unbounded visual tokens from 2D Vision-Language Models (VLMs) into a differentiable 3DGS pipeline. The approach involves:

*   **2D Pseudo Ground-truth Features:** High-dimensional visual tokens are extracted from a pre-trained 2D VLM, specifically LLaVA-OV [23]. These tokens, generated *after* LLaVA-OV's multimodal projector, are already aligned with the LLM's input space, making them ideal as pseudo ground truth for supervising the 3D-language features.
*   **Dimensionality Reduction:** Since these visual tokens are typically very high-dimensional (e.g., 3584 dimensions), they are impractical for direct 3DGS optimization and rendering. SplatTalk trains a generalizable autoencoder (composed of linear layers, batch normalization, and GeLU activations) to project these features into a compact, lower-dimensional space (e.g., 256 dimensions) and normalize them onto a unit hypersphere. This ensures feature smoothness and stability during 3DGS training. Crucially, this autoencoder is trained **once** across all scenes, enhancing generalizability and avoiding per-scene retraining. It is also trained *separately* from the 3DGS model to ensure it focuses solely on feature compression without rendering complexities.

**4.2. Self-supervised 3D-Language Gaussian Splatting Training**

This stage focuses on building the 3D-language Gaussian representation from multi-view RGB images, leveraging the compressed language features:

*   **Base Architecture:** SplatTalk builds upon the FreeSplat [46] generalizable 3DGS framework, which is designed for sparse-view synthesis. FreeSplat typically extracts multi-scale features from input RGB images, constructs adaptive cost volumes for depth prediction, and back-projects 2D features into 3D Gaussian triplets (center, weight, latent feature). A Pixel-wise Triplet Fusion (PTF) module integrates multi-view information.
*   **Joint Training of RGB and Language Features:** Unlike prior works that freeze RGB Gaussians before adding language features, SplatTalk adopts a joint training strategy. A new Gaussian parameter decoder head is introduced, which predicts a 256-dimensional language feature vector for each 3D Gaussian *alongside* the standard RGB rendering parameters (opacity, scale, rotation). This implicitly integrates semantic and visual information within the Gaussian representation, as the shared Gaussian latent features capture holistic scene information.
*   **Loss Function:** The model is trained using a combination of photometric loss (MSE + LPIPS for RGB reconstruction) and semantic loss (MSE + cosine distance for the low-dimensional language features), effectively supervising both modalities.
*   **Efficient Rendering:** A parallel CUDA rasterizer pipeline, inspired by [51], is implemented to efficiently render high-dimensional semantic features and RGB simultaneously using shared Gaussian parameters. Input RGB images are downsampled to a lower resolution (e.g., 32x32) to align with LLaVA-OV's visual token resolution and encourage a balanced representation of RGB and semantic information.

**4.3. 3D VQA Inference**

Once the 3D-language Gaussian Splatting model is trained, 3D VQA inference proceeds as follows:

*   **Extracting 3D Language Features:** During inference, language features are extracted directly from the mean position of each 3D Gaussian. The paper provides a theoretical justification, conceptually linking the training optimization process to the Expectation-Maximization (EM) algorithm, where each optimal 3D Gaussian feature is a weighted sum of 2D feature maps, thus holistically encoding scene semantics.
*   **Entropy Adaptive Gaussian Sampling:** To address the LLM's visual token limit and ensure informative input, an entropy-based sampling strategy is proposed. The model selects the top *k* Gaussians with the highest language feature entropy, where *k* matches the LLM's visual token capacity. This prioritizes Gaussians that carry more uncertain or complex semantic information.
*   **3D Tokens as Visual Inputs:** The sampled 3D Gaussian features are then mapped back to their original high-dimensional space using the pre-trained autoencoder's decoder. These resulting "3D tokens" are directly fed into a pre-trained LLM (Qwen2 [11] is mentioned in supplementary material) along with the natural language prompt. Since these tokens are spatially grounded by their 3D Gaussian origins, explicit positional encodings are not required, as their spatial relationships are implicitly captured.

**4.4. Optional - Finetuning on 3D VQA Datasets**

For further performance enhancement on specific 3D VQA benchmarks, SplatTalk allows for lightweight fine-tuning. Instead of retraining the entire model, which is computationally expensive and prone to overfitting, only the LoRA (Low-Rank Adaptation) parameters applied to the LLM are optimized. This selectively adapts the LLM's reasoning capabilities to the target dataset without disturbing the learned 3D scene representation.

### 5. Main Findings and Results

SplatTalk demonstrates significant advancements in 3D VQA, outperforming 2D LMM-based methods and achieving competitive results with explicit 3D LMMs, all without requiring explicit 3D inputs or 3D-language annotations.

**5.1. Performance on ScanQA and SQA3D Datasets (Table 1)**

*   **Outperforming 2D LMM-Based Models:** SplatTalk, even in its base, self-supervised form, significantly outperforms other 2D LMM-based models like LLaVA-OV, GPT-4V, and Claude across all metrics on both ScanQA (e.g., SplatTalk CIDEr 61.7 vs LLaVA-OV CIDEr 50.0) and SQA3D. This strongly validates the benefit of building a 3D-aware representation, even from purely 2D image inputs.
*   **Competitive with 3D LMMs:** When fine-tuned on 3D VQA datasets (SplatTalk-ScanQA-FT, SplatTalk-3DVQA-FT), SplatTalk achieves performance comparable to or surpassing many Generalist and Specialist 3D LMMs that utilize explicit 3D inputs (point clouds or point clouds + images). For instance, SplatTalk-3DVQA-FT achieves a CIDEr of 77.5 on ScanQA, which is competitive with LEO (101.4, a very strong SOTA finetuned 3D LMM) and significantly higher than several other 3D LMMs. This highlights the effectiveness of SplatTalk's approach in inferring and leveraging 3D spatial information.
*   **Value of Fine-tuning:** Fine-tuning substantially improves performance, with SplatTalk-ScanQA-FT and SplatTalk-3DVQA-FT showing considerable gains over the base SplatTalk model, indicating the adaptability of the learned 3D representations to specific VQA tasks.

**5.2. Performance on MSR3D Dataset (Table 2)**

*   **Superior Zero-Shot Performance:** On MSR3D, which is an interleaved dataset (text and images, but evaluated zero-shot with only text prompts and agent state descriptions), SplatTalk's base model significantly outperforms LLaVA-OV across all question types (e.g., 41.8 overall vs. LLaVA-OV 24.0). It also substantially outperforms LEO, a 3D LMM, which struggles in a zero-shot setting on this dataset.
*   **Category-Specific Strengths:** SplatTalk shows particularly strong gains in categories like "Existence," "Attributes," "Spatial," and "Navigation," often doubling LLaVA-OV's performance. This underscores its enhanced 3D spatial reasoning capabilities.
*   **Overfitting with Fine-tuning:** Interestingly, fine-tuning on other VQA datasets (ScanQA, SQA3D) leads to a performance drop on MSR3D. This suggests that MSR3D presents a distinct challenge, and models fine-tuned on other datasets might overfit or struggle with the domain shift, highlighting the importance of SplatTalk's strong zero-shot base performance.

**5.3. Ablation Studies**

*   **Gaussian Sampling Strategies (Table 3):** Entropy-adaptive sampling consistently outperforms other methods (Random, Point Density Adaptive, Furthest Point Sampling) across metrics like METEOR, ROUGE, and SPICE. This confirms that prioritizing Gaussians with higher language feature entropy is the most effective way to select informative tokens for LLM input, leading to better 3D VQA performance.
*   **Length of Visual Tokens (Table 4):** Increasing the number of visual tokens (from 729, equivalent to 1 image, to 32,076, equivalent to 44 images) generally improves performance across datasets. MSR3D shows the most significant gain, nearly doubling its EM@1 score. However, ScanQA and SQA3D show only marginal improvements with more tokens, suggesting potential dataset limitations or that the model may not fully leverage very extensive visual contexts for certain task complexities.

**5.4. Qualitative Results (Figures 3, 4, 5)**

The qualitative examples visually reinforce the quantitative findings, showing SplatTalk's improved spatial reasoning. It accurately identifies relationships between objects that are far apart or not simultaneously visible in single 2D views (e.g., "What is opposite the door at the other end of the room?"). This demonstrates its ability to build a truly holistic 3D understanding.

### 6. Significance and Potential Impact

SplatTalk represents a significant contribution to the field of 3D computer vision and multimodal AI, with broad implications for various applications:

1.  **Democratization of 3D Scene Understanding:** By eliminating the reliance on explicit 3D inputs (like point clouds or depth maps) and expensive 3D-language annotations, SplatTalk makes advanced 3D scene understanding far more accessible. This significantly lowers the barrier to entry for developing 3D-aware AI systems, as multi-view RGB images are readily available and easier to acquire than high-fidelity 3D scans. This is crucial for democratizing the development of 3D VQA systems for a wider range of practitioners and researchers.
2.  **Enhanced Generalizability and Scalability:** The self-supervised and generalizable nature of SplatTalk, which learns 3D-language Gaussian fields from multiple scenes without per-scene training, marks a crucial step towards scalable 3D LMMs. This approach allows models to reason about novel, unseen environments, which is essential for real-world deployment in dynamic settings.
3.  **Foundation for Robotics and Embodied AI:** The ability for AI agents to comprehend and interact with 3D environments through natural language is fundamental for embodied AI and robotics. SplatTalk's robust 3D VQA capabilities, particularly its improved spatial reasoning, can enable robots to better understand commands ("What is next to the bed?"), navigate complex spaces, and perform tasks that require contextual spatial awareness.
4.  **Advancements in AR/VR:** For Augmented Reality (AR) and Virtual Reality (VR) applications, a deep, language-guided understanding of the 3D environment is paramount. SplatTalk can facilitate more intelligent and intuitive AR/VR experiences, allowing users to query information about their surroundings or interact with virtual objects based on natural language descriptions of the real world.
5.  **Efficient Multimodal Integration:** The methodology of integrating high-dimensional VLM features into an efficient 3D Gaussian representation, coupled with entropy-adaptive sampling, offers a novel paradigm for bridging 2D and 3D modalities. This approach allows powerful pre-trained LLMs to directly leverage a 3D-aware visual context, potentially inspiring future research into more efficient and effective multimodal architectures.
6.  **Future Research Directions:** SplatTalk's success in leveraging multi-view RGB inputs to encapsulate rich semantic representations without explicit geometric priors opens avenues for further exploration. It encourages researchers to investigate alternative methods for learning implicit or explicit 3D structures that are optimized for semantic understanding rather than purely photorealistic rendering, potentially leading to more lightweight and capable 3D LMMs.

In conclusion, SplatTalk is a pioneering work that provides a practical, scalable, and self-supervised solution for 3D VQA, pushing the boundaries of what can be achieved with readily available 2D data. Its innovations pave the way for a new generation of 3D-aware AI systems capable of richer and more intuitive language-guided interaction with the physical world.
