#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


"""
============================================================================
This module defines the BaseGeometry class for handling geometric operations
============================================================================
"""


class Rectangle(BaseGeometry):
    """Initializes a Rectangle object with specified width and height"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
