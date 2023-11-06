#!/usr/bin/python3
"""
Append File Module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file,
    after each line containing a specific string
    Args:
        filename: name of file to append
        search_string: string to search in file
        new_string: string to append after line containing searched string
    """
    with open(filename, mode='r+') as f:
        lines = f.readlines()
    with open(filename, mode='w') as f:
        for line in lines:
            if search_string.lower() in line.lower():
                # lines.insert(lines.index(line) + 1, new_string)
                lines[lines.index(line)] = line + new_string
        f.writelines(lines)
