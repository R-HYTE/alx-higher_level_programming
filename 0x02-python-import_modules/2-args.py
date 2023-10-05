#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1

    # Print the number of arguments and whether it's singular or plural
    plural = 's' if num_args != 1 else ''
    ending = '.' if num_args == 0 else ':'
    print("{} argument{}{}".format(num_args, plural, ending))

    # Print the arguments and their positions
    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
