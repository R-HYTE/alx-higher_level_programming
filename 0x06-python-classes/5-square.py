#!/usr/bin/python3
""" Printing a square """


class Square:
    """
    It defines a basic square shape with a private size attribute.

    Attributes:
        __size (int): The size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance,
        with the given size (default is 0).
        area(self): Returns the current square area.
        size (property): Getter to retrieve the size attribute.
        size (property setter): Setter to set the size attribute.
        my_print(self): Prints the square to stdout with the character #.
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
        self.size = size

    def area(self):
        """
        Returns the current square area.

        Args:
            None

        Returns:
            int: The area of the square (size * size).
        """
        return self.__size * self.__size

    @property
    def size(self):
        """
        Getter method to retrieve the size attribute.

        Args:
            None

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method to set the size attribute.

        Args:
            value (int): The new size value to be assigned.

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

    def my_print(self):
        """
        Prints the square to stdout with the character #.

        Args:
            None

        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
