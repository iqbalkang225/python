# Find Integer Numbers
# Implement a program which finds integer numbers from given List.
#
# Input
#
# custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']
#
# Output
#
# 11 30 54

custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']

for num in custom_list:
    if type(num) is int:
        print(num)


