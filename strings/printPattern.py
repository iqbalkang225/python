# Create a function which takes as parameter integer number (n) and based on this number it prints the following start pattern
# using nested loop and string formatting. So if n equals 5 the maximum number of stars (*) will be 5 in the pattern.
#
# Example1
#
# print_pattern(5)
#
# Output1
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# Example2
#
# print_pattern(6)
#
# Output1
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

def print_pattern(times):

    string = ''

    for i in range(1, times + 1):
        string += '* '
        print( string)

        if i == times:
            temp = i

            while temp > 0:
                temp -= 1
                string = temp * '* '
                print(string)


print_pattern(10)