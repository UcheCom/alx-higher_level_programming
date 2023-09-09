#!/usr/bin/python3
"""Unittest for the max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for the max_integer function."""

    def test_regular(self):
        """Test with a regular list of ints: should return the max result"""
        x = [1, 2, 3, 4]
        result = max_integer(l)
        self.assertEqual(result, 4)

    def test_not_int(self):
        """Test with a list of non-ints and ints:
        should raise a TypeError exception"""
        x = ["b", "c", 8]
        self.assertRaises(TypeError, max_integer, x)

    def test_empty_list(self):
        """Test with an empty list: should return None"""
        x = []
        result = max_integer(x)
        self.assertEqual(result, None)

    def test_negative(self):
        """Test with a list of negative values: should return the max"""
        x = [-1, -2, -3]
        result = max_integer(x)
        self.assertEqual(result, -1)

    def test_float(self):
        """Test with a list of mixed ints and floats: should return the max"""
        x = [2, 6.9, 4]
        result = max_integer(x)
        self.assertEqual(result, 6.9)

    def test_not_list(self):
        """Test with a parameter that's not a list: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, 9)

    def test_unique(self):
        """Test with a list of one int: should return the value of this int"""
        x = [50]
        result = max_integer(x)
        self.assertEqual(result, 50)

    def test_identical(self):
        """Test with a list of identical values: should return the value"""
        x = [ 6, 6, 6, 6]
        result = max_integer(x)
        self.assertEqual(result, 6)

    def test_strings(self):
        """Test with a list of strings: should return the first string"""
        x = ["uche", "oko"]
        result = max_integer(x)
        self.assertEqual(result, "uche")

    def test_none(self):
        """Test with a None as parameter: should raise a TypeError"""
        self.assertRaises(TypeError, max_integer, None)

if __name__ == '__main__':
    unittest.main()
