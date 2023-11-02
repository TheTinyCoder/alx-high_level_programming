#!/usr/bin/python3
"""
Defines add_attribute
"""


def add_attribute(a_class, attribute, value):
    """
    Adds a new attribute to an object if it’s possible
    Args:
        a_class (object)
        attribute : name of attribute to add to object
        value: value of the attribute being added
    Raises:
        TypeError if the object can’t have a new attribute
    """
    if not hasattr(a_class, '__dict__'):
        raise TypeError("can't add new attribute")
    elif hasattr(a_class, '__slots__'):
        if attribute not in a_class.__slots__:
            raise TypeError("can't add new attribute")
    setattr(a_class, attribute, value)
