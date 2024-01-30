#!/usr/bin/python3
"""
Script that takes in a URL and an email,
sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.parse
import urllib.request


def send_post_request(url, email):
    """
    Send a POST request with the email as a parameter and return the response.
    """
    try:
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        req = urllib.request.Request(url, data)

        with urllib.request.urlopen(req) as response:
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        return f"Error during request to {url}: {e}"


def get_response_body(url, email):
    """Get and print the relevant part of the server response."""
    response_body = send_post_request(url, email)

    if response_body.startswith("Error"):
        print(response_body)
    else:
        # Extract only the relevant part of the server response
        relevant_info = response_body.splitlines()[-1]
        print(relevant_info)


def main():
    """Main entry point of the script."""
    if len(sys.argv) != 3:
        print("Usage: ./script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    
    get_response_body(url, email)


if __name__ == '__main__':
    main()
