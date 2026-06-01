@echo off
echo ===================================================
echo Setting up BMI Tracker (React + Vite)
echo ===================================================
echo.

:: Check if Node.js is installed
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Node.js is not installed on this system!
    echo Node.js is required to install dependencies and run the application.
    echo.
    echo Please download and install Node.js from: https://nodejs.org/
    echo After installing, please reopen/run this setup script.
    echo.
    pause
    exit /b 1
)

echo Node.js detected. Installing npm dependencies...
call npm install
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] npm install failed. Please check connection and try again.
    pause
    exit /b 1
)

echo.
echo Setup completed successfully! Run run.bat to start the application.
pause
