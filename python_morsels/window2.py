# window2.py
"""
A script defining a function, `window()`, which returns an iterator of sliding windows of a given list.

This is a variation of the same function defined in "window.py".
"""
from typing import *
from collections import deque
from itertools import islice, chain, repeat


def window(iterable: Iterable, n: int, *, fillvalue: Any = None) -> Iterator:
    """
    Return an iterable of sliding windows of size `n` over `iterable`.
    If `n` is larger than the size of `iterable`, fill in with `fillvalue`.
    """
    if n == 0:
        return 
    
    it = iter(iterable)
    first_n_items = islice(
        chain(it, repeat(fillvalue)),
        n
    )
    current = deque(first_n_items, maxlen=n)
    yield tuple(current)
    for item in it:
        current.append(item)
        yield tuple(current)


# base problem
numbers = [1, 2, 3, 4, 5, 6]
assert list(window(numbers, 2)) == [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
assert list(window(numbers, 3)) == [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
squares = (n**2 for n in numbers)
assert list(window(squares, 4)) == [(1, 4, 9, 16), (4, 9, 16, 25), (9, 16, 25, 36)]

# bonus 1, return an iterator and accept any long or lazy iterable
numbers = [1, 2, 3, 4, 5, 6]
assert next(window(numbers, 3)) == (1, 2, 3)

# bonus 2, test `n` that is longer than the given iterable
assert list(window([1, 2, 3], 6)) == [(1, 2, 3, None, None, None)]

# bonus 3, test `fillvalue` argument
assert list(window([1, 2, 3], 5, fillvalue=0)) == [(1, 2, 3, 0, 0)]