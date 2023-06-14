#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new dictionary with all values multiplied by 2

    Args:
        a_dictionary: a dictionary

    Returns:
        The new dictionary
    """
    return {k: x * 2 for k, x in a_dictionary.items()}
