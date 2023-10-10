'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''

import random
# starting variables
done = False
miles_traveled = 0
thirst = 0
camel_tiredness = 0
native_distance = -20
canteen_drinks = 4

# instructions for the game
print("Welcome to the Camel Game.")
print("The objective of this game is to travel 200 miles across the desert.")
print("During your journey, a small group of natives will be chasing you.")
print("You will have a list of choices that will decide your journey.\n")
print("Your options will be:")
print("A) Drink from your canteen.")
print("B) Ahead moderate speed.")
print("C) Ahead full speed.")
print("D) Stop for the night.")
print("E) Status check.")
print("Q) Quit the game.\n")
print("To select a choice, type the letter that corresponds to the choice\n")
print("With that out of the way, lets begin the game!\n")

# loops through the game
while not done:
    # set of randomly generated variables each iteration of the loop

    # distance natives can travel during different events
    native_miles = random.randint(7, 14)
    native_oasis = random.randint(10, 14)
    rest_native = random.randint(14, 20)
    # distances you can travel depending on speed
    full_speed = random.randint(10, 20)
    moderate_speed = random.randint(5, 12)
    # random thirst for full speed
    full_thirst = random.randint(1, 2)
    # chances for tiredness to increase and oasis discovery
    tiredness = random.randint(1, 3)
    oasis_chance = random.randint(1, 20)

    # check for player distance/win requirements
    if miles_traveled >= 200:
        print("\nYou made it safely across the desert!")
        print("\033[0;32m", "Congratulations!", "\033[0m")
        print("The natives were", native_distance, "miles away from you.")
        print("\nPlay again?")
        choice = input("Y/N: ")
        if choice.lower() == "n":
            print("Thanks for playing!")
            done = True
            continue
        else:
            print("\nMay luck be in your favor!")
            miles_traveled = 0
            thirst = 0
            camel_tiredness = 0
            native_distance = -20
            canteen_drinks = 4

    # checking for thirst levels and if the player has died
    if 4 < thirst <= 6:
        print("\n", "\033[0;31m", "You are thirsty", "\033[0m")
    elif thirst > 6:
        print("\n", "\033[0;31m", "You died of thirst!", "\033[0m")
        print("You lose.")
        print("\nPlay again?")
        choice = input("Y/N: ")
        if choice.lower() == "n":
            print("No thirst for victory?")
            done = True
            continue
        else:
            print("\nGood luck this time!")
            miles_traveled = 0
            thirst = 0
            camel_tiredness = 0
            native_distance = -20
            canteen_drinks = 4

    # checking camel tiredness levels
    if 5 < camel_tiredness <= 8:
        print("\n", "\033[0;31m", "Your camel is getting tired", "\033[0m")
    elif camel_tiredness > 8:
        print("\n", "\033[0;31m", "Your camel died of overwork!", "\033[0m")
        print("How cruel can one person be!?")
        print("\nPlay again?")
        choice = input("Y/N: ")
        if choice.lower() == "n":
            print("Maybe it's better you don't kill another camel.")
            done = True
            continue
        else:
            print("\nGood luck this time!")
            miles_traveled = 0
            thirst = 0
            camel_tiredness = 0
            native_distance = -20
            canteen_drinks = 4

    # checking for native distance traveled
    if native_distance >= miles_traveled:
        print("\n", "\033[0;31m", "The natives caught up to you and your camel!", "\033[0m")
        print("You lose.")
        print("\nPlay again?")
        choice = input("Y/N: ")
        if choice.lower() == "n":
            print("Sore loser?")
            done = True
            continue
        else:
            print("\nGood luck this time!")
            miles_traveled = 0
            thirst = 0
            camel_tiredness = 0
            native_distance = -20
            canteen_drinks = 4
    elif miles_traveled - 15 <= native_distance:
        print("\n", "\033[0;31m", "The natives are getting closer!", "\033[0m")

    # options for the player
    print("\nA) Drink from your canteen.")
    print("B) Ahead moderate speed.")
    print("C) Ahead full speed.")
    print("D) Stop for the night.")
    print("E) Status check.")
    print("Q) Quit the game.\n")
    choice = input("Select a choice: ")

    # checking the oasis chance, and if 10, they find an oasis
    # resets thirst, refills canteen
    # natives have the ability to move more distance
    # doesn't allow for the user to find an oasis during status check or drinking
    if oasis_chance == 10 and choice != "e" and choice != "a":
        print("\nYou found an oasis!")
        print("You fill your canteen.")
        canteen_drinks = 5
        thirst = 0
        camel_tiredness = 0
        native_distance += native_oasis

    # checking player input for their decisions

    # quits the game
    if choice.lower() == "q":
        print("What, are you scared or something?")
        done = True
        continue
    # status check
    elif choice.lower() == "e":
        print("\nYou have traveled", miles_traveled, "miles.")
        print("You have", canteen_drinks, "drinks left in your canteen.")
        print("The natives are", abs(miles_traveled - native_distance), "miles behind you.")

    # player rest
    # natives can move further during this time
    elif choice.lower() == "d":
        camel_tiredness = 0
        native_distance += rest_native
        print("\nYou stop to rest for the night. Your camel is happy.")

    # full speed choice, thirst increases more, tiredness can increase more
    elif choice.lower() == "c":
        miles_traveled += full_speed
        print("\nYou traveled", full_speed, "miles.")
        camel_tiredness += tiredness
        native_distance += native_miles
        thirst += full_thirst

    # moderate speed choice, thirst and tiredness increase 1
    elif choice.lower() == "b":
        miles_traveled += moderate_speed
        print("\nYou traveled", moderate_speed, "miles.")
        thirst += 1
        camel_tiredness += 1
        native_distance += native_miles

    # drinking from canteen
    # checks if player has drinks left, if so, lowers thirst to 0 and decreases canteen drinks
    elif choice.lower() == "a" and canteen_drinks > 0:
        canteen_drinks -= 1
        thirst = 0
    elif choice.lower() == "a" and canteen_drinks == 0:
        print("\nYou don't have anymore drinks left in your canteen!")
        continue
