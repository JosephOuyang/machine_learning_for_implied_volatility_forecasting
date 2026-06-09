# Neural Networks for Implied Volatility Forecasting
### Replication & Extension of Jiang, Lazar & Marra (2026)
*Carnegie Mellon University — Statistics & Machine Learning / Computational Finance*
*Supervised by Professor Chad Schafer · Student Researchers: Joseph Ouyang & Caleb Ouyang*

---

## Table of Contents
- [Overview](#overview)
- [Research Stages](#research-stages)
- [Architecture](#architecture)
- [Data Sources](#data-sources)
- [Environment](#environment)
- [Repository Structure](#repository-structure)
- [Citation](#citation)
- [AI Disclosure](#ai-disclosure)

---

## Overview
This project replicates and extends **Jiang, Lazar & Marra (2026)** — *"Neural Network-Based Implied Volatility Forecasting"*, Journal of Futures Markets 46:1137–1153 — using real S&P 100 American options data sourced from **OptionMetrics via WRDS**.
The core question: *Can neural networks and similarly complex models feasibly fit the implied volatility surface?*

---

## Research Stages

### Stage 1 — Synthetic Benchmarking *(Weeks 1–7)*
> *Reference: Della Corte, Van Mieghem, Papapantoleon & Papazoglou-Henig (2025)*
- Generated **1 million synthetic Black-Scholes** European call contracts via Latin Hypercube Sampling
- Benchmarked **12 MLP architectures** on accuracy (MSE) and computational efficiency

### Stage 2 — Real Data Pipeline *(Weeks 8–13)*
- Built a production-grade **OptionMetrics data pipeline**: OEX American + XEO European options, Jan 2016 – Aug 2023
- Implemented Jiang's exact filters: moneyness ∈ [0.80, 1.60], τ ∈ [20, 1094] days, no volume filter
- Calibrated **Black-Scholes** (closed-form) and **Heston** (FFT via characteristic function) models to market IVs daily
- Constructed transformed IV labels (intrinsic value subtraction + log-transform) to stabilize gradients
- Rate inputs aligned with IvyDB methodology: `zerocd` for r, `idxdvd` for q

### Stage 3 — Jiang Replication *(Weeks 14–15)*
Replicated all five Jiang frameworks on OEX American options using **AM-to-AM, R-splitting**:

| Framework | Description |
|---|---|
| BS+NN Independent | Black-Scholes residual, independently trained |
| BS+NN Sequential | Black-Scholes residual, sequentially trained |
| Heston+NN Independent | Heston residual, independently trained |
| Heston+NN Sequential | Heston residual, sequentially trained |
| Pure NN Sequential | No model — raw IV forecasting |

### Stage 4 — HestonFeature Extension *(Week 16)*
Novel extension: instead of treating Heston as a **residual corrector**, we feed the Heston-implied volatility **directly as a feature** to a sequentially trained NN. The hypothesis is that Heston σ captures nonlinear market structure that a residual formulation may not fully exploit.

---

## Architecture
**JiangNN** — a compact feedforward network per Jiang et al. (2026) Table 3.

| | Weeks 14–15 | Week 16 Extension |
|---|---|---|
| **Inputs** | moneyness, τ | moneyness, τ, σ_Heston |
| **Hidden layers** | 32 → 16 → 8 | 32 → 16 → 8 |
| **Activation** | ReLU | ReLU |
| **Output** | IV label | IV label |

Training uses **Adam** (ε = 10⁻⁷, lr = 10⁻³), 200 epochs, batch size 64, with per-session checkpointing and resume support.

---

## Data Sources

| Source | Table | Used For |
|---|---|---|
| OptionMetrics IvyDB via WRDS | `opprcd{YYYY}` | Option quotes |
| OptionMetrics | `zerocd` | Risk-free rate r |
| OptionMetrics | `idxdvd` | Dividend yield q |
| OptionMetrics | `secprd` | Underlying close S |

> **Note:** OptionMetrics data requires institutional WRDS access and is not included in this repository.

---

## Environment
Developed and trained on **Google Colab** with Google Drive persistence. Core dependencies:

| Package | Purpose |
|---|---|
| `torch` | Neural network training |
| `scipy` | Latin Hypercube Sampling, Heston FFT optimization |
| `pandas` / `numpy` | Data pipeline and feature engineering |
| `matplotlib` | Visualizations |
| `wrds` | WRDS Python connector (requires credentials) |

---

## Repository Structure

```
neural-networks-iv-forecasting/
├── figures/        # plots and visualizations
├── notebooks/      # Colab notebooks for each research stage
├── reports/        # writeups and progress reports
├── sources/        # reference papers and supporting literature
├── .gitignore
├── LICENSE
└── README.md
```

---

## Citation
Jiang, G. J., Lazar, E., & Marra, G. (2026). Neural network-based implied volatility forecasting. *Journal of Futures Markets*, 46, 1137–1153. https://doi.org/10.1002/fut.70101

---

## AI Disclosure
Generative AI assistance (Claude, Anthropic) was used in coding throughout this project. All research design, methodology, analysis, and written documentation are the work of Joseph Ouyang and Caleb Ouyang.

---

*CMU Statistics & Data Science · MSCF · Spring/Summer 2026*
---

## Architecture

**JiangNN** — a compact feedforward network per Jiang et al. (2026) Table 3.

| | Weeks 14–15 | Week 16 Extension |
|---|---|---|
| **Inputs** | moneyness, τ | moneyness, τ, σ_Heston |
| **Hidden layers** | 32 → 16 → 8 | 32 → 16 → 8 |
| **Activation** | ReLU | ReLU |
| **Output** | IV label | IV label |

Training uses **Adam** (ε = 10⁻⁷, lr = 10⁻³), 200 epochs, batch size 64, with per-session checkpointing and resume support.

---

## Data Sources

| Source | Table | Used For |
|---|---|---|
| OptionMetrics IvyDB via WRDS | `opprcd{YYYY}` | Option quotes |
| OptionMetrics | `zerocd` | Risk-free rate r |
| OptionMetrics | `idxdvd` | Dividend yield q |
| OptionMetrics | `secprd` | Underlying close S |

> **Note:** OptionMetrics data requires institutional WRDS access and is not included in this repository.

---

## Environment

Developed and trained on **Google Colab** with Google Drive persistence. Core dependencies:

| Package | Purpose |
|---|---|
| `torch` | Neural network training |
| `scipy` | Latin Hypercube Sampling, Heston FFT optimization |
| `pandas` / `numpy` | Data pipeline and feature engineering |
| `matplotlib` | Visualizations |
| `wrds` | WRDS Python connector (requires credentials) |

---

## Citation

Jiang, G. J., Lazar, E., & Marra, G. (2026). Neural network-based implied volatility forecasting. *Journal of Futures Markets*, 46, 1137–1153. https://doi.org/10.1002/fut.70101

---

## AI Disclosure

Generative AI assistance (Claude, Anthropic) was used in coding throughout this project. All research design, methodology, analysis, and written documentation are the work of Joseph Ouyang and Caleb Ouyang.

---

*CMU Statistics & Data Science · MSCF · Spring/Summer 2026*
