#!/usr/bin/python3
"""
Adds two integers
"""


def add_integer(a, b=98):
    """
    Addition function
    Args:
        a (float or int)
        b (float or int)
    Returns:
        addition of a and b
    Raises:
        TypeError if a or b is not an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
