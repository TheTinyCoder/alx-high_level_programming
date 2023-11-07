#!/usr/bin/python3
"""Rectangle Module"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle class: inherits from Base class
    Attributes:
        width (int; private instance attribute)
        height (int; private instance attribute)
        x (int; private instance attribute)
        y (int; private instance attribute)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances"""
        super().id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @width.setter
    def width(self, width):
        """setter for width"""
        self.width = width

    @property
    def width(self):
        """getter for width"""
        return self.width

    @height.setter
    def height(self, height):
        """setter for height"""
        self.height = height

    @property
    def height(self):
        """getter for height"""
        return self.height

    @x.setter
    def x(self, x):
        """setter for x"""
        self.x = x

    @property
    def x(self):
        """getter for x"""
        return self.x

    @y.setter
    def y(self, y):
        """setter for y"""
        self.y = y

    @property
    def y(self):
        """getter for y"""
        return self.y
