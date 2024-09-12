#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""


from urllib.parse import urlencode
from urllib.request import Request, urlopen
import sys

if __name__ == "__main__":
    values = {}
    values["email"] = sys.argv[2]
    data = urlencode(values).encode('utf-8')
    req = Request(sys.argv[1], data)
    with urlopen(req) as response:
        val = response.read().decode('utf-8')
        print(val)
