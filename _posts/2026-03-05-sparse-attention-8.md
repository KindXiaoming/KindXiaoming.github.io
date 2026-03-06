---
layout: post
title: Sparse attention 8 -- Numeric randomness speeds up emergence of symbolic structure (induction head)
date: 2026-03-05
description: 
tags: [Physics-of-AI, Sparse-attention, Symbolic]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

In [Sparse-attention-6](/blog/2026/sparse-attention-6/), we trained an in-context associative recall task as a toy model of the **induction head**. Recall that an induction head should behave *symbolically*, in the sense that

$$[A][B]...[A]\to [B]$$

should hold for any tokens [A][B], ideally even for new tokens that were not seen during training.

However, token embeddings are inherently **numeric**, since they are parameterized by a learnable embedding matrix. One way to make tokens more “symbolic” is to randomize the token embeddings, thereby encouraging the model to focus on symbolic relations rather than overfitting to numerical properties of embeddings.

Therefore, we adopt the same setup as [Sparse-attention-6](/blog/2026/sparse-attention-6/), but randomly resample the token embedding matrix at every step. We refer to this setup as "symbolic" training, and call the standard setup "numeric" training.

---

## Random embeddings lead to much faster formation of induction heads

We tested three configurations:

* n_embd = 80, n_head = 1  
* n_embd = 256, n_head = 8  
* n_embd = 256, n_head = 1  

In all cases, the induction head forms significantly faster in the symbolic formulation. When the head size is too large (the last configuration), even the symbolic formulation fails to produce an induction head within $$10^4$$ steps.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/sparse-attention-8/symbolic-numeric.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Adding noise to token embeddings also helps

In real language settings, token embeddings carry important information (e.g., capturing N-gram statistics), so it is not desirable to resample them completely at every step. A softer alternative is to add Gaussian noise (with noise scale $$\sigma$$) to the token embeddings during training.

This approach also accelerates the formation of induction heads.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/sparse-attention-8/perturb.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Comment

* It would be interesting to interpret the symbolic induction head. Since the model cannot overfit to specific numerical embedding structures, interpretation may become easier.

* It would also be interesting to test whether the noisy-embedding trick can accelerate the emergence of symbolic structures during real language model training. However, we should be careful about what we mean by “symbolic structures.” While this trick may help induction heads (which do not require embedding geometry), it could potentially harm tasks such as arithmetic, where certain embedding geometries (e.g., line or circle) may actually be necessary.

---

## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/1eJhMKFtZ1A2Q4b3kJpXXCDaf7apsWok9?usp=sharing).

---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026sparse-attention-8,
  title={Sparse attention 8 -- Numeric randomness speeds up emergence of symbolic structure (induction head)},
  author={Liu, Ziming},
  year={2026},
  month={March},
  url={https://KindXiaoming.github.io/blog/2026/sparse-attention-8/}
}
```



