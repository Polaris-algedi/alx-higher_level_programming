#!/usr/bin/python3
"""Examples to demonstrate how Input/Output works in python"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: Object to serialize.
        filename: name of the file.

    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
