---
title: "Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields"
date: 2025-03-26
arxiv: "2503.20776"
venue:
status: to-read

abstract: "Recent advancements in 2D and multimodal models have achieved remarkable success by leveraging large-scale training on extensive datasets. However, extending these achievements to enable free-form interactions and high-level semantic operations with complex 3D/4D scenes remains challenging. This difficulty stems from the limited availability of large-scale, annotated 3D/4D or multi-view datasets, which are crucial for generalizable vision and language tasks such as open-vocabulary and prompt-based segmentation, language-guided editing, and visual question answering (VQA). In this paper, we introduce Feature4X, a universal framework designed to extend any functionality from 2D vision foundation model into the 4D realm, using only monocular video input, which is widely available from user-generated content. The &#34;X&#34; in Feature4X represents its versatility, enabling any task through adaptable, model-conditioned 4D feature field distillation. At the core of our framework is a dynamic optimization strategy that unifies multiple model capabilities into a single representation. Additionally, to the best of our knowledge, Feature4X is the first method to distill and lift the features of video foundation models (e.g., SAM2, InternVideo2) into an explicit 4D feature field using Gaussian Splatting. Our experiments showcase novel view segment anything, geometric and appearance scene editing, and free-form VQA across all time steps, empowered by LLMs in feedback loops. These advancements broaden the scope of agentic AI applications by providing a foundation for scalable, contextually and spatiotemporally aware systems capable of immersive dynamic 4D scene interaction."

website: https://feature4x.github.io
code: https://github.com/ShijieZhou-UCLA/Feature4X
openreview:
issue: 4

inputs:
  - monocular-video
  - text-prompt
outputs:
  - 4dgs
  - semantic-segmentation
methods:
  - vision-language-model

benchmarks:
  - 

related:
  - 

compared:
  - 
---

# Feature4X: Bridging Any Monocular Video to 4D Agentic AI with Versatile Gaussian Feature Fields

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

![Figure](https://arxiv.org/html/2503.20776/x2.png)

*Figure 2: Method overview. Given an input monocular video, we infer 2D priors to segment static background (represented by static 3D Gaussians augmented with latent features) and dynamic foreground (represented by dynamic 3D Gaussians guided by Motion Scaffolds [35], a set of nodes {𝐯i}subscript𝐯𝑖\{\mathbf{v}*{i}\}{ bold_v start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT } encoding 3D motion trajectories and latent features hisubscriptℎ𝑖h*{i}italic_h start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT). Dynamic Gaussian features and motions are computed via interpolation from their K𝐾Kitalic_K-nearest scaffold nodes. At each timestep, dynamic Gaussians are warped and fused with static Gaussians. A parallel rasterization [102] generates RGB images and a unified latent feature map, decoded into task-specific features—illustrated here by SAM2 [68], CLIP-LSeg [36], and InternVideo2 [84] for representative 2D (novel view segmentation), 3D (scene editing), and 4D (spatiotemporal VQA) tasks. Our framework generalizes to any 2D vision foundation model and is trained end-to-end using input RGB frames and customized features from pretrained 2D models. At inference, rendered feature maps from arbitrary views and timesteps are directly fed into task-specific decoders, seamlessly supporting user prompts and LLM interactions to form a unified 4D agentic AI system.*

![Figure](https://arxiv.org/html/2503.20776/x3.png)

*Figure 3: Segment Anything in Dynamic 4D Scenes with SAM2 Feature Field. For any rendered novel view video, we support: (a) Promptless segmentation (segment everything): when no user prompt is provided, segmentation masks are automatically assigned at the first frame (t=0𝑡0t=0italic_t = 0) and then propagated across all frames. (b) Promptable segmentation (segment anything): the user can segment any object—static or dynamic—at any timestep using a point or box prompt, and the corresponding mask is robustly tracked and propagated through subsequent frames.*

![Figure](https://arxiv.org/html/2503.20776/x4.png)

*Figure 4: Baseline Comparison on SAM2 Inference. We compare segmentation quality and inference speed between (a) the naive RGB-based approach and (b) our feature-based method. Ours achieves comparable segmentation, accurately tracking the object over time, and avoids RGB artifacts (red box region at t=70𝑡70t=70italic_t = 70), while reducing inference time to about 4×\times× speed-up.*

![Figure](https://arxiv.org/html/2503.20776/x5.png)

*Figure 5: Semantic 4D Scene Understanding with CLIP Feature Field. By lifting CLIP-LSeg [36] features into a 4D feature field, we enable pixel-level semantic segmentation from any view at any timestep. This allows robust 4D scene understanding, even as object appearances change over time—for example, accurately identifying a blooming flower from bud to full bloom across views.*

![Figure](https://arxiv.org/html/2503.20776/x6.png)

*Figure 6: Scene Editing with AI Agent. Given user prompts, our GPT-powered agent interprets editing intent and autonomously performs scene edits via our 4D CLIP feature field. Examples include both geometric (e.g., “extract” and “delete”) and appearance (e.g., “change color”) editing in 3D space. While results may not be perfect due to imperfect fine-grained feature alignment and non-optimal editing parameter tuning, the agent adaptively refines parameters and applies edits consistently across views and time—greatly reducing the need for manual tuning—and demonstrates robust, interactive 4D scene manipulation.*

![Figure](https://arxiv.org/html/2503.20776/x7.png)

*Figure 7: VQA with Chatbot Agent. (Left) Our model supports free-form VQA across diverse question types—general, spatial, and temporal—by distilling InternVideo2 [84] features. (Right) At each timestep, we reconstruct both a 4D radiance field and a 4D feature field, providing more inference sources beyond the input video frame—including local (moving camera) and global (zoomed-out) novel views and their corresponding feature maps—thereby supporting VQA in 4D and enhancing the model’s spatiotemporal reasoning capabilities.*

![Figure](https://arxiv.org/html/2503.20776/x8.png)

*Figure A: Feature Field Visualizations. We visualize our versatile Gaussian feature field along with its decoded SAM2, CLIP, and InternVideo feature fields using PCA.*

![Figure](https://arxiv.org/html/2503.20776/x9.png)

*Figure B: Overview of the editing framework. GPT-4o generates different editing configurations based on user prompts, selects target regions via hybrid filtering, evaluates their outputs, and selects the best configuration.*

![Figure](https://arxiv.org/html/2503.20776/x10.png)

*Figure C: CLIP semantic segmentation quality comparison. We compare the CLIP semantic segmentation quality between ground-truth (inference from RGB) and our implementation (inference from feature map) for both training and novel views.*

![Figure](https://arxiv.org/html/2503.20776/x11.png)

*Figure D: SAM2 segmentation quality comparison for different dimensions of unified latent feature maps Best performing SAM2 segmentation is derived from the 32-dimensional unified latent feature map.*

## LLM Summary

**Feature4X** introduces a versatile framework that extends 2D vision foundation capabilities into a unified 4D Gaussian feature field derived simply from monocular video. By distilling features from various 2D vision tasks natively into an explicit 3D Gaussian Splatting scene optimized over time, the system inherently supports view-independent and temporally stable 2D segmentation, 3D scene editing, and dynamic 4D spatiotemporal Visual Question Answering (VQA). To address computational limits, it heavily compresses the underlying 4D field into a compact and sparse set of motion scaffold base features, and couples with LLMs/VLMs for complex iterative reasoning loops, forming the groundwork for comprehensive interactive 4D Agentic AI systems.

> *Auto-generated summary. Do not edit manually.*
