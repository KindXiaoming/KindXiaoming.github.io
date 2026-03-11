---
layout: post
title: A toy model of distillation
date: 2026-03-12
description: 
tags: [Physics-of-AI, Optimization]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

Distillation uses the teacher network’s **logits/probability distribution** to supervise the student network, rather than relying only on one-hot labels. Qualitatively, the benefit of distillation is intuitive: the probability distribution contains **more information** and **less noise** than a single one-hot sample. The goal of this blog is to understand this benefit **quantitatively**.

---

## Problem setup

Both the teacher network and the student network are **linear layers**. The teacher network is randomized, fixed, and scaled by a temperature factor $$T$$. Smaller $$T$$ makes the teacher distribution more one-hot-like, while larger $$T$$ makes it closer to uniform. The input $$x\in\mathbb{R}^{10}$$ is randomly sampled from the standard Gaussian distribution; the teacher maps it to logits in $$\mathbb{R}^V$$, where $$V=1000$$.

* **Regular:** the teacher is used to generate one-hot samples drawn from its probability distribution. The student is then trained on these one-hot labels using the cross-entropy loss.
* **Distillation:** the teacher produces the full probability distribution, and the student is trained to match it via the KL divergence (up to an additive constant, namely the entropy of the teacher distribution).

I use Adam for training.

---

## Observation: teacher temperature controls the speedup factor

* For $$T=1$$, distillation quickly converges to the best achievable loss (red dashed line), while regular training suffers from large stochastic noise.
* For $$T=0.1$$, distillation still converges faster than regular training.
* For $$T=0.01$$, distillation becomes comparable to regular training, and both converge slowly (following an approximate 1/3 power law) toward equilibrium. See [time-scaling](https://arxiv.org/abs/2602.03685) for an explanation.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/distillation/temp.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Each curve has two stages:

* The **burn-in stage**, where training converges toward the optimal weight;
* The **fluctuation stage**, where the model wanders around the optimum due to stochasticity.

It is clear that the objective in distillation is less stochastic than cross-entropy training with one-hot labels. Therefore, distillation has an advantage in reducing noise, which in turn lowers the overall loss. See [neural thermodynamic law](https://arxiv.org/pdf/2505.10559) for a quantitative analysis.

Below, I will mainly focus on explaining the **speedup factor in the first stage**.

---

## Speedup factor is $$1/\|p\|_2$$

Consider a probability distribution $$(p_1, p_2, \cdots, p_V)$$. A one-hot vector sampled from this distribution corresponds to class $$i$$ with probability $$p_i$$, and therefore to gradient $$g_i$$. Let us make the following assumptions:

* all $$g_i$$ have the same norm, say $$\|g_i\|=a$$;
* $$g_i$$ and $$g_j$$ are mutually orthogonal.

Then the true gradient is

$$g = \sum_i p_i g_i$$

whose magnitude is

$$a\|p\|_2.$$

Recall how Adam computes its adaptive step: the momentum is the averaged gradient and therefore has scale roughly $$a\|p\|_2$$, while the denominator has scale roughly $$a$$. Thus, compared with distillation, the effective step size in regular training is reduced by a factor of $$\|p\|_2$$. Equivalently, the speedup factor of distillation is

$$1/\|p\|_2.$$

Note that

$$\frac{1}{\sqrt{V}}\leq\|p\|_2\leq 1.$$

When $$p$$ is one-hot, $$\|p\|_2=1$$; when $$p$$ is uniform, $$\|p\|_2=\frac{1}{\sqrt{V}}$$.

**Verify**  
We verify that the speedup factor derived above provides a reasonable estimate.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/distillation/speedup.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

**SGD**  
Our explanation above relies on the adaptive step in Adam. Without such adaptivity (e.g., when using SGD), there is no speedup factor in stage 1.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/distillation/sgd_temp.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Comment

1. One might argue that the speedup factor induced by Adam’s adaptive step could be compensated for by simply increasing the learning rate. This may be true in stage 1, but it would also amplify noise in stage 2. Moreover, there are other reasons not to set the learning rate too large.

2. Our toy model considers **stochasticity** as the main reason distillation outperforms regular training. In practice, when people refer to “distillation,” they often mean a setting where the student is smaller than the teacher. In that case, there may be another benefit: without the teacher’s guidance, the smaller student may get trapped in poor local minima. However, this mechanism cannot appear in the current toy model, since the teacher and student have the same architecture and are both linear.

3. There are two sources of stochasticity:
   (a) sampling $$x$$ from the standard Gaussian distribution;  
   (b) given $$x$$, computing the teacher’s probability distribution and then sampling a one-hot vector from it.  

   My analysis has mainly focused on (b), implicitly assuming that the effect of (a) is much smaller than that of (b). A more careful analysis is needed.

---
## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/1Guegpe1qkuz1aTBF42cl3atLh3Hm_nM4?usp=sharing).


---


## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026distillation-toy,
  title={A toy model of distillation},
  author={Liu, Ziming},
  year={2026},
  month={March},
  url={https://KindXiaoming.github.io/blog/2026/distillation-toy/}
}
```



