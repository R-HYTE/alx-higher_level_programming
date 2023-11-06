#!/usr/bin/python3
"""
============================================================================
This module defines the BaseGeometry class for handling geometric operations
=============================================================================
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception to indicate that area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that the given value is a positive integer"""

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
