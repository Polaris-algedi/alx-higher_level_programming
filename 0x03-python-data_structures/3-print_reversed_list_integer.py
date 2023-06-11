#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Function that prints all integers of a list,
    in reverse order.

    Args:
        my_list: list of integers
    """
    for number in my_list[::-1]:
        print("{:d}".format(number))
