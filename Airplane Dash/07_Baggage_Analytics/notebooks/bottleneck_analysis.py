# 07_Baggage_Analytics/notebooks/bottleneck_analysis.py
import pandas as pd
import os

# Set paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '../data/baggage_flow.csv')

# Load data
df = pd.read_csv(data_path)

# Analysis: Failure rate per stage
mishandled_df = df[df['is_mishandled'] == True]
bottlenecks = mishandled_df['failure_point'].value_counts(normalize=True) * 100

print("--- Baggage Bottleneck Analysis ---")
print("Percentage of failures per stage:")
print(bottlenecks)

# Analysis: MBR by Origin Airport
mbr_by_airport = df.groupby('origin')['is_mishandled'].mean() * 1000
print("\nMBR (Mishandled Bags per 1000 passengers) by Airport:")
print(mbr_by_airport.sort_values(ascending=False))

print("\nStrategy Tip: Target the airport with the highest MBR for a 'Ground Handling Audit'.")
