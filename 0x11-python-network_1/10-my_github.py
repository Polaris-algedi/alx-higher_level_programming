#!/usr/bin/python3
"""
This module sends a request to the GitHub API and displays the user's id.
"""

import requests
import sys

username = sys.argv[1]
token = sys.argv[2]

response = requests.get('https://api.github.com/user', auth=(username, token))
print(f"{response.json().get('id')}")
