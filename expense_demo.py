#!/usr/bin/env python3
"""
Demo script to showcase the Expense Monitor functionality
"""

from expense_monitor import ExpenseMonitor

def run_demo():
    print("="*60)
    print("EXPENSE BUDGET MONITOR - DEMO")
    print("="*60)

    # Create a monitor instance with a demo file
    monitor = ExpenseMonitor('demo_expenses.json')

    print("\n1️⃣  Setting monthly budget to $2000")
    monitor.set_budget(2000.00)

    print("\n2️⃣  Adding some sample expenses...")
    monitor.add_expense(350.00, "Rent", "Monthly rent payment")
    monitor.add_expense(85.50, "Groceries", "Whole Foods shopping")
    monitor.add_expense(45.20, "Transport", "Gas for car")
    monitor.add_expense(60.00, "Entertainment", "Movie night and dinner")
    monitor.add_expense(120.00, "Utilities", "Electric and water bill")
    monitor.add_expense(42.75, "Groceries", "Local market")
    monitor.add_expense(30.00, "Transport", "Uber ride")

    print("\n3️⃣  Viewing budget summary...")
    monitor.show_summary()

    print("\n4️⃣  Viewing all expenses by category...")
    monitor.show_expenses()

    print("\n" + "="*60)
    print("📊 DEMO COMPLETE!")
    print("="*60)
    print("\nTo use the interactive program, run:")
    print("  python3 expense_monitor.py")
    print("\nYour demo data has been saved to: demo_expenses.json")
    print("The main program saves to: expenses_data.json")
    print("="*60)

if __name__ == "__main__":
    run_demo()
