#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            i = chr(ord(i) - 32)
        if (str.index(i) != -1):
            print("{:c}".format(i), end="")
        else:
            print("{}".format(i), end="")
