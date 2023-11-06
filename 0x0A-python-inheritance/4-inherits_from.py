#!/usr/bin/python3
"""
Module that checks if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """Returns True if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class"""

    return False if type(obj) is a_class else isinstance(obj, a_class)
