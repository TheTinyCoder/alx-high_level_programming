#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the value of the header X-Request-Id
"""


import sys
import requests

if __name__ == "__main__":
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        data = r.json()
        if len(data) == 0:
            print("No result")
        else:
            print(f"[{data['id']}] {data['name']}")
    except ValueError:
        print("Not a valid JSON")
