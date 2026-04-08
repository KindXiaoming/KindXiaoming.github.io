---
layout: post
title: When does Kimi's "Attention Residuals" work?
date: 2026-03-16
description: 
tags: [Physics-of-AI, Optimization, Depth, Data]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

Kimi recently released a new type of residual connection — ["Attention Residual"](https://github.com/MoonshotAI/Attention-Residuals/blob/master/Attention_Residuals.pdf). In contrast to the standard residual formulation $$h_{l+1}=h_l +f_l(h_l)$$, it learns a weighted combination of previous hidden states:

$$h_{l+1}=\alpha_0 h_1 +\sum_{i=1}^{l}\alpha_i f_i(h_i)$$

where $$\alpha$$ is computed in a way similar to attention, hence the name. In particular, each layer has a trainable query vector $$q_l$$, while the key/value vectors are set as hidden states ($$h_1$$ or $$f_i(h_i)$$).

The authors show that Attention Residuals outperform standard residual baselines, which is quite interesting. However, if we want to understand this method scientifically, we must embrace the No-Free-Lunch theorem. If this method works better than standard residuals on natural language tasks, it must also perform worse than standard residuals on some other datasets.

The goal of this blog is therefore: construct a minimal toy dataset (with a continuous variable $$\alpha$$) such that Attention Residual works better for some $$\alpha$$ values, but worse for other regions of $$\alpha$$.

---

## Intuition

**When Attention Residual should work**

Suppose we are dealing with an extremely simple dataset that only requires a single linear layer. If the attention residual mechanism learns to skip all blocks except for the last linear layer, the task can be solved easily. This is straightforward for attention residuals: one can set the last-layer query vector to be orthogonal to previous hidden states. In contrast, a standard residual network would need to learn to skip each intermediate layer one by one, which may be harder to learn.

**When Attention Residual may fail**

Although we hope the $$\alpha$$ weights are properly learned, at initialization (or if training is not effective) they may approach a uniform distribution, which may lead to representation collapse. To see this more clearly, when the alphas are uniform we have:

$$h_{l} = \frac{l-1}{l}h_{l-1} + \frac{1}{l}v_l$$

or

$$h_l = \frac{1}{l}(h_1 + \sum_{i=1}^{l-1} v_i)$$

which averages over all previous hidden states. Attention residuals may therefore suffer from this "uniform bias" during training, reducing their expressive power. (This part may not be nicely argued -- the formula above is very similar to standard residual; sutble points like norms and layer correlations may be key here. But just try to speak out loud my intuition.)

**Stability–Expressivity trade-off**

When designing neural networks, there is often a trade-off between stability and expressivity. My intuition is that Attention Residuals aim to improve stability but may sacrifice expressivity.

However, I feel somewhat conflicted about this intuition, since it appears to contradict the motivation in the paper:  

> "This uniform aggregation (standard residual) causes uncontrolled hidden-state growth with depth, progressively diluting each layer’s contribution."

This statement suggests that Attention Residuals increase expressivity rather than reduce it.

Regardless of the narrative, my goal here is to ground my intuition through concrete toy experiments.

---

## Problem setup

**Dataset**

**A simple dataset**: the output is a linear function of the input.

**A difficult dataset**: memorization (both inputs and outputs are random).

I expect that Attention Residual will work better for the simple dataset, while standard residual connections will work better for the difficult dataset. I also interpolate between these two datasets by linearly mixing their labels with a coefficient $$\alpha_{\rm clean}$$.

When $$\alpha_{\rm clean}=1$$, the dataset corresponds to the linear dataset; when $$\alpha_{\rm clean}=0$$, it corresponds to the random dataset.

**Model**

I keep only MLP blocks and remove attention layers. This gives a toy model of standard residual networks and a toy model of attention residual networks.

Both models are trained using Adam. It is interesting to sweep $$\alpha_{\rm clean}\in [0, 1]$$ to determine in which regime attention residual performs better.

---

## Results

Setting n_blocks = 10, we find that the results match my intuition:

* For small $$\alpha$$ (close to a random/memorization dataset), standard residual networks are more expressive and therefore achieve better performance.
* For large $$\alpha$$ (close to a structured/linear dataset), Attention Residuals can more easily learn the shortcut structure and therefore achieve better performance.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/attention-residual/block10.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Results for n_blocks = 4, 10, 30 are compared below:

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/attention-residual/sweep-block.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Comments

* Confession: I initialize the learnable query vectors to zero, which may enforce the uniform bias I anticipated. Initializing the query vectors to non-zero values may reduce this uniform bias.
* Ultimately, the scientific argument should not be "Attention residual works better than standard residual" or the other way around. Instead, we should embrace the No-Free-Lunch perspective and clarify under which conditions or tasks one method outperforms the other. Going further, Kimi's positive results on natural language tasks may suggest that natural language is more structured than random data. In the end, the biggest "dark matter" in AI is data (how it is generated and how the world is simulated), not the models themselves.

---

## Follow up
I have a follow-up discussion in [attention-residual-2](/blog/2026/attention-residual-2/).


---
## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/1PPJFcURwahGVJnZgn1e8t-dU5eHjE1dC?usp=sharing).



---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026AttnRes,
  title={When does Kimi's "Attention Residuals" work?},
  author={Liu, Ziming},
  year={2026},
  month={March},
  url={https://KindXiaoming.github.io/blog/2026/attention-residual/}
}
```



