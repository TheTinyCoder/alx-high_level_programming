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

    def to_json(self):
        """
        Serializes instances of Student in json
        Returns: dictionary representation of student
        """
        return self.__dict__
