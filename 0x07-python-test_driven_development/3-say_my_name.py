#!/usr/bin/python3
"""
Prints name
"""


def say_my_name(first_name, last_name=""):
    """
    Concatenates names and prints
    Args:
        first_name (str)
        last_name (str; optional)
    Raises:
        TypeError if first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
