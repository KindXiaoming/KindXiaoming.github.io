---
layout: post
title: Drifting VQ-VAE -- How "drifting models" fixe failure modes of VQ-VAE
date: 2026-03-04
description: 
tags: [Physics-of-AI, Representation, Diffusion]
categories: AI
---

**Author: Ziming Liu**

---

## Motivation

I am interested in whether video generative models encode physics internally. As a starting point, I looked into the [VideoGPT paper](https://arxiv.org/pdf/2104.10157), where [VQ-VAE](https://arxiv.org/pdf/1711.00937) is a key component. I realized that I had never understood VQ-VAE as deeply as I could, so I decided to implement a toy model to gain some first-hand experience with it.

---

## Problem setup

**VQVAE**

VQVAE consists of an encoder $$E$$, a decoder $$D$$, and $$K$$ codes in the latent space. The encoder maps the input $$x$$ to a hidden state $$h=E(x)$$. The hidden state is then mapped to the nearest code $$e = {\rm argmin}_i \|h - e_i\|$$. The loss consists of three parts (where sg means stop gradients):

* Reconstruction loss $$\ell_{\rm rec} = \|x - D(e)\|^2$$  
* Codebook loss $$\ell_{\rm code} = \|{\rm sg}[E(x)] - e\|^2$$  
* Commitment loss $$\ell_{\rm commit} = \|E(x) - {\rm sg}[e]\|^2$$  

The total loss is $$\ell=\ell_{\rm rec} + \ell_{\rm code} + \beta \ell_{\rm commit}$$. Typically $$\beta=0.25$$ is a good choice.

**Dataset**

The dataset is intentionally simple: two clusters in the 2D plane.

**Model**

Both the encoder and decoder are linear layers $$\mathbb{R}^2\to\mathbb{R}^2$$.

This is the simplest setup I could imagine. Given its simplicity, one might expect that $$K=2$$ should suffice.

---

## Failure mode of VQVAE

We visualize the hidden space during training. Codewords are visualized as stars. And the data points are visualized as blue points (they are very dense, so they look more like a rectangle or a diamond). 

$$K=2$$

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/representation-1/training_dynamics_K_2.gif" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

$$K=5$$

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/representation-1/training_dynamics_K_5.gif" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

$$K=10$$

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/representation-1/training_dynamics_K_10.gif" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Only when $$K=10$$ can the two clusters be mapped to separate codewords. Of course, there are various practical tricks to alleviate this issue, such as re-initialization or using EMA for better codebook updates. However, these do not resolve the fundamental problem. The failure mode ultimately stems from how the loss function is defined.

---

## Drifting VQ-VAE: Why drifting models can map?

**Concepts**

If we interpret hidden states as positive charges and codewords as negative charges, the matching problem can be naturally solved by [“drifting models”](https://arxiv.org/abs/2602.04770v1). Drifting models ensure that positive charges fall onto negative charges in the correct proportion — roughly one positive charge per negative charge. Situations where multiple positive charges collapse onto a single negative charge are naturally avoided, which prevents dead codes.

Note that when I refer to “drifting models,” I do not necessarily mean generative models themselves, but rather the general attraction–repulsion formulation. See [my previous blogpost for a physical interpretation of drifting models](/blog/2026/diffusion-3/).

**Experiments**

There are $$N$$ data points — so we assign a positive charge $$q = 1/N$$ to each data point. There are $$K$$ codewords — so we assign a negative charge $$q = -1/K$$ to each codeword.

The potential energy between any two particles is defined as

$$U = \tau(r+\tau){\rm exp}^{-r/\tau}$$

(corresponding to force $$f(r) = r{\rm exp}(-r/\tau)$$, which is a standard choice in drifting models).

The total potential energy is therefore

$$U=U_{pp} + U_{pn} + U_{nn}$$

and the loss function becomes

$$\ell = \ell_{\rm rec} + \beta U$$.

I call this method **Drifting VQ-VAE**.

Results:

$$K=2$$

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/representation-1/training_dynamics_drifting_K_2.gif" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

$$K=10$$

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/representation-1/training_dynamics_drifting_K_10.gif" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Drifting VQ-VAE already works for $$K=2$$! And when $$K=10$$, five codewords move to one cluster and the other five move to the other cluster. Almost all codewords are utilized.

---

## Comment

The implications of drifting models may extend far beyond generative models themselves. The high-level idea — attraction and repulsion with balanced charges — may open a new direction for representation learning.

---

## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/1w-uav5jWv8tBY2X4wpQ6kofkhNEOmTJ3?usp=sharing).


---


## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026representation-1,
  title={Drifting VQ-VAE -- How "drifting models" fixe failure modes of VQ-VAE},
  author={Liu, Ziming},
  year={2026},
  month={March},
  url={https://KindXiaoming.github.io/blog/2026/representation-1/}
}
```



