# Use find and string slicing to extract the portion of the string after the colon character and
# then use the float function to convert the extracted string into a floating point number.
#
# custom_string = 'X-MAPDS-Confidence:0.8475'
#
# Output
#
# 0.8475

custom_string = 'X-MAPDS-Confidence:0.8475'


def extract_string(string):
    colon_index = string.find(':')
    required_string = string[colon_index + 1:]
    required_number = float(required_string)
    return required_number


print(extract_string(custom_string))
