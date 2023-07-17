# chunked.py
"""
A script defining `chunked()` function that accepts an iterable and return a list of lists containing lists of size `n`.
"""
from typing import *
from itertools import islice
from collections import deque

T = TypeVar('T')
SENTINEL = object()


def chunked(iterable: Iterable[T], n: int, *, fill: T = SENTINEL) -> list[list[T]]:
    """ Return a list of chunk size `n` of `sequence`. """
    it = iter(iterable)
    while chunk := list(islice(it, n)):
        if fill is not SENTINEL:
            while len(chunk) < n:
                chunk.append(fill)
        yield chunk
    


# base problem
for chunk in chunked([1, 2, 3, 4, 5], n=2):
    print(*chunk)
#1 2
#3 4
#5
assert list(chunked([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2)) \
    == [[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
assert list(chunked([], 3)) == []
assert list(chunked(('a', 'b', 'c', 'd', 'e', 'f'), 3))\
    == [list('abc'), list('def')]

# bonus 1, accept any iterable
assert list(chunked((n**2 for n in range(10)), 4))\
    == [[0, 1, 4, 9], [16, 25, 36, 49], [64, 81]]

# bonus 2, return an iterator
squares = (n**2 for n in range(6))
chunks = chunked(squares, 3)
assert tuple(next(chunks)) == (0, 1, 4)
assert next(squares) == 9

# bonus 3, accept an optional `fill` keyword argument
assert list(chunked(range(10), 4, fill=0))\
    == [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 0]]