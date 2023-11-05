#!/usr/bin/python3
"""
Module that converts/deserializes object from json string
"""

import json


def from_json_string(my_str):
    """
    Deserializes objects from json string
    Args:
        my_str: string to deserialize
    Returns: object represented by a JSON string
    """
    return (json.loads(my_str))
