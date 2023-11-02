#!/usr/bin/python3
"""
Defines a class BaseGeometry
"""


class BaseGeometry():
    """
    Empty class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the parameter 'value'
        Args:
            name (str): name of value
            value (int)
        Raises:
            TypeError if value is not an integer
            ValueError if value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
