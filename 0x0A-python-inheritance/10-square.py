#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
===================================
This module defines the BaseGeometry, Rectangle, 
and Square classes for handling geometric operations.
===================================
"""


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Initialize a Square object with a specified size"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates and returns the area of the rectangle"""

        return self.__size ** 2
