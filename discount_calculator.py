# Design a discount calculator that:
#   - Asks for the original price of an item
#   - Applies different discount rates based on purchase amount:
#       - Below $1000: No discount
#       - $1000 - $5000: 10% discount
#       - $5000 - $10000: 15% discount
#       - Above $10000: 20% discount
#   - Calculate and display the final price after discount
#   - Show how much the customer saved (discounted amount)


def discounted_price(price):

    if price < 1000:

        discount = 0.0

    elif price <= 5000:

        discount = 0.10

    elif price <= 10000:

        discount = 0.15

    else:

        discount = 0.20

    final_discount = price * discount

    final_price = price - final_discount

    return final_price, final_discount


price = None 

while True:

    print('\nWelcome to the discount calculator. To exit the program, just type exit. Otherwise, enjoy!\n')

    price = input('What is the price of your item? ')
    
    if price.lower() == 'exit':

        break

    try:

        price = float(price)

        final_price, final_discount = discounted_price(price)

        print(f'\nThe final price for your item is ${final_price:.2f}. You saved ${final_discount:.2f} dollars.\n')

    except ValueError: 

            print("\nError: Invalid input type. Please provide a number.\n")








