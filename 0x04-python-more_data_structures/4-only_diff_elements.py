#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a set of all elements present in only one set

    Args:
        set_1: set of elements
        set_2: set of elements

    Return:
        Set of elements in the two sets but not in both.
    """
    return set_1 ^ set_2
