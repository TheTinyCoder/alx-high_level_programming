#!/usr/bin/python3
"""
Rectangle Test Module
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up test class"""
        Base._Base__nb_objects = 0
        self.rectangle_1 = Rectangle(10, 10)
        self.rectangle_2 = Rectangle(10, 10, 1, 1)

    def test_args(self):
        """Test missing and excess arguments"""
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle()
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle(10)
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle(10, 10, 10, 10, 10, 10)

    def test_integer_validator(self):
        """Test integer validator function"""
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle("10", 10)
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle(10, "10")
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle(10, 10, "10", 10)
        with self.assertRaises(TypeError):
            self.rectangle = Rectangle(10, 10, 10, "10")
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(0, 10)
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(10, 0)
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(-10, 10)
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(10, -10)
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(10, 10, -10, 10)
        with self.assertRaises(ValueError):
            self.rectangle = Rectangle(10, 10, 10, -10)

    def test_instance(self):
        """Test that instance of self.rectangle is initialized correctly"""
        self.assertTrue(isinstance(self.rectangle_1, Rectangle))
        self.assertTrue(isinstance(self.rectangle_1, Base))
        self.assertFalse(self.rectangle_1 is self.rectangle_2)
        self.assertEqual(self.rectangle_1.width, 10)
        self.assertEqual(self.rectangle_1.height, 10)
        self.assertEqual(self.rectangle_1.x, 0)
        self.assertEqual(self.rectangle_1.y, 0)
        self.assertEqual(self.rectangle_1.id, 1)

    def test_area(self):
        """Test area function"""
        self.assertEqual(self.rectangle_1.area(), 100)

    def test_display(self):
        """Test string printed"""
        file = io.StringIO()
        # redirect output stream to StringIO (in memory file)
        sys.stdout = file
        self.rectangle_2.display()
        # restore output stream to terminal
        sys.stdout = sys.__stdout__
        count = []
        for line in file.getvalue().split('\n')[:-1]:
            count.append(len(line))
        y = self.rectangle_2.y
        width = self.rectangle_2.width + self.rectangle_2.x
        height = self.rectangle_2.height + y
        self.assertTrue(all(i == width for i in count[y:]))
        self.assertTrue(len(count) == height)

    def test_str(self):
        """Test __str__"""
        file = io.StringIO()
        sys.stdout = file
        print(self.rectangle_1)
        sys.stdout= sys.__stdout__
        self.assertTrue(file.getvalue()[:-1] == "[Rectangle] (1) 0/0 - 10/10")
