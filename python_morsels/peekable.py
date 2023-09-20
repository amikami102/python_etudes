# peekable.py
"""
A script defining a callable, `peekable`, that lets you peek ahead in your iterator.
"""
from typing import *

T = TypeVar('T')
SENTINEL = object()


class peekable:
    """An iterator class that lets you peek ahead to the next item."""
    def __init__(self, iterable: Iterable[T]):
        self._iterable = iter(iterable)
        self.peeked = SENTINEL
    
    def __next__(self) -> T:
        if self.peeked is not SENTINEL:
            value, self.peeked = self.peeked, SENTINEL
            return value
        return next(self._iterable)
    
    def __iter__(self) -> 'peekable':
        return self # Required by definition of iterator
    
    def peek(self, default: T = SENTINEL) -> T:
        """Cache the next value in `_iterable` and return it."""
        if self.peeked is not SENTINEL:
            return self.peeked
        try:
            self.peeked = next(self._iterable)
            return self.peeked
        except StopIteration:
            if default is not SENTINEL:
                self.peeked = default
                return self.peeked
            else:
                raise
            

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
