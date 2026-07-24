import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(101)

# ==========================================
# 1. DATE HANDLING & HANDLING MISSING DATES
# ==========================================
# Generate irregular business dates (excluding weekends)
business_dates = pd.date_range(
    start="2024-01-01", end="2024-06-30", freq="B"
)

# Simulate stock prices with random walk drift
price = 100 + np.cumsum(np.random.normal(0.2, 2.0, size=len(business_dates)))

df = pd.DataFrame({"Price": price}, index=business_dates)

# Fill missing calendar dates (e.g., weekends/holidays) using forward-fill
full_date_range = pd.date_range(
    start="2024-01-01", end="2024-06-30", freq="D"
)
df_filled = df.reindex(full_date_range).ffill()

# Date Properties & Categorization
df_filled["Quarter"] = df_filled.index.quarter
df_filled["Day_of_Year"] = df_filled.index.dayofyear
df_filled["Week_of_Year"] = df_filled.index.isocalendar().week

print("--- Data Reindexed & Filled (First 7 Days) ---")
print(df_filled.head(7), "\n")


# ==========================================
# 2. TREND ANALYSIS: EWMA & EXPANDING WINDOWS
# ==========================================
# Exponential Moving Average (gives more weight to recent prices)
df_filled["EMA_14D"] = df_filled["Price"].ewm(span=14, adjust=False).mean()

# Expanding Window (calculates cumulative moving average from start of time series)
df_filled["Cumulative_Avg"] = df_filled["Price"].expanding(min_periods=1).mean()


# ==========================================
# 3. TIME-BASED RISK & PERIOD COMPARISONS
# ==========================================
# Log Returns (standard transformation for financial time series)
df_filled["Log_Return"] = np.log(
    df_filled["Price"] / df_filled["Price"].shift(1)
)

# 14-Day Rolling Volatility (Standard Deviation of returns)
df_filled["14D_Volatility"] = (
    df_filled["Log_Return"].rolling(window=14).std() * np.sqrt(365)
)

# Resampling to Quarterly Highs and Lows
quarterly_summary = df_filled["Price"].resample("QE").agg(["first", "max", "min", "last"])

print("--- Quarterly Summary ---")
print(quarterly_summary, "\n")


# ==========================================
# 4. VISUALIZATION
# ==========================================
fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Plot 1: Price, EMA Trend, and Cumulative Trend
axes[0].plot(
    df_filled.index, df_filled["Price"], label="Raw Price", color="black", alpha=0.6
)
axes[0].plot(
    df_filled.index,
    df_filled["EMA_14D"],
    label="14-Day Exponential Moving Avg (Trend)",
    color="orange",
    linewidth=2,
)
axes[0].plot(
    df_filled.index,
    df_filled["Cumulative_Avg"],
    label="Cumulative Average (Expanding Window)",
    color="purple",
    linestyle="--",
)
axes[0].set_title("Stock Price Trend Tracking with EWMA & Expanding Window")
axes[0].set_ylabel("Price ($)")
axes[0].legend()
axes[0].grid(True)

# Plot 2: Time-based Rolling Volatility
axes[1].plot(
    df_filled.index,
    df_filled["14D_Volatility"],
    color="crimson",
    linewidth=1.5,
)
axes[1].set_title("14-Day Rolling Volatility (Time-Based Risk Metric)")
axes[1].set_ylabel("Annualized Volatility")
axes[1].grid(True)

plt.tight_layout()
plt.show()