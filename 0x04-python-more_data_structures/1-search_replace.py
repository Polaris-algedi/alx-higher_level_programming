#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by
    another in a new list

    Args:
        my_list: list of integers
        search: the element to replace in the list
        replace: the new element
    """
    return [x if x != search else replace for x in my_list]
