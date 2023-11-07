#!/usr/bin/python3
"""
=====================================================
This module shows capability of writing to a text file
======================================================
"""


def write_file(filename="", text=""):
    """ writes a string to a text file"""

    with open(filename, "w", encoding="utf-8") as file:
        char_written = file.write(text)
        return char_written
