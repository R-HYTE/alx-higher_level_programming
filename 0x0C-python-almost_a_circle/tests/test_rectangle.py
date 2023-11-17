#!/usr/bin/python3
"""
=====================================================
This module has the unittests for the Rectangle class
=====================================================
"""


import unittest
from models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):
    """
    Test case class for the Rectangle class methods
    """

    def setUp(self):
        ''' Set up a default Rectangle instance for testing '''
        self.rect = Rectangle(5, 10, 2, 3, 1)

    def test_attributes(self):
        ''' Test the initialization of Rectangle attributes '''
        self.assertEqual(self.rect.width, 5)
        self.assertEqual(self.rect.height, 10)
        self.assertEqual(self.rect.x, 2)
        self.assertEqual(self.rect.y, 3)
        self.assertEqual(self.rect.id, 1)

    def test_area(self):
        ''' Test the area calculation of the Rectangle '''
        self.assertEqual(self.rect.area(), 50)

    def test_display(self):
        ''' Test the display method of the Rectangle '''
        # Redirect stdout to capture print output
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        self.rect.display()

        # Get the printed output
        printed_output = sys.stdout.getvalue()

        # Reset redirect.
        sys.stdout = original_stdout

        # Check if the displayed output matches the expected pattern
        expected_output = "\n" * self.rect.y + (" " * self.rect.x + "#" * self.rect.width + "\n") * self.rect.height
        self.assertEqual(printed_output, expected_output)

    def test_string_representation(self):
        ''' Test the string representation of the Rectangle '''
        expected_str = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(self.rect), expected_str)

    def test_update_method(self):
        ''' Test the update method of the Rectangle with positional arguments '''
        self.rect.update(2, 7, 14, 1, 2)
        self.assertEqual(self.rect.id, 2)
        self.assertEqual(self.rect.width, 7)
        self.assertEqual(self.rect.height, 14)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 2)

    def test_update_method_with_kwargs(self):
        ''' Test the update method of the Rectangle with keyword arguments '''
        self.rect.update(width=8, height=16, x=3, y=4)
        self.assertEqual(self.rect.width, 8)
        self.assertEqual(self.rect.height, 16)
        self.assertEqual(self.rect.x, 3)
        self.assertEqual(self.rect.y, 4)

    def test_to_dictionary(self):
        ''' Test the to_dictionary method of the Rectangle '''
        expected_dict = {'x': 2, 'y': 3, 'id': 1, 'height': 10, 'width': 5}
        self.assertEqual(self.rect.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()

