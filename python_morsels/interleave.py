# interleave.py
"""
A script defining `interleave()` function that accepts two lists and returns a new iterable with each of the given items interwoven.
interleave(s, z) -> s[0], z[0], s[1], z[1], ...
"""
from typing import *


def interleave(iterable1: Iterable, iterable2: Iterable) -> Iterator:
    """ Return a new iterable that has elements of `iterable1` and `iterable2` interwoven. """
    for elem1, elem2 in zip(iterable1, iterable2):
        yield elem1
        yield elem2


# base problem and bonus 1, test that it works with any iterable
assert list(interleave([1, 2, 3, 4], [5, 6, 7, 8])) ==\
       [1, 5, 2, 6, 3, 7, 4, 8]
nums = [1, 2, 3, 4]
assert list(interleave(nums, (n**2 for n in nums))) ==\
       [1, 1, 2, 4, 3, 9, 4, 16]

# bonus 2, test that `iterleave` returns an iterator
assert list(interleave([1, 2, 3, 4], [5, 6, 7, 8])) ==\
       [1, 5, 2, 6, 3, 7, 4, 8]
