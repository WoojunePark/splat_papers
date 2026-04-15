---
title: "Segment Any 3D Gaussians"
date: 2023-12-01
arxiv: "2312.00860"
venue:
status: read

abstract: "This paper presents SAGA (Segment Any 3D GAussians), a highly efficient 3D promptable segmentation method based on 3D Gaussian Splatting (3D-GS). Given 2D visual prompts as input, SAGA can segment the corresponding 3D target represented by 3D Gaussians within 4 ms. This is achieved by attaching an scale-gated affinity feature to each 3D Gaussian to endow it a new property towards multi-granularity segmentation. Specifically, a scale-aware contrastive training strategy is proposed for the scale-gated affinity feature learning. It 1) distills the segmentation capability of the Segment Anything Model (SAM) from 2D masks into the affinity features and 2) employs a soft scale gate mechanism to deal with multi-granularity ambiguity in 3D segmentation through adjusting the magnitude of each feature channel according to a specified 3D physical scale. Evaluations demonstrate that SAGA achieves real-time multi-granularity segmentation with quality comparable to state-of-the-art methods. As one of the first methods addressing promptable segmentation in 3D-GS, the simplicity and effectiveness of SAGA pave the way for future advancements in this field. Our code will be released."

website: https://jumpat.github.io/SAGA
code: https://github.com/Jumpat/SegAnyGAussians.git
issue: 

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

## My Notes


**[Note from GitHub, 2026-04-15]**
> ## inputs
> - posed
> - multi-view
> - images
> - 2D-pointing
>
> ## outputs
> - fast
> - 3D-segmentation
>
> ## methods
> - SAM2D
> - feature-per-splat
> - scale-aware
> - CLIP
>
>
> 1. 빠른 속도?
> GS 복원하면서 splat 단위로 feature를 미리 만들어두었다면, 사실상 그때 segmentation 다 한 거 아닌가?
> 4ms의 빠른 inference 속도는, 씬 전체에 대한 이해하는 과정이 생략되어서 빠른 거 아닐까?
>
> 2. Trick들
> 2-1. Scale 관련: Splat들이 크기가 튀는 경우가 빈번해서 크기가 큰 outlier들을 적절히 거르는 기법들 적용 (Scale-Gated Affinity Features, Local Feature Smoothing, Scale-Aware Contrastive Learning)
> 2-2. Data imbalance
> 2-3. Open set: CLIP 쓰면 가능
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

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-teaser.png)

*Figure 1: SAGA performs promptable multi-granularity segmentation within milliseconds. Prompts are marked by points.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-pipe-camera-ready.png)

*Figure 2: The architecture of SAGA. Left: SAGA attaches a Gaussian affinity feature to each 3D Gaussian. The magnitude of different affinity feature channels are adjusted by a soft scale gate to handle multi-granularity ambiguity. Right: SAGA distills segmentation ability of SAM into affinity features attached to 3D Gaussians in the 3D-GS model through scale-aware contrastive learning.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-vis-camera_ready_2.png)

*Figure 3: Qualitative results of SAGA across different scenes. We provide both the targets segmented via 2D point prompts and the “segment everything” results.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-fine-details-camera-ready.png)

*Figure 4: SAGA can maintain the high frequency texture details captured by 3D-GS. We reveal the inherent structure of these details by shrinking the Gaussians by 60%.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-ablation-camera-ready.png)

*Figure 5: Ablation study on effects of local feature smoothing (Smooth) and feature norm regularization (Feature Norm). Outliers are primarily eliminated through local feature smoothing. Feature norm regularization helps features of inner Gaussians align better with those of the surface.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-failure-case-camera-ready.png)

*Figure 6: Failure cases of SAGA. The targets of interest are labeled by red border.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-garfield-camera-ready.png)

*Figure A1: Adapting the scale gate mechanism with GARField achieves competitive results, demonstrating the potential of SAGA across different radiance fields.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-ngp-camera-ready.png)

*Figure A2: Applying SAGA to Instant-NGP achieves competitive segmentation performance, further demonstrating the generalizability and robustness of SAGA across different radiance field representations.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-comp-garfield-camera-ready.png)

*Figure A3: Qualitative comparison with GARField. We conduct feature clustering across the whole scene (LERF-figurines). Compared to GARField, which employs an additional feature field to model affinity features, SAGA demonstrates greater stability by utilizing explicit affinity features. At larger scales, SAGA effectively preserves the perception of small objects without merging them with other targets.*

![Figure](https://arxiv.org/html/2312.00860/extracted/6180491/saga-supp-vis-1.png)

*Figure A4: More qualitative results of SAGA.*
