# First and Last 2 Characters
# Implement a function which takes a string as a parameter and returns new string which is made of the first 2 and the last 2 chars from a given a string.
# If the length of given string is less than 2 then return empty string.
#
# Example
#
# first_last_characters('appmillers')
#
# Output
#
# aprs

def first_last_characters(word):
    len_of_word = len(word)

    first_letters = word[0: 2]
    last_letters = word[len_of_word - 2:]
    return first_letters + last_letters


print(first_last_characters('app millers'))

