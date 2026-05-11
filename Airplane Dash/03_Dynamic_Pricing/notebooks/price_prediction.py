# 03_Dynamic_Pricing/notebooks/price_prediction.py
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import os

# Set paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '../data/ticket_prices.csv')

# Load data
df = pd.read_csv(data_path)

# Features: Days to Departure, Weekend, Duration
X = df[['days_to_departure', 'is_weekend', 'flight_duration_min']]
y = df['price']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Results
y_pred = model.predict(X_test)
print(f"--- Price Prediction Model (Linear Regression) ---")
print(f"MAE: ${mean_absolute_error(y_test, y_pred):.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")

# Sample Prediction: 7 days left, Weekend, 180 min flight
sample = np.array([[7, 1, 180]])
predicted_price = model.predict(sample)
print(f"\nPredicted price for 7 days left: ${predicted_price[0]:.2f}")
