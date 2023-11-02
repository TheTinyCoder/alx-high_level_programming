#!/usr/bin/python3
"""
Defines class MyInt that inherits from int
"""


class MyInt(int):
    """
    Inherits from int
    """
    def __eq__(self, value):
        """checks if instances of MyInt are not equal"""
        return not super().__eq__(value)

    def __ne__(self, value):
        """checks if instances of MyInt are equal"""
        return super().__eq__(value)
