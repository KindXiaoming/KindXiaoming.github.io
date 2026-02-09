---
layout: post
title: Symbolic Regreesion? Structure Regression!
date: 2023-07-08
description: 
tags: [Modularity, Science-for-AI, Structuralism]
categories: Interpretability
---

Many scientific problems can be formulated as regression: given independent variables $$(x_1, x_2, \cdots, x_d)$$ and dependent variable $$y$$, we want to find a function such that $$y = f(x_1,x_2,\cdots, x_d)$$. Scientists, especially physicists, have put great effort and labor into solving tasks of this kind. For example, Kepler spent eight years staring at astronomical data, before he figured out his eponymous three laws. By contrast, many scientists are less crazy about symbolic formulas. They are content with empirical laws. To be specific, they set $$f$$ to be a specific functional form, allowing some tunable empirical parameters, which may not have very clear physical meanings.

Two goals mentioned above, symbolic regression (SR) and empirical regression (ER), have their own limitations: SR is powerful but brittle, while ER is robust but constrained. Is it possible to have something in the middle, which is both powerful and robust? The answer is structure regression (StR)! This blog is organized as such: Firstly, I discuss what is structure regression, arguing why structure regression is probably a better goal to pursue than symbolic regression. Secondly, I describe our method BIMT to do structure regression. Finally, I bet on scientific fields that structure regression is promising for, and most importantly, call for collaboration!

## Symbol or Structure?

Although symbols play huge roles in mathematics and physics, I am not a big believer for “everything is symbolic”. For example, only very few unary functions are labeled as “symbolic” or “analytic”, such as $$f(x)=x^2, {\rm sin}(x), {\rm exp}(x)$$. If one randomly draw a 1D curve on a piece of paper, only probability one the function is symbolic. “Symbolic functions” defined by us are too limited. The definition can also strongly depend on contexts: hypergeometric functions may be viewed as symbolic in mathematical physics, but may be unacceptably too complicated in engineering.

In contrast to symbols, structures are probably more universal. An example of structure is independence. Independence is what makes physics possible at all: our universe has infinite degrees of freedom, but physical systems we care about only depend on a finite number of them. A similar structural property is modularity, which allows us to decompose a huge object into small pieces which are much more manageable. Other examples of structural properties are hierarchy, compositionality, reusability, sparsity etc.

So, what does structure regression mean? Given independent variables $$(x_1, x_2, \cdots, x_d)$$ and dependent variable y, we want to find a structure (or structures) such that $$y = S(x_1,x_2,\cdots, x_d)$$. Suppose the structure is additive modularity, then $$S(x_1,x_2,\cdots, x_d)=\sum_{i=1}^d f_i(x_i)$$. Note that figuring out symbolic forms of $$f_i (i=1,2,\cdots,d)$$ is not necessary for structure regression. As long as the additive property is discovered, a victory is claimed.

One may say that structure regression is a weaker or less ambitious version of symbolic regression. This is true, but for good reasons. Firstly, as I argued above, there are cases where symbolic regression is impossible. If so, structure regression is probably the best thing one can hope for! Secondly, for cases where symbolic regression are indeed possible, structure regression is a nice intermediate milestone to target for, because it greatly simplifies the symbolic regression problem (e.g., AI Feynman).

One may feel that my critiques for symbolic regression can directly apply to structure regression: “the search space for symbolic regression is (discrete) symbolic formulas, the search space for structure regression is (discrete) structures. In both cases, you need to specify your symbols/structures (which can be limited and context-dependent), and combinatorial searches are needed.” This is not true. There are key differences between symbolic regression and structure regression. Let’s say we take a neural network. Structure regression only cares about the graph of how neurons connect to each other. In addition to that, symbolic regression also cares about how each neuron processes signals. Structural regression is more robust than symbolic regression: Remember how in condensed matter physics or in many emergent phenomenon, robust/universal macroscopic behavior is usually only dependent on the relations of microscopic units, but the details of each unit are not so relevant. Moreover, structure regression can be made differentiable and can be easily visualized. This is not obvious at all, but in the following I will describe a machine learning method for structure regression that mets these desirable properties.

