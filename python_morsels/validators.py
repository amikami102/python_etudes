# validators.py
"""
A script defining descriptor classes that can be used to validate values.
"""

class PositiveNumber:
    """ A descriptor class that validates that the value it is assigned to is a positive number. """
    
    def __init__(self, default: float = None) -> None:
        self.default = default
        
    def __set_name__(self, owner, name):
        self.name = '_' + name	# store the name of the descriptor instance
    
    def __get__(self, instance, owner=None):
        if not self.default:
            return getattr(instance, self.name)	# will raise AttributeError if `instance` does not have attribute named `self._name`
        else:
            return getattr(instance, self.name, self.default)	# will return default value instead of raising AttributeError
        
    def __set__(self, instance, value: float):
        """ Only allow positive `value` to be set. """
        if value <= 0:
            raise ValueError('Positive number required')
        else:
            setattr(instance, self.name, value)	# use setattr instead of updating `__dict__` directly


# base problem
class Point:
    x = PositiveNumber(1)
    y = PositiveNumber(1)
    z = PositiveNumber(1)

p = Point()
p.x = 4
assert p.x == 4
try:
    p.x = -3
except ValueError as e:
    print('ValueError raised as expected')
else:
    print('something else happened')
assert (p.x, p.y, p.z) == (4, 1, 1)

# bonus 1, make the initial value optinal and make sure PositiveNumber does not leak memory
class Point:
    x = PositiveNumber()
    y = PositiveNumber()
    z = PositiveNumber()
p = Point()
p.x = 4
assert p.x == 4
try:
    p.y
except AttributeError:
    print('AttributeError raised as expected')
else:
    print('Something else happened')