---
layout: post
title: Transformers don't learn Newton's laws? They learn Kepler's laws!
date: 2026-02-08
description: 
tags: Physics-of-AI
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

The blog explains the philosophy behind our new paper ["From Kepler to Newton:
Inductive Biases Guide Learned World Models in Transformers"](https://arxiv.org/pdf/2602.06923).

---

**Must world models know Newtonian physics?**

The answer is **no**, if we consider humans to be valid “world models.” Not everyone has a physics background or can effortlessly write down Newton’s equations, yet anyone can easily predict the trajectory of a flying ball. The computation performed by the human brain is unlikely to involve explicitly integrating Newtonian equations; instead, it relies on *intuitive physics*—for example, extrapolating a parabolic trajectory. Although this approach may be less fundamental, it is just as accurate and far more efficient for predicting the motion of a flying ball.


**The key lesson: world models are not unique.**

In science, we constantly encounter situations where multiple theories explain the same phenomenon equally well, and can only be distinguished once more experimental data become available under more diverse conditions. For instance, Newtonian kinetic energy,
$$
E_N = \frac{1}{2}mv^2,
$$
works extremely well in the classical regime, where velocities are much smaller than the speed of light $$c$$. It only breaks down—and is superseded by the relativistic expression
$$
E_R = \frac{mc^2}{\sqrt{1 - v^2/c^2}}
$$
—when $$v$$ becomes comparable to $$c$$. After all, *all models are wrong, but some are useful*.


**Transformers can’t learn Newton’s laws? They’re learning Kepler’s laws.**

[Vafa et al.](https://arxiv.org/abs/2507.06952) showed that a transformer can predict planetary motion (e.g., Earth orbiting the Sun) remarkably well, even though its internal representations do not explicitly encode gravitational forces. Does this mean transformers are not valid world models? **No.** In fact, our new paper shows that the transformer is learning a *Keplerian world model*, rather than a *Newtonian world model*. Note that I swept tokenization details under the rug; see [our paper](https://arxiv.org/pdf/2602.06923). This closely parallels the flying-ball example above:

* The **Newtonian model** is force-based and involves simulating differential equations.
* The **Keplerian model** is geometric, focusing on the continuation of elliptical trajectories.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 80%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/world-newton/kepler-newton.png" class="img-fluid rounded z-depth-1" cache_bust=true %}
    </div>
</div>

Even more intriguingly, when we replace full-context attention with *local attention* (i.e., reduce the context length), the transformer begins to behave like a **Newtonian world model**. As the context length is varied, we observe a sharp and fascinating *phase transition* between these two types of world models.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 50%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/world-newton/phase-change.png" class="img-fluid rounded z-depth-1" cache_bust=true %}
    </div>
</div>

---

**Implications for world models**

When task diversity is limited—in our case, a single task of predicting planetary motion—there may exist many different world models that all perform equally well. We cannot rule out the possibility that, in a parallel universe governed by the same physical laws, humans might develop a fundamentally different physical theory. Perhaps AI or world models have already done so. The real challenge is: *how do we extract these internal theories and make sense of them?*

If, however, we insist that AI models should know Newtonian physics, a few promising directions emerge:

* **(1) Increase task diversity.**  
  A purely geometric approach works well for planetary motion but fails for chaotic dynamics. Newtonian physics, by contrast, applies broadly to all classical systems, including both planetary motion and chaos.

* **(2) Introduce architectural inductive biases.**  
  Transformers should encourage at least some attention heads to operate locally, enabling the construction of differential operators (as in Newton’s second law). At the same time, hard constraints on context length are undesirable for long-term consistency (e.g., in video generation). Semantics are often global in time, while forces are local in time; a good architecture should accommodate both.

* **(3) Differential programming.**  
  For example, the Taichi system developed by [Yuanming Hu](https://yuanming.taichi.graphics/). If the first two directions aim to make neural models more *symbolic*, differential programming pursues the opposite paradigm: making *symbolic systems more neural*.

---


## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026world-newton,
  title={Transformers don't learn Newton's laws? They learn Kepler's laws!},
  author={Liu, Ziming},
  year={2026},
  month={February},
  url={https://KindXiaoming.github.io/blog/2026/kepler-newton/}
}
```



