# Gross Pay with Ovetime using Functions
# Instruction
# Rewrite Gross Pay with Overtime Project (Project 6) and create a function called compute_pay which takes two parameters (hours and rate).
# Additionally, we need to create another function which checks if the type of "input" is a float or not.
# If the values for hour or rate is not float we will return error.
#
# Input
# Enter Hours: 45
# Enter Rate: 5
#
# Output
# Pay: 237.5
#
# Input
# Enter Hours: five
#
# Output
# Error, please enter numeric input

def compute_pay(hours, rate):
    overtime = hours - 40

    if overtime > 0:
        total_pay = 40 * rate + overtime * rate * 1.5
    else:
        total_pay = hours * rate
    return total_pay


def check_input():
    try:
        total_hours = float(input("Enter Hours: "))
    except ValueError:
        print("Error, please enter numeric input for hours")
        quit()

    try:
        pay_rate = float(input("Enter Rate: "))
    except ValueError:
        print("Error, please enter numeric input for Rate")
        quit()

    pay = compute_pay(total_hours, pay_rate)
    print(pay)


check_input()

