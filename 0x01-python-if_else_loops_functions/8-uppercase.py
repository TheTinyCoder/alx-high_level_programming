#!/usr/bin/python3
def uppercase(str):
    if (len(str) == 0):
        print()
    else:
        for c in str:
            if (ord(c) > 96 and ord(c) < 123):
                c = chr(ord(c) - 32)
        print(str)
