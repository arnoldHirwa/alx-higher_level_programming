#!/usr/bin/python3
"""Unittests for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer function."""

    def test_int(self):
        """Test valid integers."""
        self.assertEqual(max_integer([6, -20, 30, -40]), 30)
        self.assertEqual(max_integer([20]), 20)
        self.assertEqual(max_integer([0, -15, -100]), 0)
        self.assertEqual(max_integer([0, 1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([2, 3, 4, 1, 0]), 4)
        self.assertEqual(max_integer([-1, -6, -8, -4]), -1)

    def test_type(self):
        """Test compatible data types."""
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer("string"), 't')
        self.assertEqual(max_integer((1, 2, 3, 4)), 4)
        self.assertEqual(max_integer([1, 2, 3, float('inf')]), float('inf'))
        self.assertEqual(max_integer([1, 2, 3, float('nan')]), 3)

    def test_type_error(self):
        """ type_errors """
        self.assertRaises(TypeError, max_integer, ["m", 1])
        self.assertRaises(TypeError, max_integer, [2, [2, 1]])

if __name__ == '__main__':
    unittest.main()
