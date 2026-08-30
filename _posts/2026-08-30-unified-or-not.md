---
layout: post
title: Foundation Model or Not?
date: 2026-08-30
description:
tags: [Physics-of-AI, Methodology]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**


> 天下大势，分久必合，合久必分。———— 罗贯中

> The empire, long divided, must unite; long united, must divide. ———— Luo Guanzhong

---

## Unification or specialization

There are two paradigms in AI: one is the Specialized Model, and the other is the Unified Model (the so-called Foundation Model). We can name many successful Specialized Models ———— AlphaGo, AlphaGeometry, and AlphaFold each use one model to solve one task. In contrast, the only truly successful Unified Model so far is the LLM. For multimodal models, VLAs, Time Series Foundation Models, and scientific foundation models, it is hard to point to achievements that Specialized Models could not have accomplished. Time Series Foundation Models, in particular, can even underperform linear models in some settings. But the success of LLMs has been so spectacular that it has absorbed nearly all of our attention, making us believe that Foundation Models are the only path forward. Once we step outside this enthusiasm and paradigm, however, we should ask:

Unification or specialization? This is a question. 

<div class="cr-blog-figure" style="width: 70%; max-width: 100%; margin: 1rem auto;">

<img src="/assets/img/blogs/unified-or-not/unification-or-specialization.png" alt="Unification or Specialization? This is a question." style="width: 100%; max-width: 100%; height: auto; display: block;" />

</div>

---

## Meta Model: Automating the Design of Specialized Models

I believe in the No-Free-Lunch principle ———— every task has its own optimal model. The architecture of this optimal model should correspond to the generation mechanism behind the data. This is essentially the idea of the Specialized Model (or, in an older terminology, the expert system). The problem with Specialized Models is that there are simply too many tasks in the world. If every task requires a team of human researchers to design its model, we will never finish. The emergence of LLMs offered an elegant solution to this pain point ———— if one model can solve every task, then we no longer need to design Specialized Models. But designing this Unified Model itself still requires the very best human AI researchers.

I am thinking about creating a Meta Model (model for model) that can design all kinds of Specialized Models. This would solve the same problem — “Specialized Models require many smart people to design” — but in a different way. Instead of building one universal Foundation Model, we build the ability to do AI research and model design into the Meta Model itself. A Meta Model that can design Specialized Models should, of course, also be able to design what we currently call Foundation Models. In fact, today's LLM Foundation Model is itself a kind of Specialized Model: it is specialized to the world of text, and it has boundaries. The text world simply happens to be close enough to everyone that its “generality” means more that “everyone can access it” than that “it can solve every problem.”

A concrete question then arises: given $$K$$ tasks, should the Meta Model build K Specialized Models, or should it build one Unified Model? Below, we construct a simple model to quantitatively characterize the phase transition between these two regimes.

---

## A toy model of unification-specialization phase transition

The most intuitive picture is this: when different domains have large overlap, we should build a Foundation Model, as in natural language. When the overlap is small, Specialized Models become more advantageous. Time series share a common data format, but not a common generating mechanism. Stock prices, weather, retail sales, and sensor signals follow fundamentally different dynamics, and may therefore require different model architectures and inductive biases. Compared with forcing one model to solve all tasks, Specialized Models can avoid the “Universality Tax.” In reality, this is not a binary choice but a spectrum. Techniques such as MoE and TTT can be viewed as attempts to create small pockets of Specialization inside a large Foundation Model.

<div class="cr-blog-figure" style="width: 90%; max-width: 100%; margin: 1rem auto;">

<img src="/assets/img/blogs/unified-or-not/overlap-spectrum.png" alt="Degree of Overlap / Shared Structure: Foundation Model vs Hybrid vs Meta Model" style="width: 100%; max-width: 100%; height: auto; display: block;" />

</div>

Let us build a simple mathematical model:

Suppose the optimal model parameters for task $$i$$ are $$\theta_i=\theta_{\text{shared}}+\delta_i$$, where $$\theta_{\text{shared}}$$ represents the structure shared across all tasks, and $$\delta_i$$ represents task-specific structure. Define the overlap between tasks as:

$$\rho=\frac{\sigma_{\text{shared}}^2}{\sigma_{\text{shared}}^2+\sigma_{\text{specific}}^2}$$

