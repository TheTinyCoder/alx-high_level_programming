#!/usr/bin/python3
"""
Defines is_same_class function
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class
    Args:
        obj: an object
        a_class: a class or object type
    Returns:
        True: if obj is exactly an instance of a_class
        False: otherwise
    """
    return (type(obj) is a_class)
