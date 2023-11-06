#!/usr/bin/python3
"""
====================================
Module that inherits from List class
====================================
"""


class MyList(list):
    """Class that inherits from list class"""
    pass

    def print_sorted(self):
        """Method that prints a list in ascending order"""

        print(sorted(list(self)))
