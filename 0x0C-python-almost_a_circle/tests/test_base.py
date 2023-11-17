#!/usr/bin/python3
""" This module tests the Base class """
import unittest
import os
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    """ Test suite for Base class """

    def setUp(self):
        """ Common setup for each test """
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """ Test assigned id """
        obj1 = Base(23)
        self.assertEqual(obj1.id, 23)

    def test_default_id(self):
        """ Test default id """
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

    def test_id_increment(self):
        """ Test nb_objects attribute and id incrementing"""
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_id_mix(self):
        """ Test nb_objects attributes and assigned id """
        obj1 = Base()
        obj2 = Base(3200)
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 3200)
        self.assertEqual(obj3.id, 2)

    def test_string_id(self):
        """ Test string id """
        obj1 = Base('23')
        self.assertEqual(obj1.id, '23')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            obj1 = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attributes raises AttributeError"""
        obj1 = Base()
        with self.assertRaises(AttributeError):
            obj1.__nb_objects

    def test_save_to_file_square(self):
        """ Test save_to_file method for Square class """
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_rectangle(self):
        """ Test save_to_file method for Rectangle class """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
                self.assertEqual(file.read(), "[]")
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")

if __name__ == '__main__':
    unittest.main()
