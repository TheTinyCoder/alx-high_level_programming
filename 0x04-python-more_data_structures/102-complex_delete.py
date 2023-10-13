#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = [k for k, v in a_dictionary.items() if a_dictionary[k] == value]
    for key in keys:
        del a_dictionary[key]
    return (a_dictionary)
