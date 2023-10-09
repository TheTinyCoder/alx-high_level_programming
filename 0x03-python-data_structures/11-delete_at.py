#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (idx < 0 or idx > len(my_list) - 1):
        return (my_list)
    new_list = my_list[:-1]
    j = 0
    for i in range(len(my_list)):
        if (i != idx):
            new_list[j] = my_list[i]
            j += 1
    return (new_list)
