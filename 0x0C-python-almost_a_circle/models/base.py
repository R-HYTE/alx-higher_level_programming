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

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Writes the JSON string representation of list_objs to a file '''
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        ''' Returns the list of dictionaries from the JSON string rep '''
        if not json_string or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Returns an instance with all attributes already set '''
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)  # Create a dummy Rectangle instance
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)  # Create a dummy Square instance
        else:
            raise ValueError(f"Unsupported class: {cls.__name__}")

        dummy_instance.update(**dictionary)  # Apply real values
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        ''' Returns a list of instances from the file '''
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []
