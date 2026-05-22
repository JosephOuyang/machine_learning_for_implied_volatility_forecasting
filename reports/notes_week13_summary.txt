WEEK 13 SUMMARY — Transformed Implied Volatility MLP Sweep
Partial replication of Table 6.25 / Figure 6.24, Della Corte et al. (2025)

================================================================
MOTIVATION
================================================================
The raw IV problem feeds π/K directly and asks the MLP to invert
Black-Scholes. The gradient dσ/dπ = 1/vega explodes wherever
vega ≈ 0 (deep ITM/OTM), causing all 12 models to plateau at
MSE ≈ 7×10⁻⁴ regardless of size (Table 6.23 in the paper).

Two-step fix (Liu et al. [22], Section 5.2):
  1. Subtract scaled intrinsic:  π̂/K = π/K − max(m − e^{−rτ}, 0)
  2. Log-transform:              x₄   = log(π̂/K)
Effect: 2L-150N MSE drops from 7.1×10⁻⁴ → 1.5×10⁻⁶ (~3 orders of
magnitude) with no architecture or hyperparameter changes.

================================================================
DATASET
================================================================
Source:   Synthetic BS, LHS (Table 5.11 ranges)
Train:    800,000  |  Val: 200,000  |  Test: 100,000
Features: m, τ, r, log(π̂/K)   [in_dim=4]
Label:    σ (implied volatility)
log(π̂/K) range: [-18.9994, -0.9478]
Paper Table 5.14 expected: [-18.42, -0.95]

================================================================
HYPERPARAMETERS
================================================================
Activation: ReLU | Loss: MSE | Init: Xavier Normal (Glorot)
LR: 1e-05 | Batch: 64 | Epochs: 200 | Adam ε: 1e-07
Device: CPU, 1 thread

================================================================
CONFIGS TRAINED (6 of 12) — RATIONALE
================================================================
2L  50N  baseline floor
2L 100N  first jump in 2-layer series
2L 150N  Week 7 architecture (cross-week continuity)
3L  50N  3-layer floor; depth comparison vs 2L-50N
3L 100N  mirrors 2L-100N for depth comparison
3L 150N  direct depth comparison vs 2L-150N

Omitted (taken from Table 6.25):
  2L 200N
  2L 250N
  2L 500N
  3L 200N
  3L 250N
  3L 500N

================================================================
OUR RESULTS vs TABLE 6.25
================================================================
 config  n_params  our_mse  paper_mse  ratio_our_vs_paper
 2L 50N      2851 0.000065   0.000011               5.906
2L 100N     10701 0.000029   0.000002              12.403
2L 150N     23551 0.000004   0.000002               2.700
 3L 50N      5401 0.000034   0.000004               8.611
3L 100N     20801 0.000010   0.000005               1.899
3L 150N     46201 0.000002   0.000002               1.238

Best (ours):  3L 150N  |  test MSE = 2.352e-06
Worst (ours): 2L 50N  |  test MSE = 6.496e-05
Paper best:   3L 500N  |  1.6e-07

================================================================
ARTIFACTS
================================================================
Dataset summary:          runs/week13_transformed_iv_mlp_sweep/20260517-175402/dataset_summary.json
EDA distributions:        runs/week13_transformed_iv_mlp_sweep/20260517-175402/figures/week13_transformed_iv_distributions.png
Sweep results CSV:        runs/week13_transformed_iv_mlp_sweep/20260517-175402/week13_transformed_iv_mlp_sweep.csv
Figure 6.24 replica:      runs/week13_transformed_iv_mlp_sweep/20260517-175402/figures/week13_fig6_24_style_time_vs_mse.png
Full comparison table:    runs/week13_transformed_iv_mlp_sweep/20260517-175402/week13_paper_comparison_table.csv
Per-model curves:         runs/week13_transformed_iv_mlp_sweep/20260517-175402/figures/week13_*_epoch_vs_mse.png
2L / 3L overlays:         runs/week13_transformed_iv_mlp_sweep/20260517-175402/figures/week13_train/val_curves_*.png
Depth comparison (150N):  runs/week13_transformed_iv_mlp_sweep/20260517-175402/figures/week13_depth_comparison_150N_val.png
