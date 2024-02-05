# Password Generator
# Instruction
# Create a program will generate a password based on user inputs. Initial variables are already provided.
#
# letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# nums = "1234567890"
# symbols = "-+=!@#$%^&*"
#
# Your program should ask for number of letters, symbols and numbers initially
#
# Then based on these inputed values it will generate password
#
# Output can be like this:
#
# How many letters do you want in your password? 8
# How many numbers do you want in your password? 8
# How many symbols do you want in your password? 2
# Your password is: EDUpEYIG67*@
#
# Hint
# Use choice() function from random module to select random character from letters, nums or symbols.

import random

def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = "1234567890"
    symbols = "-+=!@#$%^&*"

    password = ''
    num_of_letters = int(input('How many letters do you want in your password? '))
    num_of_nums = int(input('How many numbers do you want in your password? '))
    num_of_symbols = int(input('How many symbols do you want in your password? '))

    for letter in range(1, num_of_letters + 1):
        password += random.choice(letters)

    for num in range(1, num_of_nums + 1):
        password += random.choice(nums)

    for symbol in range(1, num_of_symbols + 1):
        password += random.choice(symbols)

    password_list = list(password)
    random.shuffle(password_list)

    new_password = ''

    for letter in password_list:
        new_password += letter

    return new_password


complex_password = generate_password()
print(complex_password)