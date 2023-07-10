#!/usr/bin/python3
"""
This module contains the function lookup()
that returns the list of available attributes
and methods of an object.

"""


def lookup(obj):
    """Returns a list of available attributes and methods
    of an object.

    Args:
        obj (class): object

    Returns:
        list: list of available attributes and methods of an object
    """
    return dir(obj)
