#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds 2 tuples
    Description:
        If a tuple is smaller than 2,
        use the value 0 for each missing integer.
        If a tuple is bigger than 2,
        use only the first 2 integers.

    Args:
        tuple_a: first tuple.
        tuple_b: second tuple.

    Returns:
        A tuple with 2 integers:
            The first element should be the addition of the
            first element of each argument.
            The second element should be the addition of the
            second element of each argument.
    """
    if len(tuple_a) >= 2 and len(tuple_b) >= 2:
        a = tuple_a[0] + tuple_b[0]
        b = tuple_a[1] + tuple_b[1]
    else:
        a = ((tuple_a[0] if len(tuple_a) >= 1 else 0)
             + (tuple_b[0] if len(tuple_b) >= 1 else 0))
        b = ((tuple_a[1] if len(tuple_a) >= 2 else 0)
             + (tuple_b[1] if len(tuple_b) >= 2 else 0))
    return (a, b)
