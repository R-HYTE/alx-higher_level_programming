#!/usr/bin/python3
""" This module has tests for the base class in the model package"""

import unittest
from models import base
Base = base.Base

class TestBase(unittest.TestCase):
    ''' Testing the base class '''
    def test_base(self):
        obj1 = Base()
        obj2 = Base()
        obj3 = Base(-3)
        obj4 = Base(12)
        obj5 = Base(2.5)
        obj6 = Base(None)
        obj7 = Base()
        obj8 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, -3)
        self.assertEqual(obj4.id, 12)
        self.assertEqual(obj5.id, 2.5)
        self.assertEqual(obj6.id, 3)
        self.assertEqual(obj7.id, 4)
        self.assertEqual(obj8.id, 5)



if __name__=="__main__":
    unittest.main()
