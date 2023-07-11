#!/usr/bin/python3
"""This module contains a function that read a file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout

    Args:
        filename: The name of the file
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
