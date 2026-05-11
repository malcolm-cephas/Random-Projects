@echo off
title Airline Analytics Portfolio - Master Dashboard
echo ========================================================
echo   Launching Aviation Command Center Dashboard...
echo ========================================================
echo.

:: Check if requirements are installed (Optional but helpful)
echo [1/2] Checking dependencies...
pip install -r 01_Flight_Delay_Prediction/requirements.txt --quiet
pip install streamlit plotly xgboost textblob statsmodels wordcloud --quiet

echo.
echo [2/2] Starting Streamlit Server...
echo Your dashboard will open in a new browser tab shortly.
echo.

:: Run the master dashboard
streamlit run master_dashboard.py

pause
