#!/usr/bin/python3
"""
=====================================================================
Module that returns a list of names in the namespace of an obj passed
=====================================================================
"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object."""
    return dir(obj)
