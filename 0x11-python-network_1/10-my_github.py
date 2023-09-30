#!/usr/bin/python3
"""Sends a request to the GitHub API and displays the user's id"""

if __name__ == '__main__':
    import requests
    import sys

    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=(username, token))
    print(f"{response.json().get('id')}")
