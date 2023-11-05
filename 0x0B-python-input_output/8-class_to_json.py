#!/usr/bin/python3
"""
Module that converts/serializes instance of a Class to json
"""


def class_to_json(obj):
    """
    Serializes instances of a Class in json
    Args:
        obj: object to serialize
    Returns: dictionary representation of obj
    """
    return obj.__dict__
