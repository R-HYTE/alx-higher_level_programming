#!/usr/bin/python3
"""
====================================================================
This module writes an object to a text file using JSON representation
=====================================================================
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using JSON representation"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(my_obj))
