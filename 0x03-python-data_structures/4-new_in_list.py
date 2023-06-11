#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element of a list at
    a specific position without modifying
    the original list like in C

    Args:
        my_list: list of elements
        idx: index of the element to be replaced
        element: new value

    Returns:
        If idx is negative or out of range
        (> of number of element in my_list),
        the function should not modify anything,
        and returns the original list.
        Otherwise the new list.
    """
    new_list = my_list[:]
    if idx in range(len(my_list)):
        new_list[idx] = element
    return new_list
