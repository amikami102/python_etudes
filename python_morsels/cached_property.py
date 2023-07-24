# cached_property.py
"""
A script re-implementing `functools.cache_property`, which is a descriptor-decorator.
"""
SENTINEL = object()	# in case the value being cached is None


class cached_property:
    """ A decorator that can cache values. """

    def __init__(self, property):
        self.property = property

    def __set__(self, instance, value):
        instance.__dict__[self.property] = value

    def __get__(self, instance, owner=None):
        if not instance:
            return self
        if instance.__dict__.get(self.property, SENTINEL) == SENTINEL:
            instance.__dict__[self.property] = self.property(instance)
        return instance.__dict__[self.property]
    
    def __delete__(self, instance):
        instance.__dict__[self.property] = SENTINEL


# base problem
from collections import namedtuple

BaseCircle = namedtuple('BaseCircle', ['radius'])

class Circle(BaseCircle):
    @cached_property
    def diameter(self): return self.radius * 2

c = Circle(radius=5)
assert c.diameter == 10

c.diameter = 20
assert c.diameter == 20
assert c.radius == 5

# bonus 1, allow the cache to be cleared
from math import sqrt

class RightTriangle:
    def __init__(self, a, b):
        self.a, self.b = a, b
    @cached_property
    def c(self):
        return sqrt(self.a**2 + self.b**2)

t = RightTriangle(3, 4)
assert t.c == 5.0
t.b = 2
assert t.c == 5.0
del t.c
assert t.c == sqrt(3**2 + 2**2)
t.c = 10
t.b = 4
assert t.c == 10
del t.c
assert t.c == 5.0

# bonus 2, access `cached_property` instances from classes
t = RightTriangle(3, 4)
print(RightTriangle.c)
assert RightTriangle.c.__get__(t) == 5.0