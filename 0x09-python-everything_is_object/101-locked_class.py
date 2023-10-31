#!/usr/bin/python3
"""
Defines a class that doesn't allow dynamically created variables
"""


class LockedClass():
    """
    Class with predefined attributes
    """
    __slots__ = ["first_name"]
    pass
