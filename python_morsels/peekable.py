# peekable.py
"""
A script defining a callable, `peekable`, which returns an iterator
that loops over a given iterable and lets you peek ahead in your iterator.
"""
from typing import *

T = TypeVar('T')
SENTINEL = object()


class peekable:
    """An iterator class that lets you peek ahead to the next item."""
    def __init__(self, iterable: Iterable[T]):
        self.iterator = iter(iterable)
        self.peeked = SENTINEL
    
    def __next__(self) -> T:
        """
        Check that `peeked` attribute has a non-sentinel value.
        If so, return that non-sentinel value and reset `peeked`.
        Otherwise, return the next value of iterator.
        """
        if self.peeked is not SENTINEL:
            value, self.peeked = self.peeked, SENTINEL
            return value
        return next(self.iterator)
    
    def __iter__(self) -> 'peekable':
        return self # Required by definition of iterator
    
    def peek(self, default: T = SENTINEL) -> T:
        """
        Cache the next value of the iterator in `peeked` attribute
        and return the cached value. If the iterator is empty,
        return `default` value as long as it is non-sentinel; otherwise,
        raise StopIteration.
        """
        if self.peeked is SENTINEL:
            # either because no peeking has occurred
            # or the cache has been reset due to recent `next()` call
            self.peeked = next(self.iterator, default)
            if self.peeked is SENTINEL:
                # because the iterator is empty
                raise StopIteration
        return self.peeked
            

# base problem
squares = peekable(n**2 for n in [1, 2, 3, 4])
assert next(squares) == 1
assert squares.peek() == 4
assert squares.peek() == 4
assert list(squares) == [4, 9, 16]
try:
    squares.peek()
except StopIteration:
    print('passed')
else:
    print('failed')

# test `default` argument in `peek()` method
squares = peekable(n**2 for n in [1, 2, 3, 4])
assert next(squares) == 1
assert squares.peek(0) == 4
assert list(squares) == [4, 9, 16]
assert squares.peek(0) == 0

# make sure `peekable` doesn't loop over the given iterable immediately
squares = (n**2 for n in [1, 2, 3])
iterator = peekable(squares)
assert next(squares) == 1
assert iterator.peek() == 4
assert next(iterator) == 4
assert next(squares) == 9

# test `iterable = [None]`
iterator = peekable(iter([None]))
assert iterator.peek() is None
assert list(iterator) == [None]
try:
    iterator.peek()
except StopIteration:
    print('passed')
assert list(iterator) == []
