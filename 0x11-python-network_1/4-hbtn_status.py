#!/usr/bin/python3
"""
This module sends a request to a URL and displays the body of the response.
"""

import requests

if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    response_text = response.text
    print(f"Body response:")
    print(f"\t- type: {type(response_text)}")
    print(f"\t- content: {response_text}")
