# head.py
"""
A script defining `head()` function that returns the first `n` items
of a given iterable.
"""
from typing import *

def head1(iterable: Iterable, n: int) -> Iterator:
    """Implement `head()` with `itertools.islice()`."""
    from itertools import islice
    if n < 0:
        n = 0
    yield from islice(iterable, n)


def head2(iterable: Iterable, n: int) -> Iterator:
    """Implement `head()` without `itertools.islice()`."""
    if n < 0:
        return None
    it = iter(iterable)
    for _ in range(n):
        try:
            yield next(it)
        except StopIteration:
            return None


# base problem
assert list(head([1, 2, 3, 4, 5], 3)) == [1, 2, 3]
assert list(head('hello', 2)) == ['h', 'e']
assert list(head('hello', 0)) == []
assert list(head(enumerate('hey'), 1)) == [(0, 'h')]

# bonus 1, test that `n` can be longer than the length of the given iterable
assert list(head([1, 2, 3], 5)) == [1, 2, 3]

# bonus 2, test negative `n` values
assert list(head([1, 2, 3], -2)) == []

# bonus 3, test that `head()` returns an iterator
h = head([1, 2, 3, 4], 2)
assert next(h) == 1