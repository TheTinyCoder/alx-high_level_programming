#!/bin/bash
# script that takes in URL and makes curl display information on stdout
curl -s -o /dev/null -w "You find me!" "$1"
