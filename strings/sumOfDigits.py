# Sum of Digits
# Write a program which asks for any given integer number from the console and prints out the sum of digits of given number.
#
# Input
#
# Enter an integer number: 134
#
# Output
#
# 8

def sum_of_digits():
    user_input = input('Enter a number: ')

    total = 0

    for char in user_input:
        total = total + int(char)

    return total


print(sum_of_digits())