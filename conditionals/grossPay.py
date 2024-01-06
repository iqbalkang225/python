#
# Gross Pay with Ovetime
# Instruction
# Rewrite the Gross Pay Project (Project 3) program to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# Here again the program prompts the user for hours and rate per hour to compute gross pay.
# You need to take into account that the result has exactly two digits after the decimal place.

# Input
# Enter Hours: 45
# Enter Rate: 5
#
# Output
# Pay: 237.5

try:
    totalHours = float(input("Enter Hours: "))
except ValueError:
    print("Error, please enter numeric input for hours")
    quit()

try:
    payRate = float(input("Enter Rate: "))
except ValueError:
    print("Error, please enter numeric input for Rate")
    quit()
else:
    totalPay = 0

    overtime = totalHours - 40

    if overtime > 0:
        totalPay = 40 * payRate + overtime * payRate * 1.5
    else:
        totalPay = totalHours * payRate

    print(f"Pay: {round(totalPay, 2)}")


