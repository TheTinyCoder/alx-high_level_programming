#!/usr/bin/python3
import sys
sys.path.append('../')
append_after = __import__('100-append_after').append_after

append_after("append_after_100.txt", "Python", "\"C is fun!\"\n")

filename = "append_after_100_1.txt"
text_search = "c is fun"
text_append = "Python is cool!\n"
append_after(filename, text_search, text_append)

