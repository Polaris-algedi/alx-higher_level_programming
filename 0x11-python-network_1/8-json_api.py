#!/usr/bin/python3
"""This module sends a POST request to a URL with a letter as a parameter,
and displays the body of the response."""

if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
