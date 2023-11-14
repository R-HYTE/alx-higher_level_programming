#!/usr/bin/python3
""" This module has the base class of the projects"""
import json


class Base:
    '''
    Manage id attribute in all future classes and avoid duplicating
    the same code (by extension, same bugs)
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Base class Constructor '''
        if not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' Returns the JSON string representation of list_dictionaries '''
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
