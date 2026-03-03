---
layout: post
title: Loss landscape visualization 1 -- Seeing sticky plateau
date: 2026-03-03
description: 
tags: [Physics-of-AI, Loss-landscape]
categories: AI
---

**Author: Ziming Liu**

---

## Motivation

I love picturing optimization as "a ball rolling down a hill". However, real loss landscape of neural networks are very high-dimensional. A convenient way is to apply PCA to weight trajectory, but unfortunately this does not capture local information well (see my prompt below). A obvious problem is that the trajectory points do not lie exactly on the 2D PC plane. 



---

## My prompt to cursor

I want to visualize the loss landscape as a 2D landscape.

To reduce the high dimensionality to 2D, we collect the weights during training, apply PCA to weights, obtain PC1 and PC2 as the two spanning axis. Now the network at each training step corresponds to a point on the 2D plane. 

However, the real trajectory does not exactly lie on the 2D plane. This is the price we have to pay -- the 2D plane nicely captures the global trajectory, but misses local informration. To bring back local information, let's do this:

* to compute the loss, we do not use the points on the global 2D plane, but to use local 2D planes centered around real true trajectory point. 

* How to determine a local 2D plane? Given a trajectory point, compute its current velocity and acceleration (velocity defiend as current state minus last step, acceleration defined as current velocity minus last velocity). When I say "last", it actually has a hyperparameter k, meaning k steps before.

* Now that the local 2D plane is defined, we can compute the loss landscape by sweeping the two axes.

* How to combine different local planes? We use a weighted average exp(-dist^2/(2*sigma^2)). Larger distance => smaller weight

* In the end, we get a 2D landscape

---
Take a simple MLP and different 1D regression problems, we show their training dynamics. Our way of visualization brings in some insights about what's happening during loss plateau, whose discussion is left to future blogs. 

$$f(x) = x$$

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/loss-visualization-1/train_loss_x.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/loss-visualization-1/landscape_ball_surface_x.gif" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

$$f(x) = x^2$$

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/loss-visualization-1/train_loss_x^2.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/loss-visualization-1/landscape_ball_surface_x^2.gif" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


$$f(x) = x^3$$

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/loss-visualization-1/train_loss_x^3.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/loss-visualization-1/landscape_ball_surface_x^3.gif" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


$$f(x) = \sin(x)$$

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/loss-visualization-1/train_loss_sinx.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/loss-visualization-1/landscape_ball_surface_sin3x.gif" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

---

## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/1cxkd8PVGA7fFrg7PukP5kU7i_imiG_98?usp=sharing).


---


## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026loss-landscape-visualization-1,
  title={Loss landscape visualization 1 -- seeing sticky plateau},
  author={Liu, Ziming},
  year={2026},
  month={March},
  url={https://KindXiaoming.github.io/blog/2026/loss-landscape-visualization-1/}
}
```



