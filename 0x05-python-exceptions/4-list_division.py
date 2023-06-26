#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists.

    Args:
        my_list1: list that can contain any type
        (integer, string, etc.)
        my_list2: list that can contain any type
        (integer, string, etc.)
        list_length: represents the number of elements to create and
        x can be bigger than the length of my_list

    Returns:
        The new list (length = list_length) with all divisions.
    """
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)

    return new_list
