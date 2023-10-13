#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return (None)
    return (sorted(a_dictionary.items(),
                   reverse=True, key=lambda item: item[1])[0][0])
