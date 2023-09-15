# Vector.py
"""
A script defining `Vector` class.
"""
from typing import *
from dataclasses import dataclass, field, astuple
from numbers import Number


@dataclass(slots=True, frozen=True, repr=True, eq=True)
class Vector:
    """A class representing a 3-dimensional vector."""
    x: int
    y: int
    z: int
    
    def __iter__(self) -> Iterator:
        yield from astuple(self)
    
    def __add__(self, other: 'Vector') -> 'Vector':
        x1, y1, z1 = self
        match other:
            case Vector(x2, y2, z2):
                return Vector(x1 + x2, y1 + y2, z1 + z2)
            case _:
                return NotImplemented
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        x1, y1, z1 = self
        match other:
            case Vector(x2, y2, z2):
                return Vector(x1 - x2, y1 - y2, z1 - z2)
            case _:
                return NotImplemented
    
    def __mul__(self, other: Union[int, 'Vector']) -> 'Vector':
        x1, y1, z1 = self
        match other:
            case Number() as scalar:
                return Vector(x1 * scalar, y1 * scalar, z1 * scalar)
            case Vector(x2, y2, z2):
                return Vector(x1 * x2, y1 * y2, z1 * z2)
            case _:
                return NotImplemented
    
    __rmul__ = __mul__
    

# base problem
v = Vector(1, 2, 3)
x, y, z = v
assert (x, y, z) == (1, 2, 3)
assert v != Vector(1, 2, 4)
assert v == Vector(1, 2, 3)
try:
    v.y = 8
except AttributeError:
    print('passed')

vector_set = {v}
assert Vector(1, 2, 3) in vector_set

try:
    v.__dict__
except AttributeError:
    print('passed')

# bonus 1, test addiction and subtraction between `Vector`'s
assert Vector(1, 2, 3) + Vector(4, 5, 6) == Vector(5, 7, 9)
assert Vector(5, 7, 9) - Vector(3, 1, 2) == Vector(2, 6, 7)

# bonus 2, test multiplication with scalars and between `Vector`'s
assert 3 * Vector(1, 2, 3) == Vector(3, 6, 9)
assert Vector(1, 2, 3) * 2 == Vector(2, 4, 6)
assert Vector(1, 2, 3) * Vector(3, 6, 9) == Vector(x=3, y=12, z=27)

# bonus 3, test pickling and copying
from copy import copy
v = Vector(1, 2, 3)
w = copy(v)
assert w == Vector(x=1, y=2, z=3)
assert w == v
assert w is not v

import pickle
v = Vector(1, 2, 3)
data = pickle.dumps(v)
w = pickle.loads(data)
assert w == Vector(x=1, y=2, z=3)
assert w == v
assert w is not v
