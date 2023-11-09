#!/usr/bin/python3
"""
Square Test Module
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up test class"""
        Base._Base__nb_objects = 0
        self.square_1 = Square(10)
        self.square_2 = Square(10, 1, 1)

    def test_args(self):
        """Test missing and excess arguments"""
        with self.assertRaises(TypeError):
            self.square = Square()
        with self.assertRaises(TypeError):
            self.square = Square(10, 10, 10, 10, 10)

    def test_integer_validator(self):
        """Test integer validator function"""
        with self.assertRaises(TypeError):
            self.square = Square("10")
        with self.assertRaises(TypeError):
            self.square = Square(10, "10", 10)
        with self.assertRaises(TypeError):
            self.square = Square(10, 10, "10")
        with self.assertRaises(ValueError):
            self.square = Square(0)
        with self.assertRaises(ValueError):
            self.square = Square(-10)
        with self.assertRaises(ValueError):
            self.square = Square(10, 10, -10)

    def test_instance(self):
        """Test that instance of self.square is initialized correctly"""
        self.assertTrue(isinstance(self.square_1, Square))
        self.assertTrue(isinstance(self.square_1, Rectangle))
        self.assertTrue(isinstance(self.square_1, Base))
        self.assertFalse(self.square_1 is self.square_2)
        self.assertEqual(self.square_1.width, 10)
        self.assertEqual(self.square_1.height, 10)
        self.assertEqual(self.square_1.x, 0)
        self.assertEqual(self.square_1.y, 0)
        self.assertEqual(self.square_1.id, 1)
        self.assertEqual(
            list(Square(1, 2).__dict__.values()), [3, 1, 1, 2, 0])
        self.assertEqual(
            list(Square(1, 2, 3).__dict__.values()), [4, 1, 1, 2, 3])
        self.assertEqual(
            list(Square(1, 2, 3, 4).__dict__.values()), [4, 1, 1, 2, 3])

    def test_area(self):
        """Test area function"""
        self.assertEqual(self.square_1.area(), 100)

    def test_display(self):
        """Test string printed"""
        file = io.StringIO()
        # redirect output stream to StringIO (in memory file)
        sys.stdout = file
        self.square_2.display()
        # restore output stream to terminal
        sys.stdout = sys.__stdout__
        count = []
        for line in file.getvalue().split('\n')[:-1]:
            count.append(len(line))
        y = self.square_2.y
        width = self.square_2.width + self.square_2.x
        height = self.square_2.height + y
        self.assertTrue(all(i == width for i in count[y:]))
        self.assertTrue(len(count) == height)
        sys.stdout = file = io.StringIO()
        self.square_1.display()
        sys.stdout = sys.__stdout__
        count = []
        for line in file.getvalue().split('\n')[:-1]:
            count.append(len(line))
        y = self.square_1.y
        width = self.square_1.width + self.square_1.x
        height = self.square_1.height + y
        self.assertTrue(all(i == width for i in count[y:]))
        self.assertTrue(len(count) == height)

    def test_str(self):
        """Test __str__"""
        file = io.StringIO()
        sys.stdout = file
        print(self.square_1)
        sys.stdout = sys.__stdout__
        self.assertTrue(file.getvalue()[:-1] == "[Square] (1) 0/0 - 10/10")


"""
    def test_update(self):
        "Test update function"
        self.square_2.update(3)
        self.assertEqual(self.square_2.id, 3)
        self.square_2.update(4, 15)
        self.assertEqual(self.square_2.id, 4)
        self.assertEqual(self.square_2.width, 15)
        self.square_2.update(5, 20, 20, 2)
        self.assertEqual(self.square_2.id, 5)
        self.assertEqual(self.square_2.width, 20)
        self.assertEqual(self.square_2.height, 20)
        self.assertEqual(self.square_2.x, 2)
        self.square_2.update(2, 10, 10, 1, 1)
        self.assertEqual(self.square_2.id, 2)
        self.assertEqual(self.square_2.width, 10)
        self.assertEqual(self.square_2.height, 10)
        self.assertEqual(self.square_2.x, 1)
        self.assertEqual(self.square_2.y, 1)
        self.square_2.update(4, y=1, width=2, x=3, id=89)
        self.assertEqual(self.square_2.id, 4)
        self.assertEqual(self.square_2.width, 10)
        self.assertEqual(self.square_2.height, 10)
        self.assertEqual(self.square_2.x, 1)
        self.assertEqual(self.square_2.y, 1)
        self.square_2.update(y=2, width=20, x=2, id=2)
        self.assertEqual(self.square_2.id, 2)
        self.assertEqual(self.square_2.width, 20)
        self.assertEqual(self.square_2.height, 10)
        self.assertEqual(self.square_2.x, 2)
        self.assertEqual(self.square_2.y, 2)
"""
