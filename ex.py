class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        self.expenses.append((description, amount))
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded yet.")
        else:
            print("----- Expenses -----")
            for index, (description, amount) in enumerate(self.expenses, start=1):
                print(f"{index}. {description}: ${amount}")

    def total_expenses(self):
        total = sum(amount for _, amount in self.expenses)
        print(f"Total expenses: ${total}")


def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(description, amount)
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.total_expenses()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
