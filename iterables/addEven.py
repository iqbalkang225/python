# Adding Even Numbers in ANY Range
# Implement a function which takes two parameters as start and end of range and returns sum of even numbers within given range.
#
# Example
#
# add_even_numbers(1,100)
#
# Output
#
# 2550

def add_even_numbers(start, end):
    if start % 2 != 0:
        start = start + 1

    total_sum = 0
    for num in range(start, end + 1, 2):
        total_sum += num

    return total_sum


total = add_even_numbers(1,100)
print(total)