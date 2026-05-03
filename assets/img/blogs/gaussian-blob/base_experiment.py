# ComfyResearch — Python export (Workflows → Blog). Matches Code tab cell order when a notebook exists.
# Dependencies: pip install torch matplotlib numpy
# Headless plots: MPLBACKEND=Agg (set below in __main__ when auto-run is appended).

# === MNIST — how to use (comment) ===
import torch


def fn_comment_stub():
    """No specialized exporter for this node type yet — implement or copy from the graph UI."""
    raise RuntimeError("Replace this stub for comment.")


# ----------

# === ResNet-18 (MNIST) (resnet_model) ===
import torch
from comfy_research.engine.vision_models import build_resnet_from_md

def model_resnet_model(num_classes: int, in_channels: int = 1):
    md = {
        "variant": "self_defined",
        "seed": 3,
        "baseChannels": 8,
        "blocksStage1": 2,
        "blocksStage2": 2,
        "blocksStage3": 2,
        "blocksStage4": 2,
        "kernelSize": 3,
    }
    torch.manual_seed(int(md["seed"]))
    return build_resnet_from_md(md, in_channels=in_channels, num_classes=num_classes)


# ----------

# === Cross-entropy (10-way) (cross_entropy_loss) ===
import torch
import torch.nn as nn


def fn_cross_entropy_loss_criterion():
    base = nn.CrossEntropyLoss()

    class ScaledCE(nn.Module):
        def forward(self, logits: torch.Tensor, target: torch.Tensor) -> torch.Tensor:
            return float(1) * base(logits, target)

    return ScaledCE()


# ----------

# === Adam (adam_optimizer) ===
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

# === Trainer (trainer) ===
# Standalone fallback (graph not wired when this cell was generated, or unsupported node mix).
# Connect Linear dataset → MLP → Adam/SGD/Muon → MSE/CE/KAN-reg → Trainer in the UI, then remove and re-add the Trainer node to get an auto-wired cell.
import torch
import torch.nn as nn


def fn_trainer_run(
    *,
    device: str | torch.device = "cpu",
    training_steps: int = 100,
    log_every: int = 1,
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

# === Observable Accuracy 0 (observable_accuracy) ===
import torch


def fn_observable_accuracy_stub():
    """No specialized exporter for this node type yet — implement or copy from the graph UI."""
    raise RuntimeError("Replace this stub for observable_accuracy.")


# ----------

# === Gaussian blob dataset 0 (gaussian_blob_dataset) ===
# Vision dataset: use the node's **View/edit code** cell (or `build_vision_numpy_arrays` in `comfy_research.engine.vision_datasets_runtime`) with `NodeKind("gaussian_blob_dataset")`.


def fn_gaussian_blob_dataset_loaders(batch_size: int = 64, device: str | torch.device = "cpu"):
    raise RuntimeError("Copy the generated spec from the canvas node, or import build_vision_numpy_arrays from comfy_research.engine.vision_datasets_runtime.")


if __name__ == "__main__":
    import os
    os.environ.setdefault("MPLBACKEND", "Agg")
    import matplotlib
    matplotlib.use(os.environ.get("MPLBACKEND", "Agg"))
    # Auto-added when you clicked Train on this canvas
    r = fn_trainer_run()
    fn_trainer_plot(r)
