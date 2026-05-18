"""
main.py

Main CLI application.
"""

from manager import ExpenseManager
from storage import save_expenses, load_expenses


manager = ExpenseManager()
manager.expenses = load_expenses()


def main():
    """Run the application."""

    while True:
        print("\n==== Expense Tracker CLI ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Search Expense")
        print("4. Sort Expenses")
        print("5. Expense Summary")
        print("6. Delete Expense")
        print("7. Save Data")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            category = input("Category: ")

            try:
                amount = float(input("Amount: "))
            except ValueError:
                print("Invalid amount.")
                continue

            description = input("Description: ")
            date = input("Date (YYYY-MM-DD): ")

            manager.add_expense(
                category,
                amount,
                description,
                date
            )
            
            save_expenses(manager.expenses)
            print("Expense added successfully.")

        elif choice == "2":
            manager.view_expenses()

        elif choice == "3":

            keyword = input("Search keyword: ")

            results = manager.search_expense(keyword)

            if results:
                for expense in results:
                    print(
                        f"{expense.category} | "
                        f"₱{expense.amount:.2f} | "
                        f"{expense.description}"
                    )
            else:
                print("No matching expenses found.")

        elif choice == "4":
            manager.sort_by_amount()
            print("Expenses sorted successfully.")

        elif choice == "5":

            total = manager.calculate_total()

            print(f"Total Expenses: ₱{total:.2f}")

        elif choice == "6":

            manager.view_expenses()

            try:
                index = int(input("Expense number to delete: ")) - 1

                if manager.delete_expense(index):
                    save_expenses(manager.expenses)
                    print("Expense deleted.")
                else:
                    print("Invalid expense number.")

            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == "7":
            save_expenses(manager.expenses)
            print("Data saved successfully.")

        elif choice == "8":
            save_expenses(manager.expenses)
            print("Exiting application. Goodbye!")
            break

        else:
            print("Invalid choice. Please input a number.")


if __name__ == "__main__":
    main()