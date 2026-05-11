# 01_Flight_Delay_Prediction/notebooks/02_model_training.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

import os

# Get the directory where the script is located
base_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(base_dir, '../data/flights_sample.csv')
models_dir = os.path.join(base_dir, '../models/')

# 1. Load data
df = pd.read_csv(data_path)

# 2. Preprocessing
# Extract features from time
df['hour'] = pd.to_datetime(df['scheduled_departure_time'], format='%H:%M:%S').dt.hour
df['day_of_week'] = pd.to_datetime(df['flight_date']).dt.dayofweek

# Define target: Delay > 15 minutes
df['target'] = (df['arrival_delay'] > 15).astype(int)

# Select features (Focusing on things we know BEFORE the flight)
features = ['hour', 'day_of_week', 'distance', 'carrier', 'origin_airport']
X = df[features]
y = df['target']

# One-hot encoding for categorical variables (Carrier, Origin)
X = pd.get_dummies(X, columns=['carrier', 'origin_airport'])

# 3. Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Model Selection & Training
print("Training Random Forest Model...")
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluation
y_pred = model.predict(X_test)
print("\nModel Performance Report:")
print(classification_report(y_test, y_pred))

# 6. Save Model & Feature List
joblib.dump(model, os.path.join(models_dir, 'delay_predictor_rf.joblib'))
joblib.dump(X.columns.tolist(), os.path.join(models_dir, 'feature_names.joblib'))
print(f"\nModel and features saved to {models_dir}")
