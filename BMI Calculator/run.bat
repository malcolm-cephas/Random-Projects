@echo off
setlocal
cd /d "%~dp0"

IF NOT EXIST node_modules (
    echo node_modules not found. Installing dependencies...
    call npm install
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo npm install failed. Please check your internet connection or Node.js installation.
    pause
    exit /b %ERRORLEVEL%
)

echo Starting BMI Calculator...
call npm start
pause
