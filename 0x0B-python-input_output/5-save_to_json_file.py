#!/usr/bin/python3
"""
Module that converts/serializes object to json and saves to file
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Serializes objects in json and writes to text file
    Args:
        my_obj: object to serialize
        filename: name of file to write to
    """
    with open(filename, mode='w') as f:
        json.dump(my_obj, f)
