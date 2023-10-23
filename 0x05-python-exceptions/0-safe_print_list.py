#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    printed_elements = 0

    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            printed_elements += 1
        except IndexError:
            continue
    print()
    return printed_elements
