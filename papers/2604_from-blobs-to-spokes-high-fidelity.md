---
title: "From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians"
date: 2026-04-08
arxiv: "2604.07337v1"
venue:
status: to-read

abstract: "3D Gaussian Splatting (3DGS) has revolutionized fast novel view synthesis, yet its opacity-based formulation makes surface extraction fundamentally difficult. Unlike implicit methods built on Signed Distance Fields or occupancy, 3DGS lacks a global geometric field, forcing existing approaches to resort to heuristics such as TSDF fusion of blended depth maps. Inspired by the Objects as Volumes framework, we derive a principled occupancy field for Gaussian Splatting and show how it can be used to extract highly accurate watertight meshes of complex scenes. Our key contribution is to introduce a learnable oriented normal at each Gaussian element and to define an adapted attenuation formulation, which leads to closed-form expressions for both the normal and occupancy fields at arbitrary locations in space. We further introduce a novel consistency loss and a dedicated densification strategy to enforce Gaussians to wrap the entire surface by closing geometric holes, ensuring a complete shell of oriented primitives. We modify the differentiable rasterizer to output depth as an isosurface of our continuous model, and introduce Primal Adaptive Meshing for Region-of-Interest meshing at arbitrary resolution. We additionally expose fundamental biases in standard surface evaluation protocols and propose two more rigorous alternatives. Overall, our method Gaussian Wrapping sets a new state-of-the-art on DTU and Tanks and Temples, producing complete, watertight meshes at a fraction of the size of concurrent work-recovering thin structures such as the notoriously elusive bicycle spokes."

website: http://diego1401.github.io/BlobsToSpokesWebsite/index.html
code: https://github.com/diego1401/GaussianWrapping
openreview: 
issue: 21

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

# From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians

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

