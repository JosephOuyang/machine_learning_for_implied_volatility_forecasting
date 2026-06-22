Week 3 Data Card — LHS Dataset (BS-ANN)

n = 1000000

Target ranges:
m (S/K):      [0.4, 1.6]
tau (T-t):    [0.2, 1.1]
r:            [0.02, 0.10]
sigma:        [0.01, 1.0]

Actual min/max (generated):
m (S/K):      [0.400000, 1.599999]
tau (T-t):    [0.200000, 1.099999]
r:            [0.020000, 0.100000]
sigma:        [0.010001, 0.999999]
V/K (label):  [0.000000, 0.893004]

Sanity checks enforced:
- S/K > 0, tau > 0, sigma > 0
- 0 <= V/K <= S/K

Visualizations:
- runs/week3_lhs_dataset_generation/20260202-024209/figures/week3_LHS_input_histograms.png
- runs/week3_lhs_dataset_generation/20260202-024209/figures/week3_LHS_input_scatterplots.png

Saved dataset:
- runs/week3_lhs_dataset_generation/20260202-024209/bs_lhs_dataset_n1e6.pt
