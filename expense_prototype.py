#!/usr/bin/env python3
"""
Expense Budget Monitor - Interactive Prototype Demo
Shows various scenarios and use cases
"""

from expense_monitor import ExpenseMonitor
import time

def print_separator(title=""):
    print("\n" + "="*70)
    if title:
        print(f"  {title}")
        print("="*70)
    else:
        print("="*70)

def pause(seconds=1.5):
    """Small pause for readability"""
    time.sleep(seconds)

def scenario_1_new_month():
    """Scenario: Starting a new month with a budget"""
    print_separator("SCENARIO 1: Starting Fresh - New Month Budget")

    monitor = ExpenseMonitor('prototype_expenses.json')

    print("\n📅 It's the start of a new month!")
    print("Setting monthly budget to $3,500")
    pause()
    monitor.set_budget(3500.00)

    print("\n✅ Budget is set! Let's see the summary:")
    pause()
    monitor.show_summary()

    return monitor

def scenario_2_weekly_expenses(monitor):
    """Scenario: Adding expenses throughout the week"""
    print_separator("SCENARIO 2: Week 1 - Adding Daily Expenses")

    expenses = [
        (1200.00, "Rent", "Monthly apartment rent"),
        (85.50, "Groceries", "Monday shopping at Trader Joe's"),
        (12.50, "Transport", "Uber to work"),
        (45.00, "Dining", "Lunch with colleagues"),
        (150.00, "Utilities", "Electric, water, internet"),
        (65.30, "Groceries", "Midweek groceries"),
        (25.00, "Entertainment", "Movie tickets"),
    ]

    print("\n📝 Adding expenses as they occur throughout the week...\n")

    for amount, category, description in expenses:
        print(f"➕ Spending ${amount:.2f} on {category}")
        monitor.add_expense(amount, category, description)
        pause(0.5)

    print("\n💰 Let's check our budget after week 1:")
    pause()
    monitor.show_summary()

    return monitor

def scenario_3_categorized_view(monitor):
    """Scenario: Reviewing expenses by category"""
    print_separator("SCENARIO 3: Reviewing Spending by Category")

    print("\n🔍 Let's see where our money is going...")
    pause()
    monitor.show_expenses()

    return monitor

def scenario_4_more_spending(monitor):
    """Scenario: Adding more expenses - mid month"""
    print_separator("SCENARIO 4: Week 2-3 - More Expenses")

    expenses = [
        (200.00, "Healthcare", "Doctor visit copay"),
        (75.00, "Groceries", "Weekend shopping"),
        (120.00, "Dining", "Weekend brunch and dinner"),
        (50.00, "Transport", "Gas for car"),
        (89.99, "Shopping", "New running shoes"),
        (40.00, "Entertainment", "Concert tickets"),
        (60.00, "Groceries", "Groceries and household items"),
        (35.00, "Transport", "Parking and tolls"),
        (95.00, "Dining", "Date night"),
    ]

    print("\n📝 Adding more expenses as the month continues...\n")

    for amount, category, description in expenses:
        print(f"➕ ${amount:.2f} - {category}: {description}")
        monitor.add_expense(amount, category, description)
        pause(0.3)

    print("\n💰 Budget check after more spending:")
    pause()
    monitor.show_summary()

    return monitor

def scenario_5_overspending(monitor):
    """Scenario: Going over budget"""
    print_separator("SCENARIO 5: Uh-oh... Unexpected Expenses!")

    expenses = [
        (450.00, "Car Repair", "Brake replacement - unexpected!"),
        (80.00, "Groceries", "Weekly shopping"),
        (125.00, "Dining", "Birthday celebration"),
        (45.00, "Transport", "Rideshares"),
        (60.00, "Entertainment", "Streaming subscriptions"),
        (110.00, "Shopping", "New work clothes"),
    ]

    print("\n😰 Some unexpected expenses came up...\n")

    for amount, category, description in expenses:
        print(f"➕ ${amount:.2f} - {category}: {description}")
        monitor.add_expense(amount, category, description)
        pause(0.3)

    print("\n⚠️  Let's see how we're doing now:")
    pause()
    monitor.show_summary()

    print("\n📊 Full expense breakdown:")
    pause()
    monitor.show_expenses()

    return monitor

