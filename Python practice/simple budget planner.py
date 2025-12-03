#Simple Budget Planner


def budget_planner():

    budget = int(input("What is your budget for the month? ")) #We use input() to get the budget from the user

    expenses_names = ["Rent", "Groceries", "Utilities", "Entertainment"]  #Since we want to loop through the names, list needs to be strings

    remaining_balance = budget

    for expense in expenses_names:

        choice = int(input(f"How much do you want to spend on {expense}? ")) #We use int() to convert the input to an integer

        remaining_balance -= choice

    if remaining_balance < 0:

        print(f"You have exceeded your budget by ${abs(remaining_balance)}") #abs() is used to get the absolute value of the negative balance

    elif remaining_balance < 50:

        print("You have less than $50 left in your account")

    else:

        print(f"You have ${remaining_balance} left in your account")

    return remaining_balance

budget_planner()
