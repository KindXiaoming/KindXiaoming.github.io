---
layout: post
title: If not LLMs, what should I work on?
date: 2026-04-10
description:
tags: [Physics-of-AI, Methodology]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Everything is Language

I believe many AI researchers (myself included) often fall into a certain kind of confusion — I don’t want to compete in the language model race, but beyond language models, what else is there to do?

In this blog, I invite you to join me in a thought experiment. I won’t elaborate further—please first accept the following two premises:

1. Data is fundamental; models are merely mirrors of data. Therefore, we will primarily discuss data, while placing models in a secondary role.

2. All data is “language.” For example, visual data, robotic sensor data, brain signals, and mathematical or physical formulas can all be viewed as forms of language (or modalities).

Next, we place these “languages” on a two-dimensional plane. These languages differ in two aspects: (1) their level of abstraction with respect to the real world; (2) the difficulty of collecting such data.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/everything-language/everything-language.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Natural language happens to lie in a particularly “blessed” region: (1) it has a high level of abstraction; (2) it is extremely easy to collect (thanks to the internet). However, not all “languages” enjoy both of these properties—many fall into a “cursed” region. I would argue that these “cursed” languages are precisely where the true blue ocean lies.

---

## More Primitive Languages

Vision is a more primitive language than natural language. More primitive languages tend to have higher redundancy. Because they are less compressed by nature, they rely more on models to perform compression and abstraction. This is why representation learning is both crucial and challenging in computer vision.

Beyond vision, robotic sensor data and raw observations in physics (e.g., planetary position records collected by :contentReference[oaicite:0]{index=0}) are also highly primitive forms of data. These data may implicitly contain symbolic physical laws, but current AI models still struggle to extract them due to insufficient compression capabilities.

Some argue that the intelligence of large language models (LLMs) comes from their ability to compress. I partially agree—but it is important to note that much of this compression comes from the data itself, not just the model. For raw data that has not been pre-compressed, the burden of compression falls heavily on the model, demanding much stronger representation learning capabilities.

The level of abstraction in neuroscience data is more debatable. I tend to view it as moderately abstract—it contains some useful abstractions (e.g., V4 encoding color), but also significant redundancy and low-level information (e.g., Gabor filters in V1). While leveraging brain data is certainly important, the more urgent challenge at present is collecting it at scale.

---

## Languages with Less Data

As discussed above, the scale of brain data is currently a core bottleneck for “Neuro for AI.” However, there is an even worse situation: a language that has not yet been created.

In a previous blog, I proposed the need for a “research language”—one that can be translated to and from natural language, but is more abstract and more compressed. The immediate task is to create such a language, and then enable people to use it, produce it, and accumulate it. In the context of AI research, “Physics of AI” may serve as such a candidate research language.

---

## Continual Learning

Once a language is sufficiently compressed (whether through natural evolution or by AI models) and exists at scale, we can use pretraining to enable models to learn it.

However, we also care about continual learning. In [Tianle Cai’s recent discussion on continual learning](https://x.com/tianle_cai/status/2042459055483207818), he outlines different stages of its evolution—from SFT, to RL, and more recently, to context management. In some sense, continual learning may appear to be largely “solved.”

But I believe this conclusion needs to be more precise: continual learning in natural language may indeed be largely solved, but for other languages, *native* continual learning remains far from solved. By “native,” I mean learning that is carried out entirely within the language itself, without relying on natural language as scaffolding.

This once again highlights the special nature of natural language. Humans can perform continual learning through natural language, a capability shaped by millions of years of evolution. Other languages do not inherently possess this property. If our models are too weak (e.g., lacking strong compression and representation learning abilities), they may require extremely long trial-and-error processes to acquire similar capabilities.

Therefore, we must leverage human intuition—also a product of long evolutionary processes—to inject better representations and structures into our models, enabling them to master these “non-natural” languages. Advocates of the Bitter Lesson may disagree, but I borrow a remark from [Saining Xie in a podcast](https://www.youtube.com/watch?v=rIwgZWzUKm8): the success of natural language is, in fact, a counterexample to the Bitter Lesson, because natural language itself is a beautifully structured artifact—a gift from natural evolution.

In summary, the success of natural language cannot be naively extrapolated to other domains. And it is precisely this gap that defines the space for innovation.

---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026everything-language,
  title={If not LLMs, what should I work on?},
  author={Liu, Ziming},
  year={2026},
  month={April},
  url={https://KindXiaoming.github.io/blog/2026/everything-is-language/}
}
```



