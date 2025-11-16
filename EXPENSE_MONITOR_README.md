# Expense Budget Monitor

A simple, interactive Python program to track your monthly expenses against a budget.

## Features

- Set and update monthly budget
- Add expenses with categories and descriptions
- View budget summary with percentage used
- View expenses grouped by category
- Delete last expense (undo feature)
- Clear all expenses to start a new month
- Data persists between sessions (saved to JSON file)
- Visual warnings when budget is running low or exceeded

## Files Created

- `expense_monitor.py` - Main interactive program
- `expense_demo.py` - Demo script showing functionality
- `expenses_data.json` - Your actual expense data (created on first run)
- `demo_expenses.json` - Demo data (created by demo script)

## How to Run

### Interactive Mode (Recommended)

Run the program interactively:

```bash
python3 expense_monitor.py
```

This will show you a menu with options:
1. Set/Update Monthly Budget
2. Add Expense
3. View Budget Summary
4. View All Expenses
5. Delete Last Expense
6. Clear All Expenses (New Month)
7. Exit

### Demo Mode

To see a quick demo with sample data:

```bash
python3 expense_demo.py
```

## Usage Examples

### Setting Your Budget

When you first run the program, you'll be prompted to set your monthly budget:
```
Enter your monthly budget: $2000
```

### Adding Expenses

Select option 2 from the menu:
```
Enter expense amount: $85.50
Enter category: Groceries
Enter description: Whole Foods shopping
```

### Viewing Summary

Option 3 shows you:
- Total budget
- Total expenses
- Percentage used
- Remaining budget
- Warning if over budget or running low

### Viewing All Expenses

Option 4 displays all expenses grouped by category with totals.

## Tips

- Use consistent category names (e.g., always "Groceries", not "groceries" or "Food")
- Add descriptions to help remember what each expense was for
- Check your summary regularly to stay on track
- Start a new month by clearing expenses (option 6)

## Customization

You can easily modify the program to:
- Add expense limits per category
- Export data to CSV
- Generate monthly reports
- Set up recurring expenses
- Add date range filtering

Just let me know what features you'd like to add!
