#!/usr/bin/python3
"""
Module that  writes a string to a text file (UTF8)
"""


def write_file(filename="", text=""):
    """
    Writes to file
    Args:
        filename: name of file to write to
        text: text to write to file
    Returns: number of characters(bytes) written
    """
    with open(filename, mode='w') as f:
        return (f.write(text))
