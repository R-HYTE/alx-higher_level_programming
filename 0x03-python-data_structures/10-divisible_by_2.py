#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Initialize an empty list to store True/False for each element
    multiples = []

    for item in my_list:
        # Check if the element is a multiple of 2
        is_divisible = (item % 2 == 0)
        multiples.append(is_divisible)

    return multiples
