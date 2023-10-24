#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Class that defines properties of square by: (based on 5-square.py).

    Attributes:
        size: size of a square (1 side).
    """
    def __init__(self, size=0, position=(0, 0)):
        """Creates new instances of square.

        Args:
            __size (int): size of the square (1 side).
            __position (tuple): position of the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area of square.

        Returns: the current square area.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.
        Args:
            None
        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): new size value to be assigned

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter method to retrieve the position attribute.
        Args:
            None
        Returns:
            tuple of int: The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Property setter for position.

        Args:
            value (tuple): position of the square.

        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints the square to stdout with the character # and specified loc
        Args:
            None
        Returns:
            None
        """

        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
