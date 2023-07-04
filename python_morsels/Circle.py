# Circle.py
"""
A script defining a class that represents a circle.
"""
from typing import *
from dataclasses import dataclass, field
from math import pi


@dataclass
class Circle:
    """ A class representing a circle."""
    radius: float
    _default_radius: float = 1.0
    
    @property
    def radius(self):
        return self._radius # privatized to prevent infinite recursion
    
    @radius.setter
    def radius(self, value: float):
        if isinstance(value, property):
            self._radius = self._default_radius
        elif value > 0:
            self._radius = value
        else:
            raise ValueError('Radius cannot be negative')
    
    @property
    def diameter(self) -> float:
        return self.radius * 2
    
    @property
    def area(self) -> float:
        return (self.radius ** 2) * pi
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.radius})"
    
    @diameter.setter
    def diameter(self, value):
        self.radius = value / 2
    
    @area.setter
    def area(self, value):
        raise AttributeError("can't set attribute")
    

# base problem
c = Circle(5)
assert str(c) == 'Circle(5)'
assert c.radius == 5
assert c.diameter == 5 * 2
assert c.area == pi * (5 ** 2)

c = Circle()
assert c.radius == 1
assert c.diameter == 1 * 2

# bonus 1, test that `diameter` and `area` update with `radius`
c = Circle(2)
c.radius = 1
assert c.diameter == 2
assert c.area == pi
assert str(c) == 'Circle(1)'

# bonus 2, test that when `diameter` is changed that `radius` is changed accordingly
c = Circle(1)
c.diameter = 4
assert c.diameter == 4
assert c.radius == 2.0
try:
    c.area = 45.678
except AttributeError:
    print('passed')
else:
    print('failed')
    
# bonus 3, test that radius (and diameter) cannot be set to negative number
c = Circle(5)
c.radius = 3
try:
    c.radius = -2
except ValueError:
    print('passed')
else:
    print('failed')

try:
    c = Circle (-10)
except ValueError:
    print('passed')
else:
    print('failed')