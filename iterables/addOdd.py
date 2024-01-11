# Adding Odd Numbers
# Implement a function that calculates the sum of all odd numbers from 1 to 100 by using range() function inside loop.
#
# Example
#
# 1+3+5+...+97+99 = 2500

total = 0
for num in range(1, 101):
    if num % 2 != 0:
        total += num

print(total)