import random
num = random.randint(1, 100)
correct = False
attempts = 0
while not correct:
    guess = int(input("Guess my number 1-100: "))
    attempts += 1
    if guess == num:
        print("Congrats, you guessed it. The number was", num)
        print("It took you", attempts, "guesses.")
        correct = True
    elif guess > num:
        print("Your guess is too high.")
    else:
        print("Your guess is too low.")
