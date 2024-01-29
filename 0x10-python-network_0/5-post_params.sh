#!/bin/bash
# Sends a POST request to the URL with email and subject parameters and displays the body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
