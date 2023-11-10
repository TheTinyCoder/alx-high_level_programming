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
        self.assertEqual(
            list(Rectangle(1, 2).__dict__.values()), [3, 1, 2, 0, 0])
        self.assertEqual(
            list(Rectangle(1, 2, 3).__dict__.values()), [4, 1, 2, 3, 0])
        self.assertEqual(
            list(Rectangle(1, 2, 3, 4).__dict__.values()), [5, 1, 2, 3, 4])
        self.assertEqual(
            list(Rectangle(1, 2, 3, 4, 5).__dict__.values()), [5, 1, 2, 3, 4])

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
        sys.stdout = file = io.StringIO()
        self.rectangle_1.display()
        sys.stdout = sys.__stdout__
        count = []
        for line in file.getvalue().split('\n')[:-1]:
            count.append(len(line))
        y = self.rectangle_1.y
        width = self.rectangle_1.width + self.rectangle_1.x
        height = self.rectangle_1.height + y
        self.assertTrue(all(i == width for i in count[y:]))
        self.assertTrue(len(count) == height)


    def test_str(self):
        """Test __str__"""
        file = io.StringIO()
        sys.stdout = file
        print(self.rectangle_1)
        sys.stdout = sys.__stdout__
        self.assertTrue(file.getvalue()[:-1] == "[Rectangle] (1) 0/0 - 10/10")

    def test_update(self):
        """Test update function"""
        self.rectangle_2.update(3)
        self.assertEqual(self.rectangle_2.id, 3)
        self.rectangle_2.update(4, 15)
        self.assertEqual(self.rectangle_2.id, 4)
        self.assertEqual(self.rectangle_2.width, 15)
        self.rectangle_2.update(5, 20, 20, 2)
        self.assertEqual(self.rectangle_2.id, 5)
        self.assertEqual(self.rectangle_2.width, 20)
        self.assertEqual(self.rectangle_2.height, 20)
        self.assertEqual(self.rectangle_2.x, 2)
        self.rectangle_2.update(2, 10, 10, 1, 1)
        self.assertEqual(self.rectangle_2.id, 2)
        self.assertEqual(self.rectangle_2.width, 10)
        self.assertEqual(self.rectangle_2.height, 10)
        self.assertEqual(self.rectangle_2.x, 1)
        self.assertEqual(self.rectangle_2.y, 1)
        self.rectangle_2.update(4, y=1, width=2, x=3, id=89)
        self.assertEqual(self.rectangle_2.id, 4)
        self.assertEqual(self.rectangle_2.width, 10)
        self.assertEqual(self.rectangle_2.height, 10)
        self.assertEqual(self.rectangle_2.x, 1)
        self.assertEqual(self.rectangle_2.y, 1)
        self.rectangle_2.update(y=2, width=20, x=2, id=2)
        self.assertEqual(self.rectangle_2.id, 2)
        self.assertEqual(self.rectangle_2.width, 20)
        self.assertEqual(self.rectangle_2.height, 10)
        self.assertEqual(self.rectangle_2.x, 2)
        self.assertEqual(self.rectangle_2.y, 2)

    def test_to_dictionary(self):
        a_dict = self.rectangle_1.to_dictionary()
        self.assertEqual(
            list(a_dict.keys()), ["id", "width", "height", "x", "y"])
        self.assertEqual(list(a_dict.values()), [1, 10, 10, 0, 0])
