#!/usr/bin/env python3

import unittest

add_integer = __import__("0-add_integer").add_integer

class TestAddInteger(unittest.TestCase):
    """Test the add integer function"""
    def test_1(self):
        self.assertRaises(TypeError, add_integer, "5", 12)

    def test_2(self):
        self.assertEqual(add_integer(5, 10), 15)

    def test_3(self):
        self.assertEqual(add_integer(2, 10), 21)




