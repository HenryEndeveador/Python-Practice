# Display the program headline

# Get user temperature in Celsius

# Convert temperature value to float

# Convert Celsius to Fahrenheit using the formula: (Celsius * 9/5) + 32

# Create clothing recommendation based on the temperature:
#   - Below 32°F (0°C): Suggest heavy winter coat, gloves, and hat
#   - Between 32°F to 50°F (0°C to 10°C): Recommend a warm jacket
#   - Between 50°F to 65°F (10°C to 18°C): Suggest a light sweater
#   - Between 65°F to 80°F (18°C to 27°C): Recommend a t-shirt
#   - Above 80°F (27°C): Suggest light, breathable clothing

# Print Fahrenheit temperature value and clothing recommendation

def temperature_converter(temperature):

    fahrenheit = (temperature * 9/5) + 32

    print(f'\nThe temperature in Fahrenheit is: {fahrenheit}°F')

    if fahrenheit < 32:

        print('\nYou should wear a heavy winter coat, with gloves and a hat!\n')

    elif fahrenheit <= 50:

        print('\nYou should wear a warm jacket!\n')

    elif fahrenheit <= 65:

        print('\nYou should wear a light sweater.\n')

    elif fahrenheit <= 80:

        print('\nYou should wear a t-shirt.\n')

    else:

        print('\nWear light, breathable clothing.\n')


while True:

    try:

        temperature = input('\nWhat is the temperature in Celsius? (or type "q" to quit): ')
    
        if temperature.lower() == 'q':

            print("Exiting program. Stay safe!")

            break  # exit the loop

        temperature = float(temperature)  # convert input to float

        temperature_converter(temperature)

    except ValueError:
        
        print('Invalid input. Please enter a numeric value for temperature.')




                  