When $$\rho\rightarrow1$$, different tasks are highly similar, making a **Foundation Model** favorable; when $$\rho\rightarrow0$$, tasks are highly different, making **Specialized Models / Meta Model** favorable. We further define task heterogeneity as $$H=\sigma_{\text{specific}}^2$$. Suppose each task has $$n$$ data points and the observation noise is $$\sigma^2$$. Then the statistical uncertainty of an individual task is approximately:

$$U=\frac{\sigma^2}{n}$$

This gives a simple critical condition:

$$H \lt U \Rightarrow \text{Foundation Model},\qquad H \gt U \Rightarrow \text{Meta Model}$$

In other words, **when the true differences between tasks are smaller than the statistical uncertainty within an individual task, we should share a model; when the differences between tasks exceed that uncertainty, we should specialize.** We can further define a dimensionless **Specialization Number**:

$$\Gamma=\frac{H}{U}=\frac{n\sigma_{\text{specific}}^2}{\sigma^2}$$

Thus, $$\Gamma \lt 1 \Rightarrow$$ Foundation Model, $$\Gamma \gt 1 \Rightarrow$$ Meta Model, with a critical point at $$\boxed{\Gamma_c\approx1}$$. As task heterogeneity increases or the amount of data per task grows, the optimal strategy may transition from **one model fits all** to **task-specific specialization**.

---

## In practice: Foundation Model or Specialized Model?

The discussion above is somewhat abstract. In practice, how do we decide whether to use a Foundation Model or a Specialized Model? Let us start with two examples:

* LLMs are highly successful Foundation Models. Although different text tasks may appear enormously diverse, they share a common vocabulary, and more importantly, their underlying generation mechanisms are highly shared. By “generation mechanism,” I mean the process by which the human brain compresses the complex natural world into text. No matter how different text tasks may appear, they are ultimately generated by human brains. There is therefore a “bottleneck” in the generation mechanism.

* Time Series Foundation Models are less successful. In many time-series tasks, foundation models can even underperform linear regression. This is because time series are merely a data format, not a generating mechanism. Stock prices, weather, retail sales, and sensor signals follow fundamentally different dynamics, and may therefore require different model architectures and inductive biases. There is no bottleneck in the generation mechanism here — or rather, the “bottleneck” is as large as the observable universe itself.

Therefore, whenever we talk about building a Foundation Model for X, we should first distinguish whether X is a **data format** or a **generating mechanism**. Roughly speaking, when X corresponds to a generating mechanism, a Foundation Model for X makes sense; when X is merely a data format, a Foundation Model for X is much less justified.

Let us consider a few examples:

* X = Math? Foundation Model, because mathematics is generated by human brains.

* X = Code? Foundation Model, because code is also generated by human brains.

* X = Sequence? Specialized Models, because, like time series, sequences are merely a data format.

Many people care about whether World Models should be Foundation Models or Specialized Models. I lean toward Specialization. The reason is again that images and videos are merely data formats: they have not been compressed and regenerated by something like the human brain. Recent Code-as-World approaches instead first transform the world into code, introducing exactly such a process of compression and regeneration. For the same reason, I am deeply skeptical of the VLA route, because VLA defines a “data format,” not a “generating mechanism.” World Models attempt to force such a unified generating mechanism to emerge, which I also find questionable. I believe different visual scenes simply have different generating mechanisms, different dynamics, or different simulation code. Learning all of them with a single end-to-end Foundation Model is unlikely to work.

---

## Meta Model is the next step

Here is a provocative hypothesis: except for natural language (extended to mathematics and code), no other modality can truly be unified by a single Foundation Model. Natural language, mathematics, and code have all been compressed and regenerated by human brains. Other modalities — vision, time series, world models, and raw scientific data that have not yet been symbolized — are generated directly by the universe itself.

So what comes next? As the opening quote says, “The empire, long divided, must unite; long united, must divide.”（“天下大势，分久必合，合久必分”）。 I expect the next stage to bring us back to the era of Specialized Models. But this time, instead of relying on massive amounts of human labor and intelligence to design expert systems, we can build a Meta Model that unifies the process of model design and creates Specialized Models for different domains.

This is a higher level of unification: **we do not unify the models themselves; we unify the process of designing models.** The resulting models can remain radically different from one another.

<div class="cr-blog-figure" style="width: 95%; max-width: 100%; margin: 1rem auto;">

<img src="/assets/img/blogs/unified-or-not/three-stages.png" alt="Stage 1 Human-designed Specialized Models, Stage 2 Foundation Model, Stage 3 Meta Model" style="width: 100%; max-width: 100%; height: auto; display: block;" />

</div>