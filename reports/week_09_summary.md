Week 9 deliverable:
- Load Week 8b SPX European dataset (321,368 rows). r is now in decimal form.
- Split: hold out 10% as separate test set, then 80/20 train/val from remainder.
  Mirrors Week 6-7 structure exactly.
- Normalize with StandardScaler fit on training set only.
- Train 4 architectures chosen to span the capacity spectrum:
    2L 50N  — baseline (simplest)
    2L 500N — wide (isolates width effect)
    3L 250N — medium capacity
    3L 500N — maximum capacity
- Same hyperparams as Weeks 6-7: lr=1e-5, batch=64, epochs=200, Adam eps=1e-7.
- Addition 1: Smile recovery plot.
- Addition 2: Bucket RMSE table and bar chart in dollar terms (OTM/ATM/ITM).
- Addition 3: Temporal split — train Jan-Sep, test Oct-Dec.
