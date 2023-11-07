#!/usr/bin/python3
"""
Module that reads stdin line by line and computes metrics
"""

import sys

totalFileSize = 0
status = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0
try:
    for line in sys.stdin:
        log = line.split()
        totalFileSize += int(log[-1])
        if int(log[-2]) in status.keys():
            status[int(log[-2])] += 1
        line_count += 1
        if line_count % 10 == 0:
            print(f"File size: {totalFileSize}")
            for (k, v) in sorted(status.items()):
                if v != 0:
                    print(f"{k}: {v}")
        sys.stdout.flush()
except KeyboardInterrupt:
    print(f"File size: {totalFileSize}")
    for (k, v) in sorted(status.items()):
        if v != 0:
            print(f"{k}: {v}")
