# Maximum and Minimum of Input Numbers
# Write another program that prompts for a list of numbers as we did in previous exercises
# and at the end prints out both the maximum and minimum of the inputted numbers.
#
# For Example
#
# Enter a number: 1
# Enter a number: 3
# Enter a number: 2
# Enter a number: 4
# Enter a number: done
# Output
#
# Maximum number: 4.0, Minimum number: 1.0

def min_max():
    user_input = int(input('Enter a number: '))
    min_num = user_input
    max_num = user_input

    while True:
        num = input('Enter a number: ')

        if num == 'done':
            break

        num = int(num)

        if num < min_num:
            min_num = num

        if num > max_num:
            max_num = num

    return min_num, max_num


number = min_max()
print(number)



