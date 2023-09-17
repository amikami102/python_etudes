# dict_from_tuple.py
"""
A script defining `dict_from_tuple()` function.
"""
from typing import Iterable

def dict_from_tuple(tuples:Iterable[tuple]) -> dict:
    """
    Create a dictionary whose keys are the first item of each tuple in `tuples`.
    """
    return {
        key: tuple(values)
        for key, *values in tuples
    }


# base problem
assert dict_from_tuple([(1, 2, 3, 4), (5, 6, 7, 8)]) ==\
    {1: (2, 3, 4), 5: (6, 7, 8)}
assert dict_from_tuple([(1, 2, 3), (4, 5, 6), (7, 8, 9)]) ==\
    {1: (2, 3), 4: (5, 6), 7: (8, 9)}