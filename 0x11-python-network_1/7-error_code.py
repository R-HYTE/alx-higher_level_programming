#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL, and displays the body
of the response.
"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]

    try:
        response = requests.get(url)
        # Raises HTTPError for bad responses (status codes 4xx and 5xx)
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.HTTPError as e:
        print("Error code:", e.response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
