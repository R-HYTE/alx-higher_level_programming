#!/usr/bin/python3
"""
==========================================================
This module has a simple implementation of a serialization and deserialization
mechanism(concept of representation of an object to another format, without
losing any information and allow us to rebuild an object based on this
representation)
==========================================================
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        If attrs is a list of strings, only attributes name contain
        in this list must be retrieved.Else, all attributes must be retrieved
        """
        if attrs is None:
            return self.__dict__

        new_dict = dict()
        for attr in attrs:
            if hasattr(self, attr):
                new_dict[attr] = getattr(self, attr)

        return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""

        self.__dict__.update(json)
