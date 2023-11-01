import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_in_upperbound(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
    def test_max_in_lowerbound(self):
        self.assertEqual(max_integer([3, 1, 2]), 3)
    def test_one_value(self):
        self.assertEqual(max_integer([4]), 4)
    def test_empty(self):
        self.assertEqual(max_integer([]), None)
    def test_max_randomly_located(self):
        self.assertEqual(max_integer([1, 20, 25, 3, 8]), 25)
    def test_max_negative_value(self):
        self.assertEqual(max_integer([-2, -1, -8]), -1)

if __name__ == '__main__':
    unittest.main()
