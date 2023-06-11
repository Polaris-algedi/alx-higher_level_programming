#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieves an element from a list like in C

    Args:
        my_list: list of elements
        idx: index

    Returns:
        If idx is negative, the function should return None.
        If idx is out of range (> of number of element in my_list),
        the function should return None.
        Otherwise the element.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
