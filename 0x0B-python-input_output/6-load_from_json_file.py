#!/usr/bin/python3
"""Examples to demonstrate how Input/Output works in python"""
import json


def load_from_json_file(filename):
    """Gets an Object from a text file,
    using JSON representation.

    Args:
        filename: name of the file.

    Returns:
        Object (Python data structure).

    """
    with open(filename) as f:
        return json.load(f)
