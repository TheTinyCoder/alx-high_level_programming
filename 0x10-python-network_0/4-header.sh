#!/bin/bash
# Script that takes an URL and displays the body of the response
curl -sL 0.0.0.0:5000/route_5 -H "X-School-User-Id: 98" -X GET -d "Hello School!"
