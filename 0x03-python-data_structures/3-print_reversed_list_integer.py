#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        # if (type(my_list[i]) is int):
        print("{:d}".format(my_list[i]))
