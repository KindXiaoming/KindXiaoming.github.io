# ComfyResearch — Python export (Workflows → Blog). Matches Code tab cell order when a notebook exists.
# Dependencies: pip install torch matplotlib numpy
# Headless plots: MPLBACKEND=Agg (set below in __main__ when auto-run is appended).

# === Memorization A dataset 0 (memorization_a_dataset) ===
# Runnable toy classification data (labels are independent of x, sampled from a class prior).
import torch
from torch.utils.data import DataLoader, TensorDataset


def fn_memorization_a_dataset_loaders(batch_size: int = 64, device: str | torch.device = "cpu"):
    g = torch.Generator(device="cpu")
    g.manual_seed(9266)
    d_in = 9
    classes = 17
    n_train = 100
    n_test = 80
    out_dist = "uniform_class_probs"
    alpha = float(1)

    def sample_x(n: int) -> torch.Tensor:
        if n <= 0:
            return torch.zeros(0, d_in)
        if "standard_normal" == "uniform_neg1_1":
            return torch.empty(n, d_in, generator=g, device="cpu").uniform_(-1.0, 1.0).to(device)
        if "standard_normal" == "uniform_0_1":
            return torch.empty(n, d_in, generator=g, device="cpu").uniform_(0.0, 1.0).to(device)
        return torch.randn(n, d_in, generator=g, device=device)

    def class_probs() -> torch.Tensor:
        idx = torch.arange(1, classes + 1, dtype=torch.float32, device=device)
        if out_dist == "power_law_class_probs":
            p = idx.pow(-max(alpha, 1e-8))
        elif out_dist == "exponential_class_probs":
            p = torch.exp(-max(alpha, 1e-8) * idx)
        else:
            p = torch.ones(classes, dtype=torch.float32, device=device)
        return p / p.sum()

    x_train = sample_x(n_train)
    probs = class_probs()
    y_train = torch.multinomial(probs, n_train, replacement=True, generator=g).to(torch.long)
    x_test = sample_x(n_test) if n_test > 0 else torch.zeros(0, d_in, device=device)
    y_test = (
        torch.multinomial(probs, n_test, replacement=True, generator=g).to(torch.long)
        if n_test > 0
        else torch.zeros(0, dtype=torch.long, device=device)
    )

    train_ds = TensorDataset(x_train, y_train)
    test_ds = TensorDataset(x_test, y_test) if n_test > 0 else None
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_ds, batch_size=batch_size) if test_ds else None
    return train_loader, test_loader


# ----------

# === MLP 0 (mlp_model) ===
# 
# ──────────────────────────────────────────────────────────────────────
# Vector MLP regressor / classifier
# 
# Server twin: comfy_research/engine (mlp stack for tabular / vector datasets).
# 
# Maps x ∈ R^9 → y ∈ R^17 through depth=2 hidden layers (see width in class __init__).
# 
import torch

class CrModel_mlp_model(torch.nn.Module):
    def __init__(
        self,
        input_dim: int = 9,
        output_dim: int = 17,
        depth: int = 2,
        width: int = 100,
        activation: str = "relu",
        seed: int = 1207,
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
        layers = []
        in_f = int(input_dim)
        for _ in range(int(depth)):
            layers.append(torch.nn.Linear(in_f, int(width)))
            layers.append(acts.get(str(activation), torch.nn.ReLU)())
            in_f = int(width)
        layers.append(torch.nn.Linear(in_f, int(output_dim)))
        self.net = torch.nn.Sequential(*layers)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


def fn_mlp_model_model() -> CrModel_mlp_model:
    import torch
    torch.manual_seed(1207)
    return CrModel_mlp_model()


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
# Wired from graph: memorization_a_dataset → mlp_model → adam_optimizer → cross_entropy_loss. Run the cells for those node types above (same kernel) so the `fn_*` helpers exist.
# Matches canvas /api/train for full-batch runs: set trainer `batchSize` to -1 on the node (or mirror the loop below).
# Mini-batch: trainer `batchSize` ≥ 1 samples random indices each step; `batch_size` here still selects DataLoader batch for the exported loaders.
# Logging follows trainer logFrequency (multiples + step 0).
import torch


def fn_trainer_run(batch_size: int = 64, device: str | torch.device = "cpu"):
    train_loader, test_loader = fn_memorization_a_dataset_loaders(batch_size=batch_size, device=device)
    x_train, y_train = train_loader.dataset.tensors
    x_train = x_train.to(device)
    y_train = y_train.to(device)
    if test_loader is not None and len(test_loader.dataset) > 0:
        x_test, y_test = test_loader.dataset.tensors
        x_test = x_test.to(device)
        y_test = y_test.to(device)
    else:
        x_test = y_test = None

    model = fn_mlp_model_model().to(device)
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

# === Weight L2 0 (observable_weight_l2) ===
# Matches ComfyResearch /api train logging: √(Σ w²) over all parameters.
import torch


def fn_observable_weight_l2_weight_l2_norm(module: torch.nn.Module) -> float:
    s = 0.0
    for p in module.parameters():
        s += float(p.detach().float().pow(2).sum().item())
    return s**0.5


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

# === Tensor slicing 0 (tensor_slicing) ===
# Executed as part of the wired graph (tensor pipeline, observables, or /api/train). See comfy_research/engine (trainer_run, activation_collect, tensor graph builders) for exact formulas.


def fn_tensor_slicing_1_describe():
    return "tensor_slicing"


# ----------

# === Tensor slicing 1 (tensor_slicing) ===
# Executed as part of the wired graph (tensor pipeline, observables, or /api/train). See comfy_research/engine (trainer_run, activation_collect, tensor graph builders) for exact formulas.


def fn_tensor_slicing_2_describe():
    return "tensor_slicing"


# ----------

# === Basic calculator (basic_calculator) ===
# Executed as part of the wired graph (tensor pipeline, observables, or /api/train). See comfy_research/engine (trainer_run, activation_collect, tensor graph builders) for exact formulas.


def fn_basic_calculator_2_describe():
    return "basic_calculator"


# ----------

# === Basic calculator (basic_calculator) ===
# Executed as part of the wired graph (tensor pipeline, observables, or /api/train). See comfy_research/engine (trainer_run, activation_collect, tensor graph builders) for exact formulas.


def fn_basic_calculator_1_describe():
    return "basic_calculator"


if __name__ == "__main__":
    import os
    os.environ.setdefault("MPLBACKEND", "Agg")
    import matplotlib
    matplotlib.use(os.environ.get("MPLBACKEND", "Agg"))
    # Auto-added when you clicked Train on this canvas
    r = fn_trainer_run()
    fn_trainer_plot(r)
