#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format()

    Args:
        value: value to be printed, it can be any type
        (integer, string, etc.)

    Returns:
        True if value has been correctly printed
        (it means the value is an integer)
        Otherwise, returns False and prints in stderr
        the error precede by Exception:
    """
    try:
        print("{:d}".format(value))
        return True
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
