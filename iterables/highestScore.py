# Highest Score A List of scores of students are given, implement a program that calculates the highest score from the given list.
#
# Example
#
# student_scores = [80, 60, 50, 65, 75, 55]
#
# The highest score in the class is: 80
#
#
# Hint: DO NOT use any built in function such as max() and sum() !


student_scores = [80, 60, 50, 65, 75, 155, 90]

max_score = student_scores[0]

for score in student_scores:
    if score > max_score:
        max_score = score

print(f"The highest score in the class is: {max_score}")