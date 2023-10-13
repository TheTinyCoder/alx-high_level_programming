#!/usr/bin/python3
import re
""" Roman to Integer conversion
"""


def roman_to_int(roman_string):
    roman_string = roman_string.upper()
    a_dict = {
        'ones': ['IX', 'VIII', 'VII', 'VI', 'V', 'IV', 'III', 'II', 'I'],
        'tens': ['XC', 'LXXX', 'LXX', 'LX', 'L', 'XL', 'XXX', 'XX', 'X'],
        'huns': ['CM', 'DCCC', 'DCC', 'DC', 'D', 'CD', 'CCC', 'CC', 'C'],
        'thous': ['MMM', 'MM', 'M']
    }
    number = 0
    while (len(roman_string) > 0):
        for key, values in a_dict.items():
            for value in values:
                str = re.match(f"^{value}", roman_string)
                if (str):
                    value_index = list(values).index(value)
                    number += (
                        (10 ** (list(a_dict.keys()).index(key))) *
                        (len(values) - value_index)
                    )
                    roman_string = roman_string.removeprefix(str.group())
    return (number)
