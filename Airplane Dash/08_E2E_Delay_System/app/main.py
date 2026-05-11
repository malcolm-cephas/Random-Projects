# 08_E2E_Delay_System/app/main.py
from fastapi import FastAPI, HTTPException
import joblib
import os
import pandas as pd

app = FastAPI(title="Airline Delay Predictor API")

# Load model and features
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, '../../01_Flight_Delay_Prediction/models/delay_predictor_rf.joblib')
features_path = os.path.join(base_dir, '../../01_Flight_Delay_Prediction/models/feature_names.joblib')

if not os.path.exists(model_path):
    print("⚠️ Model not found! Please run Project 1 training first.")
else:
    model = joblib.load(model_path)
    feature_names = joblib.load(features_path)

@app.get("/")
def home():
    return {"message": "Welcome to the Flight Delay Prediction API. Use /predict (POST)"}

@app.post("/predict")
def predict(data: dict):
    try:
        # Convert input dict to DataFrame with correct feature alignment
        input_df = pd.DataFrame([data])
        
        # Ensure all training features are present (handle one-hot encoding)
        # For simplicity in this starter, we expect pre-encoded or basic features
        # In a real app, you'd include a 'preprocessor' pipeline here.
        
        prediction = model.predict(input_df[feature_names])
        return {
            "prediction": "Delayed" if prediction[0] == 1 else "On-Time",
            "status_code": int(prediction[0])
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
