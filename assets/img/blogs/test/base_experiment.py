# ComfyResearch — Python export (Workflows → Blog). Matches Code tab cell order when a notebook exists.
# Dependencies: pip install torch matplotlib numpy
# Headless plots: MPLBACKEND=Agg (set below in __main__ when auto-run is appended).

# === Trainer (trainer) ===
# Standalone fallback (graph not wired when this cell was generated, or unsupported node mix).
# Connect Linear dataset → MLP → Adam/SGD/Muon → MSE/CE/KAN-reg → Trainer in the UI, then remove and re-add the Trainer node to get an auto-wired cell.
import torch
import torch.nn as nn


def fn_trainer_run(
    *,
    device: str | torch.device = "cpu",
    training_steps: int = 72,
    log_every: int = 6,
    batch_size: int = 64,
):
    g = torch.Generator(device="cpu").manual_seed(0)
    x_train = torch.randn(800, 10, generator=g, device=device)
    y_train = torch.randn(800, 1, generator=g, device=device)
    x_test = torch.randn(200, 10, generator=g, device=device)
    y_test = torch.randn(200, 1, generator=g, device=device)

    model = nn.Sequential(nn.Linear(10, 64), nn.ReLU(), nn.Linear(64, 1)).to(device)
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.MSELoss()

    train_losses: list[float] = []
    test_losses: list[float] = []
    steps_out: list[int] = []

    def eval_test() -> float:
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
    steps_out.append(0)
    test_losses.append(eval_test())

    model.train()
    for step in range(training_steps):
        opt.zero_grad(set_to_none=True)
        pred = model(x_train)
        loss = loss_fn(pred, y_train)
        loss.backward()
        opt.step()
        done_steps = step + 1
        if done_steps % log_every == 0:
            train_losses.append(float(loss.item()))
            steps_out.append(done_steps)
            test_losses.append(eval_test())

    return {"steps": steps_out, "train_loss": train_losses, "test_loss": test_losses, "model": model}


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

# === Modular addition dataset 0 (modular_addition_dataset) ===
# All ordered pairs (i, j) with i, j in {{0,…,p-1}}; target y = (i + j) mod p. Total p^2 samples; shuffle then split.
# Matches ComfyResearch /api/train: train rows are the first n_train after permutation; test is the remaining p^2 - n_train rows.
import numpy as np
import torch
from torch.utils.data import DataLoader, TensorDataset


def fn_modular_addition_dataset_loaders(batch_size: int = 64, device: str | torch.device = "cpu"):
    p = int(84)
    frac = float(0.3)
    seed = int(8674)
    if p < 2:
        raise ValueError("modulus must be >= 2")
    if not (0.0 < frac < 1.0):
        raise ValueError("train_fraction must be in (0, 1)")

    rng = np.random.default_rng(seed)
    a, b = np.meshgrid(np.arange(p, dtype=np.int64), np.arange(p, dtype=np.int64), indexing="ij")
    x_all = np.stack([a.reshape(-1), b.reshape(-1)], axis=1)
    y_all = ((x_all[:, 0] + x_all[:, 1]) % p).astype(np.int64)
    perm = rng.permutation(x_all.shape[0])
    x_all = x_all[perm]
    y_all = y_all[perm]
    n_train = int(round(frac * x_all.shape[0]))
    n_train = min(max(n_train, 1), x_all.shape[0])
    n_test = int(x_all.shape[0] - n_train)
    x_train = x_all[:n_train]
    y_train = y_all[:n_train]
    if n_test <= 0:
        x_test = np.zeros((0, 2), dtype=np.int64)
        y_test = np.zeros((0,), dtype=np.int64)
    else:
        x_test = x_all[n_train:]
        y_test = y_all[n_train:]

    x_train_t = torch.as_tensor(x_train, dtype=torch.long, device=device)
    y_train_t = torch.as_tensor(y_train, dtype=torch.long, device=device)
    train_ds = TensorDataset(x_train_t, y_train_t)
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)

    if n_test <= 0:
        test_loader = None
    else:
        x_test_t = torch.as_tensor(x_test, dtype=torch.long, device=device)
        y_test_t = torch.as_tensor(y_test, dtype=torch.long, device=device)
        test_ds = TensorDataset(x_test_t, y_test_t)
        test_loader = DataLoader(test_ds, batch_size=batch_size)

    return train_loader, test_loader


# ----------

# === MLP_token model 0 (mlp_token_model) ===
# 
# ──────────────────────────────────────────────────────────────────────
# MLP token LM
# 
# Server twin: comfy_research/engine (MLP token bundles in trainer_run).
# 
# Idea: embed each of L=2 tokens into D=32, flatten to a single wide vector,
# run a deep MLP, then map back to logits over vocab V=84 (often last-token CE).
# 
import torch

class CrModel_mlp_token_model(torch.nn.Module):
    def __init__(
        self,
        vocab_size: int = 84,
        embed_dim: int = 32,
        tokens_per_input: int = 2,
        depth: int = 2,
        width: int = 64,
        activation: str = "relu",
        tie_weights: str = "yes",
        seed: int = 9196,
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
    torch.manual_seed(9196)
    return CrModel_mlp_token_model()


# ----------

# === Muon 0 (muon_optimizer) ===
# Muon is not in core PyTorch; this cell uses SGD + momentum as a practical stand-in for a standalone notebook.
import torch


def fn_muon_optimizer_optimizer(params, *, lr: float | None = None):
    return torch.optim.SGD(params, lr=float(0.003) if lr is None else float(lr), momentum=float(0.95))


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
import torch


def fn_observable_accuracy_stub():
    """No specialized exporter for this node type yet — implement or copy from the graph UI."""
    raise RuntimeError("Replace this stub for observable_accuracy.")


if __name__ == "__main__":
    import os
    os.environ.setdefault("MPLBACKEND", "Agg")
    import matplotlib
    matplotlib.use(os.environ.get("MPLBACKEND", "Agg"))
    # Auto-added when you clicked Train on this canvas
    r = fn_trainer_run()
    fn_trainer_plot(r)
