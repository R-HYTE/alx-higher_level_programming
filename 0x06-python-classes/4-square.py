#!/usr/bin/python3


class Square:
    """
    Square class with private size attribute.

    Attributes:
        __size (int): Size of the square.

    Methods:
        __init__(self, size=0): Initializes a square with the given size.
        area(self): Returns the square's area.
        size (property): Getter to retrieve size.
        size (property setter): Setter to set size.
    """

    def __init__(self, size=0):
        """Initialize a square with the given size."""
        self.size = size

    def area(self):
        """Return the area of square"""
        return self.__size ** 2

    @property
    def size(self):
        """Getter for the size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
