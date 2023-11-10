#!/usr/bin/python3
"""
Base Test Module
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up class"""
        Base._Base__nb_objects = 0
        self.base_1 = Base()
        self.base_2 = Base()
        self.base_3 = Base(10)

    def test_instance(self):
        """Test that instance of base is initialized correctly"""
        self.assertTrue(isinstance(self.base_1, Base))
        self.assertTrue(isinstance(self.base_2, Base))
        self.assertFalse(self.base_1 is self.base_2)
        self.assertNotEqual(self.base_1, self.base_2)
        self.assertEqual(self.base_1.id, 1)
        self.assertEqual(self.base_2.id, 2)
        self.assertEqual(self.base_3.id, 10)

    def test_to_json_string(self):
        json = Base.to_json_string([Square(10).to_dictionary()])
        self.assertTrue(isinstance(json, str))
        json = Base.to_json_string([Rectangle(10, 10).to_dictionary()])
        self.assertTrue(isinstance(json, str))

    def test_save_to_file(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Square.save_to_file([Square(10)])
        with open("Square.json", "r") as f:
            sys.stdout = file = io.StringIO()
            print(f.read())
            sys.stdout = sys.__stdout__
        self.assertEqual(
            file.getvalue()[:-1], '[{"id": 3, "size": 10, "x": 0, "y": 0}]')
