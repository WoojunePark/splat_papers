---
title: "PackUV: Packed Gaussian UV Maps for 4D Volumetric Video"
date: 2026-02-26
arxiv: "2602.23040"
venue:
status: read

abstract: "Volumetric videos offer immersive 4D experiences, but remain difficult to reconstruct, store, and stream at scale. Existing Gaussian Splatting based methods achieve high-quality reconstruction but break down on long sequences, temporal inconsistency, and fail under large motions and disocclusions. Moreover, their outputs are typically incompatible with conventional video coding pipelines, preventing practical applications. We introduce PackUV, a novel 4D Gaussian representation that maps all Gaussian attributes into a sequence of structured, multi-scale UV atlas, enabling compact, image-native storage. To fit this representation from multi-view videos, we propose PackUV-GS, a temporally consistent fitting method that directly optimizes Gaussian parameters in the UV domain. A flow-guided Gaussian labeling and video keyframing module identifies dynamic Gaussians, stabilizes static regions, and preserves temporal coherence even under large motions and disocclusions. The resulting UV atlas format is the first unified volumetric video representation compatible with standard video codecs (e.g., FFV1) without losing quality, enabling efficient streaming within existing multimedia infrastructure. To evaluate long-duration volumetric capture, we present PackUV-2B, the largest multi-view video dataset to date, featuring more than 50 synchronized cameras, substantial motion, and frequent disocclusions across 100 sequences and 2B (billion) frames. Extensive experiments demonstrate that our method surpasses existing baselines in rendering fidelity while scaling to sequences up to 30 minutes with consistent quality."

website: https://ivl.cs.brown.edu/packuv
code: https://github.com/pytorch/torchcodec
openreview: 
issue: 

inputs:
  - posed-multi-view-video

outputs:
  - compact
  - 4dgs

methods:
  - uv-fitting
  - video-codec-compatible
  - optical-flow
  - dataset

benchmarks:
  - 

related:
  - 

compared:
  - 
---

# PackUV: Packed Gaussian UV Maps for 4D Volumetric Video

## My Notes



**[Note from GitHub, 2026-04-27]**

----

    - `PackUV`, a new volumetric video representation that packs 3D Gaussian attributes into a sequence of UV atlases for efficient streaming and storage, making it readily compatible with existing video coding infrastructure.
    - `PackUV-GS`, an efficient method to fit PackUV directly from multiview videos using optical-flow-based keyframing and Gaussian labeling to handle large motions, disocclusions, and temporal consistency.
    - `PackUV-2B`, the largest multi-view 4D dataset with 2B frames, large motions, and disocclusions. It provides 360◦ coverage from 50+ synchronized cameras.
## Results

<!-- Optional: structured benchmark results for cross-paper comparison -->
<!-- Example:
| Benchmark | PSNR | SSIM | LPIPS |
|---|---|---|---|
| mipnerf360 | 27.21 | 0.815 | 0.214 |
| tanks-and-temples | 23.14 | 0.841 | 0.183 |
-->

## Figures

