#!/bin/bash
# script that takes in a URL, sends a GET request and displays body size of the response if status is 200
curl -sLX GET "$1"
