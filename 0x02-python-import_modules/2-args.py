#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    if (len(argv) == 1):
        print("0 arguments")
    elif (len(argv) > 1):
        s = "s:" if len(argv) > 2 else ":"
        print("{} argument{}".format(len(argv) - 1, s))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
