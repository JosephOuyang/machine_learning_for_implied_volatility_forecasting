# Notebooks

Ten notebooks, organized **by topic** (research stage), split from the
original cumulative `options_pricing_main.ipynb` for easier navigation.

| Notebook | Topic | Weeks |
|---|---|---|
| `01_bs_ann_dataset_generation.ipynb` | Closed-form Black-Scholes + LHS synthetic data generation | 2–3 |
| `02_bs_ann_price_training.ipynb` | BS-ANN price training: class, LR search, sweeps, reproducibility | 4–7 |
| `03_bs_ann_iv_training.ipynb` | Transformed implied-volatility MLP training (self-contained) | 13 |
| `04_optionmetrics_dataset.ipynb` | OptionMetrics dataset construction (American OEX + European XEO) | 8–9 |
| `05_optionmetrics_spx.ipynb` | European SPX pathway | 10–14 |
| `06_optionmetrics_sp100.ipynb` | S&P 100 pathway + Jiang replication pipeline | 10–15 |
| `07_heston_feature_extension.ipynb` | HestonFeature extension (σ_Heston as direct MLP input) + framework battery start | 16–17 |
| `08_week17_framework_comparison.ipynb` | Framework comparison, RMSE tables, 60-day MA OOS | 17 |
| `09_week18_19_dropout_and_complexity_analysis.ipynb` | Overfitting study: baseline vs simpler architecture vs dropout, extended to increased model complexity (128→64→32→16) paired with dropout | 18–19 |
| `10_week20_21_heston_autoencoder_and_cnn.ipynb` | Heston-autoencoder feature engineering (fixed grid, synthetic autoencoder, deployment, AEOnly/HestonPlusAE comparison) + CNN-based parameter estimation experiments | 20–21 |

## Running a notebook

Each notebook's first code cell is a **setup cell**. It mounts Google Drive,
clones (or pulls) this repository into the Colab session, and runs:

```python
from shared.setup import *
```

This provides the standard imports, global seeds, and run-logger helpers
(`start_run`, `save_json`, `save_notes`). Editing setup logic is a one-file
change in `shared/setup.py` — every notebook picks it up on its next run.

Saved figure outputs are committed with the notebooks, so the visualizations
and tables are visible on open without re-execution. Heavy GPU training is run
on CMU's Wright cluster; those cells load results from Drive rather than
retraining in Colab.

> The OptionMetrics-based notebooks require WRDS access and Drive data that are
> not included in this repository.
