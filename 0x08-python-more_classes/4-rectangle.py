#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """
    Defines a rectangle
    Attributes:
        width (int): length of rectangle
        height (int): width of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property that retrieves width"""
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets width property
        Args:
            width: input width of rectangle
        Raises:
            TypeError if width is not an integer
            ValueError if width is less than 0
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Property that retrieves height"""
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets height property
        Args:
            height: input height of rectangle
        Raises:
            TypeError if height is not an integer
            ValueError if height is less than 0
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.width == 0 or self.height == 0:
            return (0)
        return (self.width + self.height) * 2

    def __str__(self):
        """
        define informal string representation of class Rectangle objects
        """
        if self.width == 0 or self.height == 0:
            return ("")
        return (('#' * self.width + '\n') * self.height)[:-1]

    def __repr__(self):
        """
        define official string representation of class Rectangle objects
        """
        return (f"Rectangle({self.width}, {self.height})")
