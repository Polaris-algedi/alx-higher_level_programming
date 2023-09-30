#!/usr/bin/python3
"""
This module sends a request to a URL and displays the body of the response.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f'Error code: {e.code}')
