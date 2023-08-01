# minmax.py
"""
A script defining `minmax()` function, which accepts a list and returns a tuple of its minimum and maximum values.
"""
from typing import *

T = TypeVar('T')

def minmax(iterable: Iterable[T], *, key: Callable = None) -> tuple[T, T]:
    """Return the minimum and maximum of `iterable`."""
    return min(iterable, key=key), max(iterable, key=key)


# base problem
assert minmax([0, 1, 2, 3, 4]) == (0, 4)
assert minmax([10, 8, 7, 5.0, 3, 6, 2]) == (2, 10)

try:
    minmax([])
except ValueError:
    print('passed')
else:
    print('failed')

try:
    minmax([1, 'a'])
except TypeError:
    print('passed')
else:
    print('failed')

# bonus 1, test key-word only argument `key`
words = ["hi", "HEY", "Hello"]
assert minmax(words, key=lambda s: s.lower()) == ('Hello', 'hi')
assert minmax(words, key=len) == ('hi', 'Hello')