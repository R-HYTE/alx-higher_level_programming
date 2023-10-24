#!/usr/bin/python3
""" Tis is a Square Class"""


class Square:
    """
    It defines a basic square shape with a private size attribute.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance
        with given size (default is 0).
        area(self): Returns the current square area.
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

    def area(self):
        """
        Returns the current square area.

        Args:
            None

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size
