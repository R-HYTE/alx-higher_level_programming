#!/usr/bin/python3
"""
=============================
This module reads from a file
=============================
"""


def read_file(filename=""):
    """Reads text from a file and prints to stdout"""

    with open(filename, encoding="utf-8") as file:
        content = file.read()
        print(content, end="")
