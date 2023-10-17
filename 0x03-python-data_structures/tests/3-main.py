#!/usr/bin/python3
import sys
sys.path.append('../')

print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

my_list = None
print_reversed_list_integer(my_list)


