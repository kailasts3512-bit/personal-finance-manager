from collections import defaultdict
from utils import format_currency

def generate_report(expenses):
    total = sum(exp.amount for exp in expenses)
    average = total / len(expenses) if expenses else 0

    category_totals = defaultdict(float)
    for exp in expenses:
        category_totals[exp.category] += exp.amount

    print("\n📊 EXPENSE REPORT")
    print(f"Total Expenses: {format_currency(total)}")
    print(f"Average Expense: {format_currency(average)}")

    print("\nCategory-wise Breakdown:")
    for category, amount in category_totals.items():
        print(f"- {category}: {format_currency(amount)}")