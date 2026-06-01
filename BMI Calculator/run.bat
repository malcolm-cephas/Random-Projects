@echo off
echo ===================================================
echo Starting BMI Tracker Development Server...
echo ===================================================
echo.

:: Check if Node.js is installed
where node >nul 2>nul
if %errorlevel% neq 0 (
    echo [ERROR] Node.js is not installed on this system!
    echo Node.js is required to run the development server.
    echo.
    echo Please download and install Node.js from: https://nodejs.org/
    echo.
    pause
    exit /b 1
)

:: Check if node_modules folder exists
if not exist "node_modules\" (
    echo node_modules folder not found. Installing dependencies first...
    echo.
    call npm install
    if %errorlevel% neq 0 (
        echo.
        echo [ERROR] Dependency installation failed. Please check connection and try again.
        pause
        exit /b 1
    )
)

echo Starting the development server...
call npm run dev
pause
