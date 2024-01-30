#!/usr/bin/python3
"""
Fetches a URL, sends a request,
and displays the X-Request-Id value in the response header.
"""

import sys
import requests


def get_x_request_id(url):
    """
    Send a request to the specified URL
    and retrieve the X-Request-Id header value.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        x_request_id = response.headers.get("X-Request-Id")
        return x_request_id

    except requests.RequestException as e:
        print(f"Error during request to {url}: {e}")
        return None


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: ./script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    x_request_id = get_x_request_id(url)

    if x_request_id is not None:
        print(x_request_id)
    else:
        print("Unable to retrieve X-Request-Id.")
