from datetime import datetime

def validate_amount(value):
    try:
        amount = float(value)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        raise ValueError("Invalid amount. Must be a positive number.")

def validate_date(date_text):
    try:
        datetime.strptime(date_text, "%Y-%m-%d")
        return date_text
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")

def format_currency(amount):
    return f"₹{amount:.2f}"