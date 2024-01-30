#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status using the requests package."""

import requests


def fetch_alx_intranet_status():
    """
    Fetches status from https://alx-intranet.hbtn.io and prints the response.
    """
    url = "https://alx-intranet.hbtn.io/status"

    try:
        # Send an HTTP GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Print information about the response
        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {response.text}")

    except requests.RequestException as e:
        print(f"Error during request to {url}: {e}")


if __name__ == '__main__':
    fetch_alx_intranet_status()
