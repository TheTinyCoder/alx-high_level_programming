#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """
    Square class

    Attributes:
        size (int): length of the square
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
        Getter method for size

        Returns: size of Square
        """
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes area of Square

        Returns: area
        """
        return (self.__size ** 2)