![Figure](https://arxiv.org/html/2604.07337v1/x1.png)

*Figure 1: High-fidelity surface reconstruction from 3D Gaussian Splatting. Our method, Gaussian Wrapping, reconstructs watertight and textured surface meshes of full 3D scenes given multiview RGB images, by interpreting 3D Gaussians as stochastic oriented surface elements. This figure illustrates the resulting surface meshes, with and without the RGB texture. Our meshes represent the full scene—including background geometry and extremely thin structures such as bicycle spokes where existing methods fail—with a significantly more compact representation than concurrent works [Zhang2026GeometryGrounded, chen2024pgsr].*

![Figure](https://arxiv.org/html/2604.07337v1/images/free_renders/bonsai_1_textured.jpg)

**

![Figure](https://arxiv.org/html/2604.07337v1/images/free_renders/bonsai_3_textured.jpg)

**

![Figure](https://arxiv.org/html/2604.07337v1/images/free_renders/stump_3_textured.jpg)

*(a) Mesh w/wo texture*

![Figure](https://arxiv.org/html/2604.07337v1/images/free_renders/stump_4_textured.jpg)

*(b) Close-up view of Mesh w/wo texture*

![Figure](https://arxiv.org/html/2604.07337v1/x2.png)

*Figure 3: Wrapping the surface with Oriented Gaussians. Our Gaussian Wrapping setting allows to evaluate the normal and vacancy fields of the scene. We first leverage the vacancy on our pivot-based marching tetrahedra meshing approach. We then leverage both the vacancy and normal fields in our Primal Adaptive Meshing.*

![Figure](https://arxiv.org/html/2604.07337v1/images/mipnerf360_closeup/bonsai_mtet_close.jpeg)

**

![Figure](https://arxiv.org/html/2604.07337v1/images/mipnerf360_closeup/bonsai_pam_close.jpeg)

**

![Figure](https://arxiv.org/html/2604.07337v1/images/mipnerf360_closeup/bycicle_mtet_close.jpeg)

*(a) Pivot-based Marching Tetrahedra*

![Figure](https://arxiv.org/html/2604.07337v1/images/mipnerf360_closeup/bycicle_pam_close.jpeg)

*(b) Primal Adaptive Mesh*

## LLM Summary

This report provides a detailed analysis of the research paper "From Blobs to Spokes: High-Fidelity Surface Reconstruction via Oriented Gaussians," focusing on its context, methodology, findings, and implications.

### 1. Authors and Institution(s)

The research was conducted by Diego Gomez, Antoine Guédon, Nissim Maruani, Bingchen Gong, and Maks Ovsjanikov.
All authors are affiliated with LIX, École Polytechnique, France. Nissim Maruani is additionally affiliated with Inria, Côte d’Azur, France.

### 2. How this Work Fits into the Broader Research Landscape

The reconstruction of high-quality 3D surfaces from 2D images is a fundamental problem in computer vision. Recent advancements in neural rendering, particularly Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS), have demonstrated proficiency in novel view synthesis, generating photorealistic images from arbitrary viewpoints. However, extracting accurate and explicit geometric representations, such as watertight meshes, from these volumetric or particle-based neural representations remains challenging.

Existing approaches to 3D surface reconstruction generally fall into two categories:
*   **Implicit representations (e.g., Signed Distance Functions or occupancy fields):** Methods like NeuS or VolSDF represent surfaces continuously and often produce topologically consistent results. However, they can be computationally intensive to train and may over-smooth fine details due to their global optimization nature.
*   **Explicit particle-based methods (e.g., 3DGS):** These methods represent scenes as discrete primitives (Gaussians), enabling real-time rendering and high visual fidelity. While capable of capturing fine details, they lack an inherent ordered structure, making direct mesh extraction non-trivial. Prior attempts to extract surfaces from 3DGS often rely on heuristics, such as TSDF fusion of blended depth maps, or auxiliary neural implicit fields, which can compromise rendering efficiency or detail capture.

A core limitation highlighted by this work is the conventional interpretation of a 3D Gaussian primitive. Standard approaches treat Gaussians as symmetric "blobs" of density, which conflicts with the asymmetric nature of an orientable surface—a boundary separating occupied and empty space. This symmetry bias makes accurate surface extraction from 3DGS difficult.

This paper positions itself as addressing this fundamental limitation by introducing a principled framework that reinterprets Gaussians as oriented surface elements. It draws inspiration from the "Objects as Volumes" (OaV) framework, which theoretically links volumetric rendering quantities to geometric fields. By establishing a robust theoretical connection between 3DGS and implicit surface reconstruction through oriented Gaussians, the work aims to bridge the gap between efficient volumetric rendering and high-fidelity explicit surface reconstruction. This approach contrasts with prior works that either use auxiliary implicit fields, rely on heuristic depth definitions, or suffer from surface erosion.

### 3. Key Objectives and Motivation

The primary objective of this research is to develop a principled method for reconstructing highly accurate, watertight, and textured surface meshes of complex 3D scenes directly from multiview RGB images, leveraging the efficiency and visual quality of 3D Gaussian Splatting.

The key motivations and specific objectives are:

*   **Overcoming 3DGS's surface extraction limitations:** 3DGS excels at novel view synthesis due to its opacity-based formulation and differentiable rasterization. However, this formulation, which treats Gaussians as symmetric density blobs, inherently lacks a global geometric field (like a Signed Distance Field or occupancy field) needed for robust surface extraction. Existing methods typically resort to approximations and heuristics (e.g., TSDF fusion of blended depth maps), leading to compromised geometric accuracy, missing details (especially thin structures), or non-watertight meshes.
*   **Introducing a principled geometric interpretation for Gaussians:** The authors hypothesize that the difficulty stems from interpreting Gaussians as symmetric volumes of mass rather than oriented surface elements. Their core motivation is to reinterpret the Gaussian primitive's role. Inspired by the "Objects as Volumes" (OaV) framework, which models occupied regions as a random set and occupancy as a probability, they aim to derive a principled occupancy field for 3DGS.
*   **Enabling closed-form geometric quantities:** A central objective is to introduce a learnable oriented normal at each Gaussian primitive and define an adapted attenuation formulation. This conceptual shift is motivated by the need to derive closed-form expressions for both the normal and occupancy (or vacancy) fields at arbitrary spatial locations without requiring additional learnable parameters or auxiliary networks. This would provide a direct link between Gaussian parameters and surface geometry.
*   **Ensuring watertight and complete surface reconstruction:** The standard symmetric Gaussian interpretation makes it difficult for primitives to form a complete, sealed boundary around an object. A key motivation is to develop a "wrapping" strategy to ensure Gaussians effectively form a watertight shell. This involves identifying geometric gaps where the oriented surface assumption is violated and adaptively densifying the representation to close holes.
*   **Improving mesh extraction robustness and adaptivity:** To effectively utilize the derived geometric fields, the authors aim to introduce a novel mesh extraction procedure that is both robust and adaptive. This is motivated by the limitations of conventional methods (e.g., Marching Cubes on uniform grids) in capturing fine details or scaling to large, unbounded scenes efficiently.
*   **Addressing biases in surface evaluation protocols:** The authors identify fundamental biases in standard evaluation protocols for Gaussian-based surface reconstruction, particularly concerning how point clouds are sampled from meshes and how ground truth data is acquired. A motivation is to propose more rigorous and fair evaluation alternatives to provide a more accurate assessment of geometric quality.
*   **Recovering challenging fine details:** Specifically, the ability to reconstruct extremely thin structures, such as bicycle spokes, which are notoriously difficult for existing methods, serves as a strong motivating example for the proposed approach's potential for high-fidelity detail capture.

### 4. Methodology and Approach

The method, termed "Gaussian Wrapping," proposes a framework for high-fidelity surface reconstruction from 3D Gaussian Splatting by reinterpreting Gaussians as stochastic oriented surface elements. It involves a modified Gaussian representation, a specialized training strategy, and an adaptive mesh extraction pipeline.

**4.1. Gaussian Wrapping Framework**

The core intuition is that for accurate surface reconstruction, Gaussians must form a sealed boundary around the object. This is achieved by:

*   **Oriented-Gaussians:** Each Gaussian primitive $G_i(x) = \alpha_i \exp(-\frac{1}{2}(x - \mu_i)^T \Sigma_i^{-1} (x - \mu_i))$ is augmented with a learnable, oriented normal vector parameter $n_i \in S^2$. These normals are the only additional learnable parameters. The normal $n_i$ is parameterized using a sign $s_i \in \mathbb{R}$ and a direction $d_i \in \mathbb{R}^3$, with $n_i = \tanh(s_i) \cdot \frac{d_i}{\|d_i\|}$, to stabilize optimization and allow for direction flipping.
*   **Adapted Attenuation Formulation:** The standard 3DGS opacity-based formulation is reinterpreted as an attenuation-based volumetric rendering model, drawing a theoretical link to the "Objects as Volumes" (OaV) framework. OaV connects the vacancy field ($v(x) = 1 - O(x)$, probability of a point being unoccupied) to the attenuation field $\sigma(x, w)$ under reciprocal exponential transport. The paper derives an "oriented attenuation coefficient" for each Gaussian $G_i$ as $\bar{\sigma}_i(x, w) = \mathbf{1}_{n_i^T (x-\mu_i) \geq 0} |w \cdot \nabla \log(1 - G_i(x))|$. This formulation ensures reciprocity of the total attenuation, a necessary condition for OaV.
*   **Closed-form Geometric Fields:** By satisfying OaV conditions, the method derives closed-form expressions for the Gaussian vector field $V(x) = \nabla \log v(x) = \sum_{i=1}^N \mathbf{1}_{n_i^T (x-\mu_i) \geq 0} \nabla \log(1 - G_i(x))$, and the Gaussian normal field $N(x) = \frac{V(x)}{\|V(x)\|}$. These fields provide explicit geometric quantities at any spatial location without additional neural network queries.
*   **Modified Differentiable Rasterizer:** The differentiable CUDA rasterizer from Geometry-Grounded Gaussian Splatting [57] is modified to match the proposed attenuation formulation. It renders depth as the exact 0.5-isosurface of the continuous geometric field (transmittance median), which is used for consistency.

**4.2. Training Strategy**

The training strategy promotes the "wrapping" behavior of Gaussians to form a continuous, watertight shell:

*   **Normal Alignment Loss ($L_N$):** A novel consistency loss $L_N = \sum_p (1 - N(p) \cdot \nabla D(p))$ is introduced. $N(p)$ is the rendered oriented normal at pixel $p$ (alpha-blending of Gaussian normals $n_i$), and $\nabla D(p)$ is the image-space gradient of the rendered depth. This loss encourages the learnable normals $n_i$ to align with the estimated surface normals from depth gradients, thereby enforcing geometric consistency and outward orientation.
*   **Normal-aware Densification:** Geometric gaps, where Gaussians fail to adequately cover surface sides, lead to high $L_N$ values. Every $K$ iterations, errors from $L_N(p)$ are propagated to individual Gaussians via their blending weights. Gaussians with high errors are cloned, and one clone has its normal flipped. This strategy reinforces the "shell" of oriented primitives and closes holes.
*   **Combined Loss Function:** The total loss includes the standard photometric loss ($L_{RGB}$), depth-normal consistency ($L_{DN}$), a multi-view loss ($L_{MV} = \lambda_{pc} L_{pc} + \lambda_{gc} L_{gc}$), and the novel normal alignment loss ($L_N$). Specific weights are applied ($\lambda_{DN}=0.05, \lambda_N=0.05, \lambda_{pc}=0.6, \lambda_{gc}=0.02$).

**4.3. Mesh Extraction**

The method leverages the derived vacancy field $v(x)$ as an implicit function for mesh extraction.
The vacancy $v(x)$ is estimated as a lower bound: $v(x) \geq \max_{(o,w) \in T_c} (\prod_{i=1}^N (1 - \bar{G}^{(i)}_{o,w}(t)) : x = o + tw, t > 0)$, where $T_c$ is the set of all training camera rays. This robust estimation avoids artifacts from hidden Gaussians.

Two mesh extraction procedures are presented:

*   **Pivot-Based Marching Tetrahedra:** This method generates a watertight mesh by spawning two Delaunay pivots per Gaussian: its center $\mu_i$ and an outward-shifted point $\mu_i + 3s_i n_i$ (where $s_i$ is ellipsoid scaling along $n_i$). Occupancy values are computed at these pivots using the vacancy lower bound. Marching Tetrahedra is then applied to the resulting Delaunay triangulation. Vertices are refined to the 0.5-isosurface via binary search. This approach uses significantly fewer pivots (2 per Gaussian) compared to prior works (e.g., 9), yielding lighter meshes without sacrificing fidelity.
*   **Primal Adaptive Meshing:** This advanced, adaptive framework improves mesh generation by decoupling resolution from Gaussian distribution. It proceeds in four stages:
    1.  **Vertices Initialization:** Points are sampled from the faces of an initial Marching Tetrahedra mesh, weighted inversely proportional to their distance from the nearest training camera.
    2.  **Isosurface Refinement:** Vertices are iteratively projected onto the 0.5-isosurface of $v(x)$ using a Newton update step: $x_{i+1} = x_i + \frac{1}{2}(0.5 - v(x_i))N(x_i)$. This step leverages the computed normal field $N(x)$.
    3.  **Filtering:** Outlier vertices (where $|0.5 - v(x)| > \epsilon$) are removed. Stages 1-3 iterate until no more points are removed.
    4.  **Delaunay Triangulation and Mesh Extraction:** A Delaunay tetrahedralization of the remaining vertices is computed. Tetrahedra are classified as "inside" or "outside" based on the vacancy value of randomly sampled interior points. The final surface mesh consists of triangle faces separating these classified tetrahedra. This allows for region-of-interest meshing at arbitrary resolution, improving smoothness and reducing discretization artifacts.

### 5. Main Findings and Results

The research paper presents quantitative and qualitative evaluations on standard benchmarks, highlighting the efficacy of Gaussian Wrapping and addressing biases in existing evaluation protocols.

**5.1. Surface Evaluation Protocols**
The authors identify fundamental flaws in standard evaluation practices for Gaussian-based surface reconstruction, particularly on Tanks and Temples (T&T) and structured scan datasets. These flaws include:
1.  **Vertex-density bias:** Conventional approaches construct predicted surface point clouds from mesh vertices and face centers, favoring denser tessellations over geometric accuracy.
2.  **Ground Truth (GT) acquisition bias:** GT data, often acquired via laser scanning, inherently contains occlusions and missing geometry (e.g., surfaces at grazing angles). Methods that produce incomplete meshes aligning with these GT gaps can receive inflated scores.

To address these biases, two alternative evaluation strategies are proposed:
*   **Uniform Sampling Evaluation:** A fixed number of points are uniformly sampled from the reconstructed mesh surface within the GT crop volume, eliminating vertex-count bias for geometric comparison.
*   **Virtual Scanning Evaluation:** To account for GT acquisition bias, depth maps of reconstructed meshes are rendered from input camera poses and back-projected into the GT crop volume, simulating the original data acquisition process.

**5.2. Quantitative Results**

*   **Geometry on DTU:** Gaussian Wrapping yields competitive Chamfer Distance results on the DTU dataset, performing comparably to GGGS [57] and outperforming most other methods, including foreground-only approaches. Importantly, it does not exhibit the surface erosion artifacts sometimes observed in GGGS.
*   **Geometry on Tanks and Temples (T&T):**
    *   **Uniform Sampling Evaluation:** The method establishes a new state-of-the-art among full-scene extraction methods under this unbiased protocol.
    *   **Virtual Scanning Evaluation:** Gaussian Wrapping achieves state-of-the-art performance, matching GGGS, and demonstrating robustness by showing that methods like PGSR (which appeared strong in legacy metrics due to GT bias) do not retain their advantage when this bias is accounted for.
*   **Mesh-Based Rendering (MBR) on T&T and Mip-NeRF 360:** MBR metrics, which assess background reconstruction quality and mesh completeness, show competitive performance for Gaussian Wrapping. It sets a new state-of-the-art on Mip-NeRF 360, particularly for challenging unbounded scenes. This evaluation further reveals weaknesses in methods like PGSR, whose depth-filtering strategy leads to significant holes in background geometry and degraded rendering quality, corroborating the identified evaluation bias.
*   **Novel View Synthesis (NVS) on Mip-NeRF 360:** While not the primary objective, Gaussian Wrapping achieves competitive NVS performance, setting a new state-of-the-art for outdoor scenes, indicating the representational effectiveness in complex environments.

**5.3. Qualitative Results**
Visual comparisons demonstrate that Gaussian Wrapping consistently produces surfaces with:
*   Sharper fine details.
*   Fewer topological artifacts.
*   Better coverage of extremely thin structures (e.g., bicycle spokes, blades of grass), where many baseline methods either erode geometry or fail to close holes.
*   Watertight meshes at a significantly more compact representation size than concurrent works.

**5.4. Ablation Studies**

*   **Normal Alignment Losses ($L_N$) and Densification:** Ablation studies show that while F1 scores remain stable (indicating the rasterizer already places Gaussians near the isosurface), MBR metrics improve substantially with the normal alignment loss and densification. These components are critical for aligning Gaussians with the surface, enabling clean mesh extraction with only two pivots per Gaussian, and preventing the loss of fine details and sharp edges.
*   **Generalizability:** The Gaussian Wrapping approach demonstrates generalizability by being successfully plugged into RaDe-GS [56], yielding consistent improvements across all T&T scenes. This indicates its effectiveness as an architectural-agnostic drop-in regularizer.

### 6. Significance and Potential Impact

This research presents a significant advancement in 3D surface reconstruction from neural rendering techniques, particularly 3D Gaussian Splatting (3DGS).

**Significance:**

*   **Principled Geometric Framework:** The work introduces a principled theoretical connection between 3DGS and implicit surface reconstruction by reinterpreting Gaussians as "oriented stochastic surface elements," grounded in the "Objects as Volumes" (OaV) framework. This moves beyond heuristic approaches, providing a robust, closed-form derivation for occupancy and normal fields directly from Gaussian parameters.
*   **High-Fidelity and Watertight Reconstruction:** Gaussian Wrapping demonstrates the ability to reconstruct complete, watertight meshes of complex scenes, including notoriously challenging extremely thin structures (e.g., bicycle spokes) and background geometry, where many existing methods struggle with erosion or missing parts.
*   **Compact Representation:** The method achieves state-of-the-art geometric fidelity with a significantly more compact mesh representation compared to concurrent works, which can lead to more efficient storage and processing.
*   **Adaptive and Robust Mesh Extraction:** The introduction of Primal Adaptive Meshing allows for fine-grained mesh extraction at controllable resolutions, effectively decoupling mesh quality from the underlying Gaussian distribution. The robust vacancy estimation method further minimizes artifacts from internal "floating" Gaussians.
*   **Improved Evaluation Protocols:** The paper critically exposes fundamental biases in standard surface evaluation metrics for Gaussian-based reconstruction and proposes two rigorous alternatives (Uniform Sampling and Virtual Scanning). This contribution is significant for advancing fair and accurate benchmarking in the field.
*   **Generalizability:** The core Gaussian Wrapping concepts (oriented normals, normal alignment loss, and densification) are shown to be generalizable, acting as an effective plug-in regularizer for other 3DGS-based surface reconstruction pipelines.

**Potential Impact:**

*   **Enhanced 3D Content Creation:** The ability to generate high-fidelity, watertight 3D meshes from casual multiview image captures could significantly benefit various applications, including virtual reality, augmented reality, gaming, digital twins, and visual effects, by simplifying the creation of photorealistic 3D assets.
*   **Robotics and Autonomous Systems:** Accurate and complete geometric scene representations are crucial for robot navigation, manipulation, and scene understanding. The method's robustness to thin structures could improve environmental perception.
*   **Broader Adoption of 3DGS:** By providing a principled solution for explicit surface extraction, this work enhances the utility of 3DGS beyond novel view synthesis, making it a more comprehensive tool for 3D reconstruction tasks.
*   **Foundation for Future Research:** The theoretical framework derived from OaV and the concept of oriented Gaussians could inspire further research into geometric interpretations of other neural rendering primitives or volumetric models, such as extending the formulation to more accurate volumetric rendering models like EVER [32]. Future work could also explore more principled sampling strategies for adaptive meshing, guided by local surface curvature or the Gaussian vector field, to optimize detail capture.
