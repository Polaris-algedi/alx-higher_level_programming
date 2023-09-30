#!/usr/bin/python3
"""This module sends a request to a URL and displays the 'X-Request-Id'
from the response header."""


if __name__ == "__main__":
    import urllib.request
    import sys
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.info()
        print(x_request_id.get('X-Request-Id'))
