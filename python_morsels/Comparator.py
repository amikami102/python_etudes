# Comparator.py
"""
A script defining `Comparator` class that implements an almost-equal comparison.
"""
from numbers import Number


class Comparator:
    """Object that is equal to a very small range of numbers."""
    
    def __init__(self, number: Number, *, delta: float = 0.000_0001):
        self.delta: float = delta
        self.number: Number = number
        
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.number}, delta={self.delta})'
    
    def __eq__(self, other: 'Comparator') -> bool:
        
        if isinstance(other, Comparator):
            return abs(self.number - other.number) <= max(self.delta, other.delta) 
        elif isinstance(other, Number):
            return abs(self.number - other) <= self.delta
        else:
            return NotImplemented
    
    def __add__(self, other: 'Comparator') -> 'Comparator':
        if isinstance(other, Number):
            return Comparator(self.number + other, delta=self.delta)
        elif isinstance(other, Comparator):
            return Comparator(
                self.number + other.number,
                delta=max(self.delta, other.delta)
            )
        else:
            return NotImplemented
        
    __radd__ = __add__   # reverse addition 
    
    def __sub__(self, other: 'Comparator') -> 'Comparator':
        if isinstance(other, Number):
            return Comparator(self.number - other, delta=self.delta)
        elif isinstance(other, Comparator):
            return Comparator(
                self.number - other.number,
                delta=max(self.delta, other.delta)
            )
        else:
            return NotImplemented
    
    def __rsub__(self, other: 'Comparator') -> 'Comparator':
        if not isinstance(other, Number):
            return NotImplemented
        return Comparator(other - self.number, delta = self.delta)
        

# base problem
n = 0.1 + 0.02
target_number = Comparator(0.12)
assert n == target_number

close_to_five = Comparator(5, delta=0.1)
assert close_to_five == 5.05
assert close_to_five == 4.98
assert close_to_five != 5.2

assert repr(Comparator(5, delta=0.1)) == 'Comparator(5, delta=0.1)'

import math
assert math.sqrt(5) == Comparator(2.236, delta=0.01)
assert math.sqrt(5.1) != Comparator(2.236, delta=0.01)

assert 5.5 == Comparator(6, delta=0.5)
assert Comparator(5, delta=0.01) == Comparator(5.1, delta=0.1)
assert  -5.75 == Comparator(-6, delta=0.25)


# bonus 1
almost_100 = Comparator(100, delta=1)
almost_50 = almost_100 - 50
almost_110 = 10 + almost_100
assert 109 == almost_110
assert 108 != almost_110
assert 7 - Comparator(7, delta=0.1) == 0.05
assert 6 - Comparator(7, delta=0.1) == -1.05

# bonus 2
nearly_five = Comparator(5, delta=0.1)
almost_105 = nearly_five + almost_100
assert repr(almost_105) == 'Comparator(105, delta=1)'

