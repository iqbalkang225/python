# Guessing the Number
# Instruction
# Create a program will generate a random number unknown to the user between upper and lower bond that user provided.
# The user needs to guess what that number is. If the user’s guess is wrong, the program should return some sort of indication as to how wrong
# (e.g. The number is too high or too low). If the user guesses correctly, a positive indication should appear.
#
# Your program should ask for upper and lower bound from the user initially.
#
# Calculate chances of user based on upper and lower bounds.
#
# Based on calculated number of chances ask input from user for guessing the number.
#
# If the guessed number is greater than the generated number then print - "You guessed too high", otherwise print - "You guessed too low".
# And finally if the numbers match print - "Congratulations you did it in"
#
# Output can be like this:
#
# Enter Lower bound: 1
# Enter Upper bound: 7
#     You've only  3  chances to guess the integer!
# Guess a number: 4
# You Guessed too high!
# Guess a number: 1
# You guessed too small!
# Guess a number: 2
# Congratulations you did it in  3  try
# The number is 2
#     Better Luck Next time!


import random

def guess_number():
    lower_bound = int(input("Enter Lower Bound: "))
    upper_bound = int(input("Enter Upper Bound: "))

    lives_left = 3
    retry = True

    random_number = random.randint(lower_bound, upper_bound)
    print(random_number)

    while retry:

        if lives_left == 0:
            print(f"The number is {random_number} \n Better Luck Next time!")
            break

        user_guess = int(input("Guess a number: "))

        if user_guess < random_number:
            lives_left -= 1
            print("You guessed too small!")
        elif user_guess > random_number:
            lives_left -= 1
            print("You guessed too high!")
        else:
            lives_left -= 1
            print(f"Congratulations you did it in {3 - lives_left} tries")
            retry = False


guess_number()