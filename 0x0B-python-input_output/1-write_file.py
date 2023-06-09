#!/usr/bin/python3
"""Examples to demonstrate how Input/Output works in python"""


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
