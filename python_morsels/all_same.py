# all_same.py
"""
A script defining `all_same()` function that accepts a sequence and returns True if all the items are the same.
"""
from typing import *


def all_same(iterable: Iterable) -> bool:
    """ Return True if all the items in `iterable` are the same. """
    it = iter(iterable)
    first = next(it, None)
    return not any(first != e for e in it)


# base problem, assume all values are hashable
assert all_same([1, 1, 1])
assert not all_same([1, 0, 1])
assert all_same([(1, 'a'), (1, 'a')])
assert not all_same([(1, 'a'), (1, 'b')])

# bonus 1, accept iterables with non-hashable items
assert all_same([[1, 'a'], [1, 'a']])
assert not all_same([[1, 'a'], [1, 'b']])

# bonus 2, allow function to accept non-sequence iterables
numbers = [1, 4, 7, 10]
assert not all_same(n % 2 for n in numbers)
assert all_same(n % 3 for n in numbers)

# bonus 3, make `all_same()` return False as soon as possible
cubes = (n**3 for n in range(100))
assert not all_same(cubes)
assert next(cubes) == 8  # only 0 and 1 should be consumed