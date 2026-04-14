---
title: "SceneSplat: Gaussian Splatting-based Scene Understanding with Vision-Language Pretraining"
date: 2025-03-23
arxiv: "2503.18052"
venue:
status: to-read
authors:
  - Yue Li
  - Qi Ma
  - Runyi Yang
  - Huapeng Li
  - Mengjiao Ma
  - Bin Ren
  - Nikola Popovic
  - Nicu Sebe
  - Ender Konukoglu
  - Theo Gevers
  - Luc Van Gool
  - Martin R. Oswald
  - Danda Pani Paudel

abstract: "Recognizing arbitrary or previously unseen categories is essential for comprehensive real-world 3D scene understanding. Currently, all existing methods rely on 2D or textual modalities during training or together at inference. This highlights the clear absence of a model capable of processing 3D data alone for learning semantics end-to-end, along with the necessary data to train such a model. Meanwhile, 3D Gaussian Splatting (3DGS) has emerged as the de facto standard for 3D scene representation across various vision tasks. However, effectively integrating semantic reasoning into 3DGS in a generalizable manner remains an open challenge. To address these limitations, we introduce SceneSplat, to our knowledge the first large-scale 3D indoor scene understanding approach that operates natively on 3DGS. Furthermore, we propose a self-supervised learning scheme that unlocks rich 3D feature learning from unlabeled scenes. To power the proposed methods, we introduce SceneSplat-7K, the first large-scale 3DGS dataset for indoor scenes, comprising 7916 scenes derived from seven established datasets, such as ScanNet and Matterport3D. Generating SceneSplat-7K required computational resources equivalent to 150 GPU days on an L4 GPU, enabling standardized benchmarking for 3DGS-based reasoning for indoor scenes. Our exhaustive experiments on SceneSplat-7K demonstrate the significant benefit of the proposed method over the established baselines."

website: https://unique1i.github.io/SceneSplat_webpage
code: https://github.com/unique1i/SceneSplat

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

![Figure](https://arxiv.org/html/2503.18052/x2.png)

*Figure 2: SceneSplat Overview. The SceneSplat-7K dataset enables Vision-Language Pretraining and Self-Supervised Pretraining. For vision-language pretraining, we associate each 3D Gaussian primitive with semantic features based on our label collection process and train a generalizable open-vocabulary learner that predict per-gaussian embeddings. For self-supervised pretraining, we employ Masked Gaussian Modeling to reconstruct masked primitives, Self-Distillation Learning for augmentation-invariant features, and Language-Gaussian Alignment for scenes with collected labels. The former achieves state-of-the-art zero-shot segmentation results on ScanNet200 [5], ScanNet++ [57], and Matterport3D [2] benchmarks and the latter unlocks training on large-scale 3DGS data.*

![Figure](https://arxiv.org/html/2503.18052/extracted/6509026/figs/scannetpp_lang_pred_semseg/bde1e479ad00.jpeg)

*Figure 3: Qualitative Results of Zero-Shot 3D Semantic Segmentation on ScanNet++. SceneSplat demonstrates competitive zero-shot performance, note how our model correctly annotate the regions lacking ground truth labels, e.g., desks on the top row. Best viewed zoomed in and in color.*

![Figure](https://arxiv.org/html/2503.18052/x3.png)

*Figure 4: Text-Based 3DGS Scene Query. Given text queries and SceneSplat inference results for a 3DGS scene, we can effectively localize the corresponding splats (highlighted in red for queries ”Robot Arm”, ”Box”, and ”Keyboard”).*

![Figure](https://arxiv.org/html/2503.18052/extracted/6509026/figs/ablation/psnr_vs_iou_boxplot.png)

*Figure 5: Distribution of SceneSplat Zero-Shot Semantic Segmentation mIoU w.r.t. Input 3DGS Scene PSNR. Reported on the Matterport3D test split labeled in 21 semantic classes, the box plot shows a clear positive trend between the input 3DGS scene training PSNR and the resulted mIoU once applied SceneSplat language pretraining for zero-shot semantic segmentation. This encourages the careful curation of the collected 3DGS scene dataset.*

![Figure](https://arxiv.org/html/2503.18052/extracted/6509026/figs/ablation/ablation_iou_trend_combined.png)

*Figure 6: Overall and Class-Wise IoU Changes w.r.t. to the Nearest Neighbor Number During Majority Voting. We evaluate SceneSplat using different nearest 3DGS neighbors for zero-shot task at the point locations on ScanNet++ validation split. Overall mIoU increases with different class-wise relative IoU changes.*

![Figure](https://arxiv.org/html/2503.18052/extracted/6509026/figs/supp/scannetpp_zeroshot_supervised_iou_scatter.png)

*Figure A: Comparison of SceneSplat Zero-Shot Versus Fully Supervised Segmentation Across Object Classes. Notably, our zero-shot segmentation after vision language pretraining demonstrates better performance for 18 object classes, predominantly small objects such as headphone, printer, pot, and clothes hanger.*

![Figure](https://arxiv.org/html/2503.18052/extracted/6509026/figs/supp/scannet20/scannet20_00850.jpg)

*Figure B: Consistency Issue During 2D Vision-Language Feature Map Collection on ScanNet. Erroneous 2D feature maps are collected, as shown by the mislabeled regions in the neighboring figures. The root cause is that the SAMv2+SigLip2 process we use does not guarantee temporal consistency.*

![Figure](https://arxiv.org/html/2503.18052/x4.png)

*Figure C: Qualitative Zero-shot Semantic Segmentation Results on ScanNet++ Validation Scenes. SceneSplat effectively segments the scenes and helps annotate regions with missing labels in the ground truth.*

![Figure](https://arxiv.org/html/2503.18052/x5.png)

*Figure D: Self-supervised Reconstructions across Multiple Scenes. Each row shows (left to right) the unmasked input, masked scene, reconstruction, and a PCA projection of features*

![Figure](https://arxiv.org/html/2503.18052/x6.png)

*Figure E: Comparison of Scene Query Results Using Our Predictions and GT Language Labels on ScanNet++.*

## My Notes

