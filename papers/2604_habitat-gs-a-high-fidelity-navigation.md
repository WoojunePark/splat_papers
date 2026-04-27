---
title: "Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting"
date: 2026-04-14
arxiv: "2604.12626v1"
venue:
status: to-read

abstract: "Training embodied AI agents depends critically on the visual fidelity of simulation environments and the ability to model dynamic humans. Current simulators rely on mesh-based rasterization with limited visual realism, and their support for dynamic human avatars, where available, is constrained to mesh representations, hindering agent generalization to human-populated real-world scenarios. We present Habitat-GS, a navigation-centric embodied AI simulator extended from Habitat-Sim that integrates 3D Gaussian Splatting scene rendering and drivable gaussian avatars while maintaining full compatibility with the Habitat ecosystem. Our system implements a 3DGS renderer for real-time photorealistic rendering and supports scalable 3DGS asset import from diverse sources. For dynamic human modeling, we introduce a gaussian avatar module that enables each avatar to simultaneously serve as a photorealistic visual entity and an effective navigation obstacle, allowing agents to learn human-aware behaviors in realistic settings. Experiments on point-goal navigation demonstrate that agents trained on 3DGS scenes achieve stronger cross-domain generalization, with mixed-domain training being the most effective strategy. Evaluations on avatar-aware navigation further confirm that gaussian avatars enable effective human-aware navigation. Finally, performance benchmarks validate the system&#39;s scalability across varying scene complexity and avatar counts."

website: https://zju3dv.github.io/habitat-gs
code: https://github.com/isaac-sim/IsaacSim
openreview: 
issue: 45

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

# Habitat-GS: A High-Fidelity Navigation Simulator with Dynamic Gaussian Splatting

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

![Figure](https://arxiv.org/html/2604.12626v1/x1.png)

*Figure 1: Habitat-GS is a navigation-centric embodied simulation platform with 3DGS and dynamic gaussian avatars. Compared to traditional mesh-based simulators (left), our 3DGS-based simulator (right) preserves high-frequency visual details and view-dependent effects, while gaussian avatars provide realistic and dynamic human presence for human-aware navigation scenarios, thus helping train more robust agents.*

![Figure](https://arxiv.org/html/2604.12626v1/x2.png)

*Figure 2: System overview of Habitat-GS. From left to right: Asset Preparation, where 3DGS scene assets and gaussian avatar assets are prepared respectively. Habitat-GS Simulation Environment, where the render engine performs 3DGS rasterization for scene gaussians and LBS deformation followed by rasterization for avatar gaussians, producing RGB-D observations. The NavMesh blocking module retrieves pre-computed proxy capsules at runtime and injects them into the NavMesh for obstacle blocking. Embodied Agent Loop, where the agent policy consumes sensor observations, executes actions, and receives rewards shaped by both navigation success and avatar collision.*

![Figure](https://arxiv.org/html/2604.12626v1/x3.png)

*Figure 3: Visual comparison of scene rendering. Mesh-based rendering (left) vs. our 3DGS rendering (right). Our simulator is based on 3DGS, which preserves high-frequency details and supports diverse sources of rendering assets.*

![Figure](https://arxiv.org/html/2604.12626v1/x4.png)

*Figure 4: Qualitative comparison of mesh avatars and gaussian avatars. Gaussian avatars exhibit significantly higher visual fidelity, preserving fine-grained details such as clothing wrinkles and hair texture.*

![Figure](https://arxiv.org/html/2604.12626v1/x5.png)

*Figure 5: VLM scene quality assessment. Gemini 3.0 Pro evaluates 240 rendered screenshots from each domain on three perceptual dimensions. GS scenes consistently outperform mesh scenes, confirming their superior visual fidelity and diversity.*

![Figure](https://arxiv.org/html/2604.12626v1/x6.png)

*Table 2: PointNav results and training curves. (a) Results across different training domain mixtures. Agents are trained on varying ratios of mesh (M) and 3DGS (G) scenes and evaluated on disjoint mesh and GS test sets. SR and SPL are in %; DTG is in meters (↓\downarrow). Best and Second best results per column are highlighted. (b) Training success rate curve for 100 Mesh (Config A). (c) Training success rate curve for 100 GS (Config B).*

![Figure](https://arxiv.org/html/2604.12626v1/x8.png)

*Table 3: Avatar-aware PointNav results. Top: Two training configurations are evaluated: a GS scene baseline without avatars, and a GS scene populated with GS avatars. Agents are evaluated on both mesh and GS dynamic test sets to assess in-domain performance and cross-domain generalization. SR, SPL and CR are in %. CR is the fraction of collision steps (↓\downarrow). PSI is the average personal-space intrusion (↓\downarrow). Bottom: Visual demonstration of our avatar-aware navigation policy. Agent successfully navigates through gaussian avatars without collision or personal space intrusion.*

![Figure](https://arxiv.org/html/2604.12626v1/x10.png)

*Figure 6: System architecture of Habitat-GS. The system adopts a “visual–navigation decoupling” design principle, separating the visual rendering modules handled by the CUDA-based 3DGS rasterizer and LBS deformation, from the navigation module managed by the traditional NavMesh and injected proxy capsules. This allows for photorealistic agent observations without modifying the core Habitat-Sim navigation logic.*

![Figure](https://arxiv.org/html/2604.12626v1/x11.png)

*Figure 7: Additional visualizations of 3DGS scenes and gaussian avatars. Habitat-GS supports real-time rendering of diverse, large-scale indoor and outdoor environments with photorealistic quality, while simultaneously integrating high-fidelity drivable human avatars to facilitate human-aware embodied AI research.*

![Figure](https://arxiv.org/html/2604.12626v1/x12.png)

*Figure 8: Qualitative visualization of navigation episodes. Example episodes from our navigation experiments conducted in the Habitat-GS environment. The visualizations illustrate agent trajectories in 3DGS scenes, demonstrating learned navigation behaviors including goal-directed path planning and human-aware obstacle avoidance.*

## LLM Summary