![Figure](https://arxiv.org/html/2602.23040v2/images/teaser_v6.jpg)

*Figure 1: We propose a novel and compact 4D representation, PackUV, for volumetric videos that packs 3D Gaussian attributes into a sequence of 2D UV atlases (yellow, top right). PackUV is readily compatible with existing video coding infrastructure (e.g., can be coded with HEVC, FFV1). We also propose PackUV-GS, a method to directly fit Gaussian attributes from multi-view RGB videos into structured PackUV (blue, top left) via optical flow-guided keyframing and Gaussian labeling to fit arbitrary length sequences with temporal consistency even in the presence of large motions and disocclusions. The fitted scene can be rendered back to streamable volumetric video from any viewpoint (red, bottom). We also propose PackUV-2B, the largest 4D multi-view dataset containing 2B frames captured with over 50 synchronized cameras to provide 360∘ coverage.*

![Figure](https://arxiv.org/html/2602.23040v2/x1.png)

*Figure 2: (Top) Three UV-map organization strategies: (a) naïvely stacking UV layers (deep layers become more and more sparse); (b) a geometric-progression UV pyramid (more uniform sparsity with less storage); (c) PackUV, which packs all pyramid layers into a single UV atlas for efficient, codec-friendly processing. (Bottom) We propose PackUV-GS, a new representation based on 3DGS with a discrete spatial distribution constraint via UV fitting. It uses multiple-layer UV images to store the Gaussian attributes during 3DGS fitting. To constrain the 3D Gaussians located on the discrete rays, we propose a UV-based Adaptive Density Control. We also use a stream-based training schema based on keyframes (image with yellow border).*

![Figure](https://arxiv.org/html/2602.23040v2/images/disocclusion_v4.jpg)

*Figure 3: PackUV-GS vs. baselines for large motion and disocclusion handling. The proposed keyframing and Gaussian labeling strategy effectively manages complex scenarios, such as new objects or people entering a room and dispersing. Zoom to view better.*

![Figure](https://arxiv.org/html/2602.23040v2/images/optical_flow_v3.jpg)

*Figure 4: Optical flow. To assess long-term temporal stability, we compute optical flow between consecutive timestamps.*

![Figure](https://arxiv.org/html/2602.23040v2/images/rebut_graphs.jpg)

*Figure 5: (Left) Compression evaluation via different methods. (Right) PSNR consistency over time.*

![Figure](https://arxiv.org/html/2602.23040v2/images/supp_uvgs_lossy.jpg)

*Figure 6: Post-optimization lossy UV mapping fails to capture details of a real-world scene even with 48 layers and 1K resolution.*

![Figure](https://arxiv.org/html/2602.23040v2/x2.png)

*Figure 7: CAPTURE Studio Layout.*

![Figure](https://arxiv.org/html/2602.23040v2/images/atgs_gradexplode.jpg)

*Figure 8: Shows gradient explosion in ATGS training.*

![Figure](https://arxiv.org/html/2602.23040v2/images/kitchen_results.jpg)

*Figure 9: Baseline comparison on PackUV-2B’s Kitchen sequence.*

![Figure](https://arxiv.org/html/2602.23040v2/images/baselines_selfcap2.jpg)

*Figure 10: Shows baseline comparison on SelfCap [91] dataset.*

![Figure](https://arxiv.org/html/2602.23040v2/images/baby_result2.jpg)

*Figure 11: Shows baselines comparison on PackUV-2B’s Baby Dance sequence.*

![Figure](https://arxiv.org/html/2602.23040v2/images/spot_result2.jpg)

*Figure 12: Baselines comparison on PackUV-2B’s SPOT sequence.*

## LLM Summary

The following report provides a detailed analysis of the research paper "PackUV: Packed Gaussian UV Maps for 4D Volumetric Video."

---

### Research Report: PackUV: Packed Gaussian UV Maps for 4D Volumetric Video

#### 1. Authors and Institution(s)

The research was conducted by a team of authors from multiple institutions:
*   Aashish Rai, Angela Xing, Xiaoyan Cong, Zekun Li, and Tao Lu are affiliated with Brown University.
*   Anushka Agarwal and Srinath Sridhar are affiliated with UMass Amherst.
*   Aayush Prakash is affiliated with Meta.

#### 2. How This Work Fits into the Broader Research Landscape

Volumetric video, capturing scenes in four dimensions (three spatial and one temporal), holds promise for immersive experiences in augmented reality (AR), virtual reality (VR), entertainment, sports, and robotics. However, realizing this potential necessitates overcoming significant challenges in reconstruction, storage, and streaming at scale.

Historically, volumetric video reconstruction has employed explicit representations such as point clouds, meshes, multi-plane images (MPIs), or multi-sphere images (MSIs). These methods often face limitations in rendering complex scenes efficiently and are characterized by high memory consumption.

More recently, neural representations like radiance fields (e.g., NeRF) and 3D Gaussian Splatting (3DGS) have emerged as prevalent methods for 3D reconstruction and novel view synthesis. 3DGS, in particular, has demonstrated high-quality reconstruction for static scenes. Extending these methods to dynamic, volumetric video has led to approaches like Deformable3DGS, 4DGS, and RealTime4DGS. Despite advancements, these dynamic 3DGS methods typically struggle with long-duration sequences (often limited to a few seconds), exhibit temporal inconsistencies, and may fail under large object motions or disocclusions (when objects enter or exit the scene). Streaming-oriented approaches aim to address long sequences through online fitting, but they also encounter difficulties in maintaining temporal consistency and handling complex dynamics over extended periods.

A further challenge in the existing landscape is the incompatibility of volumetric video outputs from current 3DGS methods with conventional video coding infrastructure. The unstructured nature of Gaussian primitives often necessitates bespoke compression schemes, which are not universally supported by existing multimedia pipelines, thus hindering practical deployment and widespread sharing. While some efforts have been made to flatten 3D Gaussians into 2D forms (e.g., SOG, UV projection), these are largely limited to static scenes or involve lossy post-optimization projections.

PackUV addresses these identified gaps by proposing a structured, 2D image-native representation for 4D Gaussians that is directly compatible with standard video codecs. Concurrently, it introduces a fitting methodology designed for temporal consistency and robustness to large motions and disocclusions over arbitrary sequence lengths, thereby enhancing the practicality and scalability of volumetric video. The introduction of PackUV-2B also addresses the need for more comprehensive and challenging benchmark datasets for evaluating long-duration 4D capture.

#### 3. Key Objectives and Motivation

The primary objective of this work is to develop a novel 4D Gaussian representation and an associated fitting methodology that overcome the current limitations in reconstructing, storing, and streaming high-quality volumetric videos, particularly for long sequences with complex dynamics.

The motivation for this work stems from several challenges in the field:

1.  **Scalability to Long Sequences:** Existing Gaussian Splatting (3DGS) based methods, while effective for short 3D or 4D captures, tend to degrade or become computationally prohibitive when applied to volumetric videos extending beyond a few seconds. This limitation hinders the creation of immersive experiences for real-world scenarios that often involve extended durations.
2.  **Temporal Consistency under Complex Dynamics:** Current dynamic 3DGS methods often exhibit temporal inconsistencies, especially when confronted with large object motions, rapid changes in scene content, or disocclusions (objects appearing or disappearing). Maintaining visual coherence and fidelity over time remains a significant challenge.
3.  **Efficient Storage and Streaming:** The unstructured nature of 3D Gaussian primitives typically results in large data volumes. Current representations are often incompatible with conventional video coding pipelines (e.g., HEVC, FFV1). This incompatibility necessitates specialized compression techniques, which complicates storage, transmission, and integration into existing multimedia infrastructure. A unified, codec-compatible representation is needed to enable efficient streaming and practical deployment.
4.  **Addressing Lossy Conversions:** Previous attempts to map 3DGS to 2D UV maps (e.g., UVGS) often involve post-optimization projections that can be lossy and computationally redundant, leading to a degradation in visual quality, particularly for dynamic scenes. A method that directly optimizes within a structured 2D domain is motivated to preserve detail and temporal coherence.
5.  **Lack of Comprehensive Evaluation Benchmarks:** Existing multi-view datasets for volumetric video are frequently restricted to frontal camera views, limited motions, or short durations. This restricts the thorough evaluation of methods designed to handle 360-degree coverage, extensive motion, and frequent disocclusions over long timeframes. There is a need for a dataset that reflects the complexity of real-world volumetric capture.

In summary, the motivation is to bridge the gap between high-quality 4D scene reconstruction and practical, deployable volumetric video systems by developing a compact, temporally consistent, codec-compatible representation and an robust fitting method, supported by a challenging new dataset.

#### 4. Methodology and Approach

The methodology introduces PackUV, a 4D Gaussian representation structured for efficient storage and streaming, and PackUV-GS, a fitting method that reconstructs temporally consistent volumetric videos from multi-view inputs.

**4.1. PackUV Atlas Representation**

PackUV reorganizes 3D Gaussian attributes into a sequence of structured, multi-layered 2D UV maps. Each UV map represents a single video frame.

*   **Pyramid UV Mapping:** Recognizing that deeper UV layers (after opacity-based sorting) contain progressively fewer visible Gaussians due to occlusion, PackUV employs a geometric downsampling strategy. Instead of storing all `K` layers at a uniform base resolution (`M₀ × N₀`), deeper layers (`k > 0`) are stored at progressively reduced resolutions (e.g., `M₀ × N₀/2`, `M₀/2 × N₀/2`). This approach aims to reduce memory overhead while maintaining detail where required.
*   **UV Atlas Layout:** To maximize compactness and compatibility with video codecs, the `K` progressive layers are packed into a single texture atlas `A`. This packing is achieved through recursive subdivision, resembling a quadtree structure. Layer 0 occupies the right region at full resolution, while subsequent layers subdivide the remaining space, alternating orientation and resolution. This layout reportedly achieves 88.5% packing efficiency. The atlas dimensions `W_A` and `H_A` are derived from the sum of widths and maximum height of the individual layers. The final 4D volumetric video is represented as a continuous sequence of these UV atlases.

**4.2. PackUV-GS Fitting Method**

PackUV-GS is designed to directly fit PackUV from multi-view videos, emphasizing temporal consistency, large motion handling, and disocclusion robustness.

*   **Direct UV Map Fitting:** Instead of post-processing an optimized 3DGS into UV space, PackUV-GS directly optimizes Gaussian parameters within the UV domain. The UV maps (`U ∈ R^(M×N×K×D)`) explicitly store Gaussian attributes (position `ρ`, rotation `r`, scale `s`, opacity `o`, spherical harmonics `c`) for each UV coordinate and layer. This direct optimization aims to preserve structural benefits and enforce Gaussian sparsity through the discrete UV grid.
*   **Video Keyframing:** To manage long sequences, the input multi-view video is divided into temporal segments.
    *   Optical flow magnitude is computed for a reference view, and top peaks (with minimum separation `θ`) define keyframes.
    *   The first frame of each segment becomes a keyframe. PackUV Gaussians for a keyframe are initialized from the preceding keyframe's optimized parameters, promoting temporal and spatial consistency.
    *   Intermediate "transition frames" between keyframes are initialized from their immediate predecessors and refined with fewer training iterations. This staged, stream-based approach supports efficient, parallelized reconstruction of high-fidelity dynamic scenes.
*   **Gaussian Labeling:** This module uses optical flow to differentiate and manage dynamic and static regions within the scene.
    *   **Optical Flow and Binary Motion Masks:** RAFT is used to estimate forward optical flow between consecutive frames for each camera view. A binary motion mask is generated by thresholding the flow magnitude and applying dilation to include local context.
    *   **Covariance-Aware Gaussian Masking:** For each Gaussian, its 3D covariance is projected to 2D image space, taking into account the camera view transformation and projection Jacobian. The 2D covariance (`Σ_2D`) is then used to define an ellipse. A Gaussian is labeled as "dynamic" for a specific camera if any pixel within its projected ellipse's footprint overlaps with the binary motion mask, determined using the Mahalanobis distance. An OR aggregation across all cameras determines the final dynamic label for each Gaussian. This process is implemented in a custom CUDA kernel for efficiency.
    *   **Gradient Freezing:** During backpropagation, gradients for Gaussians labeled as "static" are zeroed. Optimizer momentum for static Gaussians is also periodically reset to prevent drift. During densification, child Gaussians inherit their parent's dynamic/static label, preserving the dynamic ratio. This aims to improve temporal stability and training efficiency, especially for scenes with static backgrounds.
*   **UV-Based Pruning:** Two pruning strategies are applied to maintain sparsity and efficiency within the discretized UV mapping:
    *   **Valid UV Projection Pruning:** After densification, Gaussians whose recalculated UV coordinates do not satisfy the mapping criteria are removed. This enforces sparsity and aligns Gaussians with scene geometry.
    *   **Max-K UV Pruning:** For each UV pixel, only the top `K` Gaussians, sorted by opacity, are retained. This prevents overpopulation at specific UV coordinates, reducing memory overhead and focusing on surface-relevant details.
*   **Objective Function:** The training objective comprises a photometric loss (blend of L1 and SSIM) between rendered and ground-truth images, and regularization terms. Scale and opacity regularization are applied to discourage floaters and oversized primitives, optionally restricted to dynamic Gaussians.
*   **Low Precision Optimization (LPO):** PackUV-GS employs K-bit low-precision optimization directly during training, rather than quantizing parameters post-training. The renderer uses a quantized proxy of attributes, while gradients flow through a straight-through estimator to update FP32 master weights. Position parameters (`x`) are kept at 16-bit precision (split into two 8-bit channels for storage), while scale, rotation, opacity, and color (`s, r, α, c`) are optimized at 8-bit precision. This 8-bit-per-channel layout ensures compatibility with standard video codecs.

**4.3. PackUV-2B Dataset**

To facilitate rigorous evaluation, the paper introduces PackUV-2B, a novel, large-scale, long-duration multi-view 4D dataset.
*   It comprises 100 dynamic sequences, totaling over 2 billion frames.
*   Captured using 55 to 88 synchronized cameras, providing 360-degree coverage.
*   Includes diverse real-world scenarios in both studio and in-the-wild settings, such as human-human, human-object, and human-robot interactions.
*   Sequences average 10 minutes, with some extending up to 30 minutes, featuring broad variations in motion speed, scale, and object properties (rigid, articulated, reflective, transparent).
*   Captured at 1920 × 1200 resolution and up to 90 FPS. This dataset aims to serve as a benchmark for general-purpose, long-horizon dynamic reconstruction.

#### 5. Main Findings and Results

The research presents several findings regarding the performance of PackUV and PackUV-GS, supported by qualitative, quantitative, and ablative studies.

**5.1. Qualitative and Quantitative Results**

*   **Handling Large Motions and Disocclusions:** PackUV-GS demonstrates a capability to handle complex dynamic scenarios, including large motions and severe disocclusions (e.g., new objects or people entering a scene). Qualitative comparisons indicate that PackUV-GS produces rendered views that are sharper and more temporally coherent than baseline methods. Deformation-based methods (e.g., Deformable3DGS, RealTime4DGS, 4DGS) reportedly exhibit high VRAM usage, limited scalability to long sequences, and difficulty in modeling newly emerging objects. Streaming-based approaches (e.g., 3DGStream, ATGS, GIFStream) are described as generating artifacts, with specific issues like gradient explosion (ATGS) or flickering across segments (GIFStream).
*   **Rendering Fidelity:** Quantitative evaluations across N3DV, SelfCap, and PackUV-2B datasets indicate that PackUV-GS outperforms comparison baselines (3DGStream, 4DGS, RealTime4DGS, Deformable3DGS, ATGS, Grid4D, Ex4DGS, GIFStream) in terms of PSNR, SSIM, and LPIPS metrics. This performance is maintained across sequences up to 30 minutes in length.
*   **Long-term Temporal Consistency:** Optical flow analysis on rendered novel viewpoints highlights that deformation-based methods struggle to maintain temporal consistency over extended periods, particularly across segment boundaries in methods requiring segmented training. PackUV-GS is reported to maintain consistent rendering quality over time, in contrast to 3DGStream and ATGS, whose quality reportedly degrades over duration.

**5.2. Video Coding of PackUV**

*   PackUV's structured, image-native format facilitates direct compatibility with standard 2D video codecs (e.g., FFV1, HEVC, AVC). The temporally consistent UV layouts and per-pixel attribute updates result in high spatial locality and temporal coherence, making the atlas sequences suitable for existing video coding infrastructure.
*   Lossless encoding using FFV1 is reported to achieve perfect reconstruction with zero error. This capability allows treating 4D Gaussian scenes as conventional video assets, enabling efficient storage and streaming with off-the-shelf tools. PackUV also demonstrates storage efficiency, with an average storage rate of under 10 MBPS using FFV1, outperforming other 4DGS methods in comparative storage benchmarks (e.g., against LG, Grid4D, Ex4DGS, 3DGStream, GIFStream).
*   Low-precision optimization (LPO) directly during training, combined with 8-bit per-channel storage, contributes to this codec compatibility without significant quality loss (reported 0.11 dB PSNR drop with FFV1 lossless compression).

**5.3. Ablation Study**

Ablation studies conducted on PackUV-2B validate the contribution of key components:

*   **Direct UV-space Optimization:** Removing direct UV optimization (i.e., relying solely on post-hoc UV projection) resulted in a notable drop in PSNR and other metrics, indicating the importance of optimizing Gaussians directly in UV space for fine detail preservation.
*   **Atlas-based Packing (Pyramid UV Mapping):** Compressing deeper UV layers into lower-resolution atlases was found to incur negligible quality loss due to the inherent sparsity of these layers.
*   **Low-Precision Optimization (LPO):** LPO was found to be effectively lossless compared to post-training quantization, providing an efficient approach for Gaussian storage and seamless integration with standard video-coding pipelines.
*   **Video Keyframing:** The keyframing strategy helps maintain spatial and temporal consistency, preventing the gradual quality degradation observed when this component is removed. Its absence led to a decline in average PSNR and other metrics.
*   **Gaussian Labeling:** While the extent of impact is not detailed with specific figures in the provided abstract/introduction/results, the approach is stated to improve temporal stability and training efficiency.

#### 6. Significance and Potential Impact

The PackUV framework presents a significant advancement in the field of volumetric video, with implications for both research and practical applications.

**6.1. Bridging the Gap between Research and Deployment:**
PackUV is described as the first unified volumetric video representation capable of directly leveraging conventional video coding infrastructure (e.g., HEVC, FFV1) for all 3D Gaussian attributes without quality loss. This capability addresses a critical bottleneck in the practical deployment of 4D volumetric video, enabling efficient storage, streaming, and decoding using existing multimedia tools and pipelines. This bridges the gap between high-quality research representations and the demands of real-world media distribution.

**6.2. Scalability and Practicality:**
By enabling the compact, image-native storage of 4D Gaussian attributes in structured UV atlases, PackUV facilitates the creation and management of arbitrarily long volumetric video sequences. The PackUV-GS fitting method, with its flow-guided keyframing and Gaussian labeling, maintains high-quality reconstruction and temporal consistency even under large motions and disocclusions. This scalability and robustness enhance the practicality of volumetric video for extended, complex scenes, which are common in applications like AR/VR experiences, sports broadcasting, and film production.

**6.3. Enhanced Performance and Temporal Coherence:**
The method demonstrates superior rendering fidelity (higher PSNR, SSIM, lower LPIPS) compared to existing state-of-the-art baselines across various challenging datasets. Critically, it achieves this while maintaining long-term temporal consistency, which is a common failure point for many dynamic 3DGS methods. This consistent quality over time is essential for immersive and believable volumetric content.

**6.4. Establishment of a New Benchmark:**
The introduction of PackUV-2B, the largest long-duration multi-view 4D dataset to date, is a notable contribution to the research community. Featuring billions of frames, 360-degree coverage from numerous synchronized cameras, and diverse, challenging real-world scenarios, it provides a crucial benchmark for evaluating future advancements in general-purpose, long-horizon dynamic reconstruction. This dataset will likely drive further innovation and standardized comparisons in the field.

**6.5. Potential for Broader Applications:**
The combination of high-quality reconstruction, temporal consistency, and codec compatibility positions PackUV as a promising step toward deployable volumetric video systems. Its impact could extend across various domains, including:
*   **Immersive Media:** Enabling high-fidelity 4D content for AR/VR applications, offering more realistic and interactive experiences.
*   **Entertainment and Sports:** Facilitating free-viewpoint video streaming for live events or pre-recorded content.
*   **Robotics and 4D Understanding:** Providing robust and temporally consistent 4D scene representations that can be utilized for advanced perception and interaction in robotic systems.

In conclusion, PackUV represents a comprehensive solution that addresses key limitations in volumetric video, paving the way for more widespread adoption and practical use of this immersive media format.
