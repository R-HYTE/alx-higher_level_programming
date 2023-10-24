#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Square class defines a basic square shape with a private size attribute.

    Attributes:
        __size (int): The size of the square.

    Methods:
        None
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int): The size of the square.

        Returns:
            None
        """
        self.__size = size
