#!/usr/bin/python3

"""
This script fetches the content from a specified URL using the urllib package.
"""

import urllib.request


def fetch_url_content(url):
    """
    Fetch the content from the specified URL.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        bytes: The content of the URL as bytes, or None if there was an error.
    """
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            return response.read()

    except urllib.error.URLError as e:
        print(f"Error during request to {url}: {e}")
        return None


def main():
    """
    Main function to execute the script.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    content = fetch_url_content(url)

    if content is not None:
        print('Body response:')
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")


if __name__ == '__main__':
    main()
