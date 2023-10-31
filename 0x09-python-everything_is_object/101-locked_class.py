#!/usr/bin/python3
"""
Defines a class that doesn't allow dynamically created variables
"""
class LockedClass():
    __slots__ = ["first_name"]
    pass
