---
layout: post
title: Understanding cardinality (as in ResNext) from representation collapse
date: 2026-04-08
description:
tags: [Physics-of-AI, Representation, Cardinality]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

I was listening to the [7-hour podcast between Saining Xie and Xiaojun Zhang](https://www.youtube.com/watch?v=rIwgZWzUKm8), where Saining discussed his earlier work. That motivated me to dig deeper into it. The first paper I want to understand is [ResNext](https://arxiv.org/pdf/1611.05431), which introduces a branching structure: instead of using a single wide module, ResNext employs multiple narrow modules in parallel, sums their outputs, and then merges them into the residual stream. 

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/cardinality/resnext.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

This multi-branch design is reminiscent of mixture-of-experts (MoE), in the sense that both place multiple modules in parallel. The benefits of MoE have been discussed in [MOE-1](/blog/2026/moe-1/). However, multi-branch architectures are closer to dense modules, since they do not involve gating (unlike MoE). In this sense, a multi-branch layer can be viewed as a modularized version of a dense layer. Therefore, the core question becomes: what are the benefits (or drawbacks) of modularity?

A common argument for multi-branch designs is **specialization**. Since this notion is somewhat vague, I instead approach it from the perspective of **representation diversity**. To quantify this, I use the effective rank (as in [depth-1](/blog/2026/depth-1/)) to measure the degree of representation diversity/collapse.

---

## Problem setup and Results

We consider a simple regression problem:
$$y = \sum_{i=1}^{10} {\rm sin}^2(5x_i)$$

We train a 3-layer MLP to fit this function, fixing the total width to 512. When the cardinality is 1, the model reduces to a standard dense layer. When the cardinality $$C > 1$$, the weight matrix (512 × 512) is partitioned into $$C \times C$$ blocks, and only the diagonal blocks are kept non-zero (hence the “modular” structure). 

I plot how the effective rank varies with cardinality (left plot). For comparison, I also sweep the width while fixing $$C=1$$ (right subplot).  

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/cardinality/result.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Notably, when the total width is fixed, the number of parameters scales as $$1/C$$. Yet, the effective rank still increases with $$C$$—even as the total number of parameters decreases. 

In contrast, when $$C=1$$ and the width $$w$$ increases, the number of parameters scales as $$w^2$$. Although the effective rank does increase slightly with $$w$$, the cost is significantly higher. 

Overall, this suggests that **increasing cardinality is a far more parameter-efficient way to promote representation diversity than increasing width**.

---
## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/1cyjocG9GGVROqJDMs90TnFMjCYSN-T9x?usp=sharing).



---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026cardinality,
  title={Understanding cardinality (as in ResNext) from representation collapse},
  author={Liu, Ziming},
  year={2026},
  month={March},
  url={https://KindXiaoming.github.io/blog/2026/cardinality/}
}
```



