Week 5 — Comparison of Training Results (100k vs 1M Datasets)

This summary compares the training performance and final test Mean Squared Error (MSE) of four key MLP architectures when trained on two different dataset sizes: 100,000 data points (from Week 4) and 1,000,000 data points (from Week 5). The models considered are: (2 layers, 50 nodes), (2 layers, 100 nodes), (3 layers, 50 nodes), and (3 layers, 100 nodes).

### Data for Comparison (from df_comparison):
             label  layers  nodes dataset_size  train_hours     test_mse
 2 layers 50 nodes       2     50         100k     0.123940 2.789249e-06
 3 layers 50 nodes       3     50         100k     0.141425 2.308291e-06
2 layers 100 nodes       2    100         100k     0.135535 8.719681e-07
3 layers 100 nodes       3    100         100k     0.164692 5.470124e-07
 2 layers 50 nodes       2     50           1M     1.320568 7.129661e-07
 3 layers 50 nodes       3     50           1M     1.643483 5.869988e-07
2 layers 100 nodes       2    100           1M     1.638542 1.635349e-07
3 layers 100 nodes       3    100           1M     1.609884 1.627912e-07

### Analysis:

1.  **Impact on Training Time:**
    -   As expected, increasing the dataset size by a factor of 10 (from 100k to 1M) significantly increased training times for all models. For instance, the 2-layer, 50-node model's training time jumped from ~0.12 hours to ~1.32 hours, an increase of approximately 11 times. Similarly, the 3-layer, 50-node model's time increased from ~0.14 hours to ~1.64 hours (~11.7x).
    -   Training times scale roughly linearly with the dataset size, which is a common observation in deep learning as each epoch processes more data.

2.  **Impact on Test MSE (Model Performance):**
    -   For all models, increasing the dataset size from 100k to 1M led to a substantial improvement in test MSE, indicating better generalization and lower error. For example, the 2-layer, 50-node model improved its test MSE from 2.79e-06 to 7.13e-07 (approximately 3.9 times better).
    -   The 3-layer, 50-node model showed improvement from 2.31e-06 to 5.87e-07 (approximately 3.9 times better).
    -   The 2-layer, 100-node model improved from 8.72e-07 to 1.64e-07 (approximately 5.3 times better).
    -   The 3-layer, 100-node model improved from 5.47e-07 to 1.63e-07 (approximately 3.4 times better).
    -   This trend confirms that with more data, the models are able to learn more robust features and reduce their generalization error.

3.  **Trends by Architecture:**
    -   Across both dataset sizes, models with more nodes (100 vs. 50) generally achieved lower test MSEs, suggesting that larger capacity networks are better at capturing the underlying function. For instance, comparing (2L, 50N) vs (2L, 100N) on the 1M dataset, MSE improved from 7.13e-07 to 1.64e-07.
    -   The difference between 2-layer and 3-layer networks is less pronounced. For 50 nodes, the 3-layer model consistently performed better than the 2-layer model on both datasets. For 100 nodes on the 1M dataset, the 2-layer model now has a test MSE of 1.64e-07, which is very similar to the 3-layer model's 1.63e-07, suggesting comparable performance between these specific configurations at this scale.

4.  **Consistency with Paper Insights:**
    -   The general improvements in MSE with increased data volume align with expectations for neural networks, where more data typically leads to better performance, provided the model has sufficient capacity.
    -   The paper's Figure 6.16 (Week 4's dual-axis plot) showed that deeper/wider networks generally achieve lower MSE but take longer to train. This holds true for the 1M dataset as well, where the training times are substantially higher for the 1M dataset, and MSEs are lower across the board.

### Visualizations:

-   Bar chart comparing Training Time & Test MSE for the four models on the full dataset: `runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_full_dataset_time_vs_mse.png`
-   Training MSE curves for 2-layer networks (50/100 nodes) on full dataset: `runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_train_curves_2layer_50_100_full_dataset.png`
-   Test MSE curves for 2-layer networks (50/100 nodes) on full dataset: `runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_test_curves_2layer_50_100_full_dataset.png`
-   Training MSE curves for 3-layer networks (50/100 nodes) on full dataset: `runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_train_curves_3layer_50_100_full_dataset.png`
-   Test MSE curves for 3-layer networks (50/100 nodes) on full dataset: `runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_test_curves_3layer_50_100_full_dataset.png`
