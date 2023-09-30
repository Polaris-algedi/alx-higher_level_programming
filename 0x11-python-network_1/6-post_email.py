#!/usr/bin/python3
"""
This module sends a POST request to a URL with an email as a parameter,
and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    values = {'email': email}
    response = requests.post(url, data=values)
    print(response.text)
