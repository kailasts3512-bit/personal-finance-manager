from expense import Expense
from file_handler import (
    initialize_file, save_expense, load_expenses,
    backup_data, restore_data
)
from reports import generate_report
from utils import validate_amount, validate_date

def add_expense():
    try:
        amount = validate_amount(input("Enter amount: "))
        category = input("Enter category: ")
        date = validate_date(input("Enter date (YYYY-MM-DD): "))
        description = input("Enter description: ")

        expense = Expense(amount, category, date, description)
        save_expense(expense)
        print("✅ Expense added successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded.")
        return

    for exp in expenses:
        print(f"{exp.date} | {exp.category} | ₹{exp.amount} | {exp.description}")

def menu():
    initialize_file()
    while True:
        print("\n💰 PERSONAL FINANCE MANAGER")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Backup Data")
        print("5. Restore Data")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_report(load_expenses())
        elif choice == "4":
            backup_data()
            print("📁 Backup completed.")
        elif choice == "5":
            restore_data()
            print("🔄 Data restored.")
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice.")

if __name__ == "__main__":
    menu()