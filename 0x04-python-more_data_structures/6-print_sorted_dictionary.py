#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys

    Args:
        a_dictionary: a dictionary
    """
    for key in sorted(a_dictionary):
        print(f"{key}: {a_dictionary[key]}")
