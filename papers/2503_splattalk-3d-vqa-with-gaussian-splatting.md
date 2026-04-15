---
title: "SplatTalk: 3D VQA with Gaussian Splatting"
date: 2025-03-08
arxiv: "2503.06271"
venue:
status: to-read

abstract: "Language-guided 3D scene understanding is important for advancing applications in robotics, AR/VR, and human-computer interaction, enabling models to comprehend and interact with 3D environments through natural language. While 2D vision-language models (VLMs) have achieved remarkable success in 2D VQA tasks, progress in the 3D domain has been significantly slower due to the complexity of 3D data and the high cost of manual annotations. In this work, we introduce SplatTalk, a novel method that uses a generalizable 3D Gaussian Splatting (3DGS) framework to produce 3D tokens suitable for direct input into a pretrained LLM, enabling effective zero-shot 3D visual question answering (3D VQA) for scenes with only posed images. During experiments on multiple benchmarks, our approach outperforms both 3D models trained specifically for the task and previous 2D-LMM-based models utilizing only images (our setting), while achieving competitive performance with state-of-the-art 3D LMMs that additionally utilize 3D inputs. Project website: this https URL"

website: https://splat-talk.github.io
code: https://github.com/ngailapdi/SplatTalk
issue: 6

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

![Figure](https://arxiv.org/html/2503.06271/x2.png)

*Figure 2: Overview. Left: During the self-supervised 3D-language Gaussian Splatting training phase, multiple RGB input views are first encoded into Gaussian latent features (Gaussian triplets). These latent features are then decoded into Gaussian parameters for rendering, along with a low-dimensional visual-language feature ffitalic_f. To ensure proper supervision of this low-dimensional feature, we train an autoencoder that maps the high-dimensional, unbounded features obtained from LLaVA-OV, specifically, the visual tokens serving as direct inputs to the LLM, onto a low-dimensional hypersphere space. Right: During 3D VQA inference, visual-language features are directly extracted from the 3D Gaussians. These features are then mapped back to the original high-dimensional space using the pretrained decoder and subsequently used as direct visual token inputs to the LLM. LoRA fine-tuning of the LLM is optional.*

![Figure](https://arxiv.org/html/2503.06271/x3.png)

*Figure 3: Qualitative results on ScanQA, scene0030_00 and scene0084_00. We compare responses from LLaVA-OV, our model (Ours), and the ground truth (GT) for spatial reasoning questions in 3D VQA. Each scene highlights the referenced objects with red circles, and key relative objects are marked in blue. The answers from each model are displayed in color-coded speech bubbles: LLaVA-OV (brown), Ours (blue), and GT (green). With its 3D-aware representation, our model exhibits improved spatial reasoning capabilities, accurately identifying relationships between objects that are far apart and may never co-occur in the same image (e.g., door and window). More examples in Supp.*

![Figure](https://arxiv.org/html/2503.06271/x4.png)

*Figure 4: Qualitative results on ScanQA, scene0389_00 and scene0222_00. We compare responses from LLaVA-OV, our model (Ours), and the ground truth (GT) for spatial reasoning questions in 3D VQA. Each scene highlights the referenced objects with red circles, and key relative objects are marked in blue. The answers from each model are displayed in color-coded speech bubbles: LLaVA-OV (brown), Ours (blue), and GT (green). With its 3D-aware representation, our model exhibits improved spatial reasoning capabilities.*

![Figure](https://arxiv.org/html/2503.06271/x5.png)

*Figure 5: Qualitative results on ScanQA, scene0100_00, scene0193_00, and scene0426_00. We compare responses from LLaVA-OV, our model (Ours), and the ground truth (GT) for spatial reasoning questions in 3D VQA. Each scene highlights the referenced objects with red circles, and key relative objects are marked in blue. The answers from each model are displayed in color-coded speech bubbles: LLaVA-OV (brown), Ours (blue), and GT (green). With its 3D-aware representation, our model exhibits improved spatial reasoning capabilities.*
