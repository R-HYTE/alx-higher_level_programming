#!/bin/bash
# Takes a URL as input, sends a GET request to the URL, and displays the body of the response.
[ -z "$1" ] && echo "Usage: $0 <URL>" && exit 1; curl -Ls "$1"
