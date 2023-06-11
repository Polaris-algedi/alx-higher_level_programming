#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list.

    Args:
        my_list: list of integers
        idx: index of the element to be deleted

    Returns:
        If idx is negative or out of range, nothing change
        (returns the same list), otherwise the new list.
    """
    if idx in range(len(my_list)):
        del my_list[idx]
    return my_list
