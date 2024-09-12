#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the value of the header X-Request-Id
"""


import sys
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if "X-Request-Id" in r.headers.keys():
        print(r.headers["X-Request-Id"])
