#!/usr/bin/python3
def add_attribute(a_class, attribute, value):
    if not hasattr(a_class, attribute):
        raise TypeError("can't add new attribute")
    a_class.attribute = value
