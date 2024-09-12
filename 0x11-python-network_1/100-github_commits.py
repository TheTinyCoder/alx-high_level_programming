#!/usr/bin/python3
"""
Script that takes repo name and owner and prints
10 most recent commits by: `<sha>: <author name>`
"""


import sys
import requests

if __name__ == "__main__":
    r = requests.get(
        f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits")
    try:
        for commit in r.json()[:10]:
            print(f"{commit['sha']}: {commit['commit']['author']['name']}")
    except IndexError:
        pass
