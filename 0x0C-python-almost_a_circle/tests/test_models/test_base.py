#!/usr/bin/python3
""" This module has tests for the base class in the model package"""

import unittest
from models import base
Base = base.Base

class TestBase(unittest.TestCase):
    ''' Testing the base class '''
    def test_base(self):
        b0 = Base()
        b1 = Base()
        b2 = Base(-3)
        b3 = Base(12)
        b4 = Base(2.5)
        b5 = Base(None)
        b6 = Base()
        b7 = Base()
        self.assertEqual(b0.id, 1)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, -3)
        self.assertEqual(b3.id, 12)
        self.assertEqual(b4.id, 2.5)
        self.assertEqual(b5.id, 3)
        self.assertEqual(b6.id, 4)
        self.assertEqual(b7.id, 5)



if __name__=="__main__":
    unittest.main()
