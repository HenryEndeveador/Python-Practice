# Develop a program that:
#   - Asks the user to input their monthly income
#   - Asks for expenses in different categories (rent, food, transportation, entertainment)
#   - Calculate total expenses
#   - Provide financial advice based on spending:
#       - If expenses are less than 50% of income: "Great job saving money!"
#       - If expenses are 50-75% of income: "Consider cutting some expenses"
#       - If expenses exceed 75% of income: "Warning: You're overspending"


def budget_planner(monthly_income, total_expenses):

    if monthly_income == 0:

        print('Your income cannot be 0!')

        return
    
    percentage_of_income = (total_expenses / monthly_income) * 100
    
    if percentage_of_income < 50:

        print('Great job saving money!')

    elif percentage_of_income <= 75:

        print('Consider cutting some expenses')

    else:

        print('Warning: You\'re overspending')

while True:

    try:

        monthly_income = int(input('What is your monthly income? '))
        
        rent = int(input('How much is your rent? '))

        food = int(input('How much do you spend on food? '))

        transportation = int(input('How much do you spend on transportation? '))

        entertainment = int(input('How much do you spend on entertainment? '))
        
        total_expenses = rent + food + transportation + entertainment
        
        print(f"\nTotal expenses: ${total_expenses}")

        print(f"Percentage of income: {(total_expenses / monthly_income) * 100:.1f}%")
        
        budget_planner(monthly_income, total_expenses)
        
        # Add a way to break out of the loop

        another = input("\nWould you like to calculate another budget? (yes/no): ")

        if another.lower() != 'yes':

            break
            
    except ValueError:

        print("Please enter valid numbers only!")
        
    except ZeroDivisionError:

        print("Monthly income cannot be zero!")




    






