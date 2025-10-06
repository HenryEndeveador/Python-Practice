# ATM Simulator

def atm(balance, pin):

    while True:  # Keep running until user exits

        print(f"\nYour current balance is ${balance}.")
        print("\nDo you want to deposit (1), withdraw (2), or exit (0)?")

        try:

            option = int(input("Choose an option: "))

        except ValueError:

            print("Please enter numbers only.")

            continue

        match option:

            case 1:

                try:

                    deposit = int(input("\nHow much would you like to deposit? "))

                    balance += deposit
                    
                    print(f"You deposited ${deposit}. New balance: ${balance}.")

                except ValueError:

                    print("Invalid amount. Please enter numbers only.")

            case 2:

                try:

                    withdraw = int(input("\nHow much would you like to withdraw? "))

                    if withdraw > balance:

                        print("Insufficient funds!")

                    else:

                        balance -= withdraw

                        print(f"You withdrew ${withdraw}. New balance: ${balance}.")

                except ValueError:

                    print("Invalid amount. Please enter numbers only.")

            case 0:

                print("\nThank you for using this bank. Goodbye!\n")

                break

            case _:

                print("Invalid choice. Please pick 0, 1, or 2.")

    return balance


# Main Program
print("\nWelcome to the ATM simulator.\n")

while True:

    try:

        pin = int(input("Please enter your PIN: "))

        if pin == 6789:

            balance = 500

            atm(balance, pin)

            break

        else:

            print("Incorrect PIN. Try again.\n")

    except ValueError:

        print("PIN must be digits only.")
