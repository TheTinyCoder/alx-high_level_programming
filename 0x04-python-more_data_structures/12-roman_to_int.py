#!/usr/bin/python3
""" Roman to Integer conversion
"""


def roman_to_int(roman_string):
    if (roman_string is None or not roman_string.isalpha()):
        return (0)
    roman_string = roman_string.upper()
    set_1 = ('CM', 'CD', 'XC', 'XL', 'IX', 'IV')
    roman_list = []
    i = 0
    while i < len(roman_string):
        if (i + 1 < len(roman_string)):
            str = roman_string[i] + roman_string[i + 1]
            if str in set_1:
                roman_list.append(str)
                i += 2
                continue
        if (i < len(roman_string)):
            roman_list.append(roman_string[i])
        i += 1
    a_dict = {
        'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
        'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'VIII': 8,
        'VII': 7, 'VI': 6, 'V': 5, 'IV': 4, 'III': 3, 'II': 2, 'I': 1}
    number = 0
    for i in roman_list:
        for key, value in a_dict.items():
            if (i == key):
                number = (value - number if (number < value)
                          else number + value)
    return (number)
