# Instruction
# Define a function which takes three integer number as parameters and returns maximum of them.
#
# Input
# max_of_three(4,5,3)
#
# Output
# 5

def max_of_three(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


maxNum = max_of_three(-3,-5,-7)
print(maxNum)