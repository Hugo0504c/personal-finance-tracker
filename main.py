#We define the function that shows the "menu"
def intro():
    print("\n" * 41)
    print("================================")
    print("    PERSONAL FINANCE TRACKER    ")
    print("================================")
    print()
    print("1. Add income")
    print("2. Add expense")
    print("3. View transactions")
    print("4. View balance")
    print("5. View statistics")
    print("6. Delete transaction")
    print("0. Exit")


#We define functions for the different actions
def pause():
    input("\nPress Enter to return to the main menu...")


def ask_amount(message):
    #Keeps asking until the user writes a positive number
    while True:
        try:
            amount = float(input(message))
        except ValueError:
            print("Please introduce a valid number.")
            continue

        if amount <= 0:
            print("The amount must be greater than 0.")
            continue

        return amount


def add_income(balance, transactions, next_id):
    income = ask_amount("Introduce the income you want to add: ")
    name = input("Introduce a name for this income: ")

    balance += income

    transactions.append([next_id, "Income", name, income])

    print("Income successfully added.")
    pause()

    return balance, next_id + 1


def add_expense(balance, transactions, next_id):
    expense = ask_amount("Introduce the expense you want to add: ")
    name = input("Introduce a name for this expense: ")

    balance -= expense

    transactions.append([next_id, "Expense", name, expense])

    print("Expense successfully added.")
    pause()

    return balance, next_id + 1


def view_transactions(transactions):

    if len(transactions) == 0:
        print("There are no transactions.")

    else:
        print("\n===== TRANSACTIONS =====\n")

        for transaction in transactions:
            print(
                f"ID: {transaction[0]} | "
                f"Type: {transaction[1]} | "
                f"Name: {transaction[2]} | "
                f"Amount: {transaction[3]:.2f}€"
            )

    pause()


def view_balance(balance):

    print("\n===== BALANCE =====")
    print(f"Current balance: {balance:.2f}€")

    pause()


def view_statistics(transactions):

    total_income = 0
    total_expense = 0

    income_count = 0
    expense_count = 0

    for transaction in transactions:

        if transaction[1] == "Income":
            total_income += transaction[3]
            income_count += 1

        elif transaction[1] == "Expense":
            total_expense += transaction[3]
            expense_count += 1

    total_transactions = len(transactions)

    if income_count > 0:
        average_income = total_income / income_count
    else:
        average_income = 0

    if expense_count > 0:
        average_expense = total_expense / expense_count
    else:
        average_expense = 0

    print("\n===== STATISTICS =====")
    print(f"Total income: {total_income:.2f}€")
    print(f"Total expenses: {total_expense:.2f}€")
    print(f"Number of transactions: {total_transactions}")
    print(f"Number of incomes: {income_count}")
    print(f"Number of expenses: {expense_count}")
    print(f"Average income: {average_income:.2f}€")
    print(f"Average expense: {average_expense:.2f}€")

    pause()


def delete_transaction(balance, transactions):

    if len(transactions) == 0:
        print("There are no transactions to delete.")
        pause()
        return balance

    try:
        id_to_delete = int(input("Introduce the transaction ID: "))
    except ValueError:
        print("Invalid ID. It must be a number.")
        pause()
        return balance

    for transaction in transactions:

        if transaction[0] == id_to_delete:

            if transaction[1] == "Income":
                balance -= transaction[3]

            elif transaction[1] == "Expense":
                balance += transaction[3]

            print(
                f"Transaction '{transaction[2]}' deleted successfully."
            )

            transactions.remove(transaction)

            pause()

            return balance

    print("Transaction not found.")
    pause()

    return balance


#We define the initial parameters
balance = 0.0
transactions = []
next_id = 1


#Main program
while True:

    intro()

    try:
        action = int(input("Action: "))
    except ValueError:
        print("Invalid option.")
        pause()
        continue

    #We define what happens for each action

    if action == 0:

        print("Thank you for using Personal Finance Tracker.")
        break

    elif action == 1:

        balance, next_id = add_income(
            balance,
            transactions,
            next_id
        )

    elif action == 2:

        balance, next_id = add_expense(
            balance,
            transactions,
            next_id
        )

    elif action == 3:

        view_transactions(transactions)

    elif action == 4:

        view_balance(balance)

    elif action == 5:

        view_statistics(transactions)

    elif action == 6:

        balance = delete_transaction(
            balance,
            transactions
        )

    else:

        print("Invalid option.")
        pause()