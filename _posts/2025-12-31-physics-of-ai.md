---
layout: post
title: Physics of AI Requires Mindset Shifts
date: 2025-12-31
description: 
tags: Physics-of-AI
categories: AI
---

**The “physics of AI” is still far from arriving.**  

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 70%; margin: 0 auto;">
        {% include figure.liquid loading="eager" path="assets/img/blogs/physics-of-ai.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

If we use the Tycho–Kepler–Newton analogy, today’s AI development largely remains at the **Tycho stage**—experimentation and observation. Yet even at the level of observation, what we currently have is extremely primitive: most people focus on tuning for a handful of performance-based metrics. This stems from a fundamental difference in goals between physics and AI. Physics aims to *transform the world by understanding it*, where *understanding* itself occupies a central position. As a result, the field is very tolerant of work that provides insight even if it is (temporarily) useless. In contrast, AI aims directly to *transform the world*. The scaling laws of recent years have allowed the field to skip the “understanding” step and jump straight into transforming AI itself. In my view, this constitutes a form of **cognitive debt**—one that will inevitably have to be repaid, sooner or later, if not already.

For this reason, it is premature to talk about AI’s “Newtonian mechanics.” Even at the level of basic phenomenology, we are still at a very early stage. Phenomenology can be relatively macroscopic—connecting different models, such as **emergence** and **scaling laws**—or more microscopic—focused on training dynamics, such as **grokking**, **double descent**, or the **edge of stability**. We first need to discover more phenomena; only then will we be motivated to model them and develop theories to study them.

---

**Why Is AI Phenomenology Hard to Develop?**

Why is AI phenomenology so difficult to develop? I believe publication culture plays a major role. What is publishable is either work with strong performance gains (in which case phenomenology seems unnecessary), or a compelling story.

There are two kinds of “good stories”:

- **Universality**: the phenomenon must be demonstrated across many settings. *Edge of stability* is an example. This imposes a very high bar for publications.
- **Surprise**: the phenomenon is striking and unexpected. This is rare and highly unpredictable—*grokking* being a representative case.

This explains why the list of commonly cited AI phenomenology examples is so short. Given the historical stage of the “physics of AI,” we seem to hold phenomenology to excessively high expectations, which in fact hinders its development.

[Allen Zeyuan Zhu’s *Physics of LLMs*](https://physics.allen-zhu.com/) is excellent work, but from my conversations with friends, the common reaction is that it is interesting yet hard to know where/how to begin if they want to dive into the field. The same applies to our own work [*Superposition Leads to Robust Neural Scaling* (NeurIPS 2025 Best Paper Runner-up)](https://openreview.net/forum?id=knPz7gtjPW): people are curious about how such a story was conceived. I cannot speak for other researchers in the physics-of-AI space, but from my own experience, I spend an inordinate amount of time packaging a story—"wasting" my own time and increasing the distance between myself and readers.

Moreover, phenomena that can be packaged into a story are exceedingly rare. Many phenomena that I personally find fascinating, but cannot turn into a paper, end up casually discarded.

---

**Toward a More Accessible Phenomenology**

Therefore, I advocate for a more **accessible and inclusive form of phenomenological research**. This approach would be more tolerant than current AI phenomenology and closer in spirit to phenomenology in physics. It would:

- not be oriented toward immediate usefulness;
- not require being packaged into a complete story;
- place no restrictions on analytical tools, as long as they are effective in description/prediction.

At the same time, it would emphasize:

1. **Controllability**  
   Use toy models to simplify and abstract real-world settings, such that results can be reproduced with minimal resources (ideally a single notebook plus a CPU is sufficient).

2. **Multi-perspective characterization**  
   Describe the object of study from as many angles and metrics as possible—like blind men feeling an elephant.

3. **Curiosity / hypothesis-driven exploration**  
   Phenomena should yield new insights—qualitative is sufficient, quantitative is even better.

This kind of accessible phenomenology may not be easy to publish at mainstream AI conferences, but it is extremely valuable for **community building**. Perhaps researcher A discovers a phenomenon (the key is making it public), B connects it to another phenomenon they previously observed, C unifies the two, D develops some theoretical analysis, and E turns the insights into algorithmic improvements. The five of them can then write a paper together.

Traditionally, A might only collaborate within a small circle, but my understanding of the physics-of-AI community is that it is still highly fragmented, often divided by application domains. For example, vision researchers tend to collaborate with other vision researchers, and their intuitions are shaped primarily by vision tasks.

---

**So what can we do?**

**On my end: Starting Blogposts**

I will start sharing my (our) own “AI phenomenology” research in the form of blog posts. The right expectation for readers is that a colleague is sharing partial results: the work may be incomplete, but the raw data and thought process are presented transparently. 

The goals are threefold:

1. **To force myself to record observations**  
   As mentioned earlier, phenomena that cannot be turned into papers are often thrown away. This effort is partially inspired by [Jianlin Su's blog](https://kexue.fm/)—his focuses on mathematical principles, whereas mine will emphasize experimental observations (phenomenology), "physical" intuition, and, when necessary, some (semi-)quantitative analysis, providing problems and intuition for future mathematical work.

2. **To attract researchers and students who share similar interests**  
   If you are interested in exploring these ideas together, feel free to reach out.

3. **Course preparation**  
   I plan to offer a *Physics of AI* course at Tsinghua University. These blog posts (along with accompanying code) may eventually become course materials.

**On your end: How to Get Started**

1. **Find questions you care about**  
   For example, studying parameterizations of diffusion-model losses, or reproducing known phenomena such as grokking.

2. **Define a simple toy model**  
   For instance, [Tianhong Li and Kaiming He’s JIT paper](https://arxiv.org/pdf/2511.13720) uses a 2D spiral dataset to study loss parameterization. The best way to understand grokking is simply to train a modular addition task yourself.

3. **Commit to fully understanding the toy model**  
   This is the hardest step. We are often too eager to move from toy models to realistic ones (again, due to publishing culture). Once a toy model produces the desired positive result, we move on. This is a *supervised* use of toy models. I believe toy models reveal their greatest power when used *unsupervised*. As the name suggests, it is a toy—approach it with childlike curiosity, play with it, and understand it from every possible angle (like blind men touching elephants).
   
I cannot guarantee that the insights gained will immediately translate into performance improvements, but I believe that if we, as a field, continue to accumulate such insights, a **percolation-like phase transition** will eventually occur.

---

The first phenomenology blogpost is [here](/blog/2026/feature-learning-1/).

---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2025physics-of-ai,
  title={Physics of AI Requires Mindset Shifts},
  author={Liu, Ziming},
  year={2025},
  month={December},
  url={https://KindXiaoming.github.io/blog/2025/physics-of-ai/}
}
```



