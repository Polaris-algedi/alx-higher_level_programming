#!/usr/bin/python3
"""This module contains a function that read a file"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to write.
    Returns:
        The number of characters written.
    """
    with open(filename, "w") as f:
        return f.write(text)
