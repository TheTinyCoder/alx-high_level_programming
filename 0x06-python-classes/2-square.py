#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Square class

    Attributes:
        size (int): length of the square
    """
    def __init__(self, size=0):
        if (size < 0):
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        self.__size = size
