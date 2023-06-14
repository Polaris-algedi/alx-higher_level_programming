#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list
    (only once for each integer).

    Args:
        my_list: list of integers
    """
    int_sum = 0
    for i in set(my_list):
        int_sum += i
    return int_sum
