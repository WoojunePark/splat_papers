---
title: "SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features"
date: 2025-02-20
arxiv: "2502.14786"
venue:
status: to-read

abstract: "We introduce SigLIP 2, a family of new multilingual vision-language encoders that build on the success of the original SigLIP. In this second iteration, we extend the original image-text training objective with several prior, independently developed techniques into a unified recipe -- this includes captioning-based pretraining, self-supervised losses (self-distillation, masked prediction) and online data curation. With these changes, SigLIP 2 models outperform their SigLIP counterparts at all model scales in core capabilities, including zero-shot classification, image-text retrieval, and transfer performance when extracting visual representations for Vision-Language Models (VLMs). Furthermore, the new training recipe leads to significant improvements on localization and dense prediction tasks. We also train variants which support multiple resolutions and preserve the input&#39;s native aspect ratio. Finally, we train on a more diverse data-mixture that includes de-biasing techniques, leading to much better multilingual understanding and improved fairness. To allow users to trade off inference cost with performance, we release model checkpoints at four sizes: ViT-B (86M), L (303M), So400m (400M), and g (1B)."

website: 
code: https://github.com/google-research/big_vision/tree/main/big_vision/configs/proj/image_text/README_siglip2.md
openreview: 
issue: 30

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

# SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features

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

