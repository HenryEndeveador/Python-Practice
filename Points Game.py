#Write a Python program where we start with 10 points, and depending on the action, then change the value of points.

def point_game():

    points = 10  # Starting points

    while True:  # Keep asking until a valid option is given

        print("\nChoose an action:")
        print("a. Earn 5 points")
        print("b. Lose 3 points")
        print("c. Double the points")
        print("d. Halve the points")
        print("e. Add bonus points")

        action = input("Enter your action (a–e): ").lower() #.lower() – lets the user type uppercase or lowercase letters. 

        if action == "a":
            points += 5
            break
        elif action == "b":
            points -= 3
            break
        elif action == "c":
            points *= 2
            break
        elif action == "d":
            points /= 2
            break
        elif action == "e":
            points **= 2
            break
        else:
            print("Invalid input, please enter a valid option.")

    print(f"Your points: {points}")

point_game()
