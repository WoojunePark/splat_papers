---
title: "GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens"
date: 2026-04-16
arxiv: "2604.15284v1"
venue:
status: to-read

abstract: "The efficient spatial allocation of primitives serves as the foundation of 3D Gaussian Splatting, as it directly dictates the synergy between representation compactness, reconstruction speed, and rendering fidelity. Previous solutions, whether based on iterative optimization or feed-forward inference, suffer from significant trade-offs between these goals, mainly due to the reliance on local, heuristic-driven allocation strategies that lack global scene awareness. Specifically, current feed-forward methods are largely pixel-aligned or voxel-aligned. By unprojecting pixels into dense, view-aligned primitives, they bake redundancy into the 3D asset. As more input views are added, the representation size increases and global consistency becomes fragile. To this end, we introduce GlobalSplat, a framework built on the principle of align first, decode later. Our approach learns a compact, global, latent scene representation that encodes multi-view input and resolves cross-view correspondences before decoding any explicit 3D geometry. Crucially, this formulation enables compact, globally consistent reconstructions without relying on pretrained pixel-prediction backbones or reusing latent features from dense baselines. Utilizing a coarse-to-fine training curriculum that gradually increases decoded capacity, GlobalSplat natively prevents representation bloat. On RealEstate10K and ACID, our model achieves competitive novel-view synthesis performance while utilizing as few as 16K Gaussians, significantly less than required by dense pipelines, obtaining a light 4MB footprint. Further, GlobalSplat enables significantly faster inference than the baselines, operating under 78 milliseconds in a single forward pass. Project page is available at this https URL"

website: https://r-itk.github.io/globalsplat
code: 
openreview: 
issue: 37

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

# GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens

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

