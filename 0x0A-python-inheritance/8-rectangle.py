#!/usr/bin/python3
"""
Defines class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Inherits from BaseGeometry
    Attributes:
        width (int): length of rectangle
        height (int): width of rectangle
    """
    def __init__(self, width, height):
        if self.integer_validator("width", width) is None:
            self.__width = width
        if self.integer_validator("height", height) is None:
            self.__height = height
