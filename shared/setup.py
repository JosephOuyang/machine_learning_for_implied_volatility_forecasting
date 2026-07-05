"""
shared/setup.py
================
Universal environment setup for the BS-ANN / OptionMetrics research notebooks.

This consolidates what used to be the per-notebook "Environment Setup" cells
(Drive mount, installs, imports, global seeds, run-logger helpers) into one
importable module. Each notebook's first cell becomes a short bootstrap that
clones/pulls this repo and runs `from shared.setup import *`.

Everything that was previously copy-pasted into every notebook now lives here,
so it is edited in exactly one place.

Exports (via `from shared.setup import *`):
    np, plt, norm, qmc, torch, nn, F, optim,
    StepLR, LinearLR, OneCycleLR, LambdaLR,
    json, datetime, subprocess, os,
    SEED, start_run, save_json, save_notes,
    DRIVE_PROJECT_DIR, mount_drive
"""

import os
import json
import datetime
import subprocess

# ----------------------------------------------------------------------
# 0.1 — Drive mount + working directory
# ----------------------------------------------------------------------
# Default project directory on Drive. Override by setting the environment
# variable OPR_PROJECT_DIR before import, or by passing a path to
# mount_drive(project_dir=...). This is the one location-specific line from
# the original notebooks; keeping it configurable means a teammate whose
# Drive mounts the shared folder elsewhere can point at their own path.
DRIVE_PROJECT_DIR = os.environ.get(
    "OPR_PROJECT_DIR",
    "/content/drive/MyDrive/Options Pricing Research (S26)/"
    "machine_learning_for_options_pricing_and_implied_volatility",
)


def mount_drive(project_dir: str = None):
    """Mount Google Drive (no-op off Colab) and chdir into the project dir.

    Safe to call repeatedly. Returns the working directory actually set.
    """
    target = project_dir or DRIVE_PROJECT_DIR
    try:
        from google.colab import drive  # type: ignore
        drive.mount("/content/drive")
    except Exception:
        # Not on Colab (e.g. local / cluster) — skip the mount, keep cwd.
        print("google.colab not available; skipping Drive mount.")
        return os.getcwd()
    if os.path.isdir(target):
        os.chdir(target)
    else:
        print(f"WARNING: project dir not found, staying in {os.getcwd()}:\n  {target}")
    print("cwd =", os.getcwd())
    return os.getcwd()


# ----------------------------------------------------------------------
# 0.2 — Installs (QMC / Latin Hypercube via scipy)
# ----------------------------------------------------------------------
try:
    from scipy.stats import qmc  # noqa: F401
    import scipy
    print("scipy version:", scipy.__version__)
    print("qmc available")
except Exception as e:  # pragma: no cover
    print("qmc not available, upgrading scipy... error was:", repr(e))
    subprocess.run(["pip", "-q", "install", "--upgrade", "scipy"], check=False)
    import scipy
    from scipy.stats import qmc  # noqa: F401
    print("scipy version after upgrade:", scipy.__version__)
    print("qmc available")


# ----------------------------------------------------------------------
# 0.3 — Imports
# ----------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import qmc  # noqa: F811  (re-export after possible upgrade)

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.optim.lr_scheduler import StepLR, LinearLR, OneCycleLR, LambdaLR


# ----------------------------------------------------------------------
# 0.4 — Reproducibility (global seeds)
# ----------------------------------------------------------------------
SEED = 42
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
print("SEED =", SEED)


# ----------------------------------------------------------------------
# 0.5 — Run logger (saves run metadata/figures under runs/)
# ----------------------------------------------------------------------
def _git_hash():
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    except Exception:
        return "no-git"


def start_run(task: str, base_dir: str = "runs"):
    """Create a timestamped run folder (with figures/ subdir) and write meta.json."""
    run_id = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = os.path.join(base_dir, task, run_id)
    fig_dir = os.path.join(run_dir, "figures")
    os.makedirs(fig_dir, exist_ok=True)
    meta = {
        "task": task,
        "run_id": run_id,
        "created_at": datetime.datetime.now().isoformat(),
        "git_commit": _git_hash(),
        "seed": SEED,
    }
    with open(os.path.join(run_dir, "meta.json"), "w") as f:
        json.dump(meta, f, indent=2)
    return run_dir, fig_dir


def save_json(run_dir: str, name: str, obj: dict):
    with open(os.path.join(run_dir, f"{name}.json"), "w") as f:
        json.dump(obj, f, indent=2)


def save_notes(run_dir: str, text: str):
    with open(os.path.join(run_dir, "notes.md"), "w") as f:
        f.write(text.strip() + "\n")


def load_run_results(task: str, run_id: str = None, base_dir: str = "runs"):
    """Load JSON files from a run folder.

    If run_id is None, picks the most recent run for the given task.
    Returns (run_dir, data) where data is a dict keyed by JSON filename stem.
    """
    task_dir = os.path.join(base_dir, task)
    if run_id is None:
        runs = sorted(
            [d for d in os.listdir(task_dir) if os.path.isdir(os.path.join(task_dir, d))]
        )
        if not runs:
            raise FileNotFoundError(f"No runs found for task '{task}' in {task_dir}")
        run_id = runs[-1]
    run_dir = os.path.join(task_dir, run_id)
    data = {}
    for fname in os.listdir(run_dir):
        if fname.endswith(".json"):
            with open(os.path.join(run_dir, fname)) as f:
                data[fname[:-5]] = json.load(f)
    return run_dir, data


# Mount on import so notebooks get the original behavior with a single import.
mount_drive()
print("shared.setup ready")

__all__ = [
    "np", "plt", "norm", "qmc", "torch", "nn", "F", "optim",
    "StepLR", "LinearLR", "OneCycleLR", "LambdaLR",
    "json", "datetime", "subprocess", "os",
    "SEED", "start_run", "save_json", "save_notes", "load_run_results",
    "DRIVE_PROJECT_DIR", "mount_drive",
]
