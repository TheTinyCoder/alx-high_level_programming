#!/usr/bin/python3
"""
Script that sends a request to the URL
displays the body of the response
and handles error
"""


from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
