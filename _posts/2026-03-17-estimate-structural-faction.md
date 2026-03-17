---
layout: post
title: Estimating structural information fraction of your dataset
date: 2026-03-17
description: 
tags: [Physics-of-AI, Methodology, Data, Memory]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

Some tasks are more structural than others. For example, $$[A][B]\cdots[A] \to [B]$$ is a highly structured task — once an induction head emerges (which likely requires only a small number of bits/parameters), it can generalize to arbitrary tokens [A] and [B]. In contrast, memorizing random names or phone numbers is not a structural task, and real bits must be spent to store this information.

For a general task (e.g., natural language modeling), it likely contains both types of sub-tasks — structural and non-structural. Suppose we characterize this by saying a fraction $$p_s$$ is structural, and a fraction $$1-p_s$$ is non-structural. Is there a way to measure this quantity?

---

## A Simple Mathematical Model

Consider a toy setup in [memory-2](/blog/2026/memory-2/), where an MLP is trained to memorize purely random samples, corresponding to $$p_s=0$$. We now construct a "structural" dataset consisting of linearly separable clusters. I call this "structural" because once the model learns how to draw hyperplanes to separate the clusters, it can solve the task regardless of the number of samples.

This contrasts with the random (non-structural) dataset, where the model has a finite memorization capacity that eventually saturates as more data are added. Thus, structural and non-structural components behave differently in terms of their dependence on dataset size.

Now we build a simple mathematical model. Suppose a model has $$N$$ parameters, corresponding to a capacity of $$AN$$ bits ($$A\approx 2-4$$ bits, according to [memory-2](/blog/2026/memory-2/) and related literature). The model may use $$S$$ bits to construct structured circuits (e.g., induction heads), leaving $$AN-S$$ bits available for memorization.

Given a dataset of $$D$$ samples ($$p_s$$ fraction is structural, $$1-p_s$$ fraction is non-structural), each sample requires $$\mathrm{log}_2 V$$ bits to memorize ($$V$$ is the vocabulary size). When the dataset is large enough such that $$AN-S < (1-p_s)D\mathrm{log}_2 V$$ — meaning the model does not have sufficient capacity to memorize all non-structural data — it will memorize $$C_m=AN-S$$ bits.

At the same time, if the structural circuit is learned, the model can correctly capture $$C_g = p_sD\mathrm{log}_2V$$ structured bits. In total, the model correctly captures

$$C = C_g + C_m = p_sD\mathrm{log}_2V + AN - S$$

bits.

We can numerically estimate $$C$$ via $$C = (\mathrm{log}V-\ell_\mathrm{final})\frac{D}{\mathrm{log}2}$$ (see [memory-2](/blog/2026/memory-2/)). Since $$AN - S$$ is independent of $$D$$, if we evaluate two large enough dataset sizes $$D_1$$ and $$D_2$$ with corresponding values $$C_1$$ and $$C_2$$, we can estimate $$p_s$$ as

$$
\tilde{p}_s = \frac{C_1 - C_2}{\mathrm{log}_2V (D_1-D_2)}
$$

For a more robust estimate, one can collect multiple data points and apply linear regression.

---

## Results

I use a 2-layer MLP (input dimension = 10, hidden dimension = 20), $$V=5$$, $$D_1=1000$$, $$D_2=2000$$, and sweep $$p_s={0, 0.25, 0.50, 0.75, 1.00}$$.

<style>
  .structural-factor-table th,
  .structural-factor-table td {
    padding: 0.1rem 0.4rem;
    line-height: 1.2;
    font-size: 0.95rem;
    border: 1px solid currentColor;
    vertical-align: middle;
  }
</style>
<div class="d-flex justify-content-center my-3">
  <div class="table-responsive">
    <table class="table table-bordered text-center structural-factor-table" style="margin-bottom: 0;">
      <thead>
        <tr>
          <th>$$p_s$$</th>
          <th>0.00</th>
          <th>0.25</th>
          <th>0.50</th>
          <th>0.75</th>
          <th>1.00</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>$$M_1$$</td>
          <td>180.0</td>
          <td>810.4</td>
          <td>1378.5</td>
          <td>1970.7</td>
          <td>2321.9</td>
        </tr>
        <tr>
          <td>$$M_2$$</td>
          <td>179.7</td>
          <td>1346.8</td>
          <td>2501.8</td>
          <td>3667.7</td>
          <td>4643.9</td>
        </tr>
        <tr>
          <td>$$\tilde{p}_s$$</td>
          <td>0.00</td>
          <td>0.23</td>
          <td>0.48</td>
          <td>0.68</td>
          <td>1.00</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

The estimated value $$\tilde{p_s}$$ reasonably approximates the true $$p_s$$, supporting the validity of this simple mathematical model.

---

## Comment

* As an exercise, one can also attempt to estimate $$A$$ and $$S$$.  
* In our toy dataset, the $$V$$ classes are uniformly distributed. When applying this framework to more complex situations (e.g., LLMs), the term $$\mathrm{log}_2 V$$ may need to be replaced by the effective number of bits (e.g., unigram entropy), or alternatively $$V$$ should be interpreted as the effective vocabulary size, because some tokens may occur more frequently than others.


---
## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/1zPDkHj0C43gi189zlllXZD_4OCnbwDlu?usp=sharing).



---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026structural-fraction,
  title={Estimating structural information fraction $$p_s$$ in your dataset},
  author={Liu, Ziming},
  year={2026},
  month={March},
  url={https://KindXiaoming.github.io/blog/2026/estimate-structural-fraction/}
}
```



