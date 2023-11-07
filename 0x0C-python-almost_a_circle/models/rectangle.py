#!/usr/bin/python3
"""Rectangle Module"""


class Rectangle(Base):
    """
    Rectangle class: inherits from Base class
    Attributes:
        __width (int; private instance attribute)
        __height (int; private instance attribute)
        __x (int; private instance attribute)
        __y (int; private instance attribute)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().id
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def set_width(self, width):
        """setter for width"""
        self.__width = width

    def get_width(self):
        """getter for width"""
        return self.__width

    def set_height(self, height):
        """setter for height"""
        self.__height = height

    def get_height(self):
        """getter for height"""
        return self.__height

    def set_x(self, x):
        """setter for x"""
        self.__x = x

    def get_x(self):
        """getter for x"""
        return self.__x

    def set_y(self, y):
        """setter for y"""
        self.__y = y

    def get_y(self):
        """getter for y"""
        return self.__y
