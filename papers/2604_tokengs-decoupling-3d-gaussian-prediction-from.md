---
title: "TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens"
date: 2026-04-16
arxiv: "2604.15239v1"
venue:
status: to-read

abstract: "In this work, we revisit several key design choices of modern Transformer-based approaches for feed-forward 3D Gaussian Splatting (3DGS) prediction. We argue that the common practice of regressing Gaussian means as depths along camera rays is suboptimal, and instead propose to directly regress 3D mean coordinates using only a self-supervised rendering loss. This formulation allows us to move from the standard encoder-only design to an encoder-decoder architecture with learnable Gaussian tokens, thereby unbinding the number of predicted primitives from input image resolution and number of views. Our resulting method, TokenGS, demonstrates improved robustness to pose noise and multiview inconsistencies, while naturally supporting efficient test-time optimization in token space without degrading learned priors. TokenGS achieves state-of-the-art feed-forward reconstruction performance on both static and dynamic scenes, producing more regularized geometry and more balanced 3DGS distribution, while seamlessly recovering emergent scene attributes such as static-dynamic decomposition and scene flow."

website: https://research.nvidia.com/labs/toronto-ai/tokengs
code: https://github.com/nv-tlabs/TokenGS
openreview: 
issue: 44

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

# TokenGS: Decoupling 3D Gaussian Prediction from Pixels with Learnable Tokens

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

