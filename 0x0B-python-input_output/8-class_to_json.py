#!/usr/bin/python3
"""
Module that converts/serializes instance of a Class to json
"""

import json


def class_to_json(obj):
    """
    Serializes instances of a Class in json
    Args:
        obj: object to serialize
    Returns: JSON representation of an object
    """
    return (json.dumps(obj.__dict__))
