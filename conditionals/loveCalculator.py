# Project 8 - Love Calculator
# Instructions
# Write a program to test the compatibility between two people.
#
# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
#
# For Love Scores less than 10 or greater than 85, the message should be:
#
# "Your score is **x**, you go together like coke and mentos."
#
# For Love Scores between 40 and 70, the message should be:
#
# "Your score is **y**, you are alright together."
#
# Otherwise, the message will just be their score. e.g.:
#
# "Your score is **z**."
#
# Example
#
# name1 = "David"
#
# name2 = "Jennifer"
#
# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 0 times
#
# E occurs 2 times
#
# Total = 3
#
# L occurs 0 time
#
# O occurs 0 times
#
# V occurs 1 times
#
# E occurs 2 times
#
# Total = 3
#
# Love Score = 33
#
# Print: "Your score is 33."
#
# Example Input 1
# name1 = "David"
#
# name2 = "Jennifer"
#
# Example Output 1
# Your score is 33.
#
# Hint
# The lower() function changes all the letters in a string to lower case.
#
# The count() function will give you the number of times a letter occurs in a string.
#

you = input("Enter your name: ")
them = input("Enter his/her name: ")

you = you.lower()
them = them.lower()

t = you.count('t') + them.count('t')
r = you.count('r') + them.count('r')
u = you.count('u') + them.count('u')
e = you.count('e') + them.count('e')

l = you.count('l') + them.count('l')
o = you.count('o') + them.count('o')
v = you.count('v') + them.count('v')
e = you.count('e') + them.count('e')

true = t + r + u + e
love = l + o + v + e

score = int(str(true) + str(love))


if score < 10 or score > 85:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 70:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")
