Week 8b deliverable:
- Pull SPX European call options for 2024 from OptionMetrics.
- SPX secid = 108105. Confirm exercise_style = E via opinfd.
- Same pipeline structure as Week 8a but for a single index underlying.
- Key difference: no bs_price feature. SPX impl_vol is already BS-based,
  so adding bs_price would nearly duplicate the label (data leakage).
- Features: moneyness, tau, r, impl_volatility.
- Label: mid_price.
- Save dataset, run EDA, compare row count and distributions to Week 8a.