def scenario_6_insights(monitor):
    """Scenario: Analyzing spending patterns"""
    print_separator("SCENARIO 6: Insights & Analysis")

    total = monitor.get_total_expenses()
    remaining = monitor.get_remaining_budget()

    # Calculate category totals
    by_category = {}
    for expense in monitor.expenses:
        category = expense['category']
        if category not in by_category:
            by_category[category] = 0
        by_category[category] += expense['amount']

    print("\n📈 Spending Analysis:")
    print("-" * 70)
    print(f"\n{'Category':<20} {'Amount':>12} {'% of Budget':>15}")
    print("-" * 70)

    for category, amount in sorted(by_category.items(), key=lambda x: x[1], reverse=True):
        percentage = (amount / monitor.budget * 100)
        print(f"{category:<20} ${amount:>10.2f}   {percentage:>12.1f}%")

    print("-" * 70)
    print(f"{'TOTAL':<20} ${total:>10.2f}   {total/monitor.budget*100:>12.1f}%")
    print("="*70)

    print("\n💡 Insights:")

    # Find top spending category
    top_category = max(by_category.items(), key=lambda x: x[1])
    print(f"   • Your biggest expense is {top_category[0]} at ${top_category[1]:.2f}")

    # Find categories to watch
    discretionary = ['Dining', 'Entertainment', 'Shopping']
    discretionary_total = sum(by_category.get(cat, 0) for cat in discretionary)
    if discretionary_total > 0:
        print(f"   • Discretionary spending (Dining, Entertainment, Shopping): ${discretionary_total:.2f}")
        print(f"     That's {discretionary_total/monitor.budget*100:.1f}% of your budget")

    if remaining < 0:
        print(f"   • You're ${abs(remaining):.2f} over budget this month")
        print("   • Consider cutting back on discretionary spending next month")

    print("\n📌 Recommendations:")
    print("   • Track your spending daily to stay aware")
    print("   • Set category-specific budgets for better control")
    if 'Car Repair' in by_category or 'Healthcare' in by_category:
        print("   • Build an emergency fund for unexpected expenses")

    return monitor

def scenario_7_correction(monitor):
    """Scenario: Fixing a mistake"""
    print_separator("SCENARIO 7: Oops! Made a Mistake")

    print("\n❌ Wait, I accidentally entered a duplicate expense!")
    print("Let me delete the last entry...")
    pause()

    print("\nBefore deletion:")
    print(f"Total expenses: ${monitor.get_total_expenses():.2f}")

    monitor.delete_last_expense()
    pause()

    print(f"\nAfter deletion:")
    print(f"Total expenses: ${monitor.get_total_expenses():.2f}")

    monitor.show_summary()

    return monitor

def main():
    print("\n" + "🎯"*35)
    print("     EXPENSE BUDGET MONITOR - INTERACTIVE PROTOTYPE")
    print("🎯"*35)

    print("\nThis demo will walk through a month of expense tracking,")
    print("showing you how the program works in real-world scenarios.")
    print("\n" + "="*70)

    input("\n📍 Press ENTER to start the demo...")

    # Run through scenarios
    monitor = scenario_1_new_month()
    input("\n📍 Press ENTER to continue to Week 1...")

    monitor = scenario_2_weekly_expenses(monitor)
    input("\n📍 Press ENTER to see spending by category...")

    monitor = scenario_3_categorized_view(monitor)
    input("\n📍 Press ENTER to continue to Week 2-3...")

    monitor = scenario_4_more_spending(monitor)
    input("\n📍 Press ENTER to see what happens with unexpected expenses...")

    monitor = scenario_5_overspending(monitor)
    input("\n📍 Press ENTER to see detailed insights...")

    monitor = scenario_6_insights(monitor)
    input("\n📍 Press ENTER to see how to fix mistakes...")

    monitor = scenario_7_correction(monitor)

    print_separator("DEMO COMPLETE!")
    print("\n✅ You've seen the Expense Budget Monitor in action!")
    print("\n📝 What you learned:")
    print("   • How to set a monthly budget")
    print("   • How to track expenses with categories")
    print("   • How to monitor your spending throughout the month")
    print("   • How to identify spending patterns")
    print("   • How to correct mistakes")
    print("   • How the program warns you about budget issues")

    print("\n🚀 Ready to use it yourself?")
    print("   Run: python3 expense_monitor.py")

    print("\n💾 Your prototype data has been saved to: prototype_expenses.json")
    print("="*70 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Demo interrupted. Run again anytime!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
