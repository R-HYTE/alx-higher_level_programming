#!/usr/bin/python3
""" This module has a function that manipulates a matrix """


def matrix_divided(matrix, div):
    """ Divides all elements of a matrix """
    message = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix:
        raise TypeError(message)
    if not isinstance(matrix, list):
        raise TypeError(message)

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(message)
        for column in row:
            if type(column) not in [float, int]:
                raise TypeError(message)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(message)
    if not type(div) in [float, int]:
        raise TypeError("div must be a number")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(column / div, 2) for column in row] for row in matrix]
