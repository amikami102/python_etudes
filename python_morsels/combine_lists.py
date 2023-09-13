# combine_lists.py
"""
A script defining `combine_lists()`, which combines given iterables into one.
"""
from typing import *


def combine_lists(list1: Iterable, list2: Iterable) -> list:
    return [*list1, *list2]


# base problem
first = [1, 2, 3]
second = [4, 5, 6]
assert combine_lists(first, second) == [1, 2, 3, 4, 5, 6]

# bonus 1, test with iterables
letter_tuple = ('a', 'b', 'c')
number_list = [2, 1, 3, 4, 7]
assert combine_lists(letter_tuple, number_list) == ['a', 'b', 'c', 2, 1, 3, 4, 7]