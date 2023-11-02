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
    if not hasattr(a_class, attribute):
        raise TypeError("can't add new attribute")
    a_class.attribute = value