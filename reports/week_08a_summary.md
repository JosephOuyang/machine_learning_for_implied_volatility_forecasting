Week 8a deliverable:
- Connect to WRDS and pull OptionMetrics data for 10 stocks over full year 2024.
- Pull exercise style from opinfd and merge — confirms all equity options are American.
- Merge option prices with underlying close prices (secprd) on secid + date.
- Interpolate risk-free rate from zero curve (zerocd) for each option row.
- Compute derived columns: tau, moneyness, mid_price, strike (divide by 1000), bs_price.
- Apply liquidity and quality filters per professor's guidance.
- Final dataframe columns: ticker, secid, date, exdate, cp_flag, exercise_style,
  close, strike, tau, r, impl_volatility, bs_price, mid_price, moneyness,
  volume, open_interest.
- Save final dataset as CSV.
- EDA: distributions of all features, row counts before/after filtering, per-ticker breakdown.
