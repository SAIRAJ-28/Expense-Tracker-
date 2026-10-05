# 💰 Expense Tracker

A simple Expense Tracker application built with Python that allows users to record, view, and calculate their daily expenses through a menu-driven command-line interface.

This project was created to practice fundamental Python concepts such as lists, dictionaries, loops, conditional statements, functions, user input, and date handling.

---

## 📌 Project Overview

Managing daily expenses manually can be difficult. This Expense Tracker provides a simple way to record expenses and calculate total spending.

The application allows users to:

- Add a new expense
- View all recorded expenses
- Calculate total spending
- Exit the application

Each expense is stored as a Python dictionary containing:

- Date
- Category
- Description
- Amount

---

## ✨ Features

### 1. Add Expense

Users can enter:

- Expense date
- Expense category
- Expense description
- Amount spent

Example:

What is the spent expensive date (MM/DD/YYYY) ?: 10/05/2026
What category it belongs to ? Food
More About the Expenses: Lunch
Enter the amount spent: 150

The expense is then stored in the expense list.

---

### 2. View All Expenses

Displays all expenses entered by the user.

Example:

====== DETAILS OF EXPENSES ======

Expense Number 1 -> 10/05/2026, Food, Lunch, 150.0
Expense Number 2 -> 10/05/2026, Travel, Bus Ticket, 50.0

---

### 3. View Total Spending

Calculates the total amount spent across all recorded expenses.

Example:

```text
TOTAL SPEND = 200.0
```

---

### 4. Exit

Allows the user to safely exit the application.

---

## 🛠️ Technologies Used

- **Python 3**
- `datetime` module
- Lists
- Dictionaries
- Loops
- Conditional Statements
- User Input
- Formatted Strings (f-strings)

---

## 🧠 Python Concepts Practiced

This project helped me practice the following Python concepts:

| Concept | Usage |
|---|---|
| Variables | Store user input and calculations |
| Lists | Store multiple expenses |
| Dictionaries | Store individual expense details |
| `while` loop | Keep the application running |
| `for` loop | Display and calculate expenses |
| `if/elif/else` | Handle menu choices |
| `input()` | Get information from users |
| `float()` | Convert amount to a number |
| `datetime` | Handle expense dates |
| `strptime()` | Convert date input into a datetime object |
| f-strings | Format output |
| `append()` | Add expenses to the list |

---

## 📂 Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
└── README.md
```

---

## ▶️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/expense-tracker.git
```

### Step 2: Navigate to the Project Directory

```bash
cd expense-tracker
```

### Step 3: Run the Python Program

```bash
python expense_tracker.py
```

---

## 🖥️ Application Menu


Welcome to Expense Tracker :

==== MENU ====

1. Add Expense
2. View All Expenses
3. View Total Spending
4. Exit

Please Enter Choice:

---

## 🔄 How It Works

The basic flow of the application is:


              Start
                │
                ↓
        Display Main Menu
                │
       ┌────────┼────────┐
       ↓        ↓        ↓
   Add Expense  View    Total
       │       Expenses  Spending
       │        │        │
       └────────┼────────┘
                ↓
          Continue Menu
                │
                ↓
              Exit


---

## 📊 Data Structure

Each expense is stored as a "dictionary":

```python
expense = {
    "date": date,
    "category": category,
    "description": description,
    "amount": amount
}
```

Multiple expenses are stored inside a list:

```python
expensesList = []
```

For example:

```python
[
    {
        "date": "10/05/2026",
        "category": "Food",
        "description": "Lunch",
        "amount": 150
    },
    {
        "date": "10/05/2026",
        "category": "Travel",
        "description": "Bus Ticket",
        "amount": 50
    }
]
```



## 🎯 Learning Objective

The main objective of this project is to strengthen my understanding of **Python programming fundamentals** by building a practical command-line application.

This project demonstrates how basic Python concepts can be combined to create a useful real-world application.

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

