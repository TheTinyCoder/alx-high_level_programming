#!/usr/bin/python3
"""
Changes space at end of sentence to newlines
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after: '.', '?' and ':''
    Args:
        text (str)
    Raises:
        TypeError if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        print(text[i], end="")
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("\n")
            i += 2 if (text[i + 1] == ' ') else 1
        else:
            i += 1
