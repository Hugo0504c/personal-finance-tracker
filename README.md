# Personal Finance Tracker

A simple Python console application that helps users manage their personal finances by tracking incomes and expenses.

## Features

- Add income transactions
- Add expense transactions
- Assign a custom name to each transaction
- View all transactions
- View current balance
- View financial statistics
- Delete transactions by ID
- Automatic balance updates when a transaction is deleted
- User-friendly menu interface
- Input validation (invalid or negative amounts are rejected)

## How It Works

Each transaction contains:

- Unique ID
- Transaction type (Income or Expense)
- Name/Description
- Amount

Example:

```text
ID: 1 | Type: Income | Name: Salary | Amount: 1500€
ID: 2 | Type: Expense | Name: Rent | Amount: 700€
```

## Statistics Available

The application calculates:

- Total income
- Total expenses
- Number of transactions
- Number of incomes
- Number of expenses
- Average income
- Average expense

## Requirements

- Python 3.x

No external libraries are required.

## Installation

Clone the repository:

```bash
git clone https://github.com/Hugo0504c/personal-finance-tracker.git
```

Move to the project directory:

```bash
cd personal-finance-tracker
```

Run the program:

```bash
python main.py
```

## Example Usage

```text
================================
    PERSONAL FINANCE TRACKER
================================

1. Add income
2. Add expense
3. View transactions
4. View balance
5. View statistics
6. Delete transaction
0. Exit
```

## Project Structure

```text
personal-finance-tracker/
│
├── main.py
└── README.md
```

## Future Improvements

- Save transactions to a file
- Load previous transactions automatically
- Export data to CSV
- Monthly reports
- Expense categories
- Graphical User Interface (GUI)
- Charts and financial visualization

## Learning Objectives

This project was developed to practice:

- Functions
- Loops
- Lists
- Conditionals
- User input handling
- Basic data management in Python

## Author

Hugo Contreras

Follow me on Instagram (link on my GitHub profile).