#!/usr/bin/python3
"""
Student Module
"""


class Student():
    """
    Defines a student
    Attributes:
        first_name
        last_name
        age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Serializes instances of Student in json
        Returns: dictionary representation of student
        """
        if attrs is not None and all(type(i) is str for i in attrs):
            return {k: v for (k, v) in self.__dict__.items() if k in attrs}
        return self.__dict__
