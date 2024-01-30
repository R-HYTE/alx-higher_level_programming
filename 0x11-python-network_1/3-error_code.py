#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the body
of the response (decoded in utf-8)
"""

import sys
import urllib.error
import urllib.request


def fetch_url(url):
    """Fetch a URL and display the body of the response."""
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url(url)
