#!/usr/bin/python3
"""
Module that converts/deserializes object from json file
"""

import json


def load_from_json_file(filename):
    """
    Deserializes objects from json file
    Args:
        filename: file to deserialize
    Returns: object represented by a JSON file
    """
    with open(filename) as f:
        return (json.load(f))
