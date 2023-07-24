# computed_property.py
"""
A script defining a `computed_property` descriptor-decorator,
which accepts an attribute name and caches the value of the property as long as that attribute's value remains the same.
"""
from typing import *
import functools

from rich import print

SENTINEL = object()

class computed_property:

    def __init__(self, watched_attr):
        self.attr_name = watched_attr
        self.watched_attr = '_' + self.attr_name
    
    def __call__(self, func):
        """ Make `computed_proeperty` both a type and a callable that returns a callable."""
        self.func = func
        return self	# so that `@computed_property(...)` will return the value of `computed_property.__call__`
        
    def __get__(self, instance, owner=None):
        if not instance and owner:
            return self
        elif instance.__dict__.get(self.watched_attr, SENTINEL) != getattr(instance, self.attr_name):
            instance.__dict__[self.watched_attr] = getattr(instance, self.attr_name)
            instance.__dict__[self.func] = self.func(instance)
        return instance.__dict__[self.func]
    
    def __set__(self, obj, value):
        raise AttributeError

        

class Circle:
    def __init__(self, radius=1):
        self.radius = radius
        
    @computed_property('radius')
    def diameter(self):
        print('computing diameter')
        return self.radius * 2


# base problem
circle = Circle()
circle.diameter # computing diameter
assert circle.diameter == 2
circle.radius = 3
circle.diameter # computing diameter
assert circle.diameter == 6

try:
    circle.diameter = 4
except AttributeError:
    print('raised error as expected')
else:
    raise Exception('did not raise expected error')


# test two instance of same class
class Thing:
    @computed_property('z')
    def x(self):
        return self.y * self.z

thing1 = Thing()
thing2 = Thing()
thing1.y, thing1.z = 2, 3
thing2.y, thing2.z = 4, 5
assert thing1.x == 6
assert thing2.x == 20
thing1.y = 7
assert thing1.x == 6
