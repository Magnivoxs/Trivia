#!/usr/bin/env python3
"""
Monthly Expense Budget Monitor
A simple interactive program to track expenses against a monthly budget
"""

import json
import os
from datetime import datetime
from typing import List, Dict

class ExpenseMonitor:
    def __init__(self, data_file='expenses_data.json'):
        self.data_file = data_file
        self.budget = 0
        self.expenses = []
        self.load_data()

    def load_data(self):
        """Load budget and expenses from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.budget = data.get('budget', 0)
                    self.expenses = data.get('expenses', [])
                print(f"✓ Loaded existing data from {self.data_file}")
            except json.JSONDecodeError:
                print(f"⚠ Could not read {self.data_file}, starting fresh")
        else:
            print("Starting with new expense tracker")

    def save_data(self):
        """Save budget and expenses to file"""
        data = {
            'budget': self.budget,
            'expenses': self.expenses
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✓ Data saved to {self.data_file}")

    def set_budget(self, amount: float):
        """Set the monthly budget"""
        self.budget = amount
        self.save_data()
        print(f"✓ Monthly budget set to ${amount:.2f}")

    def add_expense(self, amount: float, category: str, description: str = ""):
        """Add a new expense"""
        expense = {
            'amount': amount,
            'category': category,
            'description': description,
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.expenses.append(expense)
        self.save_data()
        print(f"✓ Added expense: ${amount:.2f} ({category})")

    def get_total_expenses(self) -> float:
        """Calculate total expenses"""
        return sum(expense['amount'] for expense in self.expenses)

    def get_remaining_budget(self) -> float:
        """Calculate remaining budget"""
        return self.budget - self.get_total_expenses()

    def show_summary(self):
        """Display budget summary"""
        total_expenses = self.get_total_expenses()
        remaining = self.get_remaining_budget()
        percentage_used = (total_expenses / self.budget * 100) if self.budget > 0 else 0

        print("\n" + "="*50)
        print("BUDGET SUMMARY")
        print("="*50)
        print(f"Monthly Budget:    ${self.budget:>10.2f}")
        print(f"Total Expenses:    ${total_expenses:>10.2f} ({percentage_used:.1f}%)")
        print(f"Remaining:         ${remaining:>10.2f}")

        if remaining < 0:
            print("\n⚠️  WARNING: You are over budget!")
        elif remaining < self.budget * 0.2:
            print("\n⚠️  CAUTION: Less than 20% of budget remaining")
        else:
            print("\n✓ Budget is on track")
        print("="*50)

    def show_expenses(self):
        """Display all expenses"""
        if not self.expenses:
            print("\nNo expenses recorded yet.")
            return

        print("\n" + "="*70)
        print("EXPENSE HISTORY")
        print("="*70)

        # Group by category
        by_category = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(expense)

        for category, items in sorted(by_category.items()):
            category_total = sum(item['amount'] for item in items)
            print(f"\n📁 {category.upper()} - Total: ${category_total:.2f}")
            print("-" * 70)

            for expense in items:
                date = expense['date']
                amount = expense['amount']
                desc = expense['description']
                desc_str = f" - {desc}" if desc else ""
                print(f"  {date}  ${amount:>8.2f}{desc_str}")

        print("="*70)

    def clear_expenses(self):
        """Clear all expenses (start new month)"""
        self.expenses = []
        self.save_data()
        print("✓ All expenses cleared (new month started)")

    def delete_last_expense(self):
        """Delete the most recent expense"""
        if self.expenses:
            deleted = self.expenses.pop()
            self.save_data()
            print(f"✓ Deleted: ${deleted['amount']:.2f} ({deleted['category']})")
        else:
            print("No expenses to delete")


def print_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("EXPENSE BUDGET MONITOR - MAIN MENU")
    print("="*50)
    print("1. Set/Update Monthly Budget")
    print("2. Add Expense")
    print("3. View Budget Summary")
    print("4. View All Expenses")
    print("5. Delete Last Expense")
    print("6. Clear All Expenses (New Month)")
    print("7. Exit")
    print("="*50)


def main():
    """Main program loop"""
    monitor = ExpenseMonitor()

    print("\n🎯 Welcome to Expense Budget Monitor!")

    # If no budget set, prompt to set one
    if monitor.budget == 0:
        print("\nLet's start by setting your monthly budget.")
        try:
            amount = float(input("Enter your monthly budget: $"))
            monitor.set_budget(amount)
        except ValueError:
            print("Invalid amount. You can set it later from the menu.")

    # Main loop
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == '1':
            try:
                amount = float(input("Enter monthly budget: $"))
                monitor.set_budget(amount)
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")

        elif choice == '2':
            try:
                amount = float(input("Enter expense amount: $"))
                category = input("Enter category (e.g., Food, Transport, Entertainment): ").strip()
                description = input("Enter description (optional): ").strip()
                monitor.add_expense(amount, category, description)

                # Show quick summary after adding expense
                remaining = monitor.get_remaining_budget()
                print(f"Remaining budget: ${remaining:.2f}")
            except ValueError:
                print("❌ Invalid amount. Please enter a number.")

        elif choice == '3':
            monitor.show_summary()

        elif choice == '4':
            monitor.show_expenses()

        elif choice == '5':
            monitor.delete_last_expense()

        elif choice == '6':
            confirm = input("⚠️  Clear all expenses? This cannot be undone (y/n): ").strip().lower()
            if confirm == 'y':
                monitor.clear_expenses()

        elif choice == '7':
            print("\n👋 Thank you for using Expense Budget Monitor!")
            break

        else:
            print("❌ Invalid choice. Please enter 1-7.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting... Goodbye!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
