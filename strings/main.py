# Sum of Digits of 2 Digit Number
# Create a function that takes two digit number from console and returns sum of digits. e.g. if the input was 45, then the output should be 4 + 5 = 9
#
# Example Input
#
# sum_of_two_digits()
# Enter two digit number: 45
# Output
#
# 4 + 5  = 9
#
# 9

def sum_of_two_digits():
    user_input = input('Enter two digit number: ')

    num1 = int(user_input[0])
    num2 = int(user_input[1])

    return num1 + num2


print(sum_of_two_digits())

