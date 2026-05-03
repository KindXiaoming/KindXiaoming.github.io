# ComfyResearch — Python export (Workflows → Blog). Matches Code tab cell order when a notebook exists.
# Dependencies: pip install torch matplotlib numpy
# Headless plots: MPLBACKEND=Agg (set below in __main__ when auto-run is appended).

# === Bigram low-rank dataset 0 (bigram_low_rank_dataset) ===
import torch
from torch.utils.data import DataLoader, TensorDataset

def spec_bigram_low_rank_dataset(
    vocab_size = 20,
    rank = 4,
    logit_scale = 1,
    corrupt_ratio = 0,
    corrupt_scale = 5,
    decay_type = "power_law",
    alpha = 0,
    train_size = 10000,
    test_size = 10000,
    seed = 6378,
    init_seed = 0,
):
    import numpy as np

    V = int(vocab_size)
    R = int(rank)
    scale = float(logit_scale)
    corrupt_ratio_f = float(corrupt_ratio)
    corrupt_scale_f = float(corrupt_scale)
    a = float(alpha)
    dt = str(decay_type).strip().lower().replace("-", "_")
    n_train = int(train_size)
    n_test = int(test_size)
    sample_rng = np.random.default_rng(int(seed))
    init_rng = np.random.default_rng(int(init_seed))
    if V < 2:
        raise ValueError("vocab_size must be >= 2")
    if R < 1 or R > V:
        raise ValueError("rank must be in [1, vocab_size]")
    if n_train < 1 or n_test < 0:
        raise ValueError("train_size must be >= 1 and test_size >= 0")
    if corrupt_ratio_f < 0.0 or corrupt_ratio_f > 1.0:
        raise ValueError("corrupt_ratio must be in [0, 1]")
    if corrupt_scale_f < 0.0:
        raise ValueError("corrupt_scale must be >= 0")
    if dt not in ("power_law", "exponential"):
        raise ValueError("decay_type must be 'power_law' or 'exponential'")

    A = init_rng.standard_normal((V, R)).astype(np.float64)
    B = init_rng.standard_normal((R, V)).astype(np.float64)
    if a == 0.0:
        lamb = np.ones((R,), dtype=np.float64)
    elif dt == "exponential":
        n = np.arange(1, R + 1, dtype=np.float64)
        lamb = np.exp(-a * n)
    else:
        n = np.arange(1, R + 1, dtype=np.float64)
        lamb = np.power(n, -a)
    logits = (A * lamb[None, :]) @ B
    logits = scale * logits / np.sqrt(float(max(R, 1)))

    row_max = logits.max(axis=1, keepdims=True)
    probs = np.exp(logits - row_max)
    probs = probs / probs.sum(axis=1, keepdims=True)

    pi = np.full((V,), 1.0 / float(V), dtype=np.float64)
    for _ in range(256):
        pi = pi @ probs
        s = pi.sum()
        if s <= 0 or not np.isfinite(s):
            raise ValueError("invalid stationary distribution from transition matrix")
        pi = pi / s

    def _sample(n):
        if n <= 0:
            return None, None
        x = sample_rng.choice(V, size=(n,), p=pi).astype(np.int64)
        y = np.empty((n,), dtype=np.int64)
        for i in range(n):
            p = probs[x[i]]
            if corrupt_ratio_f > 0.0 and sample_rng.random() < corrupt_ratio_f:
                noisy_logits = sample_rng.standard_normal((V,)).astype(np.float64) * corrupt_scale_f
                noisy_logits = noisy_logits - np.max(noisy_logits)
                noisy = np.exp(noisy_logits)
                noisy = noisy / np.sum(noisy)
                p = noisy
            y[i] = sample_rng.choice(V, p=p)
        x = x[:, None]
        return x, y

    x_train, y_train = _sample(n_train)
    x_test, y_test = _sample(n_test)
    return {"x_train": x_train, "y_train": y_train, "x_test": x_test, "y_test": y_test}

