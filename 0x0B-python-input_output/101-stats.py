#!/usr/bin/python3
"""
Module that reads stdin line by line and computes metrics
"""

import sys

totalFileSize = 0
status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_log(size, status):
    """
    Prints parsed log
    Args:
        size (int): total file size
        status (dict): dict with status codes and no. of lines they're on
    """
    print(f"File size: {size}")
    for (k, v) in sorted(status.items()):
        if v != 0:
            print(f"{k}: {v}")


try:
    for line in sys.stdin:
        log = line.split()
        try:
            totalFileSize += int(log[-1])
            status[int(log[-2])] += 1
            line_count += 1
        except (KeyError, ValueError):
            pass
        if line_count % 10 == 0:
            print_log(totalFileSize, status)
except KeyboardInterrupt:
    print_log(totalFileSize, status)
# For lines less than 10
# print_log(totalFileSize, status)
