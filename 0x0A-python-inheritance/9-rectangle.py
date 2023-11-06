#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
===============================================================================
This module defines the BaseGeometry class for handling geometric operations
and the Rectangle class for representing rectangles.
================================================================================
"""


class Rectangle(BaseGeometry):
    """Initializes a Rectangle object with specified width and height"""

    def __init__(self, width, height):
        """Initializes a Rectangle object with specified width and height."""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle."""

        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of the rectangle."""

        return f"[Rectangle] {self.__width}/{self.__height}"
