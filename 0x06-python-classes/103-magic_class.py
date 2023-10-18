#!/usr/bin/python3
# import dis
import math
"""
Module to reproduce bytecode
"""


class MagicClass:
    """
    Defines a circle

    Attributes:
        radius (int or float): radius of circle
    """
    def __init__(self, radius=0):
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """
        Computes area of circle

        Returns: area of the circle
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """
        Computes circumference of circle

        Returns: circumference of the circle
        """
        return (math.pi * 2 * self.__radius)


# dis.dis(MagicClass)
