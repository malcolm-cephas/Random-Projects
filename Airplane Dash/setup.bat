@echo off
title Airline Analytics Portfolio - Initial Setup
echo ========================================================
echo   Setting up Airline Analytics Portfolio Environment
echo ========================================================
echo.

:: 1. Install Python Libraries
echo [1/3] Installing required Python libraries...
pip install pandas numpy matplotlib seaborn scikit-learn xgboost textblob statsmodels wordcloud plotly streamlit fastapi uvicorn httpx joblib nltk

:: Download NLTK stopwords
python -c "import nltk; nltk.download('stopwords')"

echo.
:: 2. Initialize Synthetic Datasets
echo [2/3] Generating realistic airline datasets...
python 01_Flight_Delay_Prediction/data/data_generator.py
python 02_Customer_Satisfaction/data/review_generator.py
python 03_Dynamic_Pricing/data/pricing_generator.py
python 04_Route_Profitability/data/profit_generator.py
python 05_Predictive_Maintenance/data/sensor_generator.py
python 06_Demand_Forecasting/data/demand_generator.py
python 07_Baggage_Analytics/data/baggage_generator.py

echo.
:: 3. Train Initial Models
echo [3/3] Training baseline Machine Learning models...
python 01_Flight_Delay_Prediction/notebooks/02_model_training.py

echo.
echo ========================================================
echo   SETUP COMPLETE! 
echo   You can now launch the project using 'run.bat'
echo ========================================================
pause
