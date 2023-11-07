#!/usr/bin/python3
"""
====================================================
Module for appending a string after lines containing
a specific search string in a file
====================================================
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a new string after each line containing
    a specific search string in a file"""

    if not filename:
        return

    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as fo:
        for line in lines:
            fo.write(line)
            if search_string in line:
                fo.write(new_string)
