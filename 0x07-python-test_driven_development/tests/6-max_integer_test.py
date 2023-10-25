#!/usr/bin/python3
"""
Unit test for max_integer
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Defines tests for the max_integer function
    """

    def test_empty_list(self):
        """
        Checks that None is returned if list is empty
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_list_with_1(self):
        """
        Checks that correct integer is returned
        """
        self.assertEqual(max_integer([1]), 1)

    def test_list_with_ordered_numbers(self):
        """
        Checks that correct integer is returned
        """
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6]), 6)

    def test_list_with_unsorted_numbers(self):
        """
        Checks that correct integer is returned
        """
        self.assertEqual(max_integer([5, 6, 2, 1, 4, 3]), 6)

    def test_list_with_string(self):
        """
        Checks that correct integer is returned
        """
        with self.assertRaises(TypeError):
            max_integer([1, "2"])

    def test_list_with_tuple(self):
        """
        Checks that correct integer is returned
        """
        with self.assertRaises(TypeError):
            max_integer([1, (2, 4)])

    def test_list_with_floats(self):
        """
        Checks that correct integer is returned
        """
        self.assertEqual(max_integer([1.7, 2.4, 8.5, 3.1, 9.2, 4.6]), 9.2)

    def test_non_list(self):
        """
        Checks that correct integer is returned
        """
        with self.assertRaises(KeyError):
            max_integer({1: 1, 4: 4, 3: 3})
