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
This project replicates and extends **Jiang, Lazar & Marra (2026)** — *"Improving Implied Volatility Forecasts for American Options Using Neural Networks"*, Journal of Futures Markets 46:1137–1153 — using S&P 100 European (XEO) and American (OEX) options from **OptionMetrics via WRDS**.
The core idea: model the gap between market-implied and model-implied (Black-Scholes / Heston) volatilities with a neural network, and compare against a pure neural network that uses no pricing model.

---

## Research Stages

### Stage 1 — Synthetic Black-Scholes Benchmarking *(Weeks 2–7)*
> *Reference: Della Corte, Van Mieghem, Papapantoleon & Papazoglou-Henig (2025)*
- Implemented the closed-form Black-Scholes scaled-price formula (price `V/K` as a function of moneyness `m`, `τ`, `r`, `σ`) and verified it against the absolute-price form (Week 2)
- Generated **1,000,000 synthetic** scaled-price samples via Latin Hypercube Sampling over `(m, τ, r, σ)`, with no-arbitrage validity checks (Week 3)
- Benchmarked the paper's **12-architecture grid** (2–3 layers × {50, 100, 150, 200, 250, 500} nodes) on test MSE and training time; trained on 100k then the full 1M dataset and compared (Weeks 4–5)
- Adopted the paper's exact evaluation structure (800k train / 200k validation / separate 100k test) and ran a **3-seed reproducibility study** of the 2L-150N model, reaching test MSE **(9.66 ± 1.15) × 10⁻⁸** after matching TensorFlow's Adam ε = 10⁻⁷ (Weeks 6–7)

### Stage 2 — Transformed Implied Volatility *(Week 13, synthetic)*
- Addressed the exploding-gradient problem in inverting Black-Scholes for σ (where `dσ/dπ = 1/vega` blows up near zero vega) by subtracting scaled intrinsic value and log-transforming the price input
- Trained 6 of the paper's 12 architectures on the transformed problem; best model (3L-150N) reached test MSE **2.35 × 10⁻⁶**, a ~3-order-of-magnitude improvement over the raw-IV formulation
> This stage uses **synthetic** data, so it sits with the Black-Scholes work rather than the real-data pipeline.

### Stage 3 — Real-Data Proof of Concept: 2024 Pricing *(Weeks 8–12)*
A single-year exploration on real OptionMetrics data, **pricing** observed option mid-prices (not yet forecasting IV):
- **Week 8a** — 10 American equity tickers (AAPL, MSFT, NVDA, …), 2024; `bs_price` included as a feature to anchor the early-exercise premium (American mid-price ≥ BS European price)
- **Week 8b** — SPX European options, 2024; `bs_price` deliberately **excluded** to avoid label leakage (OptionMetrics inverts BS to get SPX IV, so BS price ≈ mid-price)
- **Weeks 9–10** — trained MLPs across a capacity spectrum on the SPX set; corrected the risk-free rate to the **CRSP 10-year Treasury** and added a **dividend-adjusted (Merton 1973)** Black-Scholes benchmark, both per professor feedback
- **Week 11** — reconciled BS-benchmark rates to **IvyDB Manual v6.0** exactly (`zerocd` for r, `borrate2024` for q), driving the BS residual median to ≈ \$0
- **Week 12** — **overfitting investigation**: a jagged rate partial-dependence curve in the large 3L-500N model prompted retraining on simpler paper-grid architectures to test whether model capacity, not data, produced the non-smooth rate response

### Stage 4 — Jiang Dataset & Replication *(Weeks 14–15)*
- Built the full **S&P 100** dataset per Jiang Section 2: European **XEO** (secid 112878) and American **OEX** (secid 109764), **2016–2023** (Week 14)
- Applied Jiang's filters: moneyness ∈ [0.80, 1.60], τ ∈ [20, 1094] days, ATM band [0.97, 1.03], **no volume filter**
- IV summary statistics match Jiang's Tables 1–2 closely, though **observation counts differ** from the paper (European 3.10M vs Jiang's 2.32M); the discrepancy is documented and flagged for clarification
- Follows Jiang's pipeline: American prices are **de-Americanized** (Carr & Wu 2010, via binomial-tree IV) into European-equivalent prices before Black-Scholes and Heston (FFT) calibration (Week 15)
- Trained all five Jiang frameworks (BS+NN and Heston+NN independent/sequential, Pure NN sequential) across same-day, 1-day-ahead, and 5-day-ahead horizons on the OEX American set, reproducing Tables 4–6 (Week 15)
- Shared infrastructure extracted into `shared/jiang_common.py`: JiangNN (32→16→8→1), vectorized BS/Heston calibration with checkpoint-resume, de-Americanization, and `run_framework` (Week 15)

### Stage 5 — Heston Feature Extension *(Week 16)*
Instead of treating Heston as a **residual corrector**, this extension feeds the Heston-implied volatility **directly as a feature** to a sequentially trained NN, testing whether Heston σ supplies nonlinear structure a residual formulation does not exploit. Results are compared side-by-side against Jiang Tables 4–5.

### Stage 6 — Framework Comparison *(Week 17)*
Consolidated comparison across all frameworks and horizons: side-by-side RMSE tables versus Jiang et al., a Table-6-style breakdown by call/put × ITM/ATM/OTM, and **60-day moving-average out-of-sample RMSE** plots for the same-day, one-day-ahead, and five-day-ahead horizons.

