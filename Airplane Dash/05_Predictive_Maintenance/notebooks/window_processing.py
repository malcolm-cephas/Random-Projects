# 05_Predictive_Maintenance/notebooks/window_processing.py
import pandas as pd
import numpy as np
import os

# Set paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '../data/engine_sensors.csv')

# Load data
df = pd.read_csv(data_path)

def create_windows(df, window_size=30):
    """
    Transforms sensor data into overlapping windows for time-series forecasting.
    """
    engine_ids = df['engine_id'].unique()
    X = []
    y = []
    
    for eid in engine_ids:
        engine_data = df[df['engine_id'] == eid]
        # Only take engines with enough data for the window
        if len(engine_data) > window_size:
            for i in range(len(engine_data) - window_size):
                # Window of sensor data
                X.append(engine_data[['temperature', 'vibration']].iloc[i:i+window_size].values)
                # The RUL at the END of the window
                y.append(engine_data['rul'].iloc[i+window_size-1])
                
    return np.array(X), np.array(y)

X_windows, y_rul = create_windows(df)
print(f"--- Sensor Data Windowing Complete ---")
print(f"Original Data Shape: {df.shape}")
print(f"Windowed Feature Shape (X): {X_windows.shape} (Windows, Time-Steps, Sensors)")
print(f"Target Shape (y): {y_rul.shape}")

print("\nPro-tip: These (X, y) arrays are now ready for an LSTM or 1D-CNN model!")
