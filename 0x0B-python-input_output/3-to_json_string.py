#!/usr/bin/python3
"""Examples to demonstrate how Input/Output works in python"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        my_obj: Object to serialize.

    Returns:
        Json representation.
    """
    return json.dumps(my_obj)
