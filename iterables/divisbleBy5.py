# Numbers Divisible by 5 Until 130
# Implement a function which takes a given ordered list as a parameter and displays numbers divisible by 5
# and if a number is greater than 130 display STOP in the console.
#
# Example
#
# list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]
# numbers_divisible_byfive(list1)
# Output
#
# 15
# 40
# 75
# STOP

list = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200]


def numbers_divisible_by_five(list):
    for num in list:
        if num > 130:
            break
        if num % 5 == 0:
            print(num)

    print('STOP')


numbers_divisible_by_five(list)
