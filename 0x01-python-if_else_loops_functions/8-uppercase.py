#!/usr/bin/python3
def uppercase(str):
    if (len(str) > 0):
        for c in str:
            if (ord(c) > 96 and ord(c) < 123):
                c = chr(ord(c) - 32)
            print("{}".format(c), end="")
    print("")
