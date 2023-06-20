# final_class.py
"""
A script defining `Unsubclassable` class, which cannot be inherited.
"""
from typing import final


@final
class Unsubclassable(object):
    """ A class that cannot be subclassed. """
    
    def __repr__(self) -> str:
        return type(self).__name__
    
    def __init_subclass__(cls):
        raise TypeError


# base problem and bonus 1 where `TypeError` is raised the moment it is subclassed
d = Unsubclassable()
d.x = 4
assert d.x == 4


class MyClass(Unsubclassable):
    def __init__(self):
        print('MyClass created')

class B(MyClass):
    pass

try:
    c = MyClass()
except TypeError as e:
    print(e)

try:
    B()
except TypeError as e:
    print(e)


