# 💰Personal Finance Manager

A comprehensive **command-line based Personal Finance Management System** built using Python.  
This project helps users **track expenses, analyze spending patterns, generate reports**, and safely **backup & restore financial data** using CSV-based persistence.

---

## 🚀 Features

- 📌 Add and manage daily expenses
- 📂 Persistent storage using CSV files
- 🧠 Object-Oriented Design (OOP)
- 📊 Detailed expense reports:
  - Total expenses
  - Average expenses
  - Category-wise breakdown
- 🛡️ Robust input validation & error handling
- 💾 Data backup and restore functionality
- 🖥️ Interactive, menu-driven Command Line Interface
- 🧩 Modular and scalable code structure

---

## 🛠️ Technologies Used

- **Python 3**
- CSV module (file handling)
- Object-Oriented Programming (OOP)
- Command Line Interface (CLI)

---

## 📁 Project Structure
├── expense.py # Expense class (OOP)
├── file_handler.py # CSV operations, backup & restore
├── reports.py # Expense analysis & reports
├── utils.py # Input validation & formatting
├── main.py # Command-line interface
├── expenses.csv # Expense data (auto-created)
├── backup_expenses.csv # Backup file

2. Navigate to the Project Folder
cd personal-finance-manager

3. Run the Application
python main.py

4. Sample Menu Output
💰 PERSONAL FINANCE MANAGER
1. Add Expense
2. View Expenses
3. Generate Report
4. Backup Data
5. Restore Data
6. Exit

5. Sample Report Output
📊 EXPENSE REPORT
Total Expenses: ₹12,500.00
Average Expense: ₹2,500.00

Category-wise Breakdown:
- Food: ₹4,000.00
- Transport: ₹2,000.00
- Shopping: ₹6,500.00

Data Safety
All expenses are stored in a CSV file
Backup feature allows secure data copying
Restore feature recovers data from backup in case of loss

Learning Outcomes
Practical use of Python OOP
File handling with CSV
Modular code organization
CLI-based application design
Real-world data analysis logic

Future Enhancements
📅 Monthly & yearly trend analysis
📈 Graphical visualization
🖼️ GUI using Tkinter or Streamlit
🗄️ Database integration (SQLite)
📤 Export reports to PDF/Excel

Author
Kailas TS
📧 Email: kailasts3512@gmail.com

