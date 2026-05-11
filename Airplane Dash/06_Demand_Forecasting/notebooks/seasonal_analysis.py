# 06_Demand_Forecasting/notebooks/seasonal_analysis.py
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import os

# Set paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '../data/historical_demand.csv')
output_dir = os.path.join(base_dir, '../power_bi/')

# Load data
df = pd.read_csv(data_path)
df['month'] = pd.to_datetime(df['month'])
df.set_index('month', inplace=True)

# Decompose the time series (Multiplicative or Additive)
# We use period=12 for monthly data
result = seasonal_decompose(df['passengers'], model='additive', period=12)

# Plotting the components
plt.figure(figsize=(12, 10))
plt.subplot(4, 1, 1)
plt.plot(result.observed)
plt.title('Observed (Raw Data)')
plt.subplot(4, 1, 2)
plt.plot(result.trend)
plt.title('Trend (Long-term Growth)')
plt.subplot(4, 1, 3)
plt.plot(result.seasonal)
plt.title('Seasonality (Cyclic Patterns)')
plt.subplot(4, 1, 4)
plt.plot(result.resid)
plt.title('Residuals (Unpredictable Noise)')

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'demand_decomposition.png'))

print("--- Demand Decomposition Complete ---")
print(f"Results saved to {output_dir}")
