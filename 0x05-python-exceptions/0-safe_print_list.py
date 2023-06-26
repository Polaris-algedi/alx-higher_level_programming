#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list

    Args:
        my_list: list that can contain any type
        (integer, string, etc.)
        x: represents the number of elements to print and
        x can be bigger than the length of my_list

    Returns:
        The real number of elements printed.
    """
    for i in range(0, x):
        try:
            print(my_list[i], end='')
        except IndexError:
            print()
            return i
    print()
    return x
