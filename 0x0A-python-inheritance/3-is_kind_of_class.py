#!/usr/bin/python3
"""
Module that confirms if object is an instance of a class,
or is an instance of a class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of a_class or
    an instance of a subclass of a_class, Otherwise False
    """

    return isinstance(obj, a_class)
