---
layout: post
title: Tokenization 1 -- Factorized tokenization
date: 2026-03-14
description: 
tags: [Physics-of-AI, Tokenization]
categories: AI
---

**Author: Ziming Liu (刘子鸣)**

---

## Motivation

Tokenization is a key design choice for LLMs, yet it may be relatively underexplored. The motivation to improve current tokenization methods is two-fold:

* Token embeddings contain a large fraction of the parameters in LLMs, because the vocabulary size is usually much larger than the embedding dimension.  
* A token can often be viewed from multiple angles: whether it is an adjective or a noun, whether its meaning is positive or negative, etc. When predicting the next token "good", "great" should incur a lower loss compared to "apple", since "good" and "great" are adjectives, whereas "apple" is a noun.

Although mechanistic interpretability has shown that linear directions distinguishing nouns and adjectives can emerge in representation space, it may be beneficial to explicitly encode such distinctions during the tokenization process. This is the idea we explore below.

---

## Factorized tokenization

Suppose we live in a world where each object has 100 binary features — big or small, black or white, circle or square, etc. If we represent each object with a single token, we would need $$2^{100}$$ tokens. However, if we can identify a factorized representation, we would only need 200 tokens, with each object represented by 100 tokens.

Using a factorized representation can therefore dramatically reduce vocabulary size if the world is indeed (approximately) factorized. That said, if we do not know how to map an object into its underlying features, we must learn this mapping — i.e., we must learn the tokenization.

A concrete example is that although we know "good" is an adjective, we certainly cannot enumerate all possible features by hand. Ultimately, the tokenization process must be learned. For the sake of simplicity, however, we assume access to the factorized representation in this blog.

**Notation**

Let standard tokens be denoted as $$[0], [1], [2]\cdots, [V-1]$$, with a total of $$V$$ tokens.

We assume access to a factorization process — a mapping from one token into a group of sub-tokens. There are $$n$$ groups, and each group contains sub-tokens $$V_1, V_2, \cdots, V_n$$ ($$\sum_i V_i = V$$). The token $$[k]$$ is mapped to $$n$$ sub-tokens:

$$[k] \to [f_1(k)]_{G_1} [f_2(k)]_{G_2} \cdots [f_n(k)]_{G_n}$$

A concrete example is factorizing 100 tokens into two groups of 10 tokens based on the tens digit and the ones digit:

$$[0] \to [0]_{G_1}[0]_{G_2}, [12]\to [1]_{G_1} [2]_{G_2}, [92] \to [9]_{G_1}[2]_{G_2}$$.

---

## Datasets

In this blog we fix $$V_1=V_2=\cdots=2$$, where the factorized representation becomes equivalent to a binary string representation. For example, if there are $$n=3$$ groups,

$$[0]\to [0]_{G_1}[0]_{G_2}[0]_{G_3}, \quad [6]\to [1]_{G_1}[1]_{G_2}[0]_{G_3}$$.

As a result, $$V = 2^n$$.

**Task 1: Elementwise Inversion**

This task is easily described in factorized tokenization:

$$[k_1][k_2]\cdots[k_n] \to [1-k_1][1-k_2]\cdots[1-k_n]$$

**Task 2: Elementwise-addition**

This task is also naturally described in factorized tokenization:

$$[a_1]\cdots [a_n], [b_1]\cdots [b_n] \to [(a_1+b_1)\%2]\cdots [(a_n+b_n)\%2]$$

**Task 3: Modular addition**

This task is more naturally described in standard tokenization:

$$[a], [b] \to [(a+b) {\rm mod} V]$$

---

## Results

We find that in all three cases, factorized tokenization appears to be more data-efficient than standard tokenization. The non-monotonic behavior is likely due to random seeding.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 100%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/tokenization-1/test-acc.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Note that in the elementwise inversion task, test accuracy is close to zero because test tokens are never seen during training. However, factorized tokenization is still able to generalize due to the compositional generalization of sub-tokens.

---
## Code

Google Colab notebook available [here](https://colab.research.google.com/drive/16slLxo_dXtobZncCE45v9QPzRURhe6C-?usp=sharing).



---

## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026tokenization-1,
  title={Tokenization 1 -- Factorized tokenization},
  author={Liu, Ziming},
  year={2026},
  month={March},
  url={https://KindXiaoming.github.io/blog/2026/tokenization-1/}
}
```



