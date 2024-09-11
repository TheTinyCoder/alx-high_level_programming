#!/bin/bash
# script that takes in a URL, sends a request and displays body size of the response
curl -I "$1" |& grep "^Content-Length:" | cut -d ":" -f2 | tr -d " "
