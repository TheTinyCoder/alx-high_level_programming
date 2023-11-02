#!/usr/bin/python3
"""
Defines class Square that inherits from Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle
    Attributes:
        size (int): size of square
    """
    def __init__(self, size):
        if self.integer_validator("size", size) is None:
            self.__size = size
            super().__init__(size, size)
