#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x elements of a list and only integers

    Args:
        my_list: list that can contain any type
        (integer, string, etc.)
        x: represents the number of elements to access in my_list
        and x can be bigger than the length of my_list

    Returns:
        The real number of integers printed.
    """
    count = x
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (TypeError, ValueError):
            count -= 1

    print()
    return count
