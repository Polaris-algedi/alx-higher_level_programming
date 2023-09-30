#!/usr/bin/python3
"""
This module sends a request to a URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400,
it prints an error message.
"""

import requests
import requests.exceptions
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as http_err:
        print(f'Error code: {http_err.response.status_code}')
