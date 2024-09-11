#!/usr/bin/bash
curl -I "$1" |& grep "^Content-Length:" | cut -d ":" -f2 | tr -d " "
