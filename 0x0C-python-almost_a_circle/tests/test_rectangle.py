#!/usr/bin/python3
""" This module tests the Rectangle class """
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ Test suite for the Rectangle class """

    def setUp(self):
        """ Set up method invoked for each test """
        Base._Base__nb_objects = 0

    def test_constructor_default_values(self):
        """ Test the Rectangle constructor with default values """
        rectangle = Rectangle(10, 23)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 23)
        self.assertEqual(rectangle.x, 0)
        self.assertEqual(rectangle.y, 0)
        self.assertEqual(rectangle.id, 1)

    def test_constructor_all_attributes(self):
        """Test the Rectangle constructor with all attributes specified"""
        rectangle = Rectangle(23, 31, 23, 66, 24)
        self.assertEqual(rectangle.width, 23)
        self.assertEqual(rectangle.height, 31)
        self.assertEqual(rectangle.x, 23)
        self.assertEqual(rectangle.y, 66)
        self.assertEqual(rectangle.id, 24)

    def test_constructor_multiple_rectangles(self):
        """ Test creating multiple rectangles """
        rectangle1 = Rectangle(1, 1)
        rectangle2 = Rectangle(1, 1)
        self.assertNotEqual(rectangle1, rectangle2)
        self.assertNotEqual(rectangle1.id, rectangle2.id)

    def test_instance_of_base(self):
        """ Test if Rectangle is an instance of Base """
        rectangle = Rectangle(1, 1)
        self.assertIsInstance(rectangle, Base)

    def test_incorrect_amount_attrs(self):
        """Test if an error is raised when incorrect number of arguments is passed"""
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_incorrect_amount_attrs_1(self):
        """ Test error raised with no args passed """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_access_private_attrs(self):
        """ Trying to access to a private attribute """
        rectangle = Rectangle(1, 2)
        with self.assertRaises(AttributeError):
            rectangle.__width

    def test_access_private_attrs_2(self):
        """ Trying to access to a private attribute """
        rectangle = Rectangle(23, 14)
        with self.assertRaises(AttributeError):
            rectangle.__height

    def test_access_private_attrs_3(self):
        """ Trying to access to a private attribute """
        rectangle = Rectangle(3, 90)
        with self.assertRaises(AttributeError):
            rectangle.__x

    def test_access_private_attrs_4(self):
        """ Trying to access to a private attribute """
        rectangle = Rectangle(2, 1)
        with self.assertRaises(AttributeError):
            rectangle.__y

    def test_valide_attrs(self):
        """ Test if attributes accept valid types """
        with self.assertRaises(TypeError):
            rectangle = Rectangle("2", 2, 2, 2, 2)

    def test_valide_attrs_2(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(2, "2", 2, 2, 2)

    def test_valide_attrs_3(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(2, 2, "2", 2, 2)

    def test_valide_attrs_4(self):
        """ Trying to pass a string value """
        with self.assertRaises(TypeError):
            rectangle = Rectangle(6, 232, 11, "45", 3)

    def test_value_attrs(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(0, 1)

    def test_value_attrs_1(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, 0)

    def test_value_attrs_2(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
        """ Trying to pass invalid values """
        with self.assertRaises(ValueError):
            rectangle = Rectangle(21, 30, 1, -9)

    def test_area(self):
        """ Checking the return value of area method """
        rectangle = Rectangle(40, 2)
        self.assertEqual(rectangle.area(), 80)

    def test_area_2(self):
        """ Checking the return value of area method """
        rectangle = Rectangle(2, 2)
        self.assertEqual(rectangle.area(), 4)
        rectangle.width = 5
        self.assertEqual(rectangle.area(), 10)
        rectangle.height = 5
        self.assertEqual(rectangle.area(), 25)

    def test_area_3(self):
        """ Checking the return value of area method """
        rectangle = Rectangle(3, 8)
        self.assertEqual(rectangle.area(), 24)
        rectangle2 = Rectangle(10, 10)
        self.assertEqual(rectangle2.area(), 100)

    def test_display(self):
        """ Test string method """
        rectangle = Rectangle(2, 5)
        expected_output = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rectangle.display()
            self.assertEqual(str_out.getvalue(), expected_output)

    def test_display_2(self):
        """ Test string printed """
        rectangle1 = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rectangle1.display()
            self.assertEqual(str_out.getvalue(), expected_output)

        rectangle1.width = 5
        expected_output = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            rectangle1.display()
            self.assertEqual(str_out.getvalue(), expected_output)

    def test_str(self):
        """ Test __str__ return value """
        rectangle = Rectangle(2, 5, 2, 4)
        expected_output = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rectangle)
            self.assertEqual(str_out.getvalue(), expected_output)

    def test_str_2(self):
        """ Test __str__ return value """
        rectangle1 = Rectangle(3, 2, 8, 8, 10)
        expected_output = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rectangle1)
            self.assertEqual(str_out.getvalue(), expected_output)

        rectangle1.id = 1
        rectangle1.width = 7
        rectangle1.height = 15
        expected_output = "[Rectangle] (1) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(rectangle1)
            self.assertEqual(str_out.getvalue(), expected_output)

    def test_str_3(self):
        """ Test __str__ return value """
        r1 = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(25, 86, 4, 7)
        res = "[Rectangle] (2) 4/7 - 25/86\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r3 = Rectangle(1, 1, 1, 1)
        res = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(r1.__str__(), res)

    def test_display_3(self):
        """ Test string printed """
        r1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Test string printed """
        r1 = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_check_value_2(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        rectangle = Rectangle.create(**dictionary)
        self.assertEqual(rectangle.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_5(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file(self):
        """ Test load from file method """
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(loaded_rectangles, [])

    def test_load_from_file_after_saving(self):
        """ Test load from file after saving """
        rectangle = Rectangle(2, 2)
        Rectangle.save_to_file([rectangle])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 1)
        self.assertEqual(loaded_rectangles[0].__str__(), rectangle.__str__())

if __name__ == '__main__':
    unittest.main()
