# Dice Rolling
# Instruction
# When the program runs, it will randomly choose a number between 1 and 6. Then program will print what that number is.
# It should then ask you if you’d like to roll again.
#
# Output
# Dice1: 3
# Dice2: 6
# Roll the dice again? (Y/N)

import random


def random_number():
    return random.randint(1, 6)

def roll_dice():
    dice1 = random_number()
    dice2 = random_number()

    print(f'Dice1: {dice1}')
    print(f'Dice2: {dice2}')

def roll_again():
    roll_dice()

    while True:
        roll_again = input('Roll the dice again? (Y/N) ')

        if roll_again == 'n':
            quit()

        roll_dice()


roll_again()