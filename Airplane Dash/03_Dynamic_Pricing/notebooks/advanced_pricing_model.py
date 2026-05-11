# 03_Dynamic_Pricing/notebooks/advanced_pricing_model.py
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import os

# Set paths
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '../data/ticket_prices.csv')

# Load data
df = pd.read_csv(data_path)

# Features
X = df[['days_to_departure', 'is_weekend', 'flight_duration_min']]
y = df['price']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# XGBoost Model
print("Training Advanced XGBoost Pricing Model...")
model = xgb.XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(f"--- XGBoost Model Performance ---")
print(f"MAE: ${mean_absolute_error(y_test, y_pred):.2f}")
print(f"R2 Score: {r2_score(y_test, y_pred):.2f}")

# Portfolio Insight: Feature Importance
import matplotlib.pyplot as plt
xgb.plot_importance(model)
plt.title('Pricing Drivers (Feature Importance)')
plt.savefig(os.path.join(base_dir, '../power_bi/pricing_drivers.png'))

print(f"\nModel complete. Feature importance saved to ../power_bi/")
