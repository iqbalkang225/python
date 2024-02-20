# Create a program which prints out student names and their score as shown below
#
# names and scores lists are given
#
# names = ['John', 'Edy', 'Jane', 'Kane']
# scores = [90, 95, 80, 75]
# Sample Output:
#
# Name Score
#
# John 90
# Edy 95
# Jane 80
# Kane 75
#
# Hint
# Use format() function to format output as shown.

names = ['John', 'Edy', 'Jane', 'Kane']
scores = [90, 95, 80, 75]

def print_scores():
    print("{0:<10} {1}".format("Name", "Score"))

    for i in range(0, len(names)):
        name = names[i]
        score = scores[i]
        print("{0:<10} {1}".format(name, score))

print_scores()