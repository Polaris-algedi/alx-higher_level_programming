#!/usr/bin/python3
"""Examples to demonstrate how Input/Output works in python"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str: String to deserialize.

    Returns:
        Object (Python data structure).
    """
    return json.loads(my_str)
