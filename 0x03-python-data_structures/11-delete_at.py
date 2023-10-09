#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Check if the index is valid (not negative and within range)
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Create a new list without the element at the specified index
    new_list = my_list[:idx] + my_list[idx + 1:]

    return new_list
