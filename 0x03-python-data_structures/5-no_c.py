#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters c and C from a string

    Args:
        my_string: string

    Returns:
        The new string
    """
    new_str = ""
    for c in my_string:
        if c in 'cC':
            continue
        new_str += c
    return new_str
