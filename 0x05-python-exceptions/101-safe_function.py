#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """Executes a function safely

    Args:
        fct: pointer to a function
        args: variadic argument

    Returns:
        The result of the function, otherwise returns
        None if something happens during the function
        and prints in stderr the error precede by Exception:
    """
    try:
        return fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return None
