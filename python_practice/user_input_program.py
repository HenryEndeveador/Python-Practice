''' Create a program that:

Asks for the user's name

Asks for the user's age

Prints a personalized greeting

Tells the user if they are an adult (18 or older) '''


name = input("What is your name?")  #We get user input using input() function

age = int(input("What is your age?"))
          
print(f"\nHello, {name}!\n") # we add \n for adding space in the output

if age >= 18:  #We check if the user is 18 or older

 print("You are an adult.")

else:  #else statement runs if the if condition is false
 
 waiting_period = 18 - age  #We calculate how many years are left to become an adult

 print("You are not an adult! You have to wait aproximately " + str(waiting_period) + " years to become an adult.") #We use str() function to convert waiting_period to string for concatenation


'''Create a program that:

Asks user to input temperature in Celsius

Converts temperature to Fahrenheit 

Prints both Celsius and Fahrenheit temperatures

Prints whether it's considered hot (above 30°C)'''

temperature_celcius = float(input("Enter temperature in Celsius:")) #We use float() to allow decimal input

temperature_fahrenheit = (temperature_celcius * 9/5) + 32 #We convert Celsius to Fahrenheit using the formula

print(f"\nThe temperature in celcius is: {temperature_celcius} degrees celcius, whereas in fahrenheit is {temperature_fahrenheit} degrees fahrenheit") #We print the Celsius temperature

if temperature_celcius > 30 or temperature_fahrenheit > 86:  #We check if the temperature is above 30°C or 86°F
  
  print('It is considered hot!')

''' Create a user profile generator that:

Asks for user's name

Asks for user's age

Asks if they have a pet

Asks favorite color

Generates a formatted profile with all information

Converts age to boolean (is_adult)'''

name = input('What is your name?')

age = input('What is your age?')

boolean_pet = input('Do you have a pet? (yes/no)').lower() #We convert input to lowercase for consistency

favorite_color = input('What is your favorite color?')

print(f'\nUser Profile:\n')
print(f'Name: {name}\nAge: {age}\nHas Pet: {boolean_pet}\nFavorite Color: {favorite_color}')

is_adult = int(age) >= 18  #We convert age to integer and check if the user is an adult

print(f'Is Adult: {is_adult}')  #We print whether the user is an adult or not

#strip() removes leading and trailing whitespace from a string unless you specify characters to remove 

pet_name = ('#Sparkles#').strip('#')  #We remove '#' characters from the beginning and end of the string

print(f'\nPet Name: {pet_name}')  