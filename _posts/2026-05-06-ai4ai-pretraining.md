---
layout: post
title: AI4AI needs its own "world model"
date: 2026-05-06
description:
tags: [Physics-of-AI, Methodology]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## AI4AI Needs Its Own “World Model”

AI4AI refers to using AI to improve AI itself.

Today’s Research Agents are already capable of producing papers at an average level with a high degree of automation. However, we still struggle to evaluate the true value of these papers, and even more importantly, to deploy their ideas into real-world systems.

Some optimistic AI4AI researchers believe that “language” alone is sufficient for AI4AI. I am more pessimistic in this aspect. I do not think language is enough — at least not at the current stage.

I am not arguing that mysterious concepts like “intuition” or “taste” transcend language. In fact, I believe everything can ultimately be expressed in language. The issue is that this process takes time.

From Newton until today, physics has developed for more than four hundred years; if we start from Aristotle, then physics has evolved for over two thousand years. On the natural timescale, the emergence of a mature scientific “language” — such as physics itself — requires an extraordinarily long period of time.

And from ChatGPT until now, only three years have passed.

So in reality, we still do not yet possess a true “language of AI.” You may call it *Science of Deep Learning*, *Physics of LLMs*, or *Physics of AI* — the name does not matter. What matters is that such a language has not yet fully emerged.

Perhaps two hundred years from now, once the language of AI has matured, I would strongly support the idea that “AI4AI only needs language.” But at this moment, that language has not yet crystallized. AI4AI cannot simply be a language model with some additional post-training. AI4AI needs its own “world model.”

---

## Vibe Training

What would such a world model for AI4AI look like?

A world model of the physical world should be able to predict the future, understand the effects of interventions, and answer counterfactual questions.

For example:

> “If gravity were doubled, how would the trajectory of a ball change?”

Similarly, a world model for AI4AI should also be able to predict experimental outcomes. It should answer questions such as:

> “If I double the learning rate, how will the training curve change?”

In fact, top AI researchers already possess such a world model implicitly in their minds.

Before training even begins, they often have a fairly accurate intuition about what the experimental results will look like. This allows them to quickly discover effective architectures, hyperparameters, and training strategies.

I call this ability:

> **Vibe Training**

So how is the ability of “Vibe Training” acquired?

Fundamentally, it comes from two sources:

- Seeing a large amount of experimental data (data-driven)
- Extracting empirical regularities from experience (rule-driven)

At its core, it is an intuition about training dynamics.

---

## The Pretraining of AI4AI

I call the process of developing “Vibe Training” ability the *pretraining* of AI4AI.

Why call it pretraining?

Because this process does not yet involve any specific downstream task, and it is extremely tedious.

More formally, this pretraining process attempts to learn a mapping:

> From the configuration space of models to their training dynamics.

Unfortunately, even the best human AI researchers are still poorly pretrained in this sense. There are two main reasons.

### 1. Poor Data Diversity

Most researchers spend their careers working within only one subfield of AI.

As a result, their “pretraining” is constrained to a narrow data distribution.

I once argued with a friend working in computer vision about whether a certain trick was useful. He claimed that in every example he had seen, the trick always improved performance.

But my intuition suggested that in NLP the same trick might actually hurt performance.

At first he did not believe me. Later, after trying it on NLP experiments, the performance indeed became worse.

Many so-called “empirical rules” are merely local regularities within a specific distribution, rather than universal principles.

---

### 2. Insufficient Data Quantity

Humans are not machines.

Running 3–5 experiment iterations per day is already considered productive. But this is nowhere near enough.

This is especially true for large-scale experiments, where often:

> you only run once.

Experiments are simply too expensive.

As a result, the amount of “pretraining data” available to human researchers is negligible compared to what a true foundation model would consume.

---

## Toy Models as Synthetic Data

Many fields suffer from data scarcity, such as robotics.

Synthetic data is a common solution.

Its advantages are:

- Large-scale
- Cheap
- Controllable

But its disadvantage is:

- It may not be realistic
- There exists a Sim2Real Gap

So what counts as “synthetic data” in AI4AI?

I would argue:

> **Toy Models themselves are the synthetic data of AI4AI.**

Previously, researchers manually designed toy models one by one.

But this process is far too slow.

If we could modularize the design of Toy Models, then we could automatically generate large amounts of experimental data for the pretraining of AI4AI.

What truly matters is no longer a single carefully crafted toy model, but rather:

> The generative mechanism behind Toy Models themselves.

---

## Pretraining: Tedious but Necessary

The pretraining of LLMs is tedious, yet necessary.

Humans would never force themselves to memorize the entire Wikipedia. But without pretraining, post-training has no foundation to build upon.

The same applies to AI4AI.

Its training process will also be tedious, yet necessary.

Since the beginning of this year, my blog has essentially been an attempt to “train myself”:

- Randomly choose a toy dataset
- Randomly choose a toy model
- Observe phenomena without any explicit goal

At first, I was doing everything manually.

But as the number of experiments increased, I gradually began to perceive the hidden structure behind the design space of Toy Models.

I became less obsessed with carefully designing one or two specific toy models, and instead started thinking about:
g
> How can the generation of Toy Models itself become modularized and scalable?

The direction I am currently exploring is:

> An Agent randomly selects a toy model, conducts experiments automatically, and identifies interesting phenomena within the results.

Meanwhile, my role is to:

- Interpret these phenomena
- Summarize the underlying regularities
- Suggest the next research directions

In some sense, this may represent the earliest form of an “experimental science” for AI4AI.
