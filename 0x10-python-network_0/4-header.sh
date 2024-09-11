#!/bin/bash
# script that takes in a URL, sends a GET request with a header and displays body of the response
curl -sH "X-School-User-Id:98" -X GET "$1"
