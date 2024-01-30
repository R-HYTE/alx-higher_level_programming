#!/usr/bin/python3
"""Script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response."""

import sys
import requests


def post_email(url, email):
    """
    Send a POST request to the specified URL with the email as a parameter.
    """
    try:
        response = requests.post(url, data={'email': email})
        response.raise_for_status()  # Raise an HTTPError for bad responses
        return response.text

    except requests.RequestException as e:
        print(f"Error during request to {url}: {e}")
        return None


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = post_email(url, email)

    if response_body is not None:
        print(response_body)
    else:
        print("Unable to perform the POST request.")
