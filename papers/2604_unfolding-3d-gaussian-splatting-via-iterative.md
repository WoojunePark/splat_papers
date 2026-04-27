---
title: "Unfolding 3D Gaussian Splatting via Iterative Gaussian Synopsis"
date: 2026-04-13
arxiv: "2604.11685v1"
venue:
status: to-read

abstract: "3D Gaussian Splatting (3DGS) has become a state-of-the-art framework for real-time, high-fidelity novel view synthesis. However, its substantial storage requirements and inherently unstructured representation pose challenges for deployment in streaming and resource-constrained environments. Existing Level-of-Detail (LOD) strategies, particularly those based on bottom-up construction, often introduce redundancy or lead to fidelity degradation. To overcome these limitations, we propose Iterative Gaussian Synopsis, a novel framework for compact and progressive rendering through a top-down &#34;unfolding&#34; scheme. Our approach begins with a full-resolution 3DGS model and iteratively derives coarser LODs using an adaptive, learnable mask-based pruning mechanism. This process constructs a multi-level hierarchy that preserves visual quality while improving efficiency. We integrate hierarchical spatial grids, which capture the global scene structure, with a shared Anchor Codebook that models localized details. This combination produces a compact yet expressive feature representation, designed to minimize redundancy and support efficient, level-specific adaptation. The unfolding mechanism promotes inter-layer reusability and requires only minimal data overhead for progressive refinement. Experiments show that our method maintains high rendering quality across all LODs while achieving substantial storage reduction. These results demonstrate the practicality and scalability of our approach for real-time 3DGS rendering in bandwidth- and memory-constrained scenarios."

website: 
code: 
openreview: 
issue: 38

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

# Unfolding 3D Gaussian Splatting via Iterative Gaussian Synopsis

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

![Figure](https://arxiv.org/html/2604.11685v1/x1.png)

*Figure 1: Iterative Gaussian Synopsis enables hierarchical “unfolding” of 3D Gaussian Splatting. The top rows illustrate the anchor structure alongside the derived 3D Gaussians at both full resolution and progressively condensed levels. The bottom rows compare the Level-of-Detail progression from a compact synopsis (starting at 6.5MB) to the highest fidelity (50.7MB) for our method, against a standard 3DGS baseline with a total size of 601.1MB. Our approach achieves clearer intermediate representations and significantly improved efficiency, delivering comparable visual quality at a fraction of the storage cost.*

![Figure](https://arxiv.org/html/2604.11685v1/x2.png)

*Figure 2: Comparison of LOD Construction Strategies. Left (Bottom-Up Increment): A conventional bottom-up approach that builds from a coarse base layer by sequentially adding enhancement layers, typically requiring updates to the opacity or parameters of previous layers. Right (Top-Down Unfolding): Our proposed top-down unfolding strategy, where lower levels of detail are systematically derived from a full-fidelity model, ensuring coherent simplification and improved inter-layer consistency.*

![Figure](https://arxiv.org/html/2604.11685v1/x3.png)

*Figure 3: Overview of the Iterative Gaussian Synopsis Framework. Top: The full-resolution 3DGS model is progressively “unfolded” into coarser LODs using a learnable, mask-guided pruning strategy. Bottom: The resulting hierarchical LODs support efficient progressive rendering, where visual quality improves smoothly as more data is streamed, transitioning seamlessly from a coarse structural outline to a high-fidelity reconstruction.*

![Figure](https://arxiv.org/html/2604.11685v1/x4.png)

*Figure 4: Our hierarchical architecture. The hierarchical grids capture multi-scale contextual information while the learnable codebook models localized details, formimg the foundation for unfolding into LODs.*

![Figure](https://arxiv.org/html/2604.11685v1/x5.png)

*Figure 5: Qualitative comparison of LOD rendering across different methods. Our method yields superior visual quality (higher PSNR, and clearer details as shown in zoomed-in views) at each level, while requiring substantially less storage compared to all baseline methods.*

![Figure](https://arxiv.org/html/2604.11685v1/exp/abla_PSNR.png)

*(a)*

![Figure](https://arxiv.org/html/2604.11685v1/exp/abla_SSIM.png)

*(b)*

![Figure](https://arxiv.org/html/2604.11685v1/exp/abla_LPIPS.png)

*(c)*

![Figure](https://arxiv.org/html/2604.11685v1/x6.png)

*Figure 7: Qualitative comparison of LOD rendering across different ablated versions. The visual and quantitative results confirm the necessity of our proposed modules: adding Level-aware Decoding (LAD) or Coherent Basis Modulation (CBM) enhances rendering quality across the entire LOD hierarchy.*

## LLM Summary


