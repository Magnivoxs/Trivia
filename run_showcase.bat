@echo off
REM Expense Budget Monitor - Showcase Demo for Windows

echo ================================================
echo   EXPENSE MONITOR SHOWCASE - Windows 11
echo ================================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo Running showcase demo...
echo.

python expense_showcase.py

echo.
echo ================================================
pause
