#!/usr/bin/python3
"""Examples to demonstrate how Input/Output works in python"""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file.

    Args:
        filename (str): The name of the file.
        text (str): The text to write.
    Returns:
        The number of characters written.
    """
    with open(filename, "a") as f:
        return f.write(text)
