---
layout: post
title: Sparse attention 7 -- Stack of causal attention creates implicit positional embedding, and explaning "Loss in the middle" 
date: 2026-01-31
description: 
tags: [Physics-of-AI, Sparse-attention]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

I was reading the paper
["Why Are Positional Encodings Nonessential for Deep Autoregressive Transformers? Revisiting a Petroglyph"](https://arxiv.org/pdf/2501.00659),
which makes an interesting claim: even without explicit positional embeddings, multi-layer causal attention may implicitly encode positional information, despite the fact that a single-layer causal attention is permutation equivariant. Figure 1 from the paper is shown below:

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/sparse-attention-7/fig1.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

The goal of this article is to measure how well multi-layer causal attention can extract previous tokens based purely on position. Given a sequence of random tokens (with context length $$C$$), the target is the $$k^{\rm th}$$ token in the sequence ($$0 \leq k \leq C-1$$). For example, when $$C = 5$$ and $$k = 1$$, example sequences are

$$
[5]\ [2]\ [3]\ [7]\ [9] \to [2]
$$

$$
[1]\ [9]\ [2]\ [5]\ [8] \to [9]
$$

We set the vocabulary size to $$V = 10$$, context length to $$C = 10$$, and the number of attention heads to $$n_{\rm head} = 1$$. We are interested in varying the number of layers $$n_{\rm layer}$$, the embedding dimension $$n_{\rm embd}$$, whether residual connections are used, and whether MLPs are included.

---

## 2L is qualitatively different from 1L

For each $$0 \leq k \leq C-1$$, we train the transformer to convergence and record the final loss. We then plot how the final loss depends on $$k$$. This roughly measures positional bias: a high loss means that retrieving information from that position is difficult—the loss cannot be driven down even when the model is explicitly trained on the retrieval task.

In [sparse-attention-2](/blog/2026/sparse-attention-2/), we showed that a 1-layer causal attention model cannot retrieve any previous token ($$k \neq C-1$$), but can retrieve the current token ($$k = C-1$$). This corresponds to the left plot below (high loss for $$k \neq 9$$, and almost zero loss for $$k = 9$$). The right plot shows the result for a 2-layer causal attention model, which exhibits the well-known ["lost in the middle" phenomenon](https://arxiv.org/pdf/2307.03172): early and late tokens are easily retrieved, while tokens in the middle are difficult to extract.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/sparse-attention-7/1L-2L.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Embedding dimension and number of layers do not change the qualitative behavior

We experiment with embedding dimensions $$\{2, 10\}$$ and number of layers $$\{2, 3\}$$. The qualitative trend remains unchanged: only the first and last tokens can be retrieved reliably, while tokens in the middle remain difficult. This manifests as a long plateau in the loss curve across middle positions.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/sparse-attention-7/embd-layer.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Residual connections and MLPs destroy the long plateau

When residual connections and MLPs are added, the long plateau disappears and is replaced by a more spiky structure.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 90%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/sparse-attention-7/residual-mlp.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Comment

This study suggests a simple mechanism underlying the "lost in the middle" phenomenon: even without explicit positional embeddings, stacking multiple causal-attention layers naturally induces an architectural bias toward losing information in the middle of the sequence.

---

## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/14OOPXMz4C40aIqOoWSxBzCH7hp3g3GZ9?usp=sharing).

---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026sparse-attention-7,
  title={Sparse attention 7 -- Stack of causal attention creates implicit positional embedding, and explaning "Loss in the middle" },
  author={Liu, Ziming},
  year={2026},
  month={January},
  url={https://KindXiaoming.github.io/blog/2026/sparse-attention-7/}
}
```