## Structure regression with BIMT (Brain-inspired Modular Training)

Before introducing our method, let’s see what our method can achieve. For symbolic formulas with structural properties, our trained fully-connected neural networks display interpretable modules. You can understand the structures immediately after seeing the connectivity graph for the network!

<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/blogs/bimt_example.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

We present three examples here. The first example is independence. Two outputs depend on non-overlapping sets of input variables. Our method is able to split the network into two independent parts. The second example is feature sharing. We’d expect that $$x_i^2 (i=1,2,3)$$ are important intermediate features. Our method is able to recover this intuition. The third example is compositionality. We’d expect to compute sum of squares first, and then take the square root. Our method automatically discovers this structure too. Note that all input and output variables are numeric (nothing symbolic). With our training method, neural networks self-reveal their structures, i.e., structure regression is achieved.

Now it’s time to describe our method BIMT (Brain-inspired modular training). For technical details please refer to the paper, or the podcast. Here we do a quick walk through the basic idea.


<div class="row mt-3">
    <div class="col-sm mt-3 mt-md-0">
        {% include figure.liquid loading="eager" path="assets/img/blogs/bimt.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Our goal is to encourage modules to emerge when training (non-modular) neural networks. Remember that human brains are remarkably modular. Is there a lesson we can learn from our brains? Our brains are modular because modular brains require less energy and react faster than non-modular brains, hence have survival advantages in evolution. Modular brains have more local connections than non-local connections. To introduce the notion of “locality” into artificial neural networks, we embed NNs into geometric spaces (e.g., 2D Euclidean space), assigning each neuron a spatial coordinate and defining lengths for neuron connections. We penalize longer connections more than shorter connections in training. Specifically, our penalty term is a simple modification to $$L_1$$ regularization: $$L_1$$ penalty is $$\lambda \lvert w\rvert$$, while our penalty is $$\lambda \ell \lvert w\rvert$$ where $$w$$, $$\ell$$ are the weight and the length of the neuron connection, respectively. Besides this differentiable penalty term added to the training objective to encourage locality, we also allow swaps of neurons, to avoid topological issues.

## Structure regression for science

There are two main paradigms for science: model-driven and data-driven. Model-driven approaches start from (symbolic) models, predicting what will happen via deduction. Data-driven approaches start from data, predicting what will happen via induction. Each paradigm has its pros and cons: Model-driven methods are interpretable, but require creativity of researchers. Data-driven methods are less intellectually challenging, but may not be interpretable. Usually these two paradigms are separately applied. Recently there have been efforts to integrate models into data-driven approches (e.g., PINNs), but not the other way around, i.e., use data-driven methods to inspire models development. Structure regression can exactly do that.

Putting interpretability aside, encouraging structures in neural networks can improve generalization. This is very important for cases where only very few data are accessible, when controlled experiments are either impossible or too expensive.

I’m very excited to apply structure regression to scientific problems! BIMT might be a reasonable starting point, but very likely not the ultimate answer, so there will be a lot of fun and fruitful things to do along the journey. If you have any applications in your fields, please don’t hesitate to email me! If you ask me which fields structure regression is most promising for, my prior would be a uniform distribution over all scientific domains! Said that, if you care about interpretability or scientific insights, maybe more well-defined fields (e.g., mathematics, physics) are better. If you want to do something more practical or useful, fields with some extent of messiness (e.g., chemistry, biology, social science, engineering) might be better. To be concrete, I think structure regression is quite promising for the following fields:

* Fluid mechanics
* Biophysics
* Astro & Plasma physics
* Quantum chemistry (DFT)
* Molecular dynamics
* Atmospheric science
* Biology (Protein folding)
* Economy
* …

The list can go on and on. Again, shoot me an email if you are working on a scientific problem and are interested in applying structure regression to it! I’m open to any form of collaboration. 🙂
