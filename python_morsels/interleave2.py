# interleave2.py
"""
A script defining `interleave()` function, which at its most extended form replicates `itertools` recipe's `roundrobin()` function.
"""
from typing import *
from itertools import chain, zip_longest

SENTINEL = object()


def interleave(*iterables) -> Iterator:
    """
    Interweave the given `iterables`.
    For example, `interleave(s: Sequence, q: Sequence)` will return `s[0], q[0], s[1], q[1], ....`.
    """
    for items in zip_longest(*iterables, fillvalue=SENTINEL):
        for item in items:
            if item is not SENTINEL:
                yield item

# base problem
assert list(interleave([1, 2, 3, 4], [5, 6, 7, 8])) == [1, 5, 2, 6, 3, 7, 4, 8]
nums = [1, 2, 3, 4]
assert list(interleave(nums, (n**2 for n in nums))) == [1, 1, 2, 4, 3, 9, 4, 16]

# bonus 1, return an iterator
print(interleave([1, 2, 3, 4], [5, 6, 7, 8]))
assert list(interleave([1, 2, 3, 4], [5, 6, 7, 8])) == [1, 5, 2, 6, 3, 7, 4, 8]

# bonus 2, accept any number of arguments
assert list(interleave([1, 2, 3], [4, 5, 6], [7, 8, 9])) ==\
    [1, 4, 7, 2, 5, 8, 3, 6, 9]

# bonus 3, accept arguments of different legnth by skipping the shorter iterables when exhausted
assert list(interleave([1, 2, 3], [4, 5, 6, 7, 8])) == [1, 4, 2, 5, 3, 6, 7, 8]
assert list(interleave([1, 2, 3], [4, 5], [6, 7, 8, 9])) ==\
    [1, 4, 6, 2, 5, 7, 3, 8, 9]