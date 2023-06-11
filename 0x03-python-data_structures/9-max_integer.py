#!/usr/bin/python3
def max_integer(my_list=[]):
    """Finds the biggest integer of a list.

    Args:
        my_list: list of integers

    Returns:
            None, if the list is empty.
            The biggest integer.
    """
    if len(my_list) == 0:
        return None
    max_i = 0
    for i in my_list:
        if i > max_i:
            max_i = i
    return max_i
