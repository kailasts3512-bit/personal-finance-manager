from src.expense import Expense

def test_expense_creation():
    e = Expense(100, "Food", "2025-01-01", "Lunch")
    assert e.amount == 100
