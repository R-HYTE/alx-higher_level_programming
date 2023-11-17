#!/usr/bin/python3
"""
===================================================================
This module has unittest for Rectangle class in the models package
===================================================================
"""

from distutils.util import run_2to3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Testing Rectangle class
    """
    def test_width(self):
        """
        Checking if width is a valid integer
        """
        r1 = Rectangle(120, 0)
        r2 = Rectangle(23, 5)
        r3 = Rectangle(23, 5, 0, 2, 100)

        self.assertEqual(r1.width, 120)
        self.assertEqual(r2.width, 23)
        self.assertEqual(r3.width, 23)
        with self.assertRaises(ValueError):
            Rectangle(-1, 0)
        with self.assertRaises(TypeError):
            Rectangle(None, 0)
        with self.assertRaises(TypeError):
            Rectangle(3.5, 5)
        with self.assertRaises(TypeError):
            Rectangle(float('inf'), 998)
        with self.assertRaises(TypeError):
            Rectangle("string", 2)
        with self.assertRaises(TypeError):
            Rectangle({1, 2}, 23)
        with sel.assertRaises(TypeError):
            Rectangle((2,3), 6)

    def test_height(self):
        """
        Testing if height is valid integer
        """
        r1 = Rectangle(120, 0)
        r2 = Rectangle(23, 5)
        r3 = Rectangle(23, 5, 0, 0, 100)

        self.assertEqual(r1.height, 0)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r3.height, 5)
        with self.assertRaises(ValueError):
            Rectangle(-1, -2)
        with self.assertRaises(TypeError):
            Rectangle(0, None)
        with self.assertRaises(TypeError):
            Rectangle(189, 2.3)
        with self.assertRaises(TypeError):
            Rectangle(123, float('inf'))
        with self.assertRaises(TypeError):
            Rectangle(104, "string", 5, 12)
        with self.asserRaises(TypeError):
            Rectangle(23, {1, 4}, 8, 12, 16)

    def test_x(self):
        """
        Testing if x is a valid integer
        """
        r1 = Rectangle(1, 2, 0, 4, 5)
        r2 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.x, 3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, None, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 8.8, 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, float('inf'), 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "Poly", 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, (3, 8), 4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, {1, 2}, 4, 5)

    def test_y(self):
        """
        Testing if y is a valid integer
        """
        r1 = Rectangle(1, 2, 3, 0, 5)
        r2 = Rectangle(1, 2, 3, 4, 5)

        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.y, 4)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, None, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 8.8, 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, float('inf'), 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "Poly", 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, (3, 8), 5)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {1 , 2}, 5)

    def test_area(self):
        """
        Testing the area of a Rectangle
        """
        r1 = Rectangle(10, 15, 0, 0, 0)
        r2 = Rectangle(2, 3, 3, 0, 2)

        self.assertEqual(r1.area(), 150)
        self.assertEqual(r2.area(), 6)
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, -12, 0, 0, 12)
            r3.area()
        with self.assertRaises(ValueError):
            r4 = Rectangle(-10, 12, 0, 0, 12)
            r4.area()


if __name__ == '__main__':
    unittest.main()