> The five Jiang frameworks (BS+NN and Heston+NN, each independent/sequential, plus Pure NN sequential-only) are trained on CMU's Wright cluster across the same-day, 1-day, and 5-day horizons, with both K-splitting (strike divisible by 10) and R-splitting (70:30), over four data setups (EU→EU, AM→AM, EU→AM, EU+AM→AM). See the notebooks and `reports/` for current RMSE results.

### Stage 7 — Overfitting Study *(Weeks 18–19)*
Diagnosed the in-sample / out-of-sample gap across all frameworks and tested regularization routes under Professor Schafer's direction:
- **Task 1 — Baseline**: 800 epochs / batch 32, standard 32→16→8 architecture, no regularization
- **Task 2 — Simpler architecture**: reduced to 16→8 hidden layers; compared against baseline at focal horizon (5-day-ahead) via overfit ratio = 100 × (OOS − IS) / IS
- **Task 3 — Dropout sweep**: p ∈ {0.1, 0.2, 0.3}; overfit-ratio table as headline metric with absolute OOS RMSE as a guardrail against degraded generalization
- Horizon-pair percent-difference analysis (same-day → 1-day, → 5-day) by call/put × moneyness, baseline vs simpler architecture
- **Task 4 (Week 19) — Increased complexity + dropout**: We built a much larger 128→64→32→16 architecture swept at p ∈ {0.0, 0.02, 0.4}. Complexity alone (p=0.0) made overfitting *worse* than the Week 18 baseline in every framework (overfit ratio +35 pp on average); complexity + heavy dropout (p=0.4) pushed the overfit ratio well below Week 18's best dropout result, but absolute OOS RMSE rose in every config and was worse than Week 18's own best-dropout OOS RMSE in half of them, so the ratio gain is not a clean generalization win. See `reports/week_19_summary.txt` for the full breakdown.

---

## Architecture

**Jiang replication / Heston extension (Stages 4–7).** Per Jiang et al. (2026)
Table 3: a feed-forward network with **three hidden layers (32 → 16 → 8)**,
ReLU activation, trained with **Adam, 800 epochs, batch size 32**. Inputs are
moneyness `m` and maturity `τ`. For BS+NN and Heston+NN the network learns the
*error surface* `ε = σ_market − σ_model`; Pure NN learns the surface directly.
The Week 16 extension adds Heston-implied σ as a direct input. The Week 18
overfitting study additionally tests a **simpler 16→8 architecture** and
**dropout** (p ∈ {0.1, 0.2, 0.3}) as regularization strategies. Week 19 tests
the opposite direction on the same dropout tree: a much larger **128→64→32→16
architecture**, swept at p ∈ {0.0, 0.02, 0.4}.

**Synthetic / transformed-IV work (Stages 1–2).** Separate from the Jiang
architecture: MLPs from the Della Corte grid (2–3 layers × {50–500} nodes),
ReLU, Glorot/Xavier init, Adam (ε = 10⁻⁷), lr = 10⁻⁵, batch 64.

---

## Data Sources

| Source | Table | Used For |
|---|---|---|
| OptionMetrics IvyDB via WRDS | `opprcd{YYYY}` | Option quotes |
| OptionMetrics | `zerocd` | Risk-free rate r (BS benchmark; percent → /100) |
| OptionMetrics | `borrate2024` | Borrow rate q for SPX 2024 work (Stage 3) |
| OptionMetrics | `idxdvd` | Dividend yield q for S&P 100 / Jiang set (Stage 4) |
| CRSP via WRDS | `tfz_dly_ft` | 10-year Treasury rate, MLP feature r (Stages 3–4) |
| OptionMetrics | `secprd` | Underlying close S |

> The risk-free rate evolved across the project: early weeks interpolated the
> `zerocd` zero curve; from Week 10 the **CRSP 10-year Treasury** became the MLP
> feature rate per professor guidance, while `zerocd`/`borrate2024` were used to
> reproduce OptionMetrics' own BS inversion exactly (BS residual median ≈ \$0).

> **Note:** OptionMetrics and CRSP data require institutional WRDS access and are not included in this repository.

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
machine_learning_for_implied_volatility_forecasting/
├── shared/      # setup module imported by every notebook (setup.py)
├── notebooks/   # 9 notebooks, organized by topic — see notebooks/README.md
├── figures/     # plots and tables, by week (week_02 … week_19)
├── reports/     # weekly summaries + mid-semester progress report
├── sources/     # reference papers
├── .gitignore · LICENSE · README.md
```

Each notebook opens with a setup cell that pulls this repo and runs
`from shared.setup import *`, so environment setup lives in one place rather
than being duplicated. Notebooks are grouped by topic; figures and reports stay
by week, since some weeks span more than one notebook.

---

## Citation
Jiang, G. J., Lazar, E., & Marra, G. (2026). Neural network-based implied volatility forecasting. *Journal of Futures Markets*, 46, 1137–1153. https://doi.org/10.1002/fut.70101

---

## AI Disclosure
Generative AI assistance (Claude, Anthropic) was used in coding throughout this project. All research design, methodology, analysis, and written documentation are the work of Joseph Ouyang and Caleb Ouyang.

---

*CMU Statistics & Data Science · MSCF · Spring/Summer 2026*
