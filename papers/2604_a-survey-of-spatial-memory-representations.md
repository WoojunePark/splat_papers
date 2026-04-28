---
title: "A Survey of Spatial Memory Representations for Efficient Robot Navigation"
date: 2026-04-13
arxiv: "2604.16482v1"
venue:
status: read

abstract: "As vision-based robots navigate larger environments, their spatial memory grows without bound, eventually exhausting computational resources, particularly on embedded platforms (8-16GB shared memory, $&lt;$30W) where adding hardware is not an option. This survey examines the spatial memory efficiency problem across 88 references spanning 52 systems (1989-2025), from occupancy grids to neural implicit representations. We introduce the $\alpha = M_{\text{peak}} / M_{\text{map}}$, the ratio of peak runtime memory (the total RAM or GPU memory consumed during operation) to saved map size (the persistent checkpoint written to disk), exposing the gap between published map sizes and actual deployment cost. Independent profiling on an NVIDIA A100 GPU reveals that $\alpha$ spans two orders of magnitude within neural methods alone, ranging from 2.3 (Point-SLAM) to 215 (NICE-SLAM, whose 47,MB map requires 10GB at runtime), showing that memory architecture, not paradigm label, determines deployment feasibility. We propose a standardized evaluation protocol comprising memory growth rate, query latency, memory-completeness curves, and throughput degradation, none of which current benchmarks capture. Through a Pareto frontier analysis with explicit benchmark separation, we show that no single paradigm dominates within its evaluation regime: 3DGS methods achieve the best absolute accuracy at 90-254,MB map size on Replica, while scene graphs provide semantic abstraction at predictable cost. We provide the first independently measured $\alpha$ reference values and an $\alpha$-aware budgeting algorithm enabling practitioners to assess deployment feasibility on target hardware prior to implementation."

website: 
code: 
openreview: 
issue: 

inputs:
  - posed-multi-view-images

outputs:
  - 3dgs

methods:
  - survey

benchmarks:
  - 

related:
  - 

compared:
  - 
---

# A Survey of Spatial Memory Representations for Efficient Robot Navigation

## My Notes



**[Note from GitHub, 2026-04-28]**

----
## Problem definition

This survey examines the `spatial memory efficiency` problem across 88 references spanning 52 systems (1989–2025), from occupancy grids to neural implicit representations.

### Contribution 1
We introduce the _overhead factor_ `α` = `M_peak` / `M_map`, the ratio of peak runtime memory (the total RAM or GPU memory consumed during operation) to saved map size (the persistent checkpoint written to disk), exposing the gap between published map sizes and actual deployment cost

We introduce the _overhead factor_ `α` = `M_peak` / `M_map`, a diagnostic metric that distinguishes `α_CPU` (process Resident Set Size, RSS) from `α_GPU` (device allocation), and compile the first cross-paradigm comparison of runtime versus persistent memory, exposing the gap between published map sizes and actual deployment cost

1
메모리 사용량을 디스크 사용량으로 나누는 게 어떤 의미가 있지? 제안하는 `M_peak`은 RAM(`α_CPU`) 혹은 VRAM(`α_GPU`) 사용량이고, `M_map`은 디스크 사용량으로 보임.

예를 들어 메모리/디스크 사용량을 공간 면적으로 나누는 건 '같은 공간을 표현하는데, 메모리/디스크를 얼마나 쓰는가?'의 측정 지표로 의미가 있을 수 있다고 봄. 그런데 디스크 사용량(`M_map`)은 기법에 따라 저장 방식이 달라서 크게 다를 것으로 예상됨. 그러면 제안한 `M_peak` / `M_map`은 사실상 `M_map`에 크게 좌우되지 않을까?

2
그리고 기법마다 경량화 가능한 정도가 다를 것으로 예상되는데, 이 서베이 페이퍼에서 이 부분도 고려가 되었는지 궁금함. 예를 들어, 기법에 따라 정확도 손실을 최소화하면서 bit를 적게 사용하기 위해 파라미터/영역 단위로 adaptive한 bit를 쓰거나, 기존 이미지/동영상의 codec을 쉽게 적용할 수 있거나 하는 등 경량화 기법이 다르게 적용될 것으로 예상됨. 그러면 기법에 따라서 feasible한 압축률이 다를 것으로 예상됨. (예를 들어, 어떤 기법은 naive 구현으로는 메모리를 많이 쓰는데, 쉽게 경량화가 가능해서 실제로 경량화 후 deploy한다면 훨씬 적게 메모리나 디스크를 사용해도 된다던가 등) 인트로에서도 '실제 deploy 환경을 고려한다면 메모리/디스크 사용량은 현실적인 제약이다'라고 주장한 만큼, 실제 deploy 된다면 반드시 적용될 수 밖에 없는 경량화에 대한 고려도 반영되었어야 하지 않나 생각함.

### Contribution 2
We independently profile five neural SLAM systems (Co-SLAM, NICE-SLAM, Point-SLAM, SplaTAM, SGS-SLAM) on an NVIDIA A100 GPU, revealing that  `α_GPU` varies by two orders of magnitude even within neural methods: from 2.3 (Point-SLAM) to 215 (NICE-SLAM, whose 47 MB map requires 10 GB at runtime). These are, to our knowledge, the first independently measured `α_GPU` values for neural SLAM (Table [3](https://arxiv.org/html/2604.16482v1#S3.T3), Fig. [4](https://arxiv.org/html/2604.16482v1#S5.F4)).

일단 `α` 측정 방식에 동의가 안 돼서 두 자릿수 차이의 의의도 쉽게 동의가 안 됨.

### Contribution 3
    - a standardized evaluation protocol with four complementary metrics beyond static map-size reporting (Section [5](https://arxiv.org/html/2604.16482v1#S5))
    - α-aware budgeting algorithm that lets practitioners compute maximum feasible map size from two inputs, namely the memory budget and α, before selecting a representation (Algorithm [1](https://arxiv.org/html/2604.16482v1#algorithm1)).

### Contribution 4
We present a Pareto frontier analysis with explicit benchmark separation (Fig. [3](https://arxiv.org/html/2604.16482v1#S4.F3)), a taxonomy of 52 systems across four paradigm families (Fig. [2](https://arxiv.org/html/2604.16482v1#S0.F2)), memory dynamics categorization, and concrete open challenges with specific research questions

## Take aways
### Table 3.
    - 3DGS 기반 기법들이 정밀도가 월등히 좋다. (낮은 ATE (cm), 높은 PSNR(dB))
    - 다만 3DGS 기반 기법들이 FPS가 낮고, Peak 메모리, Map 디스크 사용량이 둘 다 높다. 경량화의 여기가 무척 높다고 볼 수 있는 부분.
    - Sparse 기법들이 정밀도는 낮아도 메모리/디스크 사용량 자릿수가 다를 정도로 낮고, FPS도 월등히 좋다.

3DGS를 (정밀도를 유지하면서) sparse하게 표현하거나, 경량화 적용이 필요하다고 볼 수 있는 부분

### Figure 4.
    - 다른 기법은 Run Progress 대비 GPU Memory 사용량이 비교적 일정
    - 이에 반해 3DGS 기반 기법인 SpalTAM은 거의 선형적으로 증가
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


