# 5.0 Jedi Training (50pts)  Name:________________
import random
'''
 1. Make the following program work. LIST THE 3 MISTAKES (5pts)
   '''  
# print("This program takes three integers and returns the sum.")
# total = 0
# for i in range(3):
#     x = int(input("Enter a number: "))
#     total += x
# print("The total is:", total)

# add int to the input
# += x not += i
# "the total is:", total


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive. (5pts)
'''
# for i in range(2, 101, 2):
#     print(i)




'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop. (5pts)
'''
# i = 10
# while i >= 0:
#     print(i)
#     i -= 1
#     if i == 0:
#         print(i)
#         print("Blast off!")
#         break





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive). (5pts)
'''


# num = random.randint(1, 11)
# print(num)





'''
  5. 7 NUMBER ANALYSIS (5pts)
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
# i = 0
# total = 0
# pos = 0
# zero = 0
# neg = 0
# print("This program will ask you for 7 different numbers, and will read out an analysis")
# print("You can enter any number you want, including negatives and zero")
# while i <= 6:
#     num = int(input("Number: "))
#     if num > 0:
#         pos += 1
#     elif num < 0:
#         neg += 1
#     else:
#         zero += 1
#     total += num
#     i += 1
# print("The sum of all the numbers you gave is:", total)
# print("You gave", pos, "positive number(s).")
# print("You gave", neg, "negative number(s).")
# print("You gave", zero, "zero(s).")






'''
6. COIN TOSS PROGRAM (10pts)
-----------------
1.) Create a program that will print a random 0 or 1.
2.) Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list.
3.) Add a loop so that the program does this 50 times.
4.) Create a running total for the number of heads and the number of tails and print the total at the end.
'''
# i = 0
# h = 0
# t = 0
# while i <= 49:
#     flip = random.randint(0, 1)
#     if flip == 1:
#         print("Heads!")
#         h += 1
#     else:
#         print("Tails!")
#         t += 1
#     i += 1
# print("You flipped:", t, "amount of tails.")
# print("You flipped:", h, "amount of heads.")


'''
ROSHAMBO PROGRAM (15pts)
----------------

Create a program that randomly chooses a 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.(1 for rock, 2 for paper, 3 for scissors and 4 for quit)
I don't want to be asked to quit each time. I will enter a 4 if I want to quit.
Add conditional statements to figure out who wins and keep the records
Each round, tell me what the computer chose, what I chose and also if I won, lost or tied.
When the user quits, print an end game message and their win/loss/tie record

'''
done = False
cpu = 0
user = 0
tie = 0
print("1) Rock\n2) Paper\n3) Scissors\n4) Enter 4 to quit the game.")
while not done:
    choice = random.randint(1, 3)
    if choice == 1:
        move = "Rock"
    elif choice == 2:
        move = "Paper"
    else:
        move = "Scissors"
    u_choice = int(input("Select an option: "))
    if u_choice == 4:
        print("You won", user, "time(s)!")
        print("The computer won", cpu, "time(s)!")
        print("You and the computer tied", tie, "amount of times!")
        print("Thanks for playing my game!")
        done = True
    elif choice == 1 and u_choice == 2:
        user += 1
        print("The computer chose", move)
        print("You chose paper")
        print("You won!")
    elif choice == 1 and u_choice == 3:
        cpu += 1
        print("The computer chose", move)
        print("You chose scissors")
        print("You lost!")
    elif choice == 2 and u_choice == 1:
        cpu += 1
        print("The computer chose", move)
        print("You chose rock")
        print("You lost!")
    elif choice == 2 and u_choice == 3:
        user += 1
        print("The computer chose", move)
        print("You chose scissors")
        print("You won!")
    elif choice == 3 and u_choice == 1:
        user += 1
        print("The computer chose", move)
        print("You chose rock")
        print("You won!")
    elif choice == 3 and u_choice == 2:
        cpu += 1
        print("The computer chose", move)
        print("You chose paper")
        print("You lost!")
    else:
        tie += 1
        print("The computer chose", move)
        print("You tied!")




