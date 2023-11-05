#!/usr/bin/python3
"""
Module that converts/serializes object to json
"""

import json


def to_json_string(my_obj):
    """
    Serializes objects in json
    Args:
        my_obj: object to serialize
    Returns: JSON representation of an object
    """
    return (json.dumps(my_obj))
