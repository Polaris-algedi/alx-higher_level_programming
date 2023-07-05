#!/usr/bin/python3
"""
This module provides a function that prints a square with the character #.

The function, 'print_square(size)', takes
an integer as argument, 'size', and prints
the square based on it.

"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: size of the square

    Raises:
        TypeError: If 'size' is not an integer
        ValueError: If 'size' is less than 0.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
