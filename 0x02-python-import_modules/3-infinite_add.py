#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    total = 0
    if (len(argv) > 1):
        for i in range(1, len(argv)):
            total += int(argv[i])

    print("{}".format(total))
