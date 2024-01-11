# Cold, Warm and Hot
# Instruction
# Define a function which takes a temperature as a parameter:
#
# returns Hot if the temperature is greater than 28
# returns Warm if the temperature is between 18 and 28, including both.
# returns Cold if the temperature is less than 18
# Input
# 18
#
# Output
# Warm

def check_weather(temp):
    temp = int(temp)
    if temp > 28:
        return 'Hot'
    elif 18 <= temp <= 28:
        return 'Warm'
    else:
        return 'Cold'


temp = input('What\'s the temperature?')
weather = check_weather(temp)
print(weather)