![Figure](https://arxiv.org/html/2604.15284v1/x1.png)

*Figure 1: Align First, Decode Later. Top: Existing feed-forward 3D Gaussian Splatting pipelines rely on view-centric, per-pixel primitive allocation. As the number of input views increases, these approaches bake massive redundancy into the 3D representation, scaling to hundreds of thousands or millions of Gaussians. In contrast, GlobalSplat aggregates multi-view inputs into a fixed set of global latent scene tokens before decoding geometry. This achieves an optimal balance: for instance, for 24 input views on RealEstate10K, GlobalSplat delivers highly competitive novel-view synthesis quality (28.5 PSNR), utilizing only 16K Gaussians and offering ultra-low GPU memory usage (1.79 GB), minimal disk size (&lt;&lt;4 MB), and extremely fast inference times (&lt;&lt;78 ms). Bottom Right: This scene-centric approach translates to a significantly stronger practical operating point in comparison to state-of-the art approaches, as demonstrated in the radar chart (evaluated on 24 input views on RealEstate10K). Bottom Left: By decoding from a global scene context (without a fixed grid), GlobalSplat stays sparse and places primitives at occupied 3D locations. This yields an adaptive allocation where low-frequency regions are covered by fewer Gaussians with larger spatial support (higher coverage), enabling complex scenes with far fewer primitives. We visualize the Gaussians as disks corresponding to their scale, as well as the Gaussian centers using a point cloud. As can be seen, this allows the model to effectively capture complex environments with drastically fewer primitives.*

![Figure](https://arxiv.org/html/2604.15284v1/x5.png)

*Figure 2: GlobalSplat Architecture Overview. Given a sparse set of input views, image features are extracted via a View Encoder. A fixed set of learnable latent scene tokens is iteratively refined through a dual-branch encoder block (repeated BB times) designed to explicitly disentangle geometry and appearance. Within each branch, queries (QG,QAQ_{G},Q_{A}) cross-attend to multi-view features (KI,VIK_{I},V_{I}) and self-attend to global context. The streams are fused via a Mixer MLP to update the tokens for the subsequent block. Specialized Geometry and Appearance Decoders then transform these globally-aware tokens into explicit 3D Gaussians. As depicted on the right, the network employs a Coarse-to-Fine Training Curriculum strategy to progressively increase the decoded Gaussian capacity, supervised jointly by rendering, self-supervised consistency, and regularization losses.*

![Figure](https://arxiv.org/html/2604.15284v1/figures/images/gathered_scene_images/0aacb1732fee7a3c/zpressor/000.png)

*Figure 3: Qualitative comparison. We compare GlobalSplat against baselines (Zpressor, DepthSplat, GGN, C3G) and the ground truth (GT) across 6 different scenes (rows).*

![Figure](https://arxiv.org/html/2604.15284v1/figures/images/gathered_scene_images-acid/0a6d679da1d11d4a/zpressor/000.png)

*Figure 4: Qualitative comparison on ACID. We compare GlobalSplat against baselines (Zpressor, DepthSplat, GGN, C3G) and the ground truth (GT) across 6 different ACID scenes (rows).*

## LLM Summary

This report provides a detailed analysis of the research paper "GlobalSplat: Efficient Feed-Forward 3D Gaussian Splatting via Global Scene Tokens."

### 1. Authors and Institution(s)

The research was conducted by:
*   **Roni Itkin, Noam Issachar, Yehonatan Keypur, and Sagie Benaim** from The Hebrew University of Jerusalem.
*   **Xingyu Chen and Anpei Chen** from Westlake University.

### 2. How This Work Fits into the Broader Research Landscape

The field of novel-view synthesis (NVS) has seen substantial advancements, with 3D Gaussian Splatting (3DGS) emerging as an explicit scene representation that enables efficient rendering. Within this domain, a key challenge involves the efficient spatial allocation of primitives, which directly influences the balance between representation compactness, reconstruction speed, and rendering fidelity.

Prior solutions in NVS can be broadly categorized into optimization-based and feed-forward approaches. Optimization-based methods, such as Neural Radiance Fields (NeRF) and initial 3DGS implementations, typically achieve high-quality per-scene reconstruction but necessitate extensive per-scene optimization, limiting their generalizability and real-time application. Efforts have been made to compress these explicit 3DGS representations or derive hierarchical levels of detail, but these still largely depend on per-scene optimization.

More recently, feed-forward 3DGS approaches have aimed to predict explicit Gaussian scene representations directly from input views in a single network pass, thereby enabling generalizable NVS without per-scene optimization. These methods offer benefits for efficient rendering and deployment. However, the paper identifies a limitation in many existing feed-forward 3DGS pipelines: they often decode scene primitives from dense, view-aligned intermediates (e.g., pixel-aligned predictions, lifted per-view features, or voxel-aligned outputs). This "view-centric" primitive formation tends to introduce redundancy, inflate representation size, and complicate the achievement of global consistency, particularly as the number of input views increases to provide broader scene coverage. Such approaches tie primitive formation to local image or grid structures, rather than the intrinsic global structure of the scene.

GlobalSplat positions itself to address this specific limitation. It departs from view-centric primitive formation by proposing an "align first, decode later" strategy. This involves fusing all input views into a globally aligned latent scene representation *before* decoding explicit 3D Gaussians. By shifting to a "scene-centric" primitive formation, GlobalSplat seeks to achieve more efficient Gaussian placement and improved global coherence, resulting in a more compact, globally consistent 3D representation with reduced memory footprint and faster inference times, especially in multi-view, large-context settings. The work is complementary to recent efforts in feed-forward 3D reconstruction that focus on global aggregation and methods that aim for compact Gaussian representations, distinguishing itself by its specific architectural design for global alignment and disentangled processing of geometry and appearance.

### 3. Key Objectives and Motivation

The primary objective of this research is to develop an efficient feed-forward 3D Gaussian Splatting framework capable of generating a highly compact set of 3D Gaussians from multiple input views in a single network pass. This framework aims to utilize a fast and lightweight architecture while achieving competitive novel-view synthesis quality.

The motivation for pursuing this objective stems from several identified limitations in existing feed-forward 3DGS pipelines:

1.  **Representation Bloat and Redundancy:** Current feed-forward methods frequently rely on local, heuristic-driven allocation strategies that lack global scene awareness. They often unproject pixels into dense, view-aligned primitives, or decode from dense, view-aligned intermediates. This process bakes redundancy into the 3D asset, causing the representation size to increase significantly as more input views are added. This leads to an excessive number of Gaussians, becoming a primary scalability bottleneck.
2.  **Fragile Global Consistency:** The reliance on local allocation strategies means that global consistency is often addressed at a late stage of the reconstruction process. As the number of input views increases, models struggle to merge a growing number of view-anchored predictions robustly, making reconstruction quality less stable across regions of dense overlap.
3.  **Trade-offs in Performance:** Previous solutions exhibit significant trade-offs between representation compactness, reconstruction speed, and rendering fidelity. Achieving high fidelity often comes at the cost of larger representation size and slower inference.
4.  **Computational and Memory Inefficiency:** The inflated representation size in existing methods directly translates to higher peak GPU memory consumption and slower inference times, hindering their practical application in scenarios requiring real-time performance or operation in resource-constrained environments.

To address these issues, GlobalSplat is motivated to:
*   **Resolve Cross-View Correspondences Globally:** Learn a compact, global, latent scene representation that encodes multi-view input and resolves cross-view correspondences *before* any explicit 3D geometry is decoded. This "align first, decode later" principle is central to achieving global consistency and compactness.
*   **Prevent Representation Bloat Natively:** Implement a coarse-to-fine training curriculum that gradually increases decoded capacity, which is designed to inherently control and prevent the uncontrolled growth of the 3D representation.
*   **Achieve a Stronger Practical Operating Point:** Develop a method that provides a favorable balance of novel-view synthesis quality, representation compactness (using a constant, view-invariant number of Gaussians), inference speed, and memory efficiency, enabling a light footprint and fast operation.

### 4. Methodology and Approach

GlobalSplat implements an "align first, decode later" principle, which involves constructing a globally aligned latent scene representation before decoding explicit 3D Gaussians. The methodology encompasses several key stages: scene normalization, input context construction, a dual-branch encoder for latent token refinement, a dual-branch decoder for Gaussian parameter prediction, a coarse-to-fine training curriculum, and a comprehensive training objective.

**4.1. Scene Normalization and Input Preparation**

*   **Camera Preprocessing:** Each scene is mapped into a canonical coordinate system. This involves computing an "average camera" frame, using the mean camera center and re-orthonormalized axes. All camera poses are then expressed in this canonical frame.
*   **Scale Normalization:** Camera translations are scaled based on the diameter of the camera constellation, providing a consistent geometric prior across scenes.
*   **Input Context Construction:** Input views are processed to create augmented tokens.
    *   Patchified RGB tokens ($u_{rgb_{i,p}}$) are extracted for each view.
    *   Geometric information is injected via a per-patch camera token ($u_{cam_{i,p}}$). This token combines a patchified Plücker-ray embedding, which provides line geometry information, with a per-view camera code.
    *   The per-view camera code is derived from the absolute camera center (encoded with Fourier features) and intrinsics (encoded with a small MLP), and broadcast to all patches within a view.
    *   Finally, appearance and camera tokens are concatenated to form the input context ($u_{i,p}$).

**4.2. GlobalSplat Architecture**

The core of GlobalSplat is an encoder-decoder structure with learnable latent tokens.

*   **Learnable Latent Tokens:** A fixed set of $M=2048$ learnable latent tokens (each of dimension $d=512$) is initialized. These tokens serve as the foundation for decoding Gaussians and are independent of the number of input frames, enforcing scalability and compactness. Learnable register tokens are also included to capture global context.
*   **Dual-Branch Encoder:**
    *   Consists of $B=4$ blocks designed to explicitly disentangle geometry and appearance processing.
    *   Within each block, latent tokens are projected into stream-specific features ($f_{geo}$, $f_{app}$).
    *   Each stream applies a cross-attention mechanism between input patches and stream features, followed by $L=2$ self-attention blocks to aggregate global context.
    *   The two streams are fused via a 2-layer mixer MLP to update the latent tokens for the subsequent block. This disentanglement aims to prevent the model from relying on texture to compensate for poor structural predictions.
*   **Dual-Branch Decoder:**
    *   Transforms the refined latent tokens into the final 3D Gaussian representation.
    *   Employs two specialized linear heads: one for geometric properties (positions, scales, quaternions, opacity) and another for appearance properties (Spherical Harmonics coefficients, SH degree 3).
    *   Each latent token predicts a fixed set of 16 Gaussian candidates throughout training. Gaussian parameters are initialized with fixed offsets (e.g., mean offset, log scale offset, logit opacity offset).

**4.3. Coarse-to-Fine Training Curriculum**

To enhance training stability and control representation capacity, a stage-wise curriculum is employed:

*   **Progressive Capacity Increase:** The decoder initially merges all 16 Gaussian candidates in a slot into a single representative Gaussian (G=1). As training progresses, the effective capacity is incrementally increased (G $\in$ {2, 4, 8}), allowing the model to refine local details only after global geometry has converged. The final model uses G=8, resulting in 16,384 Gaussians per scene.
*   **Parameter-Aware Reduction:** To merge candidates, importance weights are derived from a temperature-scaled softmax. Attributes (positions, rotations, SH coefficients) are merged by weighted averaging. Log-scales are merged in log-space with a volume-preserving correction, and opacity is merged by weighted averaging of log(1-alpha).
*   **Smooth Stage Transition:** Linear interpolation is used to smooth transitions between coarser and finer representations, gradually relaxing the merging applied to the underlying set of predictions.

**4.4. Training Objective**

The complete objective function combines several components: $L = \lambda_{ren}L_{ren} + \lambda_{con}L_{con} + \lambda_{reg}L_{reg}$.

*   **Rendering Loss ($L_{ren}$):** The primary supervision signal. It consists of an L2-norm (MSE) between the rendered image ($\hat{I}_t$) and the ground truth target view ($I_t$), augmented with a perceptual loss ($L_{perc}$).
*   **Self-Supervised Consistency Loss ($L_{con}$):** Designed to encourage compatible reconstructions from different subsets of input views. Input views are partitioned into two overlapping subsets ($I_a$, $I_b$) which share boundary views but cover complementary temporal samples. Independent forward passes are performed for each subset, and the L1-norm distance between the rendered opacity maps ($\hat{O}_a, \hat{O}_b$) and depth maps ($\hat{D}_a, \hat{D}_b$) is minimized using a symmetric stop-gradient formulation.
*   **Regularization Loss ($L_{reg}$):** Ensures structural integrity and stabilizes optimization.
    *   **Frustum Constraint ($L_{fru}$):** A soft penalty is applied to Gaussian centers that drift outside the frustum of at least one input view, preventing Gaussians from moving to unsupported regions.
    *   **Decoder-Side Regularization ($L_{dec}$):** Includes terms for opacity (to prevent early saturation), scale (to cap maximum scales), rotation (quadratic penalty on residuals), and Spherical Harmonics (SH) coefficients (soft-cap on magnitude) to stabilize compact Gaussian representations.

Training is performed using AdamW optimizer with a linear warm-up and cosine decay learning rate schedule, on 256x256 resolution images, with color jitter and multi-view consistent augmentation.

### 5. Main Findings and Results

GlobalSplat was evaluated on RealEstate10K and ACID datasets, focusing on large-context settings with 12, 24, and 36 input views. The evaluation covered novel-view synthesis quality (PSNR, SSIM, LPIPS), representation compactness (#G(K)), and efficiency (peak GPU memory, inference time, disk size).

**5.1. Quantitative Evaluation on RealEstate10K**

*   **Compactness-Quality Trade-off:** GlobalSplat achieved competitive novel-view synthesis quality while maintaining a fixed representation of 16K Gaussians, irrespective of the number of input views (12, 24, or 36). For 24 views, GlobalSplat16K achieved 28.53 PSNR, 0.883 SSIM, and 0.140 LPIPS.
*   **Comparison to Baselines:**
    *   Compared to highly compact methods like C3G (2K Gaussians), GlobalSplat demonstrated significantly higher image quality (e.g., 28.53 PSNR vs. 23.80 PSNR for 24 views).
    *   Compared to stronger but much heavier methods like Zpressor (393K Gaussians) and AnySplat (up to 3.3M Gaussians), GlobalSplat achieved comparable or slightly better quality with a substantially smaller representation. For instance, Zpressor (28.51 PSNR) and GlobalSplat16K (28.53 PSNR) show similar PSNR for 24 views, but GlobalSplat uses 16K Gaussians compared to Zpressor's 393K.
    *   The results support the claim that explicit global alignment enables compact yet high-fidelity feed-forward 3D Gaussian reconstruction.

**5.2. Cross-Dataset Generalization on ACID**

*   GlobalSplat demonstrated robust zero-shot cross-dataset transfer from RealEstate10K to ACID.
*   It remained competitive across all input-view settings (e.g., for 24 views: 28.03 PSNR, 0.813 SSIM, 0.208 LPIPS for GlobalSplat16K), using the same compact fixed-budget representation as on RealEstate10K. This indicates that the learned representation captures transferable scene structure.

**5.3. Efficiency**

*   GlobalSplat exhibited superior efficiency metrics for 24 input views:
    *   **Peak GPU Memory:** 1.79 GB, the lowest among reported Gaussian-based methods (e.g., Zpressor at 3.70 GB, DepthSplat at 29.84 GB).
    *   **Inference Time:** 77.88 ms, the fastest among reported methods (e.g., Zpressor at 194.20 ms, C3G at 387.14 ms).
    *   **Size on Disk:** 3.8 MB, an ultra-light footprint (e.g., Zpressor at 134 MB).
*   These gains are attributed to the prediction of a compact scene representation with a fixed Gaussian budget, rather than sacrificing reconstruction quality.

**5.4. Qualitative Evaluation**

*   Visual comparisons on RealEstate10K showed that GlobalSplat consistently produced sharp, artifact-free renderings that closely resembled the ground truth.
*   It effectively recovered intricate room details and maintained robust multi-view consistency.
*   Baselines like C3G struggled with fine details, resulting in blurry reconstructions. DepthSplat and GGN introduced structural artifacts. Zpressor achieved comparable visual fidelity but relied on a significantly heavier representation.
*   Similar qualitative performance was observed on ACID, demonstrating good transferability.

**5.5. Ablation Study**

*   **Compactness-Quality Tradeoff:** Increasing the number of latent scene tokens (which control the latent scene bottleneck) was found to be more effective for reconstruction quality than increasing the number of decoded Gaussians per token. This suggests that the size of the latent scene representation is a primary driver of quality in this feed-forward setting.
*   **Model Components:**
    *   The **dual-stream architecture** (disentangling geometry and appearance) contributed positively, outperforming a single-stream variant with comparable parameter count.
    *   The **coarse-to-fine training curriculum** improved performance compared to direct full-capacity prediction from the start of training, highlighting the importance of progressive capacity growth.
    *   Explicitly **injecting camera metadata** (beyond Plücker rays) was beneficial, leading to better results.
    *   The **self-supervised consistency loss** had a noticeable positive impact, preventing a drop in novel-view synthesis quality and an increase in structural artifacts.

**5.6. Limitations**

*   The current architecture relies on a strictly fixed budget of 16K Gaussians, which might be insufficient for unbounded or city-scale environments.
*   GlobalSplat currently assumes static environments and does not capture temporal dynamics.
*   Extreme sparse-view settings (e.g., 2-3 images) remain challenging due to insufficient multi-view parallax for resolving the global latent space.

### 6. Significance and Potential Impact

GlobalSplat represents an advancement in feed-forward 3D Gaussian Splatting by effectively addressing the challenges of representation bloat and scalability that affect many existing methods. By introducing an "align first, decode later" paradigm, which involves fusing multi-view input into a compact, globally-aligned latent scene representation before decoding explicit 3D geometry, the research provides a method for achieving globally consistent and compact 3D reconstructions.

The significance of this work lies in its establishment of a "stronger practical operating point" for feed-forward 3DGS. It demonstrates that competitive novel-view synthesis quality can be achieved with an ultra-compact, view-invariant Gaussian representation (as few as 16K Gaussians, resulting in a 4MB footprint), significantly reducing the resource demands compared to dense baselines.

The potential impacts of GlobalSplat include:

*   **Enhanced Deployability:** The minimal memory footprint and fast inference times (under 78 milliseconds) make generated 3DGS assets highly suitable for deployment in real-time applications, resource-constrained environments, and devices such as mobile phones or augmented/virtual reality (AR/VR) headsets.
*   **Improved Scalability for Multi-View Input:** The ability to process a large number of input views (e.g., 16-36 views) without proportional increases in representation size is critical for reconstructing complex scenes with broad coverage while maintaining efficiency.
*   **Reduced Computational Overhead:** The significant reduction in peak GPU memory and inference latency translates directly to lower operational costs and faster workflows for 3D scene reconstruction.
*   **Advancement of Generalizable NVS:** By providing a robust and compact feed-forward mechanism, GlobalSplat contributes to the broader goal of generalizable novel-view synthesis, where models can adapt to new scenes without extensive per-scene optimization.
*   **Foundation for Future Research:** The framework's design elements, such as the fixed-budget global scene tokens, dual-branch architecture, and coarse-to-fine curriculum, provide a foundation for future exploration. This could include developing adaptive or hierarchical token allocation for larger-scale environments, extending the approach to capture temporal dynamics for 4D reconstruction, or integrating stronger monocular depth priors to address sparse-view challenges.

In summary, GlobalSplat offers a highly practical and scalable solution for feed-forward 3D scene reconstruction, pushing the boundaries of efficiency in 3D Gaussian Splatting.
