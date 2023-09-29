#!/usr/bin/python3
"""
This module contains a function to find a peak in a list of unsorted integers.

A peak is defined as an element that is greater than or
equal to its neighbors.
For the first and last elements, we only compare them with
their single neighbor.

The function uses a linear search approach, leading to a time
complexity of O(n).
"""


def find_peak(list_of_integers):
    """
    Find a peak in a list of unsorted integers.

    Parameters:
    list_of_integers (list): The list of integers where to find a peak.

    Returns:
    int: A peak element from the list_of_integers. If the list is empty,
    returns None.
    """

    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]

    for i in range(1, length - 1):
        if (list_of_integers[i] >= list_of_integers[i - 1] and
                list_of_integers[i] >= list_of_integers[i + 1]):
            return list_of_integers[i]

    return max(list_of_integers[0], list_of_integers[-1])
