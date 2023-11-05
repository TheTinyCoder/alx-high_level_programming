#!/usr/bin/python3
"""
Module that appends a string to a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    Appends to file
    Args:
        filename: name of file to append to
        text: text to write to file
    Returns: number of characters(bytes) written
    """
    with open(filename, mode='a') as f:
        return (f.write(text))
