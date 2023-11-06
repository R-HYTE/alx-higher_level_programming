#!/usr/bin/python3
"""
==================================================================
module that checks if an object is an instance of a specific class
==================================================================
"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class"""

    return type(obj) is a_class
