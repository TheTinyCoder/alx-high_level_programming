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
        self.__width = width

    def get_width(self):
        return self.__width

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return self.__height

    def set_x(self, x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self, y):
        self.__y = y

    def get_y(self):
        return self.__y