![Figure](https://arxiv.org/html/2604.15239v1/x1.png)

*Figure 1: TokenGS is a feed-forward reconstruction framework that outputs a 3D Gaussian Splatting (3DGS) representation from posed input images. Our novel encoder-decoder architecture detaches 3D Gaussians from input pixels and enables multiple properties desirable for 3D reconstruction, as demonstrated in each example.*

![Figure](https://arxiv.org/html/2604.15239v1/x2.png)

*Figure 2: Our method. We design a novel network architecture that reconstructs 3DGS from input images, directly predicting 3D Gaussian mean coordinates. The model follows an encoder-decoder structure. In the decoder, 3DGS tokens are fed in as queries to obtain the final Gaussian attributes. After the base model is trained, we allow test-time token tuning from input images to improve reconstruction quality.*

![Figure](https://arxiv.org/html/2604.15239v1/x3.png)

*Figure 3: Comparison of 3DGS parametrizations in feed-forward networks. While all methods reconstruct the single input view well (shown in the inset), the quality of the occluded region behind the table varies.*

![Figure](https://arxiv.org/html/2604.15239v1/x4.png)

**

![Figure](https://arxiv.org/html/2604.15239v1/x5.png)

*Figure 4: Attention masking for dynamic scenes. The figure shows one instantiation of the 3DGS self-attention block. The horizontal axis shows queries, while the vertical axis shows keys/values of the corresponding tokens.*

![Figure](https://arxiv.org/html/2604.15239v1/x6.png)

*Figure 5: Qualitative results on RE10K [56]. Compared to the pixel-aligned Gaussian prediction of GS-LRM [54], our formulation, which is based on direct XYZ prediction and decoupling from pixel rays, produces noticeably cleaner geometry with fewer spiky artifacts.*

![Figure](https://arxiv.org/html/2604.15239v1/x7.png)

*Figure 6: View Extrapolation. Both GS-LRM and our model have been finetuned for view extrapolation. The lower-left inset figures show the ground-truth images.*

![Figure](https://arxiv.org/html/2604.15239v1/x8.png)

*Figure 7: Reconstruction under camera noise on 2-view RE10K. We add camera pose noise of magnitude 1–10 degrees to the non-reference view. We show the difference to GS-LRM [54] in terms of PSNR and LPIPS. Note, that we visualize −Δ​LPIPS-\Delta\text{LPIPS} so higher values indicate better performance for both metrics.*

![Figure](https://arxiv.org/html/2604.15239v1/x9.png)

*Figure 8: Dynamic reconstruction on Kubric [13]. We show in-between time stamps to examine temporal consistency.*

![Figure](https://arxiv.org/html/2604.15239v1/x10.png)

*Figure 9: Emergent scene flow. We visualize the trajectories of each dynamic Gaussian across time.*

![Figure](https://arxiv.org/html/2604.15239v1/figures/gaussian_token_binding/regular_rendering.png)

*Figure 10: Token assignments. Left: rendering. Center: GS from 5 random tokens highlighted with per-token colors to show their location across scenes. Others set to gray; overlaid with GT image. Right: GS from each token assigned a consistent color.*

![Figure](https://arxiv.org/html/2604.15239v1/x11.png)

*Figure 11: Effect of the visibility loss. Regularizing the model removes floaters from unobserved parts of the scene and improves the final PSNR on novel views.*

![Figure](https://arxiv.org/html/2604.15239v1/x12.png)

*Figure 12: Test-time scaling: PSNR when scaling #input views vs #gradient steps in two variants: optimizing Gaussian tokens (solid) or Gaussian parameters directly (dashed).*

![Figure](https://arxiv.org/html/2604.15239v1/x13.png)

*Figure 13: Center: renders of a feed-forward reconstruction from 4 views, completely novel viewpoint. Left: Gaussian Tuning degrades scene geometry, despite quantitative advantage on close-by views. Right: Our Token Tuning (TT) improves scene geometry with sharper renderings.*

![Figure](https://arxiv.org/html/2604.15239v1/x14.png)

*Figure 14: PSNR vs # Gaussian tokens. We study how reconstruction quality changes with different numbers of Gaussian tokens given fixed number of input views.*

## LLM Summary

### 1. Authors and Institution(s)

The research was conducted by Jiawei Ren, Michal Jan Tyszkiewicz, Jiahui Huang, and Zan Gojcic. All authors are affiliated with NVIDIA.

### 2. How This Work Fits into the Broader Research Landscape

The work presented in "TokenGS" is situated within the rapidly evolving field of feed-forward 3D reconstruction, particularly focusing on methods that predict 3D Gaussian Splatting (3DGS) representations directly from input images. This area has seen significant advancements in reconstruction quality, scalability to large datasets, and support for dynamic scenes, with some feed-forward techniques beginning to approach the fidelity of computationally intensive per-scene optimization methods.

Prior feed-forward approaches often employ large encoder-only Transformer backbones to predict pixel-aligned 3D Gaussian primitives. These methods typically regress Gaussian means as depths along camera rays, coupling the number of predicted Gaussians to the input image resolution and the number of views. This paradigm has inherent limitations, such as difficulty in correcting for noisy camera poses or multiview inconsistencies, challenges in dynamic scene modeling where points must be warped over time, and an often excessive number of primitives that scales with input view count regardless of intrinsic scene complexity. Additionally, direct optimization of Gaussian parameters during test-time refinement can degrade learned network priors.

TokenGS addresses these limitations by proposing a fundamental shift in the design of feed-forward 3DGS prediction. It moves away from pixel-aligned depth regression and encoder-only architectures towards direct 3D coordinate regression and an encoder-decoder Transformer structure utilizing learnable Gaussian tokens. This architectural change aims to decouple the 3DGS representation from input pixels and view properties, offering a more flexible and robust framework for 3D reconstruction. The work also incorporates advancements in test-time scaling, a concept explored in various fields like large language models and computer vision, by enabling refinement in a token space that preserves global priors. TokenGS positions itself as an advancement towards more efficient, robust, and geometrically consistent feed-forward 3D reconstruction, including for dynamic scenes and under challenging input conditions like pose noise.

### 3. Key Objectives and Motivation

The primary objectives of the TokenGS research are to address several limitations identified in the prevailing Transformer-based feed-forward 3D Gaussian Splatting (3DGS) prediction methods. The authors articulate specific motivations for their proposed design choices:

1.  **Address Suboptimal Gaussian Mean Regression:** Current methods commonly regress Gaussian means as depths along camera rays. The authors contend that this approach is suboptimal because it restricts the model's capacity to internally correct for noisy camera poses and multiview inconsistencies. Furthermore, it introduces complications for dynamic scenes, where points and pixels necessitate warping over time. TokenGS aims to overcome this by directly regressing 3D mean coordinates in a global canonical coordinate space.

2.  **Decouple Primitive Count from Input Properties:** The standard practice of linking the number of predicted Gaussians to the input image resolution and the number of views (e.g., one particle per pixel or patch) leads to an excessive and often redundant number of primitives. For instance, multiple input images of the same scene result in a proportional increase in Gaussians, irrespective of the scene's inherent complexity. A key objective for TokenGS is to unbind the number of predicted primitives from input image resolution and the number of views, allowing the model to allocate Gaussians based on scene complexity rather than input pixel count.

3.  **Enable Robust Test-Time Optimization:** While feed-forward neural reconstruction methods can benefit from self-supervised test-time refinement, directly optimizing the Gaussian parameters tends to degrade the network's learned priors, especially in scenarios with a low number of input views. TokenGS seeks to enable efficient and effective test-time optimization by refining only learnable token embeddings, thereby preserving the global priors embedded within the model.

4.  **Improve Robustness and Geometric Quality:** By decoupling Gaussian prediction from input pixels, the authors aim to enhance the model's robustness to noisy camera poses and multiview inconsistencies. This decoupling is also hypothesized to yield more regularized geometry, eliminating common artifacts like "spikes" observed in depth-prediction networks, and facilitating scene completion beyond the immediate input views.

5.  **Support Dynamic Scene Reconstruction:** Existing pixel-aligned formulations can struggle with dynamic content due to the fixed nature of pixel correspondences. An objective of TokenGS is to naturally extend 3DGS prediction to dynamic scenes by allowing Gaussian coordinates to be continuous in time, facilitating consistent tracking and decomposition into static and dynamic scene components.

6.  **Achieve State-of-the-Art Performance:** Ultimately, the motivation is to develop a feed-forward 3DGS framework, TokenGS, that demonstrates improved reconstruction quality and efficiency, producing compact representations with more regularized geometry, and seamlessly recovering emergent scene attributes such as static-dynamic decomposition and scene flow, thereby establishing new performance benchmarks in the field.

### 4. Methodology and Approach

TokenGS employs a novel encoder-decoder Transformer architecture designed to predict 3D Gaussian Splatting (3DGS) representations directly from posed input images, decoupling Gaussian prediction from pixel-level operations.

**4.1. Network Architecture**
The core of TokenGS is an encoder-decoder Transformer. The encoder processes input images and camera parameters into image tokens. The decoder then utilizes learnable 3DGS tokens that cross-attend to these image tokens to predict the final 3DGS parameters.

*   **Encoder:** A Vision Transformer (ViT)-based encoder is used. Each input view is first divided into patches, which are then projected into a C-dimensional latent space. Simultaneously, Plücker coordinates associated with each patch are projected. These two embeddings are summed, flattened, and passed through standard ViT layers, allowing self-attention across all views to produce image tokens.
*   **Decoder:** The decoder follows a DETR-like design. It initializes a set of $N_t$ learnable token embeddings, referred to as 3DGS tokens. These tokens act as queries in Transformer decoder blocks, engaging in cross-attention with the image tokens and self-attention among themselves. A per-token Multi-Layer Perceptron (MLP) then refines these embeddings.
*   **Gaussian Parameter Regression:** From each output embedding of the decoder, 14 Gaussian attributes (mean ($\mu$), color ($c$), scale ($s$), opacity ($\sigma$), and rotation ($q$)) are regressed for $N_G = 64$ Gaussian primitives using a linear layer. Specific activation functions are applied: $f(x) = \text{sign}(x) \cdot (\text{exp}(x) - 1)$ for XYZ coordinates, scaled tanh for color and opacity, clipped exponential for scale, and unit normalization for rotation.
*   **Efficiency Measures:** To manage memory, all decoder cross-attention layers share their key-value projections of image tokens, reducing memory allocation from $O(N_I D_{dec})$ to $O(N_I)$ where $N_I$ is the number of image tokens and $D_{dec}$ is decoder depth. LayerScale and QK-normalization are employed for training stability, while Layer Normalization is omitted before the final regression head.

**4.2. Direct Regression of Gaussian Means**
Instead of the common practice of predicting depth along camera rays, TokenGS directly regresses the 3D coordinates ($ \mu $) of Gaussian means in a global, canonical coordinate frame. This approach aims to improve extrapolation, robustness to pose noise, and reduce spiky artifacts in geometry.

*   **Zero-Gradient Problem:** A challenge with direct 3D coordinate regression is that Gaussians outside camera frusta receive no gradients from rendering loss, potentially leading to "inactive" or noisy floating points.
*   **Visibility Loss ($L_{vis}$):** To mitigate the zero-gradient problem without requiring explicit 3D supervision, a visibility loss is introduced. This loss softly constrains Gaussian particles to remain visible in at least one supervision view. It measures the minimum distance from each Gaussian's projected centroid to the nearest image boundary, providing gradients to pull Gaussians back into view if they drift out.
*   **Total Loss Function:** The model is supervised using a combination of pixel-wise mean squared error ($L_{MSE}$), SSIM loss ($L_{SSIM}$), and the proposed visibility loss ($L_{vis}$): $L = L_{MSE} + \lambda_{SSIM} L_{SSIM} + \lambda_{vis} L_{vis}$.

**4.3. Dynamic Scene Modeling**
For dynamic scenes, TokenGS extends its framework using time-conditioned dynamic 3DGS tokens in a "bullet-time" reconstruction formulation.

*   **Token Split and Time Embedding:** The 3DGS tokens are split into static tokens ($T_S$) and dynamic tokens ($T_D$). Dynamic tokens are augmented with a learnable time embedding representing the target frame, using a sinusoidal encoding linearly projected to the latent space. Static tokens remain time-invariant.
*   **Attention Masking:** A structured attention mask is applied during the self-attention phase of the decoder. Dynamic tokens are allowed to attend unidirectionally to static tokens, establishing an inductive bias that the dynamic parts of the scene depend on the static structure. This promotes decomposition of the scene into static and motion components and maintains consistent correspondences over time.

**4.4. Test-Time Scaling (TTS)**
TokenGS supports two forms of test-time scaling without requiring network retraining:

*   **Context Extension (CE):** More image tokens can be supplied at inference time than during training (e.g., more input views). Crucially, the number of predicted Gaussians remains fixed and independent of the context length, unlike pixel-aligned methods.
*   **Token-Tuning (TT):** A lightweight procedure where only the Gaussian token embeddings are fine-tuned using self-supervision on the input views, while the network parameters and image features remain frozen. This refinement adapts attention patterns to the specific scene, improving Gaussian parameters while preserving learned priors.

**4.5. Training Details**
The model is optimized using the AdamW optimizer. Training involves a base model phase (150K iterations with 1024 Gaussian tokens) followed by a finetuning phase (10K iterations with 4096 Gaussian tokens), adjusting resolution as needed. Cosine learning rate schedulers are used with warm-up. Gradient clipping, weight decay, and random flip augmentation are applied. Camera translations are rescaled for different datasets. For token tuning, typically 50 steps with a specific learning rate are used.

### 5. Main Findings and Results

The research demonstrates that TokenGS achieves notable performance improvements and introduces new capabilities in feed-forward 3D Gaussian Splatting.

**5.1. Static Scene Reconstruction**
*   **Quantitative Performance:** On the RealEstate10K (RE10K) dataset with two input views, TokenGS (4096 tokens, +TT) achieves higher PSNR (28.82), SSIM (0.910), and lower LPIPS (0.130) compared to baselines like MVSplat (PSNR 26.39), DepthSplat (PSNR 27.47), and GS-LRM (PSNR 28.10). Notably, the base model (1024 tokens) achieves competitive performance with half the Gaussians of baselines, and the finetuned model (4096 tokens) excels with 2x the Gaussians.
*   **Gaussian Control:** The method allows flexible control over the number of Gaussians, which can be adjusted independently of input resolution or view count, enabling trade-offs between compression and quality.
*   **Geometric Quality:** Qualitative comparisons on RE10K show that TokenGS produces cleaner geometry with fewer "spiky artifacts" compared to pixel-aligned methods like GS-LRM, attributed to its direct 3D coordinate prediction and decoupling from pixel rays.
*   **Generalization on DL3DV:** On the DL3DV dataset, TokenGS, trained on 4-view input, demonstrates competitive performance even when generalizing to 2-view and 6-view settings (context extension) without additional finetuning. With token tuning (+TT), it outperforms baselines in the 6-view setting while using significantly fewer Gaussians (262k vs. 688k).

**5.2. View Extrapolation**
*   TokenGS outperforms baselines (DepthSplat, MVSplat) and even those finetuned with explicit point map supervision (MVSplat+PM, DepthSplat+PM) on view extrapolation benchmarks (DL3DV and RE10K).
*   The decoupled Gaussian prediction enables the model to reconstruct more complete geometry in regions unobserved by input cameras, reinforcing its capability for scene completion.

**5.3. Reconstruction with Camera Noise**
*   TokenGS exhibits increased robustness to noisy camera poses. When random rotations are injected into camera poses on RE10K, the performance gap between TokenGS and GS-LRM widens in favor of TokenGS as noise magnitude increases (from 1 to 10 degrees), indicating less susceptibility to input pose errors.

**5.4. Dynamic Reconstruction**
*   **Quantitative Performance:** On the Kubric 4D dataset with 4 input views, TokenGS (PSNR 24.84) outperforms BTimer (PSNR 24.45).
*   **Temporal Consistency and Scene Flow:** Due to its prediction of 3D coordinates continuous in time, TokenGS reconstructs object motion more effectively than pixel-aligned representations, which often compensate by varying Gaussian opacity. This is particularly evident in intermediate timestamps. The model can provide consistent tracking over time and recovers emergent scene flow, visualized through Gaussian trajectories.
*   **Static-Dynamic Decomposition:** The structured attention masking for static and dynamic tokens enables the model to decompose scenes into time-invariant and time-varying components.

**5.5. Ablation Studies**
*   **Spatial Token Correspondence:** Visualization indicates that Gaussians decoded from a single token tend to cluster spatially within a scene and maintain similar 3D locations across different scenes, akin to "slot specialization." Regions with higher frequency details receive more tokens/Gaussians.
*   **Visibility Loss:** The visibility loss term is crucial for preventing degraded geometry (e.g., floating noisy points) from unobserved parts of the scene, resulting in a 0.4 PSNR improvement on RE10K.
*   **Test-Time Scaling (TTS):**
    *   **Context Extension:** TokenGS benefits from providing up to 4x more input views than it was trained for, leading to performance improvements before saturation.
    *   **Token-Tuning (TT):** Even a small number of optimization steps (e.g., 10 steps) for Gaussian tokens significantly improves PSNR, with benefits continuing up to 250 steps. Critically, TT improves scene geometry with sharper renderings, whereas direct Gaussian parameter tuning, while sometimes achieving higher PSNR and faster convergence on close-by views, often degrades scene geometry due to a loss of learned priors.
*   **Effect of Number of Tokens:** The approach offers independent control over both the number of Gaussians and input views. Increasing the number of Gaussian tokens from 256 to 4096 generally improves reconstruction quality, allowing flexibility in balancing compression efficiency and visual fidelity.

### 6. Significance and Potential Impact

TokenGS represents a methodological advancement in feed-forward 3D reconstruction using Gaussian Splatting, with several areas of potential impact:

1.  **Enhanced Robustness and Generalization:** By directly regressing 3D Gaussian coordinates and decoupling the prediction from pixel-aligned depths, TokenGS demonstrates improved robustness to noisy camera poses and multiview inconsistencies. This can lead to more reliable 3D reconstructions in real-world scenarios where precise pose information may be challenging to acquire. Its improved view extrapolation capabilities also suggest better generalization to novel viewpoints.

2.  **More Compact and Flexible Representations:** The introduction of learnable Gaussian tokens enables the decoupling of the number of predicted primitives from the input image resolution and the number of views. This allows for creating more compact 3D representations whose density can be scaled according to scene complexity rather than input data quantity, potentially leading to more efficient storage and processing, especially for large datasets or limited compute environments. This flexibility in controlling the number of Gaussians offers a tunable trade-off between reconstruction quality and computational resources.

3.  **Improved Geometric Fidelity:** The direct 3D coordinate regression, combined with the proposed visibility loss, contributes to more regularized and cleaner geometry, reducing common artifacts like "spiky" formations often seen in depth-prediction methods. This directly impacts the visual quality and utility of the reconstructed 3D models.

4.  **Advancements in Dynamic Scene Reconstruction:** TokenGS provides a more effective approach to modeling dynamic scenes. By enabling Gaussian centers to move continuously in 3D space and time, and through its causal attention masking for static-dynamic decomposition, the method facilitates more accurate object motion reconstruction and consistent tracking across frames. The emergent recovery of scene flow is a valuable capability for understanding dynamic environments.

5.  **Novel Test-Time Optimization Paradigm:** The proposed "token-tuning" mechanism offers a lightweight yet effective way to refine reconstruction quality at inference time without degrading the global learned priors of the network. This opens avenues for adaptive and personalized 3D reconstruction, where a base model can be quickly tailored to specific scene details or preferences, combining the generalization power of learned priors with the precision of per-scene optimization. This hybrid approach could reduce the need for extensive retraining and improve usability.

6.  **Broader Applicability:** The architectural innovations and demonstrated capabilities of TokenGS could impact various applications, including augmented and virtual reality, autonomous navigation, 3D content creation, and real-time scene understanding, where high-quality, real-time 3D reconstruction from limited inputs is crucial.

Despite these advancements, the authors acknowledge limitations, such as potential struggles with large-scale environments and fine-grained geometric detail, and the relatively high cost of token tuning. These represent areas for future research, including exploring hybrid optimization strategies that combine token and Gaussian parameter tuning, which could further enhance the impact of this work.
