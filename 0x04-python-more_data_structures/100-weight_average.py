#!/usr/bin/python3
def weight_average(my_list=[]):
    """Calculate the weighted average of all
    integers tuple (<score>, <weight>)

    Args:
        my_list: a list of tuples

    Returns:
        The weighted average of all integers tuple
    """
    numerator, denumerator, average = 0, 0, 0
    for item in my_list:
        numerator += item[0] * item[1]
        denumerator += item[1]
    if denumerator != 0:
        average = numerator / denumerator
    return average
