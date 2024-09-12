#!/usr/bin/python3
"""
Script that fetches https://alx-intranet.hbtn.io/status
"""


import sys
from requests.exceptions import HTTPError
import requests

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    try:
        r.raise_for_status()
        print(r.text)
    except HTTPError:
        print(f"Error code: {r.status_code}")
