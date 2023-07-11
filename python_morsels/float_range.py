# float_range.py
"""
A script defining a callable, `float_range`, that acts like the built-in `range` but allows for floating point numbers.
"""
from typing import *
from math import ceil


class float_range:
    """ A class that acts like `range` for float numbers. """
    
    def __init__(self, start: float, stop: float = None, step: float = 1.0):
        if stop is None:
            start, stop = 0, start
        self.start, self.stop, self.step = start, stop, step
    
    def __len__(self) -> int:
        return max(ceil((self.stop - self.start)/self.step), 0)
    
    def __iter__(self) -> Iterator[float]:
        val = self.start
        for _ in range(len(self)):
            yield val
            val += self.step
    
    def __reversed__(self) -> Iterator[float]:
        # calculate the last value first
        val = self.start + (len(self) - 1) * self.step
        for _ in range(len(self)):
            yield val
            val -= self.step
    
    def __eq__(self, other: 'float_range') -> bool:
        if not isinstance(other, (float_range, range)):
            return NotImplemented
        if len(self) == len(other) == 1:
            return list(self) == list(other)
        first_same = next(iter(self)) == next(iter(other))
        last_same = next(reversed(self)) == next(reversed(other))
        return first_same and last_same and self.step == other.step
            

# base problem
assert list(float_range(0.5, 2.5, 0.5)) == [0.5, 1.0, 1.5, 2.0]
assert list(float_range(3.5, 0, -1)) == [3.5, 2.5, 1.5, 0.5]
assert list(float_range(0, 3.0)) == [0, 1, 2]
assert list(float_range(3.0)) == [0, 1, 2]

try:
    float_range(1, 2, 3, 4)
except TypeError:
    print('Passed')
else:
    print('Failed')

# bonus 1, test that `float_range` has length and can be looped over multiple times
assert len(float_range(0.5, 2.5, 0.5)) == 4
r = float_range(0.5, 2.5, 0.5)
assert list(r) == [0.5, 1.0, 1.5, 2.0]
assert list(r) == [0.5, 1.0, 1.5, 2.0]
assert len(float_range(5, 10, 1.5)) == 4
assert len(float_range(10, 5, 1.5)) == 0
assert len(float_range(10, 5, -1.5)) == 4
assert len(float_range(5, 10, -1.5)) == 0

# bonus 2, test that `float_range` is reversible
assert list(reversed(float_range(0.5, 2.5, 0.5))) == [2.0, 1.5, 1.0, 0.5]

# bonus 3, test that `float_range` is comparable to another `float_range` and `range` objects
a = float_range(0.5, 2.5, 0.5)
b = float_range(0.5, 2.5, 0.5)
c = float_range(0.5, 3.0, 0.5)
assert a == b
assert a != c
assert float_range(5) == range(0, 5)
assert float_range(4) != range(5)
assert float_range(4) != 3
assert float_range(1, 4) == float_range(1, 3.8)
assert float_range(1, 2, 5) == float_range(1, 2, 10)