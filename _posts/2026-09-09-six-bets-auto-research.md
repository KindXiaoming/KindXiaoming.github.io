---
layout: post
title: Six Bets on Auto-Research
date: 2026-09-09
description: Can scientific research be made explicit and externalized? Different answers lead to different Auto-Research technical routes.
tags: [Physics-of-AI, Methodology]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

There has been a lot of discussion about Auto-Research lately. I want to take a higher, more philosophical perspective and ask what different paths Auto-Research might take.

The core question is: as a modality, what properties does scientific research actually have?

I think two dimensions are especially important: whether research can be made **explicit**, and whether it can be **externalized**. Different answers to these two questions lead to completely different technical routes for Auto-Research.

<div class="cr-blog-figure" style="width: 95%; max-width: 100%; margin: 1rem auto;">
<img src="/assets/img/blogs/auto-research-bets/six-bets.png" alt="Can scientific research be made explicit and externalized? Six bets and technical routes." style="width: 100%; max-width: 100%; height: auto; display: block;" />
</div>

Take language as an example. Language is a modality that can be both made explicit and externalized.

By *explicit*, I mean that it is not something that can only be intuited and never spoken. It can be clearly expressed, recorded, and operated on. By *externalized*, I mean that it can exist independently of the individual who produced it. Once someone writes a passage of text, the text remains even if that person is gone; others can still read it, copy it, and learn from it.

So: can scientific research be made explicit and externalized?

This question actually corresponds to six different bets.

---

## Bet 1: Research can be made explicit and externalized ———— and already has been

There is no doubt that the parts of research that can be summarized into natural language, mathematical formulas, and code have already been made explicit and externalized.

This is also currently the mainstream route for Auto-Research: use LLMs to do research.

The bet behind this route is: research can not only be made explicit and externalized, but humans have already externalized much of the knowledge research needs into existing language, papers, and code. Therefore, once a model sufficiently masters these existing symbolic knowledge bases, combining, searching, and sampling within that space may yield new scientific results.

In some sense, this is using an LLM to buy lottery tickets.

I do not take this bet ———— at least, I do not think it covers the whole of research. That is why I choose to explore Auto-Research routes that differ from, or at least are orthogonal to, the LLM route.

But the point of this essay is not to argue that my bets are correct. It is to discuss more objectively: if you believe different bets, what technical routes do they each lead to?

---

## Bet 2: Research can be made explicit and externalized ———— but the process is not finished yet

Imagine physics in Aristotle's time.

People of that era had already accumulated a great deal of experience and intuition about the world, but physics had not yet been truly made explicit and externalized: there was no Newtonian mechanics, no calculus, and none of the symbolic systems we can write into textbooks today.

That does not mean physics cannot be made explicit. On the contrary, later history showed that it can.

I think AI research today is likely in a similar stage.

We have already accumulated a great deal of experience: which architectures are easy to train, which optimizers work better under which conditions, why some tricks help, why certain scaling laws appear... But much of this knowledge still lives in researchers' experience, intuition, and scattered observations. It has not yet been systematically made explicit into a mature science.

This is what I have been calling the Physics of AI, or more broadly, the Science of AI.

The Science of AI Textbook has not been written yet ———— but it may be writable.

So if you take Bet 2, the most natural technical route is not to let an agent search directly in an infinitely large research space. It is first to complete a knowledge-externalization step analogous to the transition from Aristotle to Newton: gradually precipitate today's AI research experience, phenomena, regularities, and mechanisms into a knowledge system that can be expressed, composed, and reasoned over.

I believe this textbook needs to be written by excellent AI researchers and agents together.

---

## Bet 3: Research can be made explicit, but cannot be externalized

EEG signals offer an incomplete but intuitive analogy.

They can be made explicit ———— at least in principle, we can capture activity signals from the brain with devices, even if today's signal-to-noise ratio and interpretive power remain very limited.

But they are hard to externalize the way text is. They depend heavily on one particular brain, occurring in one particular person.

If research intuition is something similar ———— if it truly exists and can in principle be measured, but cannot naturally exist apart from the individual ———— then the most natural technical route is no longer language models, but brain–computer interfaces.

In other words, rather than forcing a top AI researcher to "say" their intuition out loud, one might try to read that intuition directly.

---

## Bet 4: Research cannot be made explicit, but can be externalized into machines

This is a possibility I find especially interesting.

Even an outstanding AI researcher ———— say, Kaiming He ———— may not be able to fully make their research intuition explicit. If an intuition cannot be put into words, then neither their students nor an LLM that only reads papers can truly acquire it.

But is such intuition innate?

Clearly not. When we were born, AI did not even exist.

An excellent AI researcher's intuition about model architectures, training dynamics, and experimental results is formed through seeing many models, running many experiments, and hitting many pitfalls. The end product of that learning process is tacit knowledge in the brain, not a set of explicit rules that can be fully written in language.

If so, a natural idea follows:

We do not necessarily need to replicate the "knowledge." We can replicate the "process that forms the intuition."

This is what our **Meta Model** project aims to do.

Let the meta model see sufficiently diverse model architectures, training configurations, and training curves. Let it gradually form an intuition about AI systems from a large amount of experience of the form "experimental configuration → experimental result."

It may not be able to tell you a beautiful natural-language law. But when it sees a new architecture, it may be able to judge roughly how it will train, where things will go wrong, and how to fix them.

In other words, we are not trying to translate the intuition in Kaiming He's mind into language and then have a machine learn that language.

We are trying to retrain a machine that possesses that kind of intuition.

It may even end up with more "experimental experience" than any single human researcher.

---

## Bet 5: Research cannot be made explicit, but can be externalized into people

This is essentially the same idea as the meta model, except that the thing being trained is a human rather than a machine.

If research intuition comes from abundant experience of "experimental configuration — experimental result" pairs, then in principle we can also let a person see enough such pairs to train their AI intuition.

The problem is that a human is not a neural network happy to look at a million training samples a day.

People get bored.

So if we truly want to systematically train human AI intuition, we need to design the process to be interesting enough, feedback-rich enough ———— even addictive.

That is what our Science of AI Game aims to do.

Turn the originally dull accumulation of experimental experience into prediction, decision, competition, and feedback inside a game.

You think you are playing a game.

In reality, your brain is being trained into a Meta Model.

---

## Bet 6: Research can neither be made explicit nor externalized

This is the most pessimistic world.

If research can neither be expressed nor transferred from one carrier to another by any means, then research ability remains forever locked inside particular human brains.

Knowledge cannot truly be transmitted, and research ability cannot be scaled.

In that world, Auto-Research is basically impossible.

Fortunately, I do not believe we live in such a world.

---

## Which bets do I take?

Finally, a brief note on my own judgment.

I mainly believe in Bet 2, Bet 4, and Bet 5.

On the surface, they correspond to three different routes:

- **Science of AI Textbook**: make research knowledge explicit.
- **Meta Model**: train research intuition into machines.
- **Science of AI Game**: train research intuition into human brains.

But in my view, they are three sides of the same thing.

None of them treats research as merely a problem of "sampling in language space." Instead, they treat research itself as an object worth studying: we need to understand how research ability arises, how knowledge forms, how intuition accumulates, and how these things can be transferred and scaled.

So rather than "how to automate research as quickly as possible," I care more about a more basic question:

**What is research, really?**

Because only when we understand a capability do we truly know how to copy it, train it, and eventually automate it.

Understanding precedes automation.
