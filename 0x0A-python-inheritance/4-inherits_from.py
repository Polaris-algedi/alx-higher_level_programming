#!/usr/bin/python3
"""This module contains one function inherits_from()"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the
    specified class, otherwise False.

    Args:
        obj (a_class): object to compare.
        a_class (type): type to be compared against.

    Returns:
        bool: True for success, False otherwise.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
