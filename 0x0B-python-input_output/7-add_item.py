#!/usr/bin/python3
"""
Module that adds all arguments to a list, serializes & saves them to a file
"""
import sys

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    a_list = load("add_item.json")
except Exception:
    a_list = []
a_list = a_list + sys.argv[1:]
save(a_list, "add_item.json")
