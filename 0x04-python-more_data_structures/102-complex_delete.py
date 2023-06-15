#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Deletes keys with a specific value
    in a dictionary

    Args:
        a_dictionary: a dictionary
        value: the value of the keys to delete

    Returns:
        The dictionary
    """
    new_dict = a_dictionary.copy()

    for key in new_dict:
        if a_dictionary[key] == value:
            del a_dictionary[key]

    return a_dictionary
