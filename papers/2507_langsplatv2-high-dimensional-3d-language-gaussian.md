---
title: "LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+ FPS"
date: 2025-07-09
arxiv: "2507.07136"
venue:
status: to-read

abstract: "In this paper, we introduce LangSplatV2, which achieves high-dimensional feature splatting at 476.2 FPS and 3D open-vocabulary text querying at 384.6 FPS for high-resolution images, providing a 42 $\times$ speedup and a 47 $\times$ boost over LangSplat respectively, along with improved query accuracy. LangSplat employs Gaussian Splatting to embed 2D CLIP language features into 3D, significantly enhancing speed and learning a precise 3D language field with SAM semantics. Such advancements in 3D language fields are crucial for applications that require language interaction within complex scenes. However, LangSplat does not yet achieve real-time inference performance (8.2 FPS), even with advanced A100 GPUs, severely limiting its broader application. In this paper, we first conduct a detailed time analysis of LangSplat, identifying the heavyweight decoder as the primary speed bottleneck. Our solution, LangSplatV2 assumes that each Gaussian acts as a sparse code within a global dictionary, leading to the learning of a 3D sparse coefficient field that entirely eliminates the need for a heavyweight decoder. By leveraging this sparsity, we further propose an efficient sparse coefficient splatting method with CUDA optimization, rendering high-dimensional feature maps at high quality while incurring only the time cost of splatting an ultra-low-dimensional feature. Our experimental results demonstrate that LangSplatV2 not only achieves better or competitive query accuracy but is also significantly faster. Codes and demos are available at our project page: this https URL."

website: https://langsplat-v2.github.io
code: https://github.com/ZhaoYujie2002/LangSplatV2
openreview:
issue: 8

inputs:
  - posed-multi-view-images
  - text-prompt
outputs:
  - 3d-gaussians
  - semantic-segmentation
methods:
  - 3dgs
  - clip
benchmarks:
  - 

related:
  - 

compared:
  - 
---

# LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+ FPS

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

![Figure](https://arxiv.org/html/2507.07136/x1.png)

*Figure 1: Feature rendering time comparison with different GPUs. Note that the less advanced GPUs (RTX 3090 and RTX 4090) cannot accommodate the LangSplat model with feature dimensions of 1024 or higher due to running out of memory.*

![Figure](https://arxiv.org/html/2507.07136/x2.png)

*Figure 2: The framework of LangSplatV2. LangSplatV2 introduces a sparse coefficient for each Gaussian point and a shared global codebook for the entire scene.*

![Figure](https://arxiv.org/html/2507.07136/x3.png)

*Figure 3: Our efficient sparse coefficient splatting method accelerates the speed of alpha-blending by utilizing the property of the learned sparse coefficient field and neglecting zero elements.*

![Figure](https://arxiv.org/html/2507.07136/x4.png)

*Figure 4: Qualitative comparisons of open-vocabulary 3D object localization on the LERF dataset. The red points are the model predictions and the black dashed bounding boxes denote the annotations. We observe that LangSplatV2 generates better results than LangSplat.*

![Figure](https://arxiv.org/html/2507.07136/x5.png)

*Figure 5: Qualitative comparisons of open-vocabulary 3D semantic segmentation on the LERF, Mip-NeRF360 and 3D-OVS dataset. We can see that our LangSplatV2 generates better masks than LangSplat, which shows the effectiveness of our LangSplatV2.*

![Figure](https://arxiv.org/html/2507.07136/x6.png)

*Figure 6: More qualitative comparisons of open-vocabulary 3D object localization on the LERF and Mip-NeRF360 datasets. The red points are the model predictions and the black dashed bounding boxes denote the annotations. We observe that LangSplatV2 generates better results than LangSplat.*

![Figure](https://arxiv.org/html/2507.07136/x7.png)

*Figure 7: More qualitative comparisons of open-vocabulary 3D semantic segmentation on the LERF, Mip-NeRF360 and 3D-OVS dataset. We can see that our LangSplatV2 generates better masks than LangSplat, which shows the effectiveness of our LangSplatV2.*

## LLM Summary

The following report provides a detailed analysis of the research paper "LangSplatV2: High-dimensional 3D Language Gaussian Splatting with 450+ FPS."

---

> *Auto-generated summary. Do not edit manually.*
