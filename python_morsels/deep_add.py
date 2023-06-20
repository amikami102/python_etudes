# deep_add.py
"""
A script defining `deep_add()` function which will take
a nested list of numbers and add up all the numbers.
"""
from typing import *
from numbers import Number


def deep_add(iterable_or_number: list[list[Number]]) -> int:
    """ Add up the numbers in `iterable_or_number`. """
    if isinstance(iterable_or_number, Number):
        return iterable_or_number
    else:
        return sum(deep_add(sublist) for sublist in iterable_or_number)
    
#     total = 0
#     for sublist in list_of_lists:
#         if isinstance(sublist, Number):
#             total += sublist
#         elif isinstance(sublist, Iterable):
#             total += deep_add(sublist)
#         else:
#             raise TypeError('`list_of_lists` must be a nested list of numbers')
#         
#     return total

# base problem
assert deep_add([1,2,3,4]) == 10
assert deep_add([[1, 2, 3], [4, 5, 6]]) == 21
assert deep_add([[[1, 2], [3, 4]], [[5, 6], [7, 8]]]) == 36

# bonus 1, accept any iterable
assert deep_add([(1, 2), [3, {4, 5}]]) == 15