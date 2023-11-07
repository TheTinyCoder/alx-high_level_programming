#!/usr/bin/python3
"""
Module that reads stdin line by line and computes metrics
"""

import sys

file_size = 0
metrics = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
           "405": 0, "500": 0}
count = 0
try:
    for line in sys.stdin:
        log = line.strip().split(' ')
        file_size += int(log[-1])
        if log[-2] in metrics.keys():
            metrics[log[-2]] += 1
        count += 1
        if count % 10 == 0:
            print(f"File size: {file_size}")
            for (k, v) in metrics.items():
                if v != 0:
                    print(f"{k}: {v}")
except KeyboardInterrupt:
    print(f"File size: {file_size}")
    for (k, v) in metrics.items():
        if v != 0:
            print(f"{k}: {v}")
