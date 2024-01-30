#!/usr/bin/python3
"""
This script fetches the content from a specified URL using the urllib package.
"""

import urllib.request
import logging

URL = 'https://alx-intranet.hbtn.io/status'

def fetch_url_content(url):
    """
    Fetch the content from the specified URL.

    Args:
        url (str): The URL to fetch the content from.

    Returns:
        bytes: The content of the URL as bytes, or None if there was an error.
    """
    try:
        with urllib.request.urlopen(url) as response:
            return response.read()

    except urllib.error.URLError as e:
        logging.error(f"Error during request to {url}: {e}")
        return None

def main():
    """
    Main function to execute the script.
    """
    content = fetch_url_content(URL)

    if content is not None:
        print('Body response:')
        print(f"\t- type: {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content: {content.decode('utf-8')}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.ERROR)
    main()
