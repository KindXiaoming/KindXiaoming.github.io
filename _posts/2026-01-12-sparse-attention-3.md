---
layout: post
title: Sparse attention 3 -- inefficiency of extracting similar content
date: 2026-01-12
description: 
tags: Physics-of-AI
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

In [Sparse-attention-1](/blog/2026/sparse-attention-1/), we showed that a single-layer attention model (without positional embeddings) can learn to copy the **current** token. In [Sparse-attention-2](/blog/2026/sparse-attention-2/), we showed that the same model is unable to extract a specific previous token based on *position*, e.g., the last token. But what about extracting a previous token based on *content* (token embeddings)? This is a more natural task, because it is precisely what attention is designed to do—attend to similar content.

As we show below, somewhat surprisingly, a single attention layer is very inefficient at performing this extraction task.

---

## Problem setup

**Dataset**  
The task is to extract the token that is most similar to the current token. We assume tokens have numerical meanings; for example, token $$[5]$$ represents the number $$5$$. Then $$[5]$$ is closer to $$[6]$$ than to $$[8]$$ because $$1=|5-6| < |5-8|=3.$$

Taking context length = 4 as an example, the task is to predict
$$[1][5][10][6] \rightarrow [5]$$.  
This is because $$[5]$$ is the closest to $$[6]$$, than $$[1]$$ or $$[10]$$.

**Model**  
We stick to the toy model from the [previous blog](/blog/2026/sparse-attention-1/). The model consists only of an Embedding layer, an Unembedding layer, and a single Attention layer, with no MLP layers and no positional embeddings.

---

## Failure even for context length = 3 (with small embedding dimension)

We examine the loss curves (in practice, we plot perplexity, i.e., $${\rm exp(loss)}$$). For embedding dimension = 2 and context length = 3 (task: $$[1][5][6]\to[5]$$), as we vary the vocabulary size, we consistently observe that perplexity converges to $$V/2$$ (or lower, for smaller $$V$$).

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid loading="eager" path="assets/img/blogs/sparse-attention-3/embd_2.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

By visualizing the learned embeddings, we find that they exhibit a continuous structure; that is, numerically closer tokens are embedded closer together:

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 50%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/sparse-attention-3/embd_final_2D.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Dependence on vocab size $$V$$

The existence of structure may explain why the perplexity can fall slightly below $$V/2$$: some structure is learned and leveraged to reduce the loss. However, the model largely becomes confused (similar to what we observed in the [previous blog](/blog/2026/sparse-attention-2/)) and effectively guesses a random token from the previous context. This leads to a perplexity of $$\frac{C-2}{C-1}V$$, which qualitatively (though not quantitatively) matches the experimental results:

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 80%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/sparse-attention-3/perplexity_C.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Dependence on embedding dimension

We find that the best achievable perplexity decreases with $$n_{\rm embd}$$, in fact faster than $$V/n_{\rm embd}$$:

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 80%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/sparse-attention-3/n_embd_dependence.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

This may be explained by the increasingly improved geometry of the embeddings (as seen in the first two principal components) as we increase $$n_{\rm embd}$$:

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 80%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/sparse-attention-3/embd_geometry.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Questions / Ideas
* Our results demonstrate the ineffectiveness of attention in extracting similar content in this setting.
* One possible fix is to replace the inner product of Q/K with the Euclidean distance between Q and K. Ideally, a 1D embedding would already be sufficient if the kernel computes Euclidean distances and weighs probabilities inversely proportional to distance (similar to [harmonic loss](https://arxiv.org/abs/2502.01628v1)).

---

## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/1k8IEg_zc12_8XHOE0SjWv5LyeaZBC5cK?usp=sharing).

---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026sparse-attention-3,
  title={Sparse attention 3 -- inefficiency of extracting similar content},
  author={Liu, Ziming},
  year={2026},
  month={January},
  url={https://KindXiaoming.github.io/blog/2026/sparse-attention-3/}
}
```



