#!/usr/bin/python3
def uppercase(str):
    for index, c in enumerate(str):
        if (ord(c) > 96 and ord(c) < 123):
            c = chr(ord(c) - 32)
        if (index != len(str) - 1):
            print("{}".format(c), end="")
        else:
            print("{}".format(c))