def fn_bigram_low_rank_dataset_loaders(batch_size: int = 64, device: str | torch.device = "cpu"):
    pack = spec_bigram_low_rank_dataset()
    x_train = pack["x_train"]
    if x_train is None:
        x_train_t = None
    else:
        x_train_t = torch.as_tensor(x_train, device=device, dtype=torch.int64)
    y_train = pack["y_train"]
    if y_train is None:
        y_train_t = None
    else:
        y_train_t = torch.as_tensor(y_train, device=device, dtype=torch.int64)
    x_test = pack["x_test"]
    if x_test is None:
        x_test_t = None
    else:
        x_test_t = torch.as_tensor(x_test, device=device, dtype=torch.int64)
    y_test = pack["y_test"]
    if y_test is None:
        y_test_t = None
    else:
        y_test_t = torch.as_tensor(y_test, device=device, dtype=torch.int64)
    train_ds = TensorDataset(x_train_t, y_train_t)
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    if x_test_t is not None and y_test_t is not None and int(x_test_t.shape[0]) > 0:
        test_ds = TensorDataset(x_test_t, y_test_t)
        test_loader = DataLoader(test_ds, batch_size=batch_size)
    else:
        test_loader = None
    return train_loader, test_loader


# ----------

# === Cross-entropy loss 0 (cross_entropy_loss) ===
import torch
import torch.nn as nn


