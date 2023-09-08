# easyclass.py
"""
A script defining `easyclass` decorator that makes a dataclass that is frozen and also iterable.
"""
from typing import *
from dataclasses import dataclass, FrozenInstanceError, fields


def easyclass(cls: Callable=None, /, *, frozen: bool =True, iter: bool =True, index: bool = False, **kwargs) -> Callable:
    """
    Returns a decorator that turns `cls` into a dataclass.
    Unless specified, the output will always be a frozen dataclass that is iterable.
    Can be called with or without arguments.
    """
    def classwrapper(cls):
        
        def __iter__(self):
            return (getattr(self, field.name) for field in fields(self))
        def __getitem__(self, i):
            return getattr(self, fields(self)[i].name)
        
        if iter:
            cls.__iter__ = __iter__
        if index:
            cls.__getitem__ = __getitem__
        decorated_class = dataclass(cls, frozen=frozen, **kwargs)

        return decorated_class
    
    if cls:	# triggered by `@easyclass`
        return classwrapper(cls)
    return classwrapper
        

# base problem
@easyclass
class Vector:
     x: float
     y: float
     z: float
     color: str = "black"
     
v = Vector(1, 2, 3, "purple")
u = Vector(4, 5, 6)
w = Vector(4, 5, 6)
assert v == Vector(x=1, y=2, z=3, color='purple')
assert w == u
try:
    u.x = 10
except FrozenInstanceError:
    print('Passed!')
else:
    print('Failed')
assert tuple(v) == (1, 2, 3, 'purple')

# bonus 1, accept optional arguments
@easyclass(frozen=False, order=True)
class Vector:
    x: float
    y: float
    z: float
    color: str = "black"

v = Vector(1, 2, 3, "purple")
u = Vector(1, 2, 3)
assert v != u
assert v > u
u.color = "purple"
assert v == u
assert not v > u

@easyclass()
class Thing:
    name: str
    color: str = None
duck = Thing("duck")
assert duck.name == "duck"
assert duck.color is None
try:
    duck.color = "purple"
except AttributeError:
    print('passed')
else:
    print('Failed')
assert tuple(duck) == ("duck", None)

# bonus 2,
@easyclass(index=True)
class Vector:
    x: float
    y: float
    z: float
    color: str = "black"

v = Vector(1, 2, 3, "purple")
assert v[0] == 1
assert v[1] == 2
assert v[2] == 3
assert v[3] == 'purple'
