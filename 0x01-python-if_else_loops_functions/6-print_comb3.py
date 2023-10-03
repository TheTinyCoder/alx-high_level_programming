#!/usr/bin/python3
for i in range(0, 100):
    if (i < 89):
        if ((((i % 10) * 10) + i / 10) > i and i % 11 != 0):
            print("{:02d}, ".format(i), end="")
    elif (i == 89):
        print("{}".format(i))
