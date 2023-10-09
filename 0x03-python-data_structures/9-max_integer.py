#!/usr/bin/python3

def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize max_value with the first element of the list
    max_value = my_list[0]

    # Iterate through the list and update max_value if a larger value is found
    for item in my_list:
        if item > max_value:
            max_value = item

    return max_value
