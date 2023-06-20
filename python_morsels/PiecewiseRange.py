# PiecewiseRange.py
"""
A script defining `PiecewiseRange` class which accepts a range of integers
as a string and returns a lazy iterable of integers.
"""
from typing import *

from rich import print


class PiecewiseRange:
    
    def __init__(self, range_str: str) -> None:
        self.range_str: str = range_str
        
    def __iter__(self) -> Iterator[int]:
        """ Parse the string and return the expanded ranges. """
        for x in self.range_str.split(','):
            try:
                yield int(x.strip())
            except ValueError:
                lower, upper = x.split('-')
                yield from range(int(lower), int(upper) + 1)
    
    def __len__(self) -> int:
        """ Return the number of integers in the lazy iterable. """
        return len(list(iter(self)))


# base problem
r = PiecewiseRange('1-2, 4, 8-10, 11')
assert list(r) == [1, 2, 4, 8, 9, 10, 11]
assert list(PiecewiseRange('1-3,4-6,8-10')) == [1, 2, 3, 4, 5, 6, 8, 9, 10]

# bonus 1
assert len(r) == 7
try:
    next(r)
except TypeError as e:
    print(f'{type(e).__name__} raised')