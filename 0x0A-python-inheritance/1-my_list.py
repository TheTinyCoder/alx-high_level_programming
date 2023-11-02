#!/usr/bin/python3
"""
Defines a class MyList
"""
class MyList(list):
    """
    Inherits fron list
    """
    def print_sorted(self):
        """
        Prints list sorted in ascending order
        """
        print(sorted(self))
