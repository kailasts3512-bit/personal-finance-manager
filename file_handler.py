import csv
import os
from expense import Expense

FILE_NAME = "expenses.csv"
BACKUP_FILE = "backup_expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Amount", "Category", "Date", "Description"])

def save_expense(expense):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(expense.to_list())

def load_expenses():
    expenses = []
    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            expenses.append(
                Expense(row["Amount"], row["Category"], row["Date"], row["Description"])
            )
    return expenses

def backup_data():
    with open(FILE_NAME, "r") as src, open(BACKUP_FILE, "w") as dest:
        dest.write(src.read())

def restore_data():
    if os.path.exists(BACKUP_FILE):
        with open(BACKUP_FILE, "r") as src, open(FILE_NAME, "w") as dest:
            dest.write(src.read())