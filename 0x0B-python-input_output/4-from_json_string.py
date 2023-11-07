#!/usr/bin/python3
"""
=======================================================
This module converts a JSON string back to python object
========================================================
"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string"""
    return json.loads(my_str)
