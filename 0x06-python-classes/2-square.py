#!/usr/bin/python3
""" This is a Square class"""


class Square:
    """
    It defines a basic square shape with a private size attribute.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance
        (default is 0)
    """
    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size.

        Args:
            size (int, optional): The size of the square. Default is 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        Returns:
            None
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
