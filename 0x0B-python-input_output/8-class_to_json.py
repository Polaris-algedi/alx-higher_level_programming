#!/usr/bin/python3
"""Examples to demonstrate how Input/Output works in python"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure
    """
    return obj.__dict__
