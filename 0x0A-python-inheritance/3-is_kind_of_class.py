#!/usr/bin/python3
"""This module contains one function is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class, otherwise False.

    Args:
        obj (a_class): object to compare.
        a_class (type): type to be compared against.

    Returns:
        bool: True for success, False otherwise.
    """
    return isinstance(obj, a_class)
