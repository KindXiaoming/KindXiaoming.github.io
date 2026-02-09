---
layout: post
title: Training dynamics of A Single ReLU Neuron
date: 2026-01-03
description: 
tags: [Physics-of-AI, Non-linearity]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

In a previous [blog post](/blog/2026/feature-learning-1/), we studied feature learning in shallow, wide MLPs. In this article, we consider an even simpler setting: an MLP with only **one hidden layer**, **a single ReLU neuron**, and a **self-generated target function** (a teacher network).  

In this setting, we know that there exists a set of weights for which the loss is exactly zero. But will gradient-based optimization run into difficulties? For example, if the neuron is initialized to be overly **active** (positive pre-activation for all inputs), or overly **inactive** (negative pre-activation for all inputs), will optimization fail? Even if the initialization is reasonable, can the training dynamics drive the neuron into a bad state (too active or too inactive)?

For convenience, we define three states of a neuron:

- **Hyperactive**: activated for all inputs (pre-activation always positive)
- **Inactive / Dead**: never activated (pre-activation always negative)
- **Balanced**: activated for some inputs and inactive for others

Although this setup is extremely simple, our ultimate goal is to gain insights relevant to LLM training. One intuition is that many tricks used in LLM training—such as LR warmup, LR decay, weight decay, and MoE balancing—may implicitly control neuron activity levels, thereby influencing feature learning.

---

## Problem Setup

An MLP with one hidden layer and one neuron can be written as (for simplicity, the input is also 1D):

$$
f(x; w_1, b_1, w_2, b_2) = w_2\sigma(w_1x+b_1)+b_2, \quad \sigma(x) ={\rm ReLU}(x) \equiv {\rm max}(0,x)
$$

For the teacher network, we set $$w_1^T = w_2^T = 1, \quad b_1^T = b_2^T = 0$$, and so $$f(x)\equiv {\rm ReLU}(x)$$. We take the input domain to be $$x \in [-1,1].$$  

For the student network, we initialize  $$w_1^S = w_2^S = 1,$$  and focus on varying the initializations of $$b_1^S$$ and $$b_2^S$$. Training uses MSE loss and the Adam optimizer (default LR = 0.01). Below, we only discuss the student’s weights, so we omit the superscript $$S$$.

---

## Observation 0: Large $$|b_1|$$ Leads to Local Minima

We fix the initialization $$b_2 = 0$$.  

- When $$b_1 > 1$$, the neuron is initialized in the **hyperactive** state, and the loss gets stuck around 0.02 (corresponding to approximating ReLU with linear regression).
- When $$b_1 < -1$$, the neuron is initialized in the **dead** state, and the loss gets stuck around 0.1 (corresponding to approximating ReLU with a constant function).

This may help explain why some initialization schemes (e.g., Kaiming initialization) set the bias to zero.

---

## Observation 1: Large $$|b_2|$$ Can Kill the Neuron

We fix $$b_1 = 0$$, so the neuron is **balanced** at initialization. Is everything fine then? Not quite. We find that when $$b_2 = -1.1$$, the loss can go to zero, but when $$b_2 = -1.2$$, the loss gets stuck around 0.02 (again corresponding to approximating ReLU with linear regression).

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 90%; margin: 0 auto;">
        {% include figure.liquid loading="eager" path="assets/img/blogs/single-relu-neuron/loss.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

By closely examining the training dynamics, we find that the turning point  $$x_t \equiv - b_1 / w_1$$ moves left during training (starting from 0). When it moves past -1, the neuron transitions from **balanced** to **hyperactive**.

The local minimum for $$b_2 = -1.2$$ corresponds to the linear regression solution (the neuron is in the hyperactive state):

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 90%; margin: 0 auto;">
        {% include figure.liquid loading="eager" path="assets/img/blogs/single-relu-neuron/large_b2_init.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Conversely, if we increase the bias of the target function, the neuron also transitions from **balanced** to **hyperactive**.

This observation connects to two empirical practices:

- **Model bias**: In some LLM training setups, bias terms are disabled. The observation above suggests that bias dynamics can drive neurons away from the balanced state.
- **Data bias**: Whitening inputs and normalizing intermediate representations are common practices.

---

## Observation 2: Too Large a Learning Rate Can Also Kill the Neuron

We fix $$b_1 = 0$$ and $$b_2 = -1$$.  

- When LR = 0.2, the model’s loss can be optimized to zero.
- When LR = 0.4, the loss only reaches 0.1 (again corresponding to fitting ReLU with a constant function), because the neuron becomes **dead**.

This may be related to LR warmup in LLM training: if the initial learning rate is too large, the loss may decrease quickly, but at the cost of killing some neurons. Once dead, these neurons are hard (or impossible) to bring back to a balanced state.

---

## Observation 3: SiLU Eventually Recovers, but Gets Stuck at a Saddle Point for a Long Time

For SiLU, we observe that the loss can eventually reach zero (up to machine precision), but training gets stuck at saddle points for very long time, reducing training efficiency.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 90%; margin: 0 auto;">
        {% include figure.liquid loading="eager" path="assets/img/blogs/single-relu-neuron/silu.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Takeaway

**Irreversibility**: once a neuron leaves the balanced state, it is very hard to return. Bias plays a crucial role. This might be why we have various ugly tricks for LLM (learning rate schedule, weight decay, etc).

---

## Questions/Ideas

**Question 1: How can we better control bias?**

- Can we analytically compute the bias instead of learning it via gradient descent?
- Can we use a different parameterization to better control neuron activation? For example,  $$wx + b \;\to\; w(x + b'),$$  where $$b'$$ directly controls neuron activation (assuming the input distribution is known). This may allow us to more directly control neuron activity, e.g., by applying weight decay to $$b'$$ or explicitly enforcing balancing.

**Question 2: Which neurons have better learning dynamics?**

- SiLU is better than ReLU. Is there something better, gating?


---

## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/1gSrKOVfEtVNTa7ZCUOpqOI1uTXm0SL9s?usp=sharing).

---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026single-relu-neuron,
  title={Training dynamics of A Single ReLU Neuron},
  author={Liu, Ziming},
  year={2026},
  month={January},
  url={https://KindXiaoming.github.io/blog/2026/single-relu-neuron/}
}
```



