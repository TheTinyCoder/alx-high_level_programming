#!/usr/bin/python3
"""Base Module"""


class Base:
    """
    Base class
    Attributes:
        nb_objects (int: private class attribute)
        id: (int: public instance attribute)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return str(list_dictionaries)
