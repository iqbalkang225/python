# Factorial using Loop
# Implement a function that takes an integer number as a parameter and returns factorial of this number.
#
# Factorial Equation (!)
#
# 5! = 5 x 4 x 3 x 2 x 1 = 120
#
# 4! = 4 x 3 x 2 x 1 = 24
#
# If input is 0 then the return value will be: The factorial of 0 is 1
#
# if input is a negative number then the return value will be: Factorial does not exist for negative numbers
#
# Example
#
# factorial(4) # The factorial of 4 is 24
# factorial(-1)  # Factorial does not exist for negative numbers

def factorial(number):
    if number < 0:
        return 'Factorial does not exist for negative numbers'
    if number == 0:
        return 1

    fact = 1
    for num in range(1, number + 1):
        fact = num * fact

    return fact


total = factorial(-1)
print(total)