#!/usr/bin/python3
"""Base Module"""
import json
import csv


class Base:
    """
    Base class
    Attributes:
        nb_objects (int: private class attribute)
        id (int: public instance attribute)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries
        Args:
            list_dictionaries: a list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        Args:
            list_objs: list of instances that inherit from Base
        """
        filename = cls.__name__ + ".json"
        with open(filename, mode='w') as file:
            if list_objs is None:
                file.write(cls.to_json_string(list_objs))
            else:
                dict_list = [i.to_dictionary() for i in list_objs]
                file.write(cls.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list represented by JSON string
        Args:
            json_string: string representing a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set
        Args:
            dictionary (dict: double pointer to a dictionary)
        """
        if cls.__name__ == "Rectangle":
            new_class = cls(10, 10)
        else:
            new_class = cls(10)
        new_class.update(**dictionary)
        return new_class

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r') as f:
                dict_list = cls.from_json_string(f.read())
            return ([cls.create(**i) for i in dict_list])
        except FileNotFoundError:
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes list_objs in CSV
        Args:
            list_objs: list of instances that inherit from Base
        """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w') as file:
            if list_objs is None:
                csv.writer(file).writerow([])
            else:
                dict_list = [i.to_dictionary() for i in list_objs]
                w = csv.DictWriter(file, dict_list[0].keys())
                w.writeheader()
                w.writerows(dict_list)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances from CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r') as file:
                dict_list = [{k: int(v) for (k, v) in row.items()}
                             for row in csv.DictReader(file)]
            return ([cls.create(**i) for i in dict_list])
        except FileNotFoundError:
            return ([])
