#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to store the result
    new_string = ""

    # Iterate through each character in the input string
    for c in my_string:
        # Skip 'c' and 'C' characters
        if c.lower() != 'c':
            new_string += c
    return new_string
