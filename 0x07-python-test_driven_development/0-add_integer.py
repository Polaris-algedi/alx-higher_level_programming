#!/usr/bin/python3
"""
This module provides a function to add two integers or floats.

The function, 'add_integer(a, b=98)', takes two numeric arguments,
'a' and 'b', and returns their sum. If either 'a' or 'b' is a float,
it first casts them to integers before performing the addition.

"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result.

    a and b must be first casted to integers if they are float.

    Args:
        a (int or float): The first number.
        b (int or float): The second number. Default is 98.

    Raises:
        TypeError: If either 'a' or 'b' is not an integer or float.

    Returns:
        int: The sum of 'a' and 'b'.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
