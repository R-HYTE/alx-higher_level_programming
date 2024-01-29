#!/bin/bash
# Displays all HTTP methods the server will accept for the given URL
curl -s -i -X OPTIONS "$1" | awk -F': ' '/Allow/ {print $2}'
