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
    data = []
    for commit in r.json():
        data.append({
            "name": commit['commit']['author']['name'],
            "date": commit['commit']['author']['date'],
            "sha": commit['sha']})
    for x in range(10):
        print(f"{data[x]['sha']}: {data[x]['name']}")
