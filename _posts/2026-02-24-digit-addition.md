---
layout: post
title: 181-parameter transformer-like models for 10-digit addition 
date: 2026-02-24
description: 
tags: [Physics-of-AI, Toy-language, Sparse-attention]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

Dimitris Papailiopoulos recently posted [a tweet](https://x.com/DimitrisPapail/status/2024555561199480918) describing how he pushed AI agents to discover minimal transformers capable of performing 10-digit addition. Claude Code managed to find a 6,080-parameter transformer — not bad.

If we imagine solving the task with an RNN, the parameter count could likely be fewer than 10 — we would probably only need one neuron to represent the current digit and another to represent the carry bit. However, using an RNN may feel like too much “cheating,” since a transformer is not inherently recursive.

That said, I still want to “cheat” a little — because I think a good human researcher (or AI agent) should optimize not only hyperparameters within a fixed architecture, but also explore and optimize in the **architecture space** itself.

---

## What I don’t like about (standard) transformers

Softmax attention is not well-suited for simulating short convolutions. I discussed this in a previous blog post, [“Physics 1 -- Attention can't exactly simulate uniform linear motion.”](/blog/2026/physics-1/). Digit addition shares structural similarities with uniform linear motion.

To be clear, I think the high-level idea of transformers is excellent: attention governs information flow across context, while MLPs govern information flow across neurons (embedding dimensions). However, there are many possible mechanisms (layers) to drive information flow. One natural alternative to attention layers is short convolutional layers (or what Allen Zeyuan Zhu calls ["Canon" layers](https://arxiv.org/abs/2512.17351)).

---

## Construction

I attempted a manual construction.

If the convolution kernel size is 3, and if the model can perfectly learn convolution weights proportional to (0.01, 0.1, 1), the accuracy should reach 99.5%, exceeding Dimitris’s 99% threshold — because it would only fail on cases involving three consecutive carry operations. I admit this is somewhat hacking the 99% target (sorry :-)).

After the convolution step, computing the current digit requires learning a sawtooth function, which can be implemented with 3 ReLU neurons. Computing the carry bit requires 2 additional ReLU neurons.

So in theory, O(10) parameters should suffice for digit addition (3 convolution weights + 5 ReLU neurons). However, in practice, learning hierarchical weights like (0.01, 0.1, 1) is difficult, and ReLU neurons may become dead depending on initialization. Therefore, the actual network likely needs to be somewhat larger.

Moreover, I am not a fan of number tokenization, based on insights from our recent paper [From Kepler to Newton: Inductive Biases Guide Learned World Models in Transformers”](https://arxiv.org/abs/2602.06923) which shows that inappropriate tokenization can significantly delay or even prevent the learning of world models.

Therefore:

* I did not use any tokenization — digits are directly treated as inputs and outputs.
* MSE loss does not work well, but a hybrid loss — **Gaussian cross-entropy loss** — does. It behaves like MSE when the inverse temperature $$\beta$$ is small, and like cross-entropy when $$\beta$$ is large (using Euclidean distance as the distance metric rather than inner product).

---

## A 181-parameter network successfully learns

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/digit-addition/train_dynamics.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

The model uses kernel size 3, hidden channels 2, and 2 blocks (each block consists of a short convolution layer followed by an MLP). The learned convolution weight in the first block is:

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/digit-addition/conv_weight.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

The weights exhibit both **symmetry** (similar weights for the two digits at the same position) and **hierarchy** (across context positions, the coefficients are roughly in a 1:10:100 ratio).

I admit that my construction might be a bit cheating (overfit to the digit-addition task). But digit-addition isn't that special actually -- Newontian physics (blogpost: [uniform linear motion](/blog/2026/physics-1/), [circular motion](/blog/2026/physics-2/), [planetary motion](/blog/2026/kepler-newton/)) shares simiar local structures, and in these cases, a short convolutional layer should be better than a long-context softmax layer. If unsure, a model can just use both, as in ["Canon" layers](https://arxiv.org/abs/2512.17351). 

---

## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/1jQxjfduGyqEjuLy6SRK7QcYymHwKkjcT?usp=sharing).


---


## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026digit-addition,
  title={181-parameter transformer-like models for 10-digit addition },
  author={Liu, Ziming},
  year={2026},
  month={February},
  url={https://KindXiaoming.github.io/blog/2026/digit-addition/}
}
```



