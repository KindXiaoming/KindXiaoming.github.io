---
layout: post
title: A True World Model Requires Mixture of Compression
date: 2026-08-29
description:
tags: [Physics-of-AI, Methodology]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## The Tension Between Physics and Visual Realism

Today I came across an interesting [paper]\([https://arxiv.org/pdf/2608.15555), whose Figure](https://arxiv.org/pdf/2608.15555\), whose Figure) 2 shows that the visual realism (SSIM) and physical realism (ATE-3D) of video generation models are negatively correlated. If this finding is universal, we may have to stop and rethink the current path toward world models ———— it would suggest that visually realistic models (for entertainment) and physically realistic models (for embodiment) are difficult to unify.

<div class="cr-blog-figure" style="width: 50%; max-width: 100%; margin: 1rem auto;">

<img src="/assets/img/blogs/mixture-of-abstraction/ssim-ate.png" alt="SSIM vs ATE-3D correlation" style="width: 100%; max-width: 100%; height: auto; display: block;" />

</div>

---

## A Compression Perspective

Why are they difficult to unify? I would like to look at this question from the perspective of compression.

First, a "philosophical" question that has puzzled me for a long time is whether symbolism and connectionism (neural networks), which seem like fundamentally different paradigms, can actually be unified. From the perspective of data compressibility, they can ———— symbols emerge from data that are highly compressible, while less compressible data need to be handled by neural networks. Therefore, the world should not be divided into two discrete categories, the easy-to-compress (e.g., physics) and the hard-to-compress (e.g., complex textures), but rather viewed as a continuous spectrum:

\(\boxed{\text{Law} \rightarrow \text{Program} \rightarrow \text{Structured Latent} \rightarrow \text{Neural Latent} \rightarrow \text{Stochastic Residual}}\)

The further left we go, the higher the compression ratio, and the more we tend to call it understanding.

The further right we go, the harder it becomes to compress the information any further. Yet this information must still be preserved for photorealism, so we typically leave it to generative models.

---

## Homogeneous or Adaptive Compression

Here we make a conjecture, which we call the **Homogeneous Compression Conjecture**: a model tends to apply the same compression ratio to all parts of its input, regardless of whether they correspond to physics or complex visual details. This naturally gives rise to the tension between physics and visual realism. Given a dataset, when a model is too large, its compression ratio is low: its outputs look more visually realistic, but the underlying physics is not sufficiently compressed. When a model is too small, its compression ratio is high: its outputs look blurrier, but the physical structure is compressed more thoroughly.

Naturally, an ideal World Model should support multiple compression ratios, adaptively compressing different components to different degrees. Multi-scale approaches may indirectly and partially address this problem, but they are unlikely to get to its core. As illustrated below, compressibility and physical scale do not seem to have any obvious relationship.

<div class="cr-blog-figure" style="width: 85%; max-width: 100%; margin: 1rem auto;">

<img src="/assets/img/blogs/mixture-of-abstraction/compressibility-scale.png" alt="Compressibility and Scale Are Unrelated" style="width: 100%; max-width: 100%; height: auto; display: block;" />

</div>

As a fan of the **Minimum Description Length (MDL)** principle, I believe information theory may offer useful insights into world models ———— we should explicitly model **adaptive compression**, allowing neural networks to control the compression ratio applied to different components of the data, and ultimately build a world model that is both visually realistic and physically realistic.
