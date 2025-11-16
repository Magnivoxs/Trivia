@echo off
REM Expense Budget Monitor - Windows Launcher
REM Checks for Python and runs the expense monitor

echo ================================================
echo   EXPENSE BUDGET MONITOR - Windows 11
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3 from:
    echo https://www.python.org/downloads/
    echo.
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo Python found:
python --version
echo.
echo Starting Expense Monitor...
echo.

REM Run the expense monitor
python expense_monitor.py

if errorlevel 1 (
    echo.
    echo An error occurred while running the program.
    pause
)