![Figure](https://arxiv.org/html/2502.14786/x1.png)

*Figure 1: SigLIP 2 adds the captioning-based pretraining from LocCa [62] as well as self-distillation and masked prediction from SILC [45] and TIPS [38] (during the last 20% of training) to the sigmoid loss from SigLIP [71]. For some variants, the recipe additionally involves fine-tuning with data curation [61] or adaptation to native aspect ratio and variable sequence length [6, 12].*

![Figure](https://arxiv.org/html/2502.14786/x2.png)

*Figure 2: Per-language image-text retrieval performance for SigLIP, SigLIP 2 and mSigLIP on Crossmodal-3600 [58]. SigLIP 2 almost matches the performance of mSigLIP (SigLIP trained on multilingual data) despite performing substantially better on English vision-language tasks (Table 1).*

![Figure](https://arxiv.org/html/2502.14786/x3.png)

*Figure 3: Comparing the NaFlex (a single checkpoint per model size supporting native aspect ratio and variable sequence length/resolution) and the standard square-input SigLIP 2 variants which use a separate checkpoint for each sequence length/resolution. The sequence lengths annotated on the x-axis correspond to training sequence lengths for NaFlex. NaFlex interpolates fairly well between training resolutions, but does not extrapolate well (not shown).*

![Figure](https://arxiv.org/html/2502.14786/x4.png)

*Figure 4: Comparison of different vision encoders after training a Gemma 2 LLM for 50M steps with a frozen vision encoder (PaliGemma [7] stage 1), followed by fine-tuning the VLM on individual datasets (PaliGemma stage 3). SigLIP 2 performs better than SigLIP and AIMv2 [20] for different model sizes and resolutions. Same data as in Table 6.*

![Figure](https://arxiv.org/html/2502.14786/x5.png)

*Figure 5: 10-shot and 0-shot accuracy for geographically diverse object classification tasks (Dollar Street, GeoDE), as well as geolocalization (GeoDE country/region) and landmark localization (GLDv2) tasks. SigLIP 2 consistently performs better than SigLIP (see Table 8 for additional results).*

![Figure](https://arxiv.org/html/2502.14786/x6.png)

*Figure 6: Representation bias (association of random objects with gender; lower is better) for different models.*

## LLM Summary

## Research Paper Analysis: SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features

This report provides a detailed analysis of the research paper "SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features," published in February 2025.

### 1. Authors, Institution(s), and Notable Context

The paper is authored by a large team of researchers from **Google DeepMind**. The authors are: Michael Tschannen, Alexey Gritsenko, Xiao Wang, Muhammad Ferjad Naeem, Ibrahim Alabdulmohsin, Nikhil Parthasarathy, Talfan Evans, Lucas Beyer, Ye Xia, Basil Mustafa, Olivier Hénaff, Jeremiah Harmsen, Andreas Steiner, and Xiaohua Zhai.

Several authors are specifically noted as "Core contributors" (Michael Tschannen, Alexey Gritsenko, Xiao Wang, Muhammad Ferjad Naeem, Ibrahim Alabdulmohsin, Nikhil Parthasarathy, and Xiaohua Zhai), indicating their central role in the project. Michael Tschannen and Xiaohua Zhai are further designated as "Project leads," highlighting their leadership in this research initiative. Talfan Evans, Lucas Beyer, and Olivier Hénaff are noted as having done "Work done while at Google DeepMind," suggesting their contributions were made during their tenure at the institution.

This strong affiliation with Google DeepMind, a leading artificial intelligence research laboratory known for its foundational work in deep learning, multimodal AI, and large-scale model training, provides significant context. The research group, operating within Google DeepMind, leverages extensive computational resources (e.g., TPUs, FSDP) and access to massive datasets (e.g., WebLI) that are critical for training billion-scale vision-language models. Many of the cited works, such as SigLIP, PaLI, PaliGemma, NaViT, FlexiViT, and various data filtering and self-supervised learning techniques, originate from or involve researchers closely associated with Google or Google DeepMind. This suggests a continuous and iterative research program focused on advancing state-of-the-art vision-language understanding, building upon their own prior successes and integrating independently developed but related techniques from the broader research community. The release of "open models" is also a notable aspect, aligning with a broader trend of sharing foundational AI models to foster wider research and application development.

### 2. How This Work Fits into the Broader Research Landscape

The development of SigLIP 2 directly builds upon the success of contrastive image-text embedding models, a paradigm pioneered by foundational works like **CLIP [50]** and **ALIGN [28]**. These models revolutionized high-level semantic understanding of visual data by enabling fine-grained zero-shot classification and efficient image-text retrieval. Their capabilities were further extended when combined with Large Language Models (LLMs) to form Vision-Language Models (VLMs), opening doors for more complex vision-language understanding.

While CLIP-style models demonstrated remarkable initial success, the research community has since proposed numerous improvements to address their limitations and enhance specific functionalities. These advancements include:
*   **Data Quality and Curation:** Techniques like re-captioning images [38] or applying filtering methods [19, 66] to improve the quality of training data.
*   **Self-supervised Learning:** Incorporating image-only self-supervised losses [38, 45] to learn richer visual representations.
*   **Auxiliary Tasks and Decoders:** Adding small decoders for tasks like captioning and localization [32, 62, 67] to improve dense features and fine-grained understanding.
*   **Loss Function Modifications:** SigLIP [71] itself introduced a sigmoid loss as an alternative to the traditional contrastive loss, demonstrating improved performance.
*   **Model Architectures and Adaptations:** Innovations in handling variable resolutions and aspect ratios (e.g., NaViT [12], FlexiViT [6]).

The authors observe that existing open-source model releases generally adhere closely to CLIP's original approach and do not fully integrate the breadth of these latest improvements into a single, unified model. SigLIP 2 emerges in this context as an attempt to consolidate these disparate, yet impactful, advancements into a "unified recipe" building upon the robust SigLIP foundation. By doing so, it aims to deliver a new family of models that not only excel at core CLIP capabilities (zero-shot classification, retrieval, VLM feature extraction) but also significantly improve on areas where vanilla CLIP-style models traditionally lagged, such as localization and dense semantic representations. Furthermore, by addressing multilingual understanding and fairness, SigLIP 2 tackles critical real-world applicability and ethical considerations in VLM deployment.

### 3. Key Objectives and Motivation

The primary objective of SigLIP 2 is to introduce a new family of multilingual vision-language encoders that significantly enhance the capabilities of the original SigLIP models by integrating several independently developed, cutting-edge techniques into a cohesive training recipe.

The key motivations and specific objectives can be summarized as follows:

*   **Improved Core Capabilities:** To outperform previous SigLIP models and other baselines in fundamental vision-language tasks such as zero-shot classification, image-text retrieval, and serving as visual encoders for Vision-Language Models (VLMs).
*   **Enhanced Localization and Dense Features:** To address the limitations of vanilla CLIP-style models in tasks requiring fine-grained spatial understanding, such as semantic segmentation, depth estimation, and referring expression comprehension. This involves leveraging decoder-based pretraining and self-supervised losses.
*   **Strong Multilingual Understanding:** To provide models that perform excellently on English-focused tasks while also delivering robust results on multilingual benchmarks. This is crucial for enabling applications across diverse languages and cultural contexts.
*   **Improved Fairness:** To mitigate societal biases present in training data regarding representation and association, specifically by integrating data de-biasing techniques.
*   **Practical Utility and Versatility:**
    *   **Backward Compatibility:** To maintain architectural compatibility with original SigLIP models, allowing users to easily swap out weights and leverage existing infrastructure.
    *   **Variable Resolution and Native Aspect Ratio Support:** To introduce "NaFlex" variants that can handle multiple resolutions and preserve the native aspect ratio of images, benefiting applications like document understanding.
    *   **Strong Small Models:** To optimize the performance of smaller model scales (e.g., ViT-B) through distillation via active data curation, making them more accessible and efficient for various applications.
*   **Open-Weight Release:** To make these advanced model checkpoints publicly available, fostering innovation and application development within the open-source community.

In essence, SigLIP 2 aims to be a comprehensive, high-performing, and ethically conscious family of vision-language encoders, setting a new benchmark for unified multimodal representation learning.

### 4. Methodology and Approach

SigLIP 2's methodology is centered on extending the original SigLIP training recipe by integrating a combination of three key independent techniques in a staged approach: decoder-based pretraining (from LocCa [62]), self-distillation, and masked prediction (from SILC [45] and TIPS [38]), in addition to online data curation [61].

**Core Training Recipe Components:**

1.  **Sigmoid Loss (SigLIP v1 baseline):** The foundational component. Unlike CLIP's contrastive loss, SigLIP formulates image-text matching as a binary classification problem for all image-text pairs within a mini-batch using a logistic regression (sigmoid) loss. This loss is applied throughout the training.
2.  **Decoder-based Pretraining (LocCa Integration):**
    *   A standard transformer decoder with cross-attention is attached to the un-pooled vision encoder representation.
    *   The decoder is trained for auxiliary tasks: image captioning (using parallel prediction), automatic referring expression prediction (predicting bounding box coordinates for captions describing regions), and grounded captioning (predicting region-specific captions given bounding box coordinates).
    *   Region-caption pairs are automatically annotated using n-grams from alt-texts and open-vocabulary detection [41].
    *   This component is combined with the sigmoid loss from the very beginning of pretraining with equal weight, aiming to improve OCR capabilities and localization.
3.  **Self-supervised Losses (SILC/TIPS Integration):**
    *   Added during the last 20% of training (at 80% completion) to enhance local semantics of feature representations, crucial for dense prediction tasks.
    *   **Local-to-global consistency loss (Self-distillation):** The vision encoder (student) processes a partial (local) view of an image and is trained to match the representation of a teacher network, which processes the full image. The teacher's parameters are an exponential moving average (EMA) of the student's.
    *   **Masked prediction objective:** 50% of embedded image patches in the student network are replaced with mask tokens. The student is trained to match the teacher's features at these masked locations, with both student and teacher seeing the same global view (up to masking in the student).
    *   These losses are applied on additional augmented views to avoid negatively impacting image-text alignment, with specific weighting factors for different model sizes to balance global and dense task quality.

**Architecture and Data:**

*   **Architecture:** Follows SigLIP, using standard ViT architecture [15] with learned positional embeddings. A MAP head [69] is used for vision and text representation pooling. The text encoder uses the multilingual Gemma tokenizer [22] (vocabulary size 256k) with a text length of 64.
*   **Training Data:** The WebLI dataset [10] is used, comprising 10 billion images and 12 billion alt-texts across 109 languages. A data mixture of 90% English and 10% non-English image-text pairs is used, as recommended in [49], for balance between English and multilingual performance.
*   **Fairness Mitigation:** Filtering techniques from [2] are applied to mitigate biases related to sensitive attributes (e.g., gender representation and association).
*   **Optimizer and Compute:** Adam optimizer (learning rate 10^-3, weight decay 10^-4), batch size of 32k, cosine schedule with 20k warmup steps, trained for 40B examples on up to 2048 TPUv5e chips [24] using a fully-sharded data-parallel (FSDP) strategy [72].

**Resolution Adaptation Variants:**

1.  **Fixed-resolution variant:** Checkpoints are resumed at 95% of training, positional embeddings are resized to target sequence length, and training continues at the new resolution with all losses.
2.  **Variable Aspect and Resolution (NaFlex) variant:** Combines FlexiViT [6] (multiple predefined sequence lengths) and NaViT [12] (preserving native aspect ratio).
    *   Images are resized to be multiples of patch size while minimizing aspect ratio distortion and keeping sequence length below a target.
    *   Bilinear resizing of learned positional embeddings adapts to non-square patch grids.
    *   Attention layers are masked for padding tokens.
    *   Training starts at 90% completion from default checkpoints, switching to aspect-preserving resizing and uniformly sampling sequence lengths ({128, 256, 576, 784, 1024}) per mini-batch.
    *   Self-distillation and masked prediction losses are *not* applied to NaFlex variants to manage complexity.

**Distillation via Active Data Curation:**

*   To boost performance of smaller fixed-resolution models (ViT-B/16 and B/32), implicit "distillation through data" is applied using the ACID method [61] during a short fine-tuning stage (additional 4B examples).
*   A strong teacher model (SigLIP 2 So400m), fine-tuned on a high-quality curated dataset [16], scores "learnability" of examples. These scores are used to select an optimal batch from a larger super-batch. This approach aims to recover benefits of explicit distillation without its computational overhead.

### 5. Main Findings and Results

SigLIP 2 demonstrates significant improvements across a wide array of vision-language tasks and benchmarks, often outperforming its predecessor SigLIP and other leading open-source models.

**5.1. Zero-shot Classification and Retrieval (Table 1, Figure 2):**
*   SigLIP 2 consistently outperforms SigLIP and other open-weight baselines (CLIP, OpenCLIP, MetaCLIP, EVA-CLIP, DFN) across zero-shot classification benchmarks (ImageNet, ObjectNet, ImageNet-v2, ImageNet ReaL) and image-text retrieval (COCO, Flickr).
*   The improvements are particularly pronounced for the smaller B-sized models, attributed to the active data curation/distillation technique.
*   On the multilingual Crossmodal-3600 (XM3600) retrieval benchmark (36 languages), SigLIP 2 substantially exceeds SigLIP's recall and nearly matches mSigLIP (a SigLIP variant specifically trained on multilingual data), despite SigLIP 2's superior English performance.

**5.2. NaFlex Variant (Figure 3, Table 7):**
*   The NaFlex variant, supporting variable resolutions and native aspect ratios, generally outperforms the standard square-input SigLIP 2 variants on most OCR/document/screen-focused image-text retrieval benchmarks (TextCaps, HierText, SciCap, Screen2Words), especially at smaller sequence lengths.
*   For natural image benchmarks, the standard B-sized variant performs better (likely due to distillation), while the So400m NaFlex variant is on par with its standard counterpart. This highlights the practical benefits of NaFlex for aspect-sensitive applications.

**5.3. SigLIP 2 as a Vision Encoder for VLMs (Figure 4, Table 6):**
*   When used as a frozen vision encoder for a Gemma 2B LLM (following the PaliGemma 2 recipe), SigLIP 2 consistently outperforms SigLIP across various multimodal benchmarks (VQA, captioning, grounded captioning, OCR-VQA, etc.) for different model sizes and resolutions.
*   SigLIP 2 also surpasses the recently released AIMv2 model for L-sized vision encoders, indicating its effectiveness as a foundational visual component for VLMs.

**5.4. Dense Prediction Tasks (Table 2, Table 3):**
*   **Semantic Segmentation, Depth Estimation, Surface Normal Estimation:** Probing the frozen SigLIP 2 representation (with a linear layer or DPT decoder) shows SigLIP 2 significantly outperforms other open, CLIP-style vision encoders (CLIP, OpenCLIP, SigLIP) on benchmarks like PASCAL, ADE20k, NYUv2, and NAVI. This confirms the efficacy of incorporated self-supervised and decoder-based losses for learning dense features.
*   **Open-vocabulary Segmentation:** Using Cat-Seg [11] framework, SigLIP 2 (L/16) demonstrates improvements over SigLIP and even outcompetes the larger OpenCLIP G/14 model on various Pascal and ADE20k datasets, showcasing its enhanced capabilities for segmenting novel classes.

**5.5. Localization Tasks (Table 5, Table 4):**
*   **Referring Expression Comprehension:** On RefCOCO variants, SigLIP 2 substantially outperforms SigLIP, CLIP, and image-captioning pretraining (Cap) by a large margin. This is attributed to the decoder-based pretraining (LocCa). SigLIP 2 is only marginally outperformed by LocCa, which was trained exclusively on English data, suggesting a trade-off with multilingual coverage.
*   **Open-vocabulary Detection:** When adapted via OWL-ViT [40], SigLIP 2 achieves better performance than SigLIP on COCO and LVIS, with the most pronounced improvements observed for LVIS rare categories.

**5.6. Cultural Diversity and Fairness (Figure 5, Figure 6, Table 8, Table 9):**
*   **Cultural Diversity:** SigLIP 2 shows consistent improvements over SigLIP on geographically diverse object classification tasks (Dollar Street, GeoDE) and geolocalization tasks (GeoDE country/region, GLDv2). For instance, 10-shot geolocalization accuracy in GeoDE (region) improves from 36.2% (SigLIP L/16) to 44.4% (SigLIP 2 L/16).
*   **Fairness (Representation Bias):** SigLIP 2 significantly reduces representation bias (the tendency to associate random objects with a particular gender group) compared to SigLIP. For example, SigLIP L/16 has a 35.5% bias, while SigLIP 2 of the same size has only 7.3%. Larger models also tend to exhibit less representation bias. Minor benefits are observed for income level and geographic region disparity.

### 6. Significance and Potential Impact

SigLIP 2 represents a significant advancement in the field of vision-language models, offering a highly capable and versatile family of encoders with a broad range of implications:

*   **Setting a New State-of-the-Art:** By unifying and effectively combining several independently developed techniques (captioning-based pretraining, self-supervised losses, and active data curation), SigLIP 2 achieves superior performance across a diverse set of benchmarks, including zero-shot classification, retrieval, dense prediction, and localization tasks. This "unified recipe" approach demonstrates that integrating these methods can yield compounded benefits beyond individual application.
*   **Enhanced Multimodal Understanding:** The substantial improvements in localization and dense feature extraction directly address critical limitations of earlier CLIP-style models, opening doors for more precise and fine-grained applications such as advanced image editing, robotics, and medical imaging.
*   **True Multilinguality and Fairness:** The deliberate inclusion of diverse language data and the application of de-biasing techniques lead to improved multilingual understanding and significantly reduced representation bias. This is crucial for developing AI systems that are more inclusive, equitable, and globally applicable, minimizing the risk of perpetuating societal biases.
*   **Practical Deployment and Accessibility:**
    *   The "NaFlex" variant's ability to handle variable resolutions and native aspect ratios makes SigLIP 2 exceptionally well-suited for specialized applications like document analysis, OCR, and user interface understanding, where aspect ratio preservation is critical.
    *   The optimization of smaller model sizes through distillation makes high-performance vision-language capabilities more accessible for deployments with limited computational resources, democratizing access to powerful AI models.
    *   Backward compatibility with the original SigLIP architecture simplifies adoption for existing users, enabling them to upgrade their models with minimal effort.
*   **Catalyst for Open-Source Innovation:** The release of SigLIP 2 model checkpoints as open-weight resources is highly significant. It allows researchers, developers, and practitioners worldwide to build upon this advanced foundation, fostering further innovation in multimodal AI research, enabling the creation of new applications, and facilitating independent verification and extension of the reported findings.

In conclusion, SigLIP 2 pushes the boundaries of vision-language understanding by demonstrating that a synergistic combination of advanced training techniques can yield a robust, versatile, and ethically more responsible family of models. Its open-source release is poised to accelerate progress and enable diverse applications within the broader AI community.
