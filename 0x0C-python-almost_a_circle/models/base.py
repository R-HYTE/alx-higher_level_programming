#!/usr/bin/python3
""" This module has the base class of the projects"""


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
