#!/usr/bin/python3
"""
=================================
Module that uses the issubclass()
=================================
"""


def inherits_from(obj, a_class):
    """Returns True if an object is an instance of a class
    that inherited (directly or indirectly) from the specified class"""

    return issubclass(type(obj), a_class)
