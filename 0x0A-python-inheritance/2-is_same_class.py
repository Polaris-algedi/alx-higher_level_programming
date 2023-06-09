#!/usr/bin/python3
"""This module contains one function is_same_class()"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the,
    specified class, otherwise False.

    Args:
        obj (a_class): object to compare.
        a_class (type): type to be compared against.

    Returns:
        bool: True for success, False otherwise.
    """
    return type(obj) == a_class
