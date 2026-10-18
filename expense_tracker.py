"""
=== EXPENSE TRACKER ===

1. Add an expense
2. Display expenses
3. Calculate the total
4. Display the largest expense
5. Search for an expense
6. Delete an expense
7. Quit
"""

# List of expenses
expenses = []


def add_expense():
    # Ask the user to enter an expense amount
    expense = float(input("Expense amount: "))
    expenses.append(expense)


def display_expenses():
    # Display all expenses
    for expense in expenses:
        print(expense)


def calculate_total():
    # Calculate the total of all expenses
    total = sum(expenses)
    return total


def largest_expense():
    # Check if there are no expenses
    if len(expenses) == 0:
        print("No expenses")
    else:
        # Find and display the largest expense
        largest = max(expenses)
        print("The largest expense is:", largest)


def search_expense():
    # Ask for the amount to search for
    amount = float(input("Amount to search for: "))

    # Check if the expense exists
    if amount in expenses:
        print("Expense found")
    else:
        print("Expense not found")


def delete_expense():
    # Ask for the amount to delete
    amount = float(input("Amount to delete: "))

    # Check if the expense exists before deleting it
    if amount in expenses:
        expenses.remove(amount)
        print("Expense deleted")
    else:
        print("Expense not found")


# Add three expenses
add_expense()
add_expense()
add_expense()

# Test the list of expenses
assert expenses == [10, 25, 5]

# Test the total calculation
assert calculate_total() == 40

# Test the largest expense
assert largest_expense() == 25

# Test searching for an expense
assert search_expense(25) == True
assert search_expense(50) == False

# Test deleting an expense
assert delete_expense(25) == True
