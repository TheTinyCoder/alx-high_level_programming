#!/usr/bin/python3
"""
Defines inherits_from function
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherits
    from the specified class (directly or indirectly)
    Args:
        obj: an object
        a_class: a class or object type
    Returns:
        True: if obj is an instance of a class that inherits a_class
        False: otherwise
    """
    return (type(obj) is not a_class and issubclass(type(obj), a_class))
