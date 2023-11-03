# RandomNumber.py
from random import randrange


class RandomNumber:
    """Generate new random number every time attribute is accessed."""
    
    def __init__(self, *args, cache: bool = False
            ):
        self.args = args
        self.cache = cache
    
    def __set_name__(self, instance, name):
        self.name = name
    
    def __get__(self, obj, objtype=None):
        attributes = obj.__dict__
        if self.cache and self.name in attributes:
            return attributes[self.name]
        number = randrange(*self.args)
        if self.cache:
            attributes[self.name] = number
        return randrange(*self.args)
    
    #def __set__(self, obj, value):
        #raise AttributeError(f'Cannot set attribute {self.name!r}')


class RandomNumber:
    def __init__(self, *args, cache=False):
        self.args = args
        self.cache = cache
    def __get__(self, instance, cls=None):
        number = randrange(*self.args)
        if self.cache:
            setattr(instance, self.name, number)
        return number
    def __set_name__(self, instance, name):
        self.name = name

# base problem
class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

p = MagicPoint()
print(p.x, p.y, p.z)
print(p.x, p.y, p.z)
print(p.x, p.y, p.z)

# bonus 1, test `cache` argument
class MagicPoint:
    x = RandomNumber(5, cache=True)
    y = RandomNumber(5, cache=True)
    z = RandomNumber(5)

p = MagicPoint()
p_x, p_y = p.x, p.y
assert p.x == p_x and p.y == p_y
print(p.x, p.y, p.z)
print(p.x, p.y, p.z)

q = MagicPoint()
print(q.x, q.y, q.z)
print(q.x, q.y, q.z)

# bonus 2, test that attributes cannot be assigned to be overwritten
class MagicPoint:
    x = RandomNumber(5, cache=True)
    y = RandomNumber(5, cache=True)
    z = RandomNumber(5, cache=True)

p = MagicPoint()
print(p.x)
try:
    p.x = 10
except AttributeError:
    print('passed')
else:
    print(p.x)
    print('failed')
