# minmax.py
"""
A script defining `minmax()` function, which accepts a list and returns a tuple of its minimum and maximum values.
"""
from typing import *
from collections import namedtuple

T = TypeVar('T')
MinMax = namedtuple('MinMax', ('min', 'max'))


def minmax(iterable: Iterable[T], *, key: Callable = None) -> MinMax:
    """Return the minimum and maximum of `iterable`."""
    iterable = list(iterable)
    return MinMax(min(iterable, key=key), max(iterable, key=key))


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

# bonus 2, accept any iterable
numbers = {8, 7, 5, 3, 9, 6, 2}
assert minmax(numbers) == (2, 9)
assert minmax(n**2 for n in numbers) == (4, 81)

# bonus 3, return an object that can be unpacked
mm = minmax([3, 2, 5, 4, -1])
assert mm.min == -1
assert mm.max == 5
smallest, largest = mm
assert smallest == -1
assert largest == 5