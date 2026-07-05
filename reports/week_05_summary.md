Week 5 Summary (Full Dataset Training):

I trained four paper-aligned models on the full 1 million data points dataset. The goal was to evaluate their performance and training characteristics when exposed to a larger volume of data compared to the 100k dataset used in Week 4.

Models Trained:
- (2 layers, 50 nodes)
- (2 layers, 100 nodes)
- (3 layers, 50 nodes)
- (3 layers, 100 nodes)

Dataset:
- Full LHS dataset (n=1,000,000) generated in Week 3.

Hyperparameters (aligned with paper):
- Activation: ReLU
- Loss: MSE
- Epochs: 200
- Batch Size: 64
- Learning Rate: 1e-05

Artifacts and Visualizations:
- CSV summary of training results: runs/week5_full_dataset_4_models_sweep/20260208-213848/week5_full_mlp_sweep.csv
- Bar chart of Training Time & Test MSE: runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_full_dataset_time_vs_mse.png
- Training MSE curves (2-layer networks): runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_train_curves_2layer_50_100_full_dataset.png
- Test MSE curves (2-layer networks): runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_test_curves_2layer_50_100_full_dataset.png
- Training MSE curves (3-layer networks): runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_train_curves_3layer_50_100_full_dataset.png
- Test MSE curves (3-layer networks): runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_test_curves_3layer_50_100_full_dataset.png