def fn_cross_entropy_loss_criterion():
    base = nn.CrossEntropyLoss()

    class ScaledCE(nn.Module):
        def forward(self, logits: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
            return float(1) * base(logits, target)

    return ScaledCE()


# ----------

# === Observable Accuracy 0 (observable_accuracy) ===
# Executed as part of the wired graph (tensor pipeline, observables, or /api/train). See comfy_research/engine (trainer_run, activation_collect, tensor graph builders) for exact formulas.


def fn_observable_accuracy_describe():
    return "observable_accuracy"


# ----------

# === Trainer (trainer) ===
# Wired from graph: bigram_low_rank_dataset → mlp_token_model → adam_optimizer → cross_entropy_loss. Run the cells for those node types above (same kernel) so the `fn_*` helpers exist.
# Matches canvas /api/train for full-batch runs: set trainer `batchSize` to -1 on the node (or mirror the loop below).
# Mini-batch: trainer `batchSize` ≥ 1 samples random indices each step; `batch_size` here still selects DataLoader batch for the exported loaders.
# Logging follows trainer logFrequency (multiples + step 0).
import torch


def fn_trainer_run(batch_size: int = 64, device: str | torch.device = "cpu"):
    train_loader, test_loader = fn_bigram_low_rank_dataset_loaders(batch_size=batch_size, device=device)
    x_train, y_train = train_loader.dataset.tensors
    x_train = x_train.to(device)
    y_train = y_train.to(device)
    if test_loader is not None and len(test_loader.dataset) > 0:
        x_test, y_test = test_loader.dataset.tensors
        x_test = x_test.to(device)
        y_test = y_test.to(device)
    else:
        x_test = y_test = None

    model = fn_mlp_token_model_model().to(device)
    opt = fn_adam_optimizer_optimizer(model.parameters())
    loss_fn = fn_cross_entropy_loss_criterion()
    if hasattr(loss_fn, "to"):
        loss_fn = loss_fn.to(device)

    train_losses: list[float] = []
    test_losses: list[float] = []
    step_axis: list[int] = []

    def eval_test() -> float:
        if x_test is None or y_test is None:
            return float("nan")
        was_training = model.training
        model.eval()
        try:
            with torch.no_grad():
                return float(loss_fn(model(x_test), y_test).item())
        finally:
            if was_training:
                model.train()

    model.eval()
    with torch.no_grad():
        train_losses.append(float(loss_fn(model(x_train), y_train).item()))
    step_axis.append(0)
    test_losses.append(eval_test())

    model.train()
    trainer_batch = -1
    n_train = int(x_train.shape[0])
    for step in range(1000):
        opt.zero_grad(set_to_none=True)
        if trainer_batch > 0 and trainer_batch < n_train:
            g_step = torch.Generator(device=x_train.device)
            g_step.manual_seed((0x51ED7A77 + int(step)) & 0x7FFFFFFF)
            idx = torch.randperm(n_train, generator=g_step, device=x_train.device)[:trainer_batch]
            xb = x_train.index_select(0, idx)
            yb = y_train.index_select(0, idx)
        else:
            xb, yb = x_train, y_train
        pred = model(xb)
        loss = loss_fn(pred, yb)
        loss.backward()
        opt.step()
        done_steps = step + 1
        if done_steps % 10 == 0:
            train_losses.append(float(loss.item()))
            step_axis.append(done_steps)
            test_losses.append(eval_test())

    return {"steps": step_axis, "train_loss": train_losses, "test_loss": test_losses, "model": model}


def fn_trainer_plot(result: dict):
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("matplotlib not installed; skipping plot")
        return
    # ComfyResearch notebook: plt.show() is captured and shown under this cell (no extra window).
    steps_axis = result["steps"]
    plt.figure(figsize=(4.6, 2.6))
    plt.plot(steps_axis, result["train_loss"], label="train", color="#e74c3c")
    plt.plot(steps_axis, result["test_loss"], label="test", color="#3498db")
    plt.xlabel("step")
    plt.ylabel("loss")
    plt.title("Trainer")
    plt.gca().margins(x=0.05, y=0.05)
    plt.legend()
    plt.grid(True, alpha=0.25)
    plt.tight_layout()
    plt.show()


# ----------

# === Adam 0 (adam_optimizer) ===
import torch


def fn_adam_optimizer_optimizer(params, *, lr: float | None = None):
    return torch.optim.Adam(
        params,
        lr=float(0.001) if lr is None else float(lr),
        betas=(0.9, 0.999),
        eps=float(1e-8),
        weight_decay=float(0),
    )


# ----------

# === MLP_token model 0 (mlp_token_model) ===
# 
# ──────────────────────────────────────────────────────────────────────
# MLP token LM
# 
# Server twin: comfy_research/engine (MLP token bundles in trainer_run).
# 
# Idea: embed each of L=1 tokens into D=64, flatten to a single wide vector,
# run a deep MLP, then map back to logits over vocab V=20 (often last-token CE).
# 
import torch

class CrModel_mlp_token_model(torch.nn.Module):
    def __init__(
        self,
        vocab_size: int = 20,
        embed_dim: int = 64,
        tokens_per_input: int = 1,
        depth: int = 2,
        width: int = 64,
        activation: str = "relu",
        tie_weights: str = "yes",
        seed: int = 0,
    ):
        super().__init__()
        acts = {
            "relu": torch.nn.ReLU,
            "gelu": torch.nn.GELU,
            "tanh": torch.nn.Tanh,
            "sigmoid": torch.nn.Sigmoid,
            "leaky_relu": torch.nn.LeakyReLU,
            "silu": torch.nn.SiLU,
            "identity": torch.nn.Identity,
        }
        self.vocab_size = int(vocab_size)
        self.embed_dim = int(embed_dim)
        self.tokens_per_input = int(tokens_per_input)
        self.tie_weights = str(tie_weights).lower() not in ("no", "false", "0")
        self.seed = int(seed)
        d_flat = int(self.embed_dim) * int(self.tokens_per_input)
        self.embedding = torch.nn.Embedding(self.vocab_size, self.embed_dim)
        body_layers: list[torch.nn.Module] = []
        in_f = d_flat
        for _ in range(int(depth)):
            body_layers.append(torch.nn.Linear(in_f, int(width)))
            body_layers.append(acts.get(str(activation), torch.nn.ReLU)())
            in_f = int(width)
        body_layers.append(torch.nn.Linear(in_f, d_flat))
        self.body = torch.nn.Sequential(*body_layers)
        self.unembed = torch.nn.Linear(d_flat, self.vocab_size, bias=True)
        if self.tie_weights and self.unembed.weight.shape == self.embedding.weight.shape:
            self.embedding.weight = self.unembed.weight

    def forward(self, token_ids: torch.Tensor) -> torch.Tensor:
        x = token_ids.long()
        if x.ndim != 2:
            raise ValueError("MLPTokenModel expects shape [batch, tokens_per_input]")
        if x.shape[1] != self.tokens_per_input:
            raise ValueError("tokens_per_input must match input width")
        h = self.embedding(x).reshape(x.shape[0], -1)
        h = self.body(h)
        if self.tie_weights and self.unembed.weight.shape == self.embedding.weight.shape:
            return torch.nn.functional.linear(h, self.unembed.weight, self.unembed.bias)
        return self.unembed(h)


def fn_mlp_token_model_model() -> CrModel_mlp_token_model:
    import torch
    torch.manual_seed(0)
    return CrModel_mlp_token_model()


# ----------

# === Train vs test gap 0 (observable_train_test_gap) ===
# Executed as part of the wired graph (tensor pipeline, observables, or /api/train). See comfy_research/engine (trainer_run, activation_collect, tensor graph builders) for exact formulas.


def fn_observable_train_test_gap_describe():
    return "observable_train_test_gap"


if __name__ == "__main__":
    import os
    os.environ.setdefault("MPLBACKEND", "Agg")
    import matplotlib
    matplotlib.use(os.environ.get("MPLBACKEND", "Agg"))
    # Auto-added when you clicked Train on this canvas
    r = fn_trainer_run()
    fn_trainer_plot(r)
