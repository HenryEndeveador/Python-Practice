# Build a basic login system that:
#
# - Has a predefined correct username and password
# - Allows 3 login attempts
# - Provides different messages based on login attempts:
#       - Correct credentials: "Login Successful! Welcome to Python Authentication Program."
#       - Wrong credentials: "Invalid username or password"
#       - After 3 failed attempts: "Account locked. Please contact support"
#         HINT: Use loop


username = 'Loksahumm34'
password = 'yworldpp230032M'

def credentials(stored_username, stored_password, max_attempts=3):

    attempts_left = max_attempts

    for i in range(3):

        # Ask for credentials each attempt
        entered_username = input('What is your username? ').strip()

        entered_password = input('What is your password? ').strip()

        # Compare (username case-insensitive)
        if entered_username.lower() == stored_username.lower() and entered_password == stored_password:

            print('Login Successful! Welcome to Python Authentication Program.')
            
            break  # stop on success

        elif not entered_username.lower() == stored_username.lower() or not entered_password == stored_password:

            attempts_left -= 1

            print(f'Invalid username or password. {attempts_left} attempts remaining.')


        if attempts_left == 0:

            print('Account locked. Please contact support.')

            break  # locked after last try

# Call once
try:

    credentials(username, password)

except Exception as e:

    print('An error occurred:', e)



        