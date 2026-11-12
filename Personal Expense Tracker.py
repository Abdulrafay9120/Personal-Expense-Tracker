print("===== Personal Expense Tracker =====")

name = input("Enter your name: ")

budget = float(input("Enter your monthly budget: "))

total_expenses = 0
expense_count = 0

while True:

    expense_name = input("\nEnter expense name (or type 'done' to finish): ")

    if expense_name == "done":
        break

    amount = float(input("Enter expense amount: "))

    total_expenses = total_expenses + amount
    expense_count = expense_count + 1

remaining_budget = budget - total_expenses

print("\n===== Expense Report =====")

print("Name:", name)
print("Monthly Budget:", budget)
print("Total Expenses:", total_expenses)
print("Number of Expenses:", expense_count)
print("Remaining Budget:", remaining_budget)

if remaining_budget > 0:
    print("Status: You are within your budget!")

elif remaining_budget == 0:
    print("Status: You have used your entire budget!")

else:
    print("Status: You have exceeded your budget!")

print("\nThank you for using Expense Tracker!")
