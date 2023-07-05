#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """Unittests for max_integer function"""

    def test_ordered_list(self):
        self.assertEqual(max_integer([-20, 5, 100, 350]), 350)

    def test_unordered_list(self):
        self.assertEqual(max_integer([5, -20, 100, 35]), 100)

    def test_negative_ints(self):
        self.assertEqual(max_integer([-20, -6, -2, -3]), -2)

    def test_one_element_list(self):
        self.assertEqual(max_integer([10]), 10)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_floats_list(self):
        self.assertEqual(max_integer([3.3, 7.7, 5.5, 2.2]), 7.7)

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([6.6, 15.5, -17, 4]), 15.5)

    def test_same_number_list(self):
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_big_list(self):
        self.assertEqual(max_integer([
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            99, 98, 97, 96, 95, 94, 93, 92, 91]), 99)

    def test_repeated_numbers(self):
        self.assertEqual(max_integer([10, 20.20, 10, 20.20]), 20.20)

    def test_string(self):
        with self.assertRaises(TypeError):
            max_integer([0, 'Hi'])

    def test_tuple(self):
        with self.assertRaises(TypeError):
            max_integer([5.5, (2.2, 3.3)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'n1': 1, 'n2': 2})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(7)
