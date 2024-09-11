#!/bin/bash
# script that takes in a URL & file, sends a JSON POST request to the URL and displays the body of the response
curl -H "Content-Type: application/json" -d "$(cat "$2")" -sX POST "$1"
