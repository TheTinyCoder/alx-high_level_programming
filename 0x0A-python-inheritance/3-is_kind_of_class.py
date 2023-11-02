#!/usr/bin/python3
"""
Defines is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a specified class
    or an instance of a class derived from the specified class
    Args:
        obj: an object
        a_class: a class or object type
    Returns:
        True: if obj is an instance of a_class or derived class
        False: otherwise
    """
    return (isinstance(obj, a_class))
