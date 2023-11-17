#!/usr/bin/python3
"""
====================================================================
This module has the Unittest for the init method in the Base class
====================================================================
"""

import unittest
from models.base import Base


class Test_Base_Init(unittest.TestCase):
    """Class Testing the init method in Base class"""

    def test_id_int(self):
        """Testing assignement of integers to the id"""
        base_obj = Base(10)
        self.assertEqual(base_obj.id, 10)
        base_obj = Base(0)
        self.assertEqual(base_obj.id, 0)
        base_obj = Base(-5)
        self.assertEqual(base_obj.id, -5)

    def test_id_incrementation(self):
        """Testing  id incrementation"""
        Base._Base__nb_objects = 0
        base_obj = Base()
        self.assertEqual(base_obj.id, 1)
        base_obj = Base(None)
        self.assertEqual(base_obj.id, 2)
        base_obj = Base(5)
        self.assertEqual(base_obj.id, 5)
        base_obj = Base()
        self.assertEqual(base_obj.id, 3)

    def test_id_non_int(self):
        """Testing the assignment of non integers data types to id"""
        base_obj = Base("A")
        self.assertEqual(base_obj.id, "A")
        base_obj = Base('Trying out a string')
        self.assertEqual(base_obj.id, 'Trying out a string')
        base_obj = Base([1, 2, 3])
        self.assertEqual(base_obj.id, [1, 2, 3])
        base_obj = Base((1, 2, 3))
        self.assertEqual(base_obj.id, (1, 2, 3))
        base_obj = Base({"id": 1, "name": "Poly"})
        self.assertEqual(base_obj.id, {"id": 1, "name": "Poly"})
        base_obj = Base(True)
        self.assertEqual(base_obj.id, True)

    def test_id_error(self):
        """Testing error associated with number of arguments"""
        with self.assertRaises(TypeError):
            base_obj = Base(1, 2)
        with self.assertRaises(TypeError):
            base_obj = Base(None, 1)


if __name__ == '__main__':
    unittest.main()
