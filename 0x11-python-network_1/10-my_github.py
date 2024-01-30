#!/usr/bin/python3
"""Script that takes your GitHub credentials (username and personal access token)
and uses the GitHub API to display your id"""

import sys
from requests.auth import HTTPBasicAuth
import requests


def get_github_user_id(username, personal_access_token):
    """Retrieve and display the GitHub user ID using provided credentials."""
    try:
        auth = HTTPBasicAuth(username, personal_access_token)
        response = requests.get('https://api.github.com/user', auth=auth)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            user_id = response.json().get('id')
            print(user_id)
        else:
            print(None)

    except Exception as e:
        print(None)


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <username> <personal_access_token>")
        sys.exit(1)

    username, personal_access_token = sys.argv[1], sys.argv[2]
    get_github_user_id(username, personal_access_token)
