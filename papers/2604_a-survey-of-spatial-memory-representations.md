---
title: "A Survey of Spatial Memory Representations for Efficient Robot Navigation"
date: 2026-04-13
arxiv: "2604.16482v1"
venue:
status: to-read

abstract: "As vision-based robots navigate larger environments, their spatial memory grows without bound, eventually exhausting computational resources, particularly on embedded platforms (8-16GB shared memory, $&lt;$30W) where adding hardware is not an option. This survey examines the spatial memory efficiency problem across 88 references spanning 52 systems (1989-2025), from occupancy grids to neural implicit representations. We introduce the $\alpha = M_{\text{peak}} / M_{\text{map}}$, the ratio of peak runtime memory (the total RAM or GPU memory consumed during operation) to saved map size (the persistent checkpoint written to disk), exposing the gap between published map sizes and actual deployment cost. Independent profiling on an NVIDIA A100 GPU reveals that $\alpha$ spans two orders of magnitude within neural methods alone, ranging from 2.3 (Point-SLAM) to 215 (NICE-SLAM, whose 47,MB map requires 10GB at runtime), showing that memory architecture, not paradigm label, determines deployment feasibility. We propose a standardized evaluation protocol comprising memory growth rate, query latency, memory-completeness curves, and throughput degradation, none of which current benchmarks capture. Through a Pareto frontier analysis with explicit benchmark separation, we show that no single paradigm dominates within its evaluation regime: 3DGS methods achieve the best absolute accuracy at 90-254,MB map size on Replica, while scene graphs provide semantic abstraction at predictable cost. We provide the first independently measured $\alpha$ reference values and an $\alpha$-aware budgeting algorithm enabling practitioners to assess deployment feasibility on target hardware prior to implementation."

website: 
code: 
openreview: 
issue: 48

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

# A Survey of Spatial Memory Representations for Efficient Robot Navigation

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

![Figure](https://arxiv.org/html/2604.16482v1/static/browse/0.3.4/images/arxiv-logo-one-color-white.svg)

*Figure 1: Evolution of spatial memory representations along two competing demands: geometric completeness and memory efficiency. Sparse features (1) traded completeness for efficiency; neural methods (2) recovered completeness via learned compression; scene graphs (3) added semantic abstraction. The scene graph box is dashed to indicate that the 48 MB figure reflects only the graph abstraction layer [26]; the required metric-semantic backend [54] adds scene-dependent cost (dashed arrow), shifting the true system footprint leftward. The scene graph’s vertical position reflects its semantic completeness (objects, rooms, places) rather than geometric fidelity.*

## LLM Summary


