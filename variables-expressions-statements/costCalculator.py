# Trip Cost Calculator Project
# Instruction
# Write a program which calculates trip cost for a user.

# Ask the user for number of days.
# Ask the user for hotel price.
# Ask the user for flight price.
# Ask the user for rental car price.
# Ask for other expenses.
# Combine all expenses together and print with 2 digits after decimal places.
# Input

# How many days will you stay? 3
# How much does hotel cost per night? $30
# How much does flight cost? $50
# If you need rental car please enter the price otherwise enter zero. $10
# Enter other possible expenses $0
#
# Output
# Total Cost: $170.0

days = input('How many days will you stay? ')
hotel = input('How much does hotel cost per night? $')
flight = input('How much does flight cost? $')
car = input('If you need rental car please enter the price otherwise enter zero. $')
other = input('Enter other possible expenses $')

days = int(days)
hotel = float(hotel)
flight = float(flight)
car = float(car)
other = float(other)
# print(days,hotel,flight,car,other)
total = round((days * hotel) + flight + (car * days) + other, 2)

print(f'Total Cost: ${total}')