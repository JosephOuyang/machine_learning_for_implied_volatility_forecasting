# Week 5 — Comparison of Training Results (100k vs 1M Datasets)

This summary compares the training performance and final test Mean Squared Error (MSE) of four key MLP architectures when trained on two different dataset sizes: 100,000 data points (from Week 4) and 1,000,000 data points (from Week 5). The models considered are: **2 layers, 50 nodes**, **2 layers, 100 nodes**, **3 layers, 50 nodes**, and **3 layers, 100 nodes**.

## Data for Comparison

| Label | Layers | Nodes | Dataset Size | Train Hours | Test MSE |
|---|---:|---:|---:|---:|---:|
| 2 layers 50 nodes | 2 | 50 | 100k | 0.123940 | 2.789249e-06 |
| 3 layers 50 nodes | 3 | 50 | 100k | 0.141425 | 2.308291e-06 |
| 2 layers 100 nodes | 2 | 100 | 100k | 0.135535 | 8.719681e-07 |
| 3 layers 100 nodes | 3 | 100 | 100k | 0.164692 | 5.470124e-07 |
| 2 layers 50 nodes | 2 | 50 | 1M | 1.320568 | 7.129661e-07 |
| 3 layers 50 nodes | 3 | 50 | 1M | 1.643483 | 5.869988e-07 |
| 2 layers 100 nodes | 2 | 100 | 1M | 1.638542 | 1.635349e-07 |
| 3 layers 100 nodes | 3 | 100 | 1M | 1.609884 | 1.627912e-07 |

## Analysis

### 1. Impact on Training Time

As expected, increasing the dataset size by a factor of 10, from 100k to 1M, significantly increased training times for all models. For instance, the 2-layer, 50-node model's training time increased from approximately **0.12 hours** to **1.32 hours**, an increase of about **11×**. Similarly, the 3-layer, 50-node model's training time increased from approximately **0.14 hours** to **1.64 hours**, or about **11.7×**.

Training times scale roughly linearly with dataset size, which is expected because each epoch processes more data.

### 2. Impact on Test MSE

For all models, increasing the dataset size from 100k to 1M led to a substantial improvement in test MSE, indicating better generalization and lower prediction error.

- The **2-layer, 50-node** model improved from **2.79e-06** to **7.13e-07**, about **3.9× better**.
- The **3-layer, 50-node** model improved from **2.31e-06** to **5.87e-07**, about **3.9× better**.
- The **2-layer, 100-node** model improved from **8.72e-07** to **1.64e-07**, about **5.3× better**.
- The **3-layer, 100-node** model improved from **5.47e-07** to **1.63e-07**, about **3.4× better**.

This trend confirms that with more data, the models are able to learn more robust representations and reduce their generalization error.

### 3. Trends by Architecture

Across both dataset sizes, models with more nodes generally achieved lower test MSEs. This suggests that larger-capacity networks are better at capturing the underlying function. For example, on the 1M dataset, the 2-layer, 50-node model had a test MSE of **7.13e-07**, while the 2-layer, 100-node model achieved **1.64e-07**.

The difference between 2-layer and 3-layer networks is less pronounced. For 50-node models, the 3-layer model consistently performed better than the 2-layer model on both datasets. However, for 100-node models on the 1M dataset, the 2-layer model achieved a test MSE of **1.64e-07**, which is very close to the 3-layer model's **1.63e-07**. This suggests that these two configurations have comparable performance at the 1M scale.

### 4. Consistency with Paper Insights

The general improvement in MSE with increased data volume aligns with expectations for neural networks, where more data typically leads to better performance when the model has sufficient capacity.

The paper's Figure 6.16, referenced in Week 4's dual-axis plot, showed that deeper and wider networks generally achieve lower MSE but take longer to train. The Week 5 results are consistent with this pattern: the 1M dataset required substantially longer training times, while all models achieved lower test MSEs.

## Visualizations

- Bar chart comparing training time and test MSE for the four models on the full dataset:  
  `runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_full_dataset_time_vs_mse.png`

- Training MSE curves for 2-layer networks with 50 and 100 nodes on the full dataset:  
  `runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_train_curves_2layer_50_100_full_dataset.png`

- Test MSE curves for 2-layer networks with 50 and 100 nodes on the full dataset:  
  `runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_test_curves_2layer_50_100_full_dataset.png`

- Training MSE curves for 3-layer networks with 50 and 100 nodes on the full dataset:  
  `runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_train_curves_3layer_50_100_full_dataset.png`

- Test MSE curves for 3-layer networks with 50 and 100 nodes on the full dataset:  
  `runs/week5_full_dataset_4_models_sweep/20260208-213848/figures/week5_test_curves_3layer_50_100_full_dataset.png`
