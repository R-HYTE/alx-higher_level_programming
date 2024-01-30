#!/usr/bin/python3
"""
Script that performs a user search based on
a letter using a POST request to http://0.0.0.0:5000/search_user
"""

import requests
import sys


def perform_user_search(letter=""):
    """
    Perform a user search request with the given letter.

    Args:
        letter (str): The letter to search for.

    Returns:
        None: Displays the result as specified.
    """
    search_payload = {"q": letter}
    response = requests.post(
        "http://0.0.0.0:5000/search_user",
        data=search_payload
    )

    try:
        user_data = response.json()
        if user_data:
            print("[{}] {}".format(user_data.get("id"), user_data.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    search_letter = "" if len(sys.argv) == 1 else sys.argv[1]
    perform_user_search(search_letter)
