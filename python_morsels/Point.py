# Point.py
"""
A class representing a 3-dimensional point.
"""
from typing import *
from numbers import Number
from dataclasses import dataclass, field, astuple


@dataclass
class Point:
    x: float
    y: float
    z: float
    
    def __add__(self, other: 'Point') -> 'Point':
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return NotImplemented
    
    def __sub__(self, other: 'Point') -> 'Point':
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            return NotImplemented
    
    def __mul__(self, scalar: Number) -> 'Point':
        if isinstance(scalar, Number):
            return Point(self.x * scalar, self.y * scalar, self.z * scalar)
        else:
            return NotImplemented
    
    __rmul__ = __mul__
    
    def __iter__(self) -> Iterator[float]:
        yield from astuple(self)


# base problem
p1 = Point(1, 2, 3)
assert str(p1) in ['Point(x=1, y=2, z=3)', 'Point(x=1.0, y=2.0, z=3.0)']
p2 = Point(1, 2, 3)
assert p1 == p2
p2.x = 4
assert p1 != p2
assert str(p2) in ['Point(x=4, y=2, z=3)', 'Point(x=4.0, y=2.0, z=3.0)']

# bonus 1, allow `Point` objects to be added and subtracted from each other
p1 = Point(1, 2, 3)
p2 = Point(4, 5, 6)
assert p1 + p2 == Point(x=5, y=7, z=9)
p3 = p2 - p1
assert p3 == Point(x=3, y=3, z=3)

# bonus 2, allow `Point` objects to be scaled up and down by numerical factors
p1 = Point(1, 2, 3)
p2 = p1 * 2
assert p2 == Point(x=2, y=4, z=6)
p2 = 2 * p1
assert p2 == Point(x=2, y=4, z=6)

# bonus 3, allow `POint` to be unnpacked
p1 = Point(1, 2, 3)
x, y, z = p1
assert (x, y, z) == (1, 2, 3)