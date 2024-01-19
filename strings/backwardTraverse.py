# Backward Traversal
# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
#
# Input
#
# Enter a string: Python
#
# Output
#
# n
# o
# h
# t
# y
# P

def backward():
    user_input = input('Enter a string: ')

    index = -1
    length = -len(user_input)

    while index >= length:
        print(user_input[index])
        index = index - 1


backward()
