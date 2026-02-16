---
layout: post
title: When should I use physics of AI?
date: 2026-02-15
description: 
tags: [Physics-of-AI, Methodology]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

A student recently told me, “I’m not as convinced as you are about Physics of AI. I think it may apply to some problems, but not to others.”  

I paused for a moment—because I completely agree with that assessment. In fact, it is almost too obvious to require explanation. But after further discussion with the student, and some reflection on my own part, I realized something important: perhaps I had overemphasized the *methodology* of Physics of AI, unintentionally making it seem as if one must adopt this framework to earn my approval.

If a particular methodology becomes the only acceptable way to solve problems, then it ceases to be a methodology—it becomes a doctrine, even a religion.

So I had a long conversation with the student to clarify my perspective. Some parts of that discussion may be helpful for students who are just starting their research journey, so I decided to write down a few core ideas.

---

## Research = Problems + Solutions

A research project consists of two elements: **problems** and **solutions**. Problems are primary; solutions are secondary.

Karl Popper once said:

> *We are not students of some subject matter, but students of problems. And problems may cut right across the borders of any subject matter or discipline.*

I find that many students implicitly treat *methods/solutions* as primary. This is understandable—it is how knowledge is often transmitted. To maximize efficiency, we present polished answers in structured textbooks. But in doing so, we often omit the story of how earlier researchers *formulated* the problems in the first place.  

What makes it into textbooks are mature areas of knowledge—areas that may no longer be fertile ground for major discoveries.

Even experienced researchers sometimes believe that methods matter more than problems. This is partly due to publication culture: only a small number of breakthrough papers define new problems, while the vast majority solve existing ones. This imbalance exists in almost every field. Beginners may mistakenly conclude that “what most people do” must be “what is most important.”

The best research, however, begins with a good problem and then designs a good solution around it. This is similar to product development: without a real user need, a product has no foundation.

But as I say this, I realize I risk slipping into dogmatism again. In reality, both research and product design are iterative processes. You rarely start with a perfect problem and a perfect solution. You may begin with a solution (“I have an intuition to add a certain layer to the network”), then ask: *What problem does this solve?* (“It accelerates training.”) Once you identify a valuable problem, you can revisit your solution and refine it. Iterate the problem; iterate the solution; repeat.

### How to find problems?

Curiosity is essential. Work on problems you genuinely find interesting. When you have too many ideas, introduce a second criterion: **impact**. (We will discuss how to identify impactful problems later.)

### How to find solutions?

Learn from existing approaches (“existing information”), and generate new ideas through thinking and experimentation (“new information”). Research is fundamentally an information acquisition and processing game. The more high-quality information you can obtain per unit time, the stronger your advantage.

Physics of AI is simply one methodology for acquiring and processing information. It encourages you not to stay at the surface level (e.g., final model performance), but to dig deeper—measuring more statistics and understanding mechanisms.

To be clear, “digging deeper” does *not* mean that surface-level information is invalid. If tuning hyperparameters alone solves the problem, that’s great. But increasingly, that is no longer sufficient. The era when blind hyperparameter tuning could yield major breakthroughs is largely over. We must either dig deeper (understand the science of AI) or explore sideways (open up new problems).

---

## Digging Deeper: The Role of Physics of AI

Physics of AI is a methodology for digging deeper. The ultimate goal aims to address practical questions (I will define five “levels” of AI research):
* Short term（Level 1 or Level 4）：Given an exerperimental setting, how should we tune hyper-parameters?
* Long term（Level 5）：How do we design new models (creating new experimental settings)?

We can model AI research as follows: given a **configuration** (architecture, hyperparameters, etc.), training produces a network with measurable **metrics**. The forward model of AI research is thus a mapping from configuration space to metric space. As we move up levels, we gain increasingly rich knowledge about this mapping.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/when-physics-of-ai/physics-of-ai-five-levels.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

* **Level 1:** Measure only performance metrics; tune hyperparameters blindly. (Very small metric space.)
* **Level 2:** Measure additional metrics (e.g., weight or representation statistics), but without understanding structure. (Expanded metric space, but only isolated experiments.)
* **Level 3:** Conduct controlled experiments or toy models to understand how configuration affects metrics. (Understanding the structure of the mapping.)
* **Level 4:** Given an optimization objective, infer the optimal configuration. (Understanding the inverse mapping.)
* **Level 5:** Design new models and introduce new variables. (Expanding configuration space.)

Historically, Levels 1 and 2 dominated AI research because they were effective. But as the “easy gold” has been mined, we must dig deeper.  

Level 3 can feel intimidating—it may appear to produce no immediate “practical” output. But I believe that if we endure Level 3 and build a scientific understanding of AI, then Levels 4 and 5 will reveal vast new opportunities.

---

## The Life Cycle of Research Fields

A successful research field typically follows this trajectory:

1. No one cares.
2. A few people care.
3. Exponential growth.
4. Peak.
5. Gradual decline (or rapid collapse due to a black swan).
6. Enters textbooks.

The optimal time to enter is Stage 2—before consensus forms, but as it begins to emerge. Stage 3 is still good. Stage 1 is often too early; Stage 4 or later may be too late.

If a field you are interested in is already at Stage 4, consider deviating from the mainstream and identifying a niche. That niche may still be in Stage 2 or 3.

Some students say: “But I’m interested in the mainstream field.” Then ask yourself: is your interest strong enough to endure failure and competition? Entering at Stage 4 means you may struggle to compete, especially against large tech companies.

Two additional thoughts about “interest”:

1. Interest is closely tied to competence. If you discover you are not good at something, your interest may fade.
2. Interest is also tied to familarity (sense of control). Narrow interest (“I must work on this topic”) may reflect limited exposure. Often we lack interest because we lack familarity. If you are familar with a topic but still don't like it, then the uninterest is real. 

My hot take: **research fields do not truly exist.** No two people are interested in exactly the same thing. As *Sapiens* teaches us, many concepts—including “research fields”—are shared stories. Stories help coordinate collaboration, but internally, do not let them constrain you. Mainstream stories will eventually fade. Learn from previous stories, but tell your own.

---

## Final Words: My Research Philosophy

Physics of AI is not a doctrine. It is my attempt to synthesize lessons from failures—mine and my collaborators’—into a promising path under current AI development trends. I fully acknowledge that other paths may exist, and that circumstances may change in a few years.

Taking action is the ultimate test of truth. Any principle detached from context becomes dogma.

My attitude is: understand as many perspectives as possible, **but don’t fall in love with any of them**. Use whatever works in practice. And what “works” is highly context-dependent.

Although some classify my style as theoretical, my mindset is fundamentally pragmatic. I value experimentation, observation and induction. In AI research, my philosophy is simple:

> *All models are wrong, but some are useful.*

So, returning to the original question: when should we use the Physics of AI methodology?

When it works.

No single tool solves every problem. But adding another tool to your toolbox increases your probability of solving the problem.


---


## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026when-physics-of-ai,
  title={When should I use physics of AI?},
  author={Liu, Ziming},
  year={2026},
  month={February},
  url={https://KindXiaoming.github.io/blog/2026/when-physics-of-ai/}
}
```



