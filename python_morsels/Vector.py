# Vector.py
"""
A class representing 3-dimensional vector.
"""
from typing import *
from numbers import Number
from dataclasses import dataclass, astuple


@dataclass(slots=True, frozen=True)
class Vector:
    """A class representing a vector in R^3 space."""
    x: Number
    y: Number
    z: Number
    
    def __iter__(self) -> Iterator[Number]:
        yield from astuple(self)
    
    def __eq__(self, other: Iterable|'Vector') -> bool:
        if not isinstance(self, (Iterable, Vector)):
            return NotImplemented
        return all(p == q for p, q in zip(self, other))
    
    def __add__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            return NotImplemented
        x1, y1, z1 = self
        x2, y2, z2 = other 
        return Vector(x1 + x2, y1 + y2, z1 + z2)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        if not isinstance(other, Vector):
            return NotImplemented
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Vector(x1 - x2, y1 - y2, z1 - z2)
    
    def __mul__(self, scalar: Number) -> 'Vector':
        if not isinstance(scalar, Number):
            return NotImplemented
        x, y, z = self
        return Vector(x * scalar, y * scalar, z * scalar)
            
    __rmul__ = __mul__
    
    def __truediv__(self, scalar: Number) -> 'Vector':
        if not isinstance(scalar, Number):
            return NotImplemented
        x, y, z = self
        return Vector(x / scalar, y / scalar, z / scalar)
            

# base problem
v = Vector(1, 2, 3)
x, y, z = v
assert (x, y, z) == (1, 2, 3)
assert v != Vector(1, 2, 4)
assert v == Vector(1, 2, 3)

try:
    v.a = 4
except (AttributeError, TypeError):
    print('passed')
else:
    print('failed')

try:
    v.__dict__
except (AttributeError, TypeError):
    print('passed')
else:
    print('failed')

# bonus 1, make `Vector` support addition and subtraction with other `Vector` objects
assert Vector(1, 2, 3) + Vector(4, 5, 6) == Vector(5, 7, 9)
assert Vector(5, 7, 9) - Vector(3, 1, 2) == Vector(2, 6, 7)

# bonus 2, support multiplication and division by scalars
assert 3 * Vector(1, 2, 3) == Vector(3, 6, 9)
assert Vector(1, 2, 3) * 2 == Vector(2, 4, 6)
assert Vector(1, 2, 3) / 2 == Vector(0.5, 1, 1.5)

# bonus 3, make `Vector` immutable
v = Vector(1, 2, 3)
try:
    v.x = 4
except AttributeError:
    print('passed')
else:
    print('failed')