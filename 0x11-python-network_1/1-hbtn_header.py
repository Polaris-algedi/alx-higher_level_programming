#!/usr/bin/python3
"""
This module sends a request to a URL and displays the 'X-Request-Id'
from the response header.
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
