Week 4 Summary (Paper alignment: MLP + LR search):

(1) LR Range Test:
- Ran an exponential LR range test on a small paper-aligned model (2 layers, 50 nodes).
- Saved LR-vs-loss plot: runs/week4_mlp_lr_search_and_paper_alignment/20260126-003223/figures/week4_lr_range_test.png
- Suggested LR from min-loss heuristic (for intuition), but for strict paper replication we fix lr = 1e-5.

(2) Paper-aligned MLP sweep (Table 6.15 grid):
- Trained 12 networks: layers in {2,3} × nodes in {50,100,150,200,250,500}
- Activation: ReLU | Loss: MSE | Epochs: 200 | Batch: 64 | LR: 1e-05
- Timing setup: CPU with torch.set_num_threads(1) for comparability
- Saved CSV: runs/week4_mlp_lr_search_and_paper_alignment/20260126-003223/week4_paper_mlp_sweep.csv
- Saved Figure 6.16-style plot: runs/week4_mlp_lr_search_and_paper_alignment/20260126-003223/figures/week4_fig6_16_style_time_vs_mse.png

(3) Optional curves:
- Plotted train/test MSE vs epoch for 2-layer networks with 50/250/500 nodes to mirror the paper’s discussion.
