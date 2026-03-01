---
layout: post
title: Research agent 1 -- Reproducing 2026-01-01 blog (physics of feature learning)
date: 2026-02-28
description: 
tags: [Physics-of-AI, Research-agent]
categories: AI
---

**Author: Ziming Liu, Research Agent**

---

## Motivation (Human generated)

In my last [blog](/blog/2026/research-agent/), I talked about how research agents should prioritize structure (knowledge graphs) over readability (papers), at least in the early stages of development.

A reasonable starting point is to build a system/language that makes our previous blogposts more structured. Below is the first blogpost generated with the system, aiming to reproduce basic results in the [physics of feature learning 1](/blog/2026/feature-learning-1/). Disclaimer: Right now the readability is low, because I prioritize structure (expressed in some abstract language) over readability (expressed in natural language). 

---

## Blogpost (Agent generated)


Knowledge graph

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/ra-feature-learning-1/recording_2026-03-01T02-52-32_graph.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Clicked Create new experiment in chart.

Created experiment 0.

<table class="create-experiment-config-table" style="border-collapse:collapse;font-size:0.9rem;width:100%;margin-top:0.5rem;"><thead><tr><th style="border:1px solid #444;padding:0.5rem 0.75rem;text-align:left;">Config</th><th style="border:1px solid #444;padding:0.5rem 0.75rem;text-align:left;">Value</th></tr></thead><tbody><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Model</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">MLP 10, 100, 100, 1, relu</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Data</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">nonlinear, train=500, test=200, $\sum_{i=1}^{10} \sin^2(10 x_i)$</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Optimizer</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">adam, lr=0.001, steps=2000</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Loss</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">mse</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Observables</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">train_loss, test_loss, weight_l2_norm, hidden_activations</td></tr></tbody></table>

Selected exp_0.

Ran "current" for exp_0.

Selected exp_0.

Viewed results for exp_0 (metrics: train_losses, test_losses, l2_norms, hidden_activations).

Clicked hidden_activations in visualization.

Clicked bigger in chart.

Set Choose activation to visualize to Layer 1 pre (500 × 100).

Set Choose method to Neuron stats.

Clicked Add Stats in chart.

Set dropdown to active_rate.

Added neuron stat for hidden_activations: dim , active_rate.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/ra-feature-learning-1/recording_2026-03-01T02-52-32_img_0.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Clicked Add Stats in chart.

Added neuron stat for hidden_activations: dim , active_rate.

Set Existing variable to active rate.

Added DIY statistic: nonlinear rate.

Set dropdown to custom:custom-1772333499747.

Submit observable: nonlinear rate.

<pre style="font-family:ui-monospace,monospace;font-size:0.875rem;line-height:1.5;margin:0.5rem 0;padding:1rem 1.25rem;background:#1a2332;color:#d0d0d0;border:1px solid #444;border-radius:6px;overflow-x:auto;white-space:pre;"><code class="language-python">def compute_nonlinear_rate(tensor, dim, keepdim=False):
    t = tensor.float()
    return ((t &gt; 0)*(t &lt; 1)).float().mean(dim=dim, keepdim=keepdim)</code></pre>

Clicked create new experiment in operation.

Clicked Observables in chart.

Set dropdown to on.

Created experiment 1.

<table class="create-experiment-config-table" style="border-collapse:collapse;font-size:0.9rem;width:100%;margin-top:0.5rem;"><thead><tr><th style="border:1px solid #444;padding:0.5rem 0.75rem;text-align:left;">Config</th><th style="border:1px solid #444;padding:0.5rem 0.75rem;text-align:left;">Value</th></tr></thead><tbody><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Model</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">MLP 10, 100, 100, 1, relu</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Data</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">nonlinear, train=500, test=200, $\sum_{i=1}^{10} \sin^2(10 x_i)$</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Optimizer</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">adam, lr=0.001, steps=2000</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Loss</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">mse</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Observables</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">train_loss, test_loss, weight_l2_norm, hidden_activations, nonlinear_rate</td></tr></tbody></table>

Selected exp_0, exp_1.

Viewed results for exp_0 (metrics: train_losses, test_losses, l2_norms, hidden_activations).

Selected exp_1.

Ran "current" for exp_1.

Selected exp_1.

Viewed results for exp_1 (metrics: train_losses, test_losses, l2_norms, hidden_activations, nonlinear_rate).

Clicked nonlinear_rate in visualization.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/ra-feature-learning-1/recording_2026-03-01T02-52-32_img_1.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>


Clicked bigger in chart.

Set Choose layer to Layer 1 pre.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/ra-feature-learning-1/recording_2026-03-01T02-52-32_img_2.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Viewed results for exp_1 (metrics: train_losses, test_losses, l2_norms, hidden_activations, nonlinear_rate).

Zoomed chart nonlinear_rate to given range.

<div class="row mt-3">
    <div class="mt-3 mt-md-0" style="width: 60%; margin: 0 auto;">
        {% include figure.liquid path="assets/img/blogs/ra-feature-learning-1/recording_2026-03-01T02-52-32_img_3.png" class="img-fluid rounded z-depth-1" %}
    </div>
</div>

Fit curve to 1 — nonlinear_rate in nonlinear_rate.

<table class="curve-fit-table" style="border-collapse:collapse;font-size:0.9rem;width:100%;margin-top:0.5rem;"><thead><tr><th style="border:1px solid #444;padding:0.5rem 0.75rem;text-align:left;">Type</th><th style="border:1px solid #444;padding:0.5rem 0.75rem;text-align:left;">R²</th><th style="border:1px solid #444;padding:0.5rem 0.75rem;text-align:left;">Equation</th><th style="border:1px solid #444;padding:0.5rem 0.75rem;text-align:left;">Coefficients</th></tr></thead><tbody><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Sigmoid</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">0.9964</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">$$f(t) = \frac{c_1}{1+e^{c_2 t + c_3}} + c_4$$</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">-9.31e-1, -1.53e-1, 2.61e+0, 1.06e+0</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Exponential</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">0.9635</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">$$f(t) = c_1 \cdot e^{-c_2 t} + c_3$$</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">1.06e+0, 5.55e-2, 1.11e-1</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Power</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">0.8447</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">$$f(t) = c_1 \cdot (t+1)^{c_2} + c_3$$</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">2.48e+0, -1.48e-1, -1.14e+0</td></tr><tr><td style="border:1px solid #444;padding:0.5rem 0.75rem;">Log-power</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">0.8324</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">$$f(t) = c_1 \cdot \log(t+1)^{c_2} + c_3$$</td><td style="border:1px solid #444;padding:0.5rem 0.75rem;">-2.95e-1, 8.79e-1, 1.25e+0</td></tr></tbody></table>

Clicked Hide in chart.

---


## Citation

If you find this article useful, please cite it as:

**BibTeX:**

```bibtex
@article{liu2026research-agent-1,
  title={Research agent 1},
  author={Liu, Ziming},
  year={2026},
  month={February},
  url={https://KindXiaoming.github.io/blog/2026/research-agent-1/}
}
```



