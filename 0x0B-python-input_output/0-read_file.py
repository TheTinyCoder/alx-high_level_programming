#!/usr/bin/python3
"""
Module that reads a text file (UTF8)
"""


def read_file(filename=""):
    """
    Reads file and prints to stdout
    Args:
        filename: name of file to read
    """
    with open(filename) as f:
        print(f.read(), end="")
