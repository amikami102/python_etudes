# compact.py
"""
A script defining `compact()`, which accepts a sequence and returns a new iterable with adjacent duplicate values removed.
"""
from typing import *

SENTINEL = object()


def compact(iterable: Iterable) -> Iterator:
    """ Remove adjacent duplicate values in `sequence`. """
    previous = SENTINEL
    for item in iterable:
        if previous != item:
            yield item
            previous = item
            

# base problem
assert list(compact([1, 1, 1])) == [1]
assert list(compact([1, 1, 2, 2, 3, 2])) == [1, 2, 3, 2]
assert list(compact([])) == []
assert list(compact([None, 0, "", []])) == [None, 0, "", []]

# bonus 1, test with any iterable
assert list(compact(n**2 for n in [1, 2, 2])) == [1, 4]

# bonus 2, test that `compac()` returns an iterator
c = compact(n**2 for n in [1, 2, 2])
assert iter(c) is c