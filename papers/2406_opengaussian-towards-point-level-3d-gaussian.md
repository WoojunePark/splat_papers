---
title: "OpenGaussian: Towards Point-Level 3D Gaussian-based Open Vocabulary Understanding"
date: 2024-06-04
arxiv: "2406.02058"
venue:
status: to-read
authors:
  - Yanmin Wu
  - Jiarui Meng
  - Haijie Li
  - Chenming Wu
  - Yahao Shi
  - Xinhua Cheng
  - Chen Zhao
  - Haocheng Feng
  - Errui Ding
  - Jingdong Wang
  - Jian Zhang

abstract: "This paper introduces OpenGaussian, a method based on 3D Gaussian Splatting (3DGS) capable of 3D point-level open vocabulary understanding. Our primary motivation stems from observing that existing 3DGS-based open vocabulary methods mainly focus on 2D pixel-level parsing. These methods struggle with 3D point-level tasks due to weak feature expressiveness and inaccurate 2D-3D feature associations. To ensure robust feature presentation and 3D point-level understanding, we first employ SAM masks without cross-frame associations to train instance features with 3D consistency. These features exhibit both intra-object consistency and inter-object distinction. Then, we propose a two-stage codebook to discretize these features from coarse to fine levels. At the coarse level, we consider the positional information of 3D points to achieve location-based clustering, which is then refined at the fine level. Finally, we introduce an instance-level 3D-2D feature association method that links 3D points to 2D masks, which are further associated with 2D CLIP features. Extensive experiments, including open vocabulary-based 3D object selection, 3D point cloud understanding, click-based 3D object selection, and ablation studies, demonstrate the effectiveness of our proposed method. The source code is available at our project page: this https URL"

website: https://3d-aigc.github.io/OpenGaussian
code: 

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

## LLM Summary



## Results

<!-- Optional: structured benchmark results for cross-paper comparison -->
<!-- Example:
| Benchmark | PSNR | SSIM | LPIPS |
|---|---|---|---|
| mipnerf360 | 27.21 | 0.815 | 0.214 |
| tanks-and-temples | 23.14 | 0.841 | 0.183 |
-->

## Figures

![Figure](https://arxiv.org/html/2406.02058/x1.png)

*Figure 1: Illustration of two text query strategies. (a) demonstrates the process of rendering a feature map and computing its similarity with text features to obtain a 2D mask, which is then used to generate a corresponding rendered image. (b) demonstrates the direct similarity computation of 3D Gaussian language features with text features, selecting Gaussian points with high similarity, and rendering to obtain a rendered image corresponding to the text.*

![Figure](https://arxiv.org/html/2406.02058/x2.png)

*Figure 2: (a) We use the view-independent SAM boolean mask to train 3D instance features with 3D consistency for 3DGS.(b) We propose a two-level codebook for discretizing instance features from coarse to fine. (c) An instance-level 3D-2D feature association method to associate 2D CLIP features with 3D points without training.*

![Figure](https://arxiv.org/html/2406.02058/x3.png)

*Figure 3: (a) Reference image/mesh; (b) instance features learned from Sec. 3.1; (c)-(d) Point features after discretization by coarse-level and fine-level codebook (Sec. 3.2).*

![Figure](https://arxiv.org/html/2406.02058/x4.png)

*Figure 4: We render 3D instance points to an arbitrary training view, and associate 3D points with 2D masks based on the principle of joint IoU and feature similarity, which have already been extracted with mask-level CLIP features, thereby indirectly associating 3D points with CLIP features.*

![Figure](https://arxiv.org/html/2406.02058/x5.png)

*Figure 5: Open-vocabulary 3D object selection on the LERF dataset. OpenGaussian outperforms LangSplat and LEGaussians in accurately identifying the 3D objects corresponding to text queries.*

![Figure](https://arxiv.org/html/2406.02058/x6.png)

*Figure 6: 3D feature visualization comparison. From left to right, the scenes are ramen, teatime, scannet_0140_00, and scannet_0645_00. Our proposed method, OpenGaussian, exhibits enhanced granularity and accuracy in its features.*

![Figure](https://arxiv.org/html/2406.02058/x7.png)

*Figure 7: Subjective result of click-based 3D object selection. OpenGaussian demonstrates a more complete 3D object selection without the issues of incompleteness or redundancy.*

![Figure](https://arxiv.org/html/2406.02058/x8.png)

*Figure 8: Examples of scene editing. (a) The original scene was reconstructed using OpenGaussian. (b) Selecting an object for removal. (c) Inserting a new object. (d) Changing the color of the selected object. Note that all edits are performed in 3D space, not on the image.*

![Figure](https://arxiv.org/html/2406.02058/x9.png)

*Figure 9: A demo of text-to-3D Gaussian retrieval on ScanNet. Top: scene0000_00; bottom: scene0645_00.*

![Figure](https://arxiv.org/html/2406.02058/x10.png)

*Figure 10: We rasterize the 3D point instance features into multi-view images, demonstrating cross-view consistency.*

## My Notes

