#!/usr/bin/python3
import sys
sys.path.append('../')
print_list_integer = __import__("0-print_list_integer").print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
my_list = []
print_list_integer(my_list)
my_list = [1, 2, "H", 9]
print_list_integer(my_list)
