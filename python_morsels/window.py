# window.py
"""
A script defining `window()` function that takes an iterable and returns an iterable of sliding window of size `n`.
"""
from typing import *
from collections import deque
from itertools import islice


def window(iterable: Iterable, n: int) -> Iterator:
    """ Return a sliding window of size `n` of `iterable. """
    it = iter(iterable)
    slider = deque(islice(it, n), maxlen=n)	# fill in the whole deque
    yield tuple(slider)
    for item in it:
        slider.append(item)
        yield tuple(slider)


# base problem and bonus 1, accept any iterable
numbers = [1, 2, 3, 4, 5, 6]
assert list(window(numbers, 2)) ==\
    [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
assert list(window(numbers, 3)) ==\
    [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
assert list(window(numbers, 4)) ==\
    [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]

# bonus 1, return an iterator
numbers = [1, 2, 3, 4, 5, 6]
assert next(window(numbers, 3)) == (1, 2, 3)
