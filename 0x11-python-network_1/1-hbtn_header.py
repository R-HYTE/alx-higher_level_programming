#!/usr/bin/python3
"""
This script takes a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable
found in the header of the response.
"""

import sys
import urllib.request


def get_x_request_id(url):
    """
    Send a request to the specified URL and
    retrieve the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str or None: The value of the X-Request-Id header
        None if the header is not present.
    """
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            headers = dict(response.headers)
            x_request_id = headers.get("X-Request-Id")
            return x_request_id

    except urllib.error.URLError as e:
        print(f"Error during request to {url}: {e}")
        return None


if __name__ == '__main__':
    url = sys.argv[1]
    x_request_id = get_x_request_id(url)

    if x_request_id is not None:
        print(x_request_id)
    else:
        print("Unable to retrieve X-Request-Id.")
