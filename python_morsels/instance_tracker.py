# instance_tracker.py
"""
A script defining a class factory, `instance_tracker` , that allows classes to keep track of themselves.
"""
from typing import *


def instance_tracker(attr_name: str = 'instances') -> 'InstanceTracker':
    """
    Return a class that has an attribute that keeps track of instances.
    The name of the attribute can be customized by `attr_name` argument.
    """
    class InstanceTracker:
        def __new__(cls, *args, **kwargs):
            """Relying on `__new__` in case the subclass doesn't use `super().__init__`."""
            obj = super().__new__(cls)	# create new instance using __new__ defined by next MRO class
            getattr(cls, attr_name).append(obj)
            return obj
    setattr(InstanceTracker, attr_name, [])     
    return InstanceTracker


# base problem
class Account(instance_tracker()):
    
    def __init__(self, number):
        self.number = number
        super().__init__()
    def __repr__(self):
        return 'Account({!r})'.format(self.number)

a1 = Account('4056')
a2 = Account('8156')
assert Account.instances == [a1, a2]

# test multiple inheritance
class Animal:
    def __init__(self, name):
        self.name = name
        
class Squirrel(instance_tracker(), Animal):
    def __init__(self, name, nervousness=0.99):
        self.nervousness = nervousness
        super().__init__(name)
        
squirrel1 = Squirrel(name='Mike')
squirrel2 = Squirrel(name='Carol', nervousness=0.5)
assert squirrel1.name == 'Mike'
assert squirrel2.name == 'Carol'
assert list(Squirrel.instances) == [squirrel1, squirrel2]

# bonus 1, test that `instance_tracker` can optional accept attribute name to use for storing instances
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    
class TrackedPerson(instance_tracker('registry'), Person):
    """ Example of inheritance and renaming 'instance' to 'registry'. """
    
    
brett = TrackedPerson("Brett Cannon")
guido = TrackedPerson("Guido van Rossum")
carol = TrackedPerson("Carol Willing")
assert list(TrackedPerson.registry) == [brett, guido, carol]

# bonus 2, make sure `instance_tracker` factory works for subclasses that don't call `super().__init__()`
class Person(instance_tracker()):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "Person({!r})".format(self.name)

tanjiro = Person('Kamado Tanjiro')
nezuko = Person('Kamado Nezuko')
assert list(Person.instances) == [tanjiro, nezuko]