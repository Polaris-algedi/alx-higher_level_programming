#!/usr/bin/python3
"""Examples to demonstrate how Input/Output works in python"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

    Args:
        filename: The name of the file
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
