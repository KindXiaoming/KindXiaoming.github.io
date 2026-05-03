---
layout: post
title: Data efficiency of Bi-gram data
date: 2026-05-03
description:
tags: [ComfyResearch, Workflow]
categories: AI
---

Black: Agent generated; <span style="color: red;">Red: Added by human</span>

## Introduction

<span style="color: red;">Bi-gram data is a simple dataset capturing some basic aspect of natural language. When there are $$V$$ tokens in vocabulary, it is expected that at least $$V^2$$ tokens should be seen to learn the bi-gram model well. As a result, I'm interested in measuring generalization gap as a function of vocabulary size and train size, as swept in this blog. </span>

## Experimental setup

<div class="cr-blog-figure" style="width: 100%; max-width: 100%; margin: 1rem 0;">
<img src="/assets/img/blogs/bigram-data-efficiency/graph.png" style="width: 100%; max-width: 100%; height: auto; display: block;" />
</div>

**Dataset:** Bigram low-rank dataset

**Model:** MLP_token model

**Optimizer:** Adam

**Loss:** Cross-entropy loss

**Observables wired to training:** Observable Accuracy

Train vs test gap

**Trainer:** Trainer

## Sweep experiments


## Sweep comparison — Grid: vocab size × train size — Loss

<div class="cr-blog-figure" style="width: 100%; max-width: 100%; margin: 1rem 0;">
<img src="/assets/img/blogs/bigram-data-efficiency/sweep-01-sweep-comparison-grid-vocab-size-train-size-loss.png" alt="Sweep comparison — Grid: vocab size × train size — Loss" style="width: 100%; max-width: 100%; height: auto; display: block;" />
</div>

## Sweep comparison — Grid: vocab size × train size — Accuracy

<div class="cr-blog-figure" style="width: 100%; max-width: 100%; margin: 1rem 0;">
<img src="/assets/img/blogs/bigram-data-efficiency/sweep-02-sweep-comparison-grid-vocab-size-train-size-accu.png" alt="Sweep comparison — Grid: vocab size × train size — Accuracy" style="width: 100%; max-width: 100%; height: auto; display: block;" />
</div>

## Sweep comparison — Grid: vocab size × train size — Train vs test gap — last step (lines)

<div class="cr-blog-figure" style="width: 100%; max-width: 100%; margin: 1rem 0;">
<img src="/assets/img/blogs/bigram-data-efficiency/sweep-03-sweep-comparison-grid-vocab-size-train-size-trai.png" alt="Sweep comparison — Grid: vocab size × train size — Train vs test gap — last step (lines)" style="width: 100%; max-width: 100%; height: auto; display: block;" />
</div>

<span style="color: red;">The result is expected: generalization gap (test loss minus train loss) decreases as train data increases, and larger vocabulary size requires more data. (TODO: automatic quantitative analysis)</span>

## Code

Code can be downloaded [here](/assets/img/blogs/bigram-data-efficiency/base_experiment.py).
