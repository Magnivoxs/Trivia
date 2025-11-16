# Expense Budget Monitor - Windows 11 Setup Guide

## Quick Start for Windows 11

### Prerequisites

1. **Install Python 3** (if not already installed)
   - Download from: https://www.python.org/downloads/
   - **IMPORTANT**: During installation, check the box "Add Python to PATH"
   - Verify installation by opening PowerShell and typing: `python --version`

### Installation Steps

1. **Get the files** (choose one method):

   **Method A: Clone the repository**
   ```powershell
   git clone https://github.com/Magnivoxs/Trivia.git
   cd Trivia
   git checkout claude/expense-budget-monitor-0111yZRiSfYfnChsNcumXG2k
   ```

   **Method B: Download the files manually**
   - Download these files to a folder:
     - `expense_monitor.py`
     - `expense_demo.py`
     - `expense_showcase.py`
     - `run_expense_monitor.bat`
     - `run_showcase.bat`

2. **Run the program**:

   **Option 1: Double-click the batch file**
   - Double-click `run_expense_monitor.bat`

   **Option 2: Use PowerShell**
   ```powershell
   cd path\to\Trivia
   python expense_monitor.py
   ```

   **Option 3: Use Command Prompt**
   ```cmd
   cd path\to\Trivia
   python expense_monitor.py
   ```

### Running the Programs

#### Interactive Expense Tracker
```powershell
# Double-click: run_expense_monitor.bat
# OR run in PowerShell:
python expense_monitor.py
```

#### See the Demo/Showcase
```powershell
# Double-click: run_showcase.bat
# OR run in PowerShell:
python expense_showcase.py
```

#### Quick Demo with Sample Data
```powershell
python expense_demo.py
```

### File Locations on Windows

Your expense data will be saved in the same folder as the program:
- `expenses_data.json` - Your actual expense data
- `demo_expenses.json` - Demo data (from running demo)
- `showcase_expenses.json` - Showcase data (from running showcase)

### Troubleshooting

#### "Python is not recognized"
- Python is not installed or not in PATH
- Install Python from https://www.python.org/downloads/
- **Make sure to check "Add Python to PATH" during installation**

#### "python3: command not found"
- On Windows, use `python` instead of `python3`
- All commands should use `python expense_monitor.py`

#### Permission Issues
- Right-click the `.bat` file and select "Run as administrator"

#### File Path Issues
- Make sure you're in the correct directory
- Use `cd` to navigate: `cd C:\Users\YourName\Documents\Trivia`

### Windows-Specific Features

The program works identically on Windows 11 as on Linux/Mac:
- ✅ Full Unicode support (emojis display correctly)
- ✅ JSON data files work the same
- ✅ All features are cross-platform compatible
- ✅ Data files are portable between Windows/Linux/Mac

### Daily Usage Tips

1. **Create a desktop shortcut** to `run_expense_monitor.bat`:
   - Right-click the `.bat` file
   - Send to → Desktop (create shortcut)

2. **Pin to Start Menu**:
   - Right-click `run_expense_monitor.bat`
   - Pin to Start

3. **Run from anywhere**:
   - Add the Trivia folder to your PATH
   - Or create an alias in PowerShell profile

### Data Backup

Your expense data is stored in JSON files. To backup:
```powershell
# Backup your data
copy expenses_data.json expenses_data_backup.json

# Or backup to another location
copy expenses_data.json C:\Users\YourName\Documents\Backups\
```

### Next Steps

Once installed, read the main documentation:
- See `EXPENSE_MONITOR_README.md` for full feature details
- Run `python expense_showcase.py` to see all features in action

## Need Help?

Common PowerShell commands:
- `ls` or `dir` - List files in current directory
- `cd foldername` - Change directory
- `cd ..` - Go up one directory
- `pwd` or `cd` - Show current directory path

Happy expense tracking! 💰
