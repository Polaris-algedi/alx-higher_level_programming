#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in a list.

    Args:
        my_list: list of integers

    Returns:
            A new list with True or False, depending on whether
            the integer at the same position in the original
            list is a multiple of 2.
    """
    new_list = []
    for i in my_list:
        new_list.append(i % 2 == 0)
    return new_list
