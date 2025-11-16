#!/usr/bin/env python3
"""
Expense Budget Monitor - Full Showcase (No pauses/inputs)
"""

from expense_monitor import ExpenseMonitor

def print_separator(title=""):
    print("\n" + "="*70)
    if title:
        print(f"  {title}")
        print("="*70)

print("\n" + "🎯"*35)
print("     EXPENSE BUDGET MONITOR - LIVE SHOWCASE")
print("🎯"*35)

# SCENARIO 1: New Month
print_separator("SCENARIO 1: Starting Fresh - New Month Budget")
monitor = ExpenseMonitor('showcase_expenses.json')
print("\n📅 It's the start of a new month!")
print("Setting monthly budget to $3,500")
monitor.set_budget(3500.00)
print("\n✅ Budget is set! Let's see the summary:")
monitor.show_summary()

# SCENARIO 2: Week 1 Expenses
print_separator("SCENARIO 2: Week 1 - Adding Daily Expenses")
expenses_week1 = [
    (1200.00, "Rent", "Monthly apartment rent"),
    (85.50, "Groceries", "Monday shopping at Trader Joe's"),
    (12.50, "Transport", "Uber to work"),
    (45.00, "Dining", "Lunch with colleagues"),
    (150.00, "Utilities", "Electric, water, internet"),
    (65.30, "Groceries", "Midweek groceries"),
    (25.00, "Entertainment", "Movie tickets"),
]

print("\n📝 Adding expenses as they occur throughout the week...\n")
for amount, category, description in expenses_week1:
    print(f"➕ Spending ${amount:.2f} on {category}")
    monitor.add_expense(amount, category, description)

print("\n💰 Budget check after week 1:")
monitor.show_summary()

# SCENARIO 3: Category View
print_separator("SCENARIO 3: Reviewing Spending by Category")
print("\n🔍 Let's see where our money is going...")
monitor.show_expenses()

# SCENARIO 4: Week 2-3 Expenses
print_separator("SCENARIO 4: Week 2-3 - More Expenses")
expenses_mid = [
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
for amount, category, description in expenses_mid:
    print(f"➕ ${amount:.2f} - {category}: {description}")
    monitor.add_expense(amount, category, description)

print("\n💰 Budget check after more spending:")
monitor.show_summary()

# SCENARIO 5: Unexpected Expenses
print_separator("SCENARIO 5: Uh-oh... Unexpected Expenses!")
expenses_late = [
    (450.00, "Car Repair", "Brake replacement - unexpected!"),
    (80.00, "Groceries", "Weekly shopping"),
    (125.00, "Dining", "Birthday celebration"),
    (45.00, "Transport", "Rideshares"),
    (60.00, "Entertainment", "Streaming subscriptions"),
    (110.00, "Shopping", "New work clothes"),
    (320.00, "Groceries", "Big monthly restock"),
]

print("\n😰 Some unexpected expenses came up...\n")
for amount, category, description in expenses_late:
    print(f"➕ ${amount:.2f} - {category}: {description}")
    monitor.add_expense(amount, category, description)

print("\n⚠️  Let's see how we're doing now:")
monitor.show_summary()

print("\n📊 Full expense breakdown:")
monitor.show_expenses()

# SCENARIO 6: Analysis
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
    bar_length = int(percentage / 3)
    bar = "█" * bar_length
    print(f"{category:<20} ${amount:>10.2f}   {percentage:>12.1f}%  {bar}")

print("-" * 70)
print(f"{'TOTAL':<20} ${total:>10.2f}   {total/monitor.budget*100:>12.1f}%")
print("="*70)

print("\n💡 Insights:")
top_category = max(by_category.items(), key=lambda x: x[1])
print(f"   • Your biggest expense is {top_category[0]} at ${top_category[1]:.2f}")

discretionary = ['Dining', 'Entertainment', 'Shopping']
discretionary_total = sum(by_category.get(cat, 0) for cat in discretionary)
if discretionary_total > 0:
    print(f"   • Discretionary spending: ${discretionary_total:.2f} ({discretionary_total/monitor.budget*100:.1f}%)")

if remaining < 0:
    print(f"   • You're ${abs(remaining):.2f} over budget this month")
    print("   • Consider these high-impact cuts:")
    for cat in ['Dining', 'Shopping', 'Entertainment']:
        if cat in by_category:
            print(f"     - Reduce {cat} by 20% = Save ${by_category[cat] * 0.2:.2f}")

print("\n📌 Recommendations:")
print("   ✓ Track your spending daily to stay aware")
print("   ✓ Set category-specific budgets for better control")
print("   ✓ Build an emergency fund for unexpected expenses")
print("   ✓ Look for ways to reduce grocery costs (meal planning)")
print("   ✓ Consider limiting dining out to special occasions")

# SCENARIO 7: Correction
print_separator("SCENARIO 7: Fixing a Mistake")
print("\n❌ Oops! That last expense was entered wrong...")
print("Let me delete it and fix it...")

print(f"\nBefore: Total expenses = ${monitor.get_total_expenses():.2f}")
monitor.delete_last_expense()
print(f"After deletion: Total expenses = ${monitor.get_total_expenses():.2f}")

print("\n✅ Now adding the correct amount...")
monitor.add_expense(150.00, "Groceries", "Big monthly restock (corrected)")
print(f"Corrected total: ${monitor.get_total_expenses():.2f}")

monitor.show_summary()

print_separator("SHOWCASE COMPLETE!")
print("\n✅ You've seen the Expense Budget Monitor in action!")
print("\n📝 Key Features Demonstrated:")
print("   ✓ Set monthly budgets")
print("   ✓ Track expenses with categories and descriptions")
print("   ✓ Real-time budget monitoring")
print("   ✓ Visual warnings when over budget")
print("   ✓ Detailed categorized expense views")
print("   ✓ Spending analysis and insights")
print("   ✓ Easy error correction")
print("   ✓ Persistent data storage")

print("\n🚀 Ready to track your own expenses?")
print("   Run: python3 expense_monitor.py")
print("\n💾 Showcase data saved to: showcase_expenses.json")
print("="*70 + "\n")
