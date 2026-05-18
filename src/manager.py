"""
manager.py

Handles expense operations.
"""

from models import Expense


class ExpenseManager:
    """Manages expense records."""

    def __init__(self):
        self.expenses = []

    def add_expense(self, category, amount, description, date):
        """Add new expense."""

        expense = Expense(category, amount, description, date)
        self.expenses.append(expense)

    def view_expenses(self):
        """Display all expenses."""

        if not self.expenses:
            print("No expenses found.")
            return

        for index, expense in enumerate(self.expenses, start=1):
            print(
                f"{index}. "
                f"{expense.category} | "
                f"₱{expense.amount:.2f} | "
                f"{expense.description} | "
                f"{expense.date}"
            )

    def search_expense(self, keyword):
        """Search expenses by category or description."""

        return [
            expense for expense in self.expenses
            if keyword.lower() in expense.category.lower()
            or keyword.lower() in expense.description.lower()
        ]

    def sort_by_amount(self):
        """Sort expenses by amount."""

        self.expenses.sort(key=lambda expense: expense.amount)

    def calculate_total(self):
        """Calculate total expenses."""

        return sum(expense.amount for expense in self.expenses)

    def delete_expense(self, index):
        """Delete expense by index."""

        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            return True

        return False