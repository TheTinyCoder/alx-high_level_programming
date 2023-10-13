#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set(i for i in set_1 if i in set_2)
    return (set(set_1 | set_2) - new_set)
