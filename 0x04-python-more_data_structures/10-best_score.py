#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value

    Args:
        a_dictionary: a dictionary

    Returns:
        a key with the biggest integer value
    """
    return max(a_dictionary, key=a_dictionary.get)
