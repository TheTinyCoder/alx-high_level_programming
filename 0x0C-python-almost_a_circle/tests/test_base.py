#!/usr/bin/python3
"""
Base Test Module
"""
import io
import json
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
        """Test to_json_string function"""
        json = Base.to_json_string([Square(10).to_dictionary()])
        self.assertTrue(isinstance(json, str))
        json = Base.to_json_string([Rectangle(10, 10).to_dictionary()])
        self.assertTrue(isinstance(json, str))

    def test_save_to_file(self):
        """Test save_to_file function"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        r1, r2 = Rectangle(3, 4), Rectangle(5, 8, 1)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(
                json.load(file), [r1.to_dictionary(), r2.to_dictionary()])
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")
        Square.save_to_file([Square(10, 0, 0, 3)])
        with open("Square.json", "r") as f:
            sys.stdout = file = io.StringIO()
            print(f.read())
            sys.stdout = sys.__stdout__
        self.assertEqual(
            file.getvalue()[:-1], '[{"id": 3, "size": 10, "x": 0, "y": 0}]')
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_from_json_string(self):
        """Test from_json_string function"""
        json = Base.to_json_string([Square(10, 0, 0, 3).to_dictionary()])
        self.assertTrue(isinstance(json, str))
        self.assertTrue(isinstance(Base.from_json_string(json), list))
        a_list = Base.from_json_string(json)
        self.assertEqual(a_list, [{"id": 3, "size": 10, "x": 0, "y": 0}])
        json = Base.to_json_string([Rectangle(10, 10).to_dictionary()])
        self.assertTrue(isinstance(json, str))
        self.assertTrue(isinstance(Base.from_json_string(json), list))

    def test_create(self):
        """Test create function"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        sys.stdout = file1 = io.StringIO()
        print(r1)
        sys.stdout = file2 = io.StringIO()
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(file1.getvalue(), file2.getvalue())
        s1 = Square(5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        sys.stdout = file1 = io.StringIO()
        print(s1)
        sys.stdout = file2 = io.StringIO()
        print(s2)
        sys.stdout = sys.__stdout__
        self.assertEqual(file1.getvalue(), file2.getvalue())

    def test_load_from_file(self):
        """Test load_from_file function"""
        r1 = Rectangle(10, 7)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        r3, r4 = Rectangle.load_from_file()
        sys.stdout = file1 = io.StringIO()
        print(r1)
        sys.stdout = file2 = io.StringIO()
        print(r3)
        sys.stdout = sys.__stdout__
        self.assertEqual(file1.getvalue(), file2.getvalue())
        sys.stdout = file1 = io.StringIO()
        print(r2)
        sys.stdout = file2 = io.StringIO()
        print(r4)
        sys.stdout = sys.__stdout__
        self.assertEqual(file1.getvalue(), file2.getvalue())
        s1 = Square(10)
        s2 = Square(4)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        s3, s4 = Square.load_from_file()
        sys.stdout = file1 = io.StringIO()
        print(s1)
        sys.stdout = file2 = io.StringIO()
        print(s3)
        sys.stdout = sys.__stdout__
        self.assertEqual(file1.getvalue(), file2.getvalue())
        sys.stdout = file1 = io.StringIO()
        print(s2)
        sys.stdout = file2 = io.StringIO()
        print(s4)
        sys.stdout = sys.__stdout__
        self.assertEqual(file1.getvalue(), file2.getvalue())

    def test_save_to_file_csv(self):
        """Test save_to_file_csv function"""
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file:
            self.assertEqual(file.read(), "\n")
        r1, r2 = Rectangle(3, 4), Rectangle(5, 8, 1)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            i = 0
            a_list = ["width,height,x,y", "3,4,0,0", "5,8,1,0"]
            sys.stdout = file1 = io.StringIO()
            print(file.read())
            sys.stdout = sys.__stdout__
            for line in file1.getvalue().split('\n')[:-2]:
                line = ",".join(line.split(',')[1:])
                self.assertTrue(line == a_list[i])
                i += 1
        Square.save_to_file_csv([Square(10, 0, 0, 3)])
        with open("Square.csv", "r") as file:
            i = 0
            a_list = ["size,x,y", "10,0,0"]
            sys.stdout = file1 = io.StringIO()
            print(file.read())
            sys.stdout = sys.__stdout__
            for line in file1.getvalue().split('\n')[:-2]:
                line = ",".join(line.split(',')[1:])
                self.assertTrue(line == a_list[i])
                i += 1

    def test_load_from_file_csv(self):
        """Test load_from_file_csv function"""
        r1 = Rectangle(10, 7)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        r3, r4 = Rectangle.load_from_file_csv()
        sys.stdout = file1 = io.StringIO()
        print(r1)
        sys.stdout = file2 = io.StringIO()
        print(r3)
        sys.stdout = sys.__stdout__
        self.assertEqual(file1.getvalue(), file2.getvalue())
        sys.stdout = file1 = io.StringIO()
        print(r2)
        sys.stdout = file2 = io.StringIO()
        print(r4)
        sys.stdout = sys.__stdout__
        self.assertEqual(file1.getvalue(), file2.getvalue())
        s1 = Square(10)
        s2 = Square(4)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        s3, s4 = Square.load_from_file_csv()
        sys.stdout = file1 = io.StringIO()
        print(s1)
        sys.stdout = file2 = io.StringIO()
        print(s3)
        sys.stdout = sys.__stdout__
        self.assertEqual(file1.getvalue(), file2.getvalue())
        sys.stdout = file1 = io.StringIO()
        print(s2)
        sys.stdout = file2 = io.StringIO()
        print(s4)
        sys.stdout = sys.__stdout__
        self.assertEqual(file1.getvalue(), file2.getvalue())
