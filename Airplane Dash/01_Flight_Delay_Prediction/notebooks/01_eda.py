# 01_Flight_Delay_Prediction/notebooks/01_eda.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import os

# Get the directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '../data/flights_sample.csv')
output_dir = os.path.join(base_dir, '../power_bi/')

# 1. Load Data
df = pd.read_csv(data_path)

# 2. Basic Cleaning
df['flight_date'] = pd.to_datetime(df['flight_date'])
df['is_delayed'] = df['arrival_delay'] > 15 # Industry standard for OTP

# 3. ANALYSIS: Delay by Hour of Day
df['hour'] = pd.to_datetime(df['scheduled_departure_time']).dt.hour

plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='hour', y='arrival_delay', estimator='mean')
plt.title('Average Arrival Delay by Hour of Day (The Ripple Effect)')
plt.xlabel('Scheduled Departure Hour')
plt.ylabel('Average Delay (Minutes)')
plt.grid(True)
plt.savefig(os.path.join(output_dir, 'delay_by_hour.png'))

# 4. ANALYSIS: Carrier Performance
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='carrier', y='is_delayed')
plt.title('Percentage of Delayed Flights by Carrier')
plt.ylabel('Delay Rate')
plt.savefig(os.path.join(output_dir, 'carrier_performance.png'))

print("📊 EDA Visuals saved to ../power_bi/ folder.")
print(f"Dataset Shape: {df.shape}")
print(f"Overall OTP %: {100 - (df['is_delayed'].mean() * 100):.2f}%")
