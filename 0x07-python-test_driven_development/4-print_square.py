#!/usr/bin/python3
""" Module contains a function that prints a square """


def print_square(size):
    """ prints a square """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
