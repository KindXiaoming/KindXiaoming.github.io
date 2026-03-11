---
layout: post
title: How to ground your ideas?
date: 2026-03-13
description: 
tags: [Physics-of-AI, Methodology]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

**Motivation**

Almost everyone has experienced the following situation: you have an abstract idea in your mind. Your subconscious senses its beauty, yet you cannot clearly express it in language. For researchers, this is both a beautiful and a dangerous moment. It is beautiful because it feels like you have glimpsed some hidden truth; it is dangerous because that “truth” cannot be tested against reality—since you cannot even articulate it.

At one point, I strongly believed in “inspiration” and the “subconscious,” thinking that many clever ideas were inherently difficult to express in language. Over time, however, I realized that many ideas *can* in fact be expressed in language. If they cannot, it is often because our understanding is still shallow. In AI research, this “language” often takes the form of **toy models** — language provides an abstraction of the world, while toy models provide an abstraction of the research object. If I cannot explain an idea through a toy model, it is very likely that I do not truly understand it. Of course, having a toy model does not mean we fully understand the phenomenon, but it at least provides one perspective for understanding it—similar to the story of the blind men touching different parts of an elephant.

In working with students, I often notice that they propose “off-the-cuff” conclusions or ideas without any intention of testing them. In such cases, I usually encourage them to concretize their ideas into a toy model. Sometimes they feel that this approach is too low-level, or that it does not fully capture their original intuition. I understand this mindset: people often feel a certain “charm” toward abstract ideas, while once those ideas become concrete, they seem less magical. Students with theoretical backgrounds are especially prone to thinking that the more abstract and profound something is, the more advanced it must be, whereas the more concrete and practical it is, the less sophisticated it seems.

Reality is quite the opposite. If we want to have a real impact on the world, we must **build and break things fast**. The first step is to transform abstract ideas into something concrete and iterative. This process of “concretization” inevitably loses some information, but that is acceptable—the purpose of subsequent iterations is precisely to recover and refine it. The first version will likely be rough or even ugly, but only when we begin to make concrete **measurements** can meaningful iteration begin. Even when we study mechanisms, this does not mean that “science is slow.” With the right methodology, the science of AI (which does not suffer from the bottleneck of physical experiments) can progress very quickly. Moreover, the ultimate goal is not understanding mechanisms for their own sake—mechanistic research is only a **means**. The ultimate goal is to achieve more intelligent, efficient, and safe AGI. Therefore, we must find a balance between **idealism** and **pragmatism**.

Below are two common scenarios.

---

**Scenario 1: I want to understand an existing method**

When learning existing methods, we often encounter various arguments explaining why a method works or does not work. Although these arguments may sound intuitively reasonable, I rarely feel fully convinced, nor do I easily incorporate them into my own knowledge graph. Instead, I tend to construct a toy model to test these arguments. I also try to modify the toy model to **break** these arguments, in order to understand the conditions and boundaries under which they hold.

**Q: Why not keep things simpler? Why not just verify the argument instead of trying to break it?**

**A:** If we only verify, we easily fall into **confirmation bias**. Every conclusion holds only under certain conditions. To truly understand a conclusion, we must understand not only when it is correct, but also when it fails.

**Q: Why not make the model more realistic? The mechanism in a toy model may differ from that in real models.**

**A:** I completely agree. The mechanism in a toy model may indeed differ from that in real models. However, it at least provides one **possible mechanism**. Moreover, toy models have shorter experimental cycles and are easier to control, making them ideal for rapid exploration. A toy model provides a **starting point and an anchor for thinking**.

---

**Scenario 2: I come up with an idea off the top of my head**

In addition to studying existing methods, we also generate new ideas, and sometimes these ideas genuinely come from intuition. How can we make such ideas concrete? The approach is similar to Scenario 1: construct a toy model (a dataset, an application, or a task) to test the idea.

The **No Free Lunch Theorem** tells us that no method can outperform others across all problems. Every method has its own domain of applicability. Constructing toy models is a way to explore this **scope of applicability**. Through toy models, abstract ideas can quickly become concrete and enter an iterative cycle.

When we already have a specific application, we should ask whether our idea is suitable for that application. By the way, there are generally three ways to conduct research. “Finding applications for a method” is the second one. Ranked by impact, they are:

* **Best:** Identify an important application and solve it by any means necessary (I use the word “application” broadly—for example, “solving continual learning” is also an application).
* **Second:** Start with a method and then find applications where it works well.
* **Worst:** Fix both the method and the application in advance and force them to work together, even though they may fundamentally be incompatible.


---


## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026ground-idea,
  title={How to ground your ideas?},
  author={Liu, Ziming},
  year={2026},
  month={March},
  url={https://KindXiaoming.github.io/blog/2026/ground-your-idea/}
}
```



