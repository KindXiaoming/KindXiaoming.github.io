---
layout: post
title: Discovering 108 tricks to accelerate grokking
date: 2026-06-22
description:
tags: [Physics-of-AI, Methodology, Research-agent, Learning-mechanics]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

Over the past year, AI research agents have made significant progress. They can read papers, modify code, design experiments, and even propose new algorithmic improvements.

But these systems share a common problem: they lack research intuition.

When faced with a new idea, human researchers often form a preliminary judgment — this direction might work, that one probably won't; something here looks like a phase transition, something there might just be noise.

Most AI agents today do not have this ability. For a new training trick, they typically have to actually run the experiment to completion and only then judge whether the idea is good or bad based on the final result.

In other words, they are more like diligent lab technicians than experienced researchers.

This raises a question:

**Can we build an AI that develops intuition about the model training process?**

## Learning Mechanics

When human researchers analyze a model, we rarely look only at the final test accuracy.

We also observe a large number of internal signals throughout training:

* Changes in weights
* Changes in gradients
* Changes in representations
* Changes in attention patterns
* The evolution of various statistics over training time

Often, researchers use these signals to judge what stage the model is currently in and what might happen next.

We call these phenomena about the training process **Learning Mechanics** (or "Physics of AI").

Today, however, Learning Mechanics still lacks a unified description. Different researchers focus on different phenomena, use different terminology, and much of the knowledge remains at the level of personal experience.

Therefore, a unifying goal is not to solve everything at once, but to establish a more systematic way of observing training.

## Starting from 100 observables

We chose the classic grokking problem as our starting point.

Grokking is a fascinating phenomenon in training dynamics: the model stays in a memorization phase for a long time, then suddenly acquires generalization ability and test accuracy rises quickly.

During training, we recorded not only the final accuracy but also monitored more than 100 observables simultaneously.

These observables come from different parts of the model, including weights, gradients, representations, and various statistical features of the optimization process.

We then let the agent automatically analyze the most relevant observables.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 80%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/grokking-tricks/observables.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## From observation to intervention

After identifying relevant observables, the agent goes further and proposes hypotheses. The agent then automatically generates new training strategies based on these observables and validates them through experiments.

The whole process forms a loop:

observe → analyze → hypothesize → intervene → verify.

In the end, we discovered 108 tricks that accelerate the onset of grokking.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 80%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/grokking-tricks/tricks.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

The tricks themselves are interesting, but what matters more is where they came from.

They did not come from random search, nor from exhaustive hyperparameter sweeps. They came from analyzing the training process itself.

## Next steps

For us, grokking is only a starting point.

The more important question is:

For any given training task, can we automatically analyze its Learning Mechanics and, based on that, propose improvements to model design, training strategies, and hyperparameters?

If so, then AI will no longer just run experiments automatically.

It will begin to learn how to understand experiments.

And that is exactly the goal of the system we are building.

---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026grokking-tricks,
  title={Discovering 108 tricks that accelerate grokking},
  author={Liu, Ziming},
  year={2026},
  month={June},
  url={https://KindXiaoming.github.io/blog/2026/grokking-tricks/}
}
```
