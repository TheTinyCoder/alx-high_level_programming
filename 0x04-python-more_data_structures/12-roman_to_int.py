#!/usr/bin/python3
""" Roman to Integer conversion
"""


def roman_to_int(roman_string):
    roman_string = [i for i in roman_string.upper()]
    a_dict = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
        'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'VIII': 8,
        'VII': 7, 'VI': 6, 'V': 5, 'IV': 4, 'III': 3, 'II': 2, 'I': 1}
    number = 0
    for i in roman_string:
        for key, value in a_dict.items():
            if (i == key):
                number = (value - number if (number < value)
                          else number + value)
    return (number)
