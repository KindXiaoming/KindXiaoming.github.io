---
layout: post
title: Research agents should target knowledge graphs, not papers
date: 2026-02-25
description: 
tags: [Physics-of-AI, Methodology, Research-agent]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 80%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/research-agent/research-agent.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

## Motivation: Automating Blog Writing

Recently, I have been thinking about automating blog generation. While writing code and drafting blog posts, I realized that roughly 90% of the process could, in principle, be automated.

When preparing a blog post, I typically decompose the workflow into four steps:

* 1. Write the code  
* 2. Compute various observables  
* 3. Visualize the observables, inspect them manually, and identify interesting phenomena  
* 4. Write the blog post  

Here is how I currently use AI in this pipeline:

* 1. I use coding agents extensively. They perform quite well.  
* 2. I use agents to write code for computing observables, but when it comes to *defining* meaningful observables, agents sometimes make mistakes.  
* 3. I do not use agents at all for interpretation — I rely entirely on manual inspection.  
* 4. I write the blog myself and use AI only for polishing at the end.  

When I shared my idea of automating blog generation with friends, they all suggested: *Why not use a research agent?* That’s a good question.

---

## Research Agents Should Aim at Knowledge Graphs, Not Papers

In my view, current research agents are optimized for generating papers, not for building coherent knowledge graphs. Roughly put -- knowledge graphs are compressed/abstract version of papers.

Hinton once said that top researchers (for example, Ilya) possess strong “intuition.” What people call “intuition” is actually inference based on a well-structured internal knowledge graph. They trust their judgments because their knowledge graphs are stable and robust — not easily shaken by external noise.

What about average researchers? They do not have a solid knowledge graph. They are easily influenced by external inputs (e.g., new papers).

My judgment is that current research agents resemble average researchers. They can generate a large number of papers, but it is difficult to evaluate what we truly learn from them. A paper may claim that a method works on a certain dataset, but we do not know *why* it works, under what conditions it works, or how it informs future experiments. In that sense, the paper is useless — it does not help refine my knowledge graph.

The same principle applies to humans. I often tell students: the first principle of research is building your own knowledge graph. Publishing papers is merely a byproduct of the knowledge graph growing large enough to overflow.

Some might argue that citation networks already form a knowledge graph. I agree that citations constitute a graph, but it is not sufficient. It contains too much noise and operates at too low a level of abstraction to serve as a true research knowledge graph.

A genuine research knowledge graph should constitute a new data modality. In other words, we need a “language of research.”

---

## What Would a “Language of Research” Look Like?

What should research data look like?

* In some sense, the dialogue between a mentor and a student is excellent data. Unfortunately, we do not have much of it.  
* Similarly, a researcher’s “self-talk” during exploration may also be valuable data — but again, we do not have much of it.  

I have become aware of these data sources and have intentionally tried to collect them:

* Through interactions with students, I summarize how to teach research effectively.  
* My blog posts are essentially externalized versions of my “self-talk.”  

However, the data I collect is still expressed in natural language. I would like to construct a more formal symbolic system — a “language of research” that is more abstract than natural language — enabling the generation of large amounts of synthetic data. Alternatively, one could build software where researchers interact by clicking buttons rather than writing prompts in natural language or coding manually.

This symbolic system might resemble the symbolic reasoning engine in AlphaGeometry, which generates large numbers of derived conclusions, or the use of physics simulators in robotics to generate synthetic data.

Many people are skeptical of symbolic AI. I believe earlier symbolic AI systems were limited because they could not evolve. Now, however, connectionist AI offers an opportunity to *evolve symbolic systems*. In a sense, coding agents already use neural networks to manipulate symbolic code. But I suspect there exists a research language that is neither natural language nor code.

In robotics, defining the abstraction of actions is crucial. Actions themselves are symbolic, while VLA models are neural. In robotics, defining actions is relatively intuitive; in research, defining actions is far less obvious.

To create such a language, we must revisit research methodology — focusing on how to construct knowledge graphs, not merely how to publish papers. Once a coherent knowledge graph exists, continual learning becomes natural.

To draw an analogy with humans: as Hinton suggests, top researchers possess robust knowledge graphs and therefore critically evaluate new information — they do not suffer from catastrophic forgetting. Average researchers have fragile knowledge graphs and are easily swayed — effectively experiencing catastrophic forgetting.

These reflections lead me to a conclusion: **Physics of AI must be combined with agents.** Physics of AI provides the initial structure of this research language; agents provide the mechanism for its evolution. Physics of AI alone would be too rigid and primitive. Agents alone would lack rigor and structure.

---


## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026research-agent,
  title={How to automate my blog posts with research agents?},
  author={Liu, Ziming},
  year={2026},
  month={February},
  url={https://KindXiaoming.github.io/blog/2026/research-agent/}
}
```



