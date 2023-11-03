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
wins = 0
loss = 0

# instructions for the game
print("Welcome to the Camel Game.")
print("The objective of this game is to travel 250 miles across the desert.")
print("During your journey, a small group of natives will be chasing you.")
print("You will have a list of choices that will decide your journey.\n")
print("Your options will be:")
print("A) Drink from your canteen.")
print("B) Ahead moderate speed.")
print("C) Ahead full speed.")
print("D) Stop for the night.")
print("E) Status check.")
print("I) Instructions.")
print("Q) Quit the game.\n")
print("To select a choice, type the letter that corresponds to the choice\n")
print("\nYou will be able to drink from a canteen, which has a capacity for 4 drinks.")
print("During your journey, you will have a small chance to find an oasis.")
print("While at an oasis, you will refill your canteen, and your camel will rest.")
print("Make sure you watch your back, before long, the natives could be right behind you!")
print("\nWith that out of the way, lets begin the game!\n")

# loops through the game
while not done:
    # set of randomly generated variables each iteration of the loop

    # distance natives can travel during different events
    native_miles = random.randint(8, 14)
    native_oasis = random.randint(10, 14)
    rest_native = random.randint(14, 20)
    sandstorm_natives = random.randint(3, 7)
    # distances you can travel depending on speed
    full_speed = random.randint(10, 20)
    moderate_speed = random.randint(5, 12)
    sandstorm_speed = random.randint(4, 9)
    before_sandstorm_movement = random.randint(1, 10)
    miles_lost_fall = random.randint(2, 5)
    cactus_severity = random.randint(1, 3)
    cactus_trip = random.randint(1, 2)
    cactus_fall = random.randint(2, 5)
    # random thirst for full speed
    full_thirst = random.randint(1, 2)
    # chances for tiredness to increase
    tiredness = random.randint(1, 3)
    # chances for random events to occur
    common_event_chance = random.randint(1, 20)
    rare_event_chance = random.randint(1, 25)
    unique_event_chance = random.randint(1, 35)
    crazy_event_chance = random.randint(1, 45)
    # boolean for dead character, camel or player
    dead_character = False
    # boolean for choice loop
    # keeps the player from manipulating random variables by restarting the loop with an invalid choice
    # generated values will stay the same if the user inputs a faulty option
    is_valid_choice = False

    # check for player distance/win requirements
    if miles_traveled >= 250:
        wins += 1
        print("\nYou made it safely across the desert!")
        print("\033[0;32m", "Congratulations!", "\033[0m")
        print("The natives were", abs(miles_traveled - native_distance), "miles away from you.")
        print("You have won", wins, "time(s)")
        print("You have lost", loss, "time(s)")
        print("\nPlay again?")
        choice = input("Y/N: ")
        while choice.lower() != "y" or choice.lower() != "n":
            if choice.lower() == "n":
                print("Thanks for playing!")
                break
            elif choice.lower() == "y":
                print("\nMay luck be in your favor!")
                miles_traveled = 0
                thirst = 0
                camel_tiredness = 0
                native_distance = -20
                canteen_drinks = 4
                break
            else:
                choice = input("Y/N: ")
                continue
        if choice.lower() == "n":
            done = True
            continue
    # checking for thirst levels and if the player has died
    if thirst > 6 or camel_tiredness > 8 or native_distance >= miles_traveled:
        dead_character = True

    if 4 < thirst <= 6 and not dead_character:
        print("\n", "\033[0;31m", "You are thirsty", "\033[0m")
    elif thirst > 6:
        loss += 1
        print("\n", "\033[0;31m", "You died of thirst!", "\033[0m")
        print("You lose.")
        print("You have lost", loss, "time(s)")
        print("You have won", wins, "times(s)")
        print("\nPlay again?")
        choice = input("Y/N: ")
        while choice.lower() != "y" or choice.lower() != "n":
            if choice.lower() == "n":
                print("No thirst for victory?")
                break
            elif choice.lower() == "y":
                print("\nGood luck this time!")
                miles_traveled = 0
                thirst = 0
                camel_tiredness = 0
                native_distance = -20
                canteen_drinks = 4
                break
            else:
                choice = input("Y/N: ")
                continue
        if choice.lower() == "n":
            done = True
            continue
    # checking camel tiredness levels
    if 5 < camel_tiredness <= 8 and not dead_character:
        print("\n", "\033[0;31m", "Your camel is getting tired", "\033[0m")
    elif camel_tiredness > 8:
        loss += 1
        print("\n", "\033[0;31m", "Your camel died of overwork!", "\033[0m")
        print("How cruel can one person be!?")
        print("You lose.")
        print("You have lost", loss, "time(s)")
        print("You have won", wins, "times(s)")
        print("\nPlay again?")
        choice = input("Y/N: ")
        while choice.lower() != "y" or choice.lower() != "n":
            if choice.lower() == "n":
                print("Maybe it's better you don't kill another camel.")
                break
            elif choice.lower() == "y":
                print("\nGood luck this time!")
                miles_traveled = 0
                thirst = 0
                camel_tiredness = 0
                native_distance = -20
                canteen_drinks = 4
                break
            else:
                choice = input("Y/N: ")
                continue
        if choice.lower() == "n":
            done = True
            continue
    # checking for native distance traveled
    if native_distance >= miles_traveled:
        loss += 1
        print("\n", "\033[0;31m", "The natives caught up to you and your camel!", "\033[0m")
        print("\nYou traveled", miles_traveled, "miles before the natives caught you.")
        print("Such a tragic fate.")
        print("You lose.")
        print("You have lost", loss, "time(s)")
        print("You have won", wins, "times(s)")
        print("\nPlay again?")
        choice = input("Y/N: ")
        while choice.lower() != "y" or choice.lower() != "n":
            if choice.lower() == "n":
                print("Sore loser?")
                break
            elif choice.lower() == "y":
                print("\nGood luck this time!")
                miles_traveled = 0
                thirst = 0
                camel_tiredness = 0
                native_distance = -20
                canteen_drinks = 4
                break
            else:
                choice = input("Y/N: ")
                continue
        if choice.lower() == "n":
            done = True
            continue
    elif miles_traveled - 15 <= native_distance:
        print("\n", "\033[0;31m", "The natives are getting closer!", "\033[0m")

    # options for the player
    # loops as long as the player inputs a wrong choice
    while not is_valid_choice:
        print("\nA) Drink from your canteen.")
        print("B) Ahead moderate speed.")
        print("C) Ahead full speed.")
        print("D) Stop for the night.")
        print("E) Status check.")
        print("I) Instructions.")
        print("Q) Quit the game.\n")
        choice = input("Select a choice: ")

        # checking the oasis chance, and if 10, they find an oasis
        # resets thirst, refills canteen
        # natives have the ability to move more distance
        # only allows an event to occur if their choice is movement related
        if choice == "c" or choice == "b":
            if common_event_chance == 10 and rare_event_chance != 12 and unique_event_chance != 15 \
                    and crazy_event_chance != 20:
                print("\n", "\033[0;32m", "You found an oasis!", "\033[0m")
                print("Your camel rests while you fill your canteen.")
                print("You are no longer thirsty.")
                canteen_drinks = 4
                thirst = 0
                camel_tiredness = 0
                native_distance += native_oasis
                is_valid_choice = True
        # checking the chance for a sandstorm to happen
        # you can either seek shelter or continue through the sandstorm
        # you have a chance to travel between 1 and 10 miles before the sandstorm breaks out
        # seeking shelter keeps you safe, but the natives can progress
        # continuing through can increase your distance, but lowers your drink amount and tires your camel
        # natives will also progress
        if choice == "c" or choice == "b":
            if common_event_chance == 11 and rare_event_chance != 12 and unique_event_chance != 15 \
                    and crazy_event_chance != 20:
                miles_traveled += before_sandstorm_movement
                print("\nYou traveled", before_sandstorm_movement, "miles before a violent"
                      "\033[1;33m", "sandstorm", "\033[0m""broke out.")
                print("Finding shelter from the sandstorm will allow you and your camel to be safe.")
                print("However, the natives will travel through the sandstorm.")
                print("Choosing to continue through the sandstorm could have many consequences.")
                print("Seek shelter from the sandstorm?")
                event_choice = input("Y/N: ")
                while event_choice.lower() != "y" or event_choice.lower() != "n":
                    if event_choice.lower() == "y":
                        print("\nA wise decision, however the natives get closer.")
                        native_distance += sandstorm_natives
                        thirst -= 1
                        break
                    elif event_choice.lower() == "n":
                        print("\nYou decide to move through the sandstorm.")
                        print("You traveled an additional", sandstorm_speed, "miles.")
                        print("You took a drink from your canteen.")
                        print("Your camel dislikes you.")
                        canteen_drinks -= 1
                        thirst = 2
                        tiredness += 2
                        native_distance += sandstorm_natives
                        miles_traveled += sandstorm_speed
                        break
                    else:
                        event_choice = input("Y/N: ")
                        continue
                is_valid_choice = True

        # checking chance to fall off of your camel
        # you lose a drink out of your canteen and potentially some distance if this happens
        if choice == "c" or choice == "b":
            if rare_event_chance == 12 and common_event_chance != 10 and common_event_chance != 11 \
                    and unique_event_chance != 15 and crazy_event_chance != 20:
                print("\nYou dozed off riding your camel and\033[0;35m", "fell off.", "\033[0m")
                print("You spilled a portion of your canteen and have one less drink.")
                print("Slight injuries cause you to lose", miles_lost_fall, "miles.")
                print("Your camel is laughing at you.")
                if canteen_drinks > 0:
                    canteen_drinks -= 1
                miles_traveled -= miles_lost_fall
                is_valid_choice = True

        # cactus event
        # can trip over a cactus, different severities have different outcomes
        if choice == "c" or choice == "b":
            if unique_event_chance == 15 and common_event_chance != 10 and common_event_chance != 11 \
                    and rare_event_chance != 12 and crazy_event_chance != 20:
                print("\nYour camel tripped over a\033[1;32m", "cactus.", "\033[0m")
                if cactus_severity == 1:
                    print("Your camel is slightly annoyed, but recovers quickly.")
                elif cactus_severity == 2:
                    print("Your camel scrapes its knee and becomes mildly annoyed.")
                    if cactus_trip == 1:
                        print("You lose 1 mile.")
                    else:
                        print("You lose 2 miles")
                    miles_traveled -= cactus_trip
                else:
                    print("Your camel took quite a\033[0;31m", "tumble.", "\033[0m")
                    print("It becomes extremely annoyed and slightly more tired.")
                    print("You lose", cactus_fall, "miles.")
                    miles_traveled -= cactus_fall
                    camel_tiredness += 1
                is_valid_choice = True

        # bad weather event, prevents the character from moving that day
        # pretty hard to get
        if choice == "c" or choice == "b":
            if crazy_event_chance == 20 and common_event_chance != 10 and common_event_chance != 11 \
                    and rare_event_chance != 12 and unique_event_chance != 15:
                print("It's bad\033[0;34m", "weather", "\033[0m""today.")
                print("You are forced to rest and don't move the entire day.")
                camel_tiredness = 1
                thirst = 1
                native_distance += native_miles
                is_valid_choice = True
                continue
        # checking player input for their decisions

        # quits the game
        if choice.lower() == "q":
            print("What, are you scared or something?")
            is_valid_choice = True
            done = True
            continue

        # status check
        elif choice.lower() == "e":
            print("\nYou have traveled", miles_traveled, "miles.")
            print("You have", canteen_drinks, "drinks left in your canteen.")
            print("The natives are", abs(miles_traveled - native_distance), "miles behind you.")
            is_valid_choice = True
            continue

        # player rest
        # natives can move further during this time
        elif choice.lower() == "d":
            camel_tiredness = 0
            native_distance += rest_native
            print("\nYou stop to rest for the night. Your camel is happy.")
            is_valid_choice = True

        # full speed choice, thirst increases more, tiredness can increase more
        elif choice.lower() == "c":
            if rare_event_chance != 12 and unique_event_chance != 15 and common_event_chance != 11:
                # normal movement if an event doesnt occur
                miles_traveled += full_speed
                print("\nYou traveled", full_speed, "miles today.")
                camel_tiredness += tiredness
                native_distance += native_miles
                thirst += full_thirst
            elif rare_event_chance == 12:
                # falling off camel event, distance calculation and proper readout after losing certain amount of miles
                miles_traveled += full_speed
                print("\nYou traveled", full_speed - miles_lost_fall, "miles today.")
                camel_tiredness += tiredness
                native_distance += native_miles
                thirst += full_thirst
            elif unique_event_chance == 15:
                # distance calculation for cactus event(s)
                if cactus_severity == 2:
                    miles_traveled += full_speed
                    print("\nYou traveled", full_speed - cactus_trip, "miles today.")
                else:
                    miles_traveled += full_speed
                    print("\nYou traveled", full_speed - cactus_fall, "miles today.")
            is_valid_choice = True

        # moderate speed choice, thirst and tiredness increase 1
        elif choice.lower() == "b":
            # normal distance if event doesn't happen
            if rare_event_chance != 12 and unique_event_chance != 15:
                miles_traveled += moderate_speed
                print("\nYou traveled", moderate_speed, "miles today.")
                thirst += 1
                camel_tiredness += 1
                native_distance += native_miles
            elif rare_event_chance == 12:
                # falling off camel event distance calculation
                miles_traveled += moderate_speed
                print("\nYou traveled", moderate_speed - miles_lost_fall, "miles today.")
                thirst += 1
                camel_tiredness += 1
                native_distance += native_miles
            elif unique_event_chance == 15:
                # cactus event distance calculation
                if cactus_severity == 2:
                    miles_traveled += moderate_speed
                    print("You traveled", moderate_speed - cactus_trip, "miles today.")
                else:
                    miles_traveled += moderate_speed
                    print("You traveled", moderate_speed - cactus_fall, "miles today.")
            is_valid_choice = True

        # drinking from canteen
        # checks if player has drinks left, if so, lowers thirst to 0 and decreases canteen drinks
        elif choice.lower() == "a" and canteen_drinks > 0:
            canteen_drinks -= 1
            thirst = 0
            is_valid_choice = True
        elif choice.lower() == "a" and canteen_drinks == 0:
            print("\nYou don't have anymore drinks left in your canteen!")
            is_valid_choice = True
        # prints out the instructions for the game again
        elif choice.lower() == "i":
            print("Welcome to the Camel Game.")
            print("The objective of this game is to travel 250 miles across the desert.")
            print("During your journey, a small group of natives will be chasing you.")
            print("You will have a list of choices that will decide your journey.\n")
            print("Your options will be:")
            print("A) Drink from your canteen.")
            print("B) Ahead moderate speed.")
            print("C) Ahead full speed.")
            print("D) Stop for the night.")
            print("E) Status check.")
            print("I) Instructions.")
            print("Q) Quit the game.\n")
            print("To select a choice, type the letter that corresponds to the choice\n")
            print("\nYou will be able to drink from a canteen, which has a capacity for 4 drinks.")
            print("During your journey, you will have a small chance to find an oasis.")
            print("While at an oasis, you will refill your canteen, and your camel will rest.")
            print("Make sure you watch your back, before long, the natives could be right behind you!")
            is_valid_choice = True
        else:
            print("That isn't an option.")
            print("Type in the letter of the choice you want to select.")
            if 4 < thirst <= 6 and not dead_character:
                print("\n", "\033[0;31m", "You are thirsty", "\033[0m")
            if 5 < camel_tiredness <= 8 and not dead_character:
                print("\n", "\033[0;31m", "Your camel is getting tired", "\033[0m")
            if miles_traveled - 15 <= native_distance:
                print("\n", "\033[0;31m", "The natives are getting closer!", "\033[0m")
            continue
