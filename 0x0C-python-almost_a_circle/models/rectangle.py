#!/usr/bin/python3
"""
Module for Rectangle
Inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle: inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @width.setter
    def width(self, width):
        """setter for width"""
        self.__width = width

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @height.setter
    def height(self, height):
        """setter for height"""
        self.__height = height

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @x.setter
    def x(self, x):
        """setter for x"""
        self.__x = x

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @y.setter
    def y(self, y):
        """setter for y"""
        self.__y = y

    @property
    def y(self):
        """getter for y"""
        return self.__y
