# track_instances.py
"""
A script defining class decorator `track_instances` which tracks all instances of the decorated classes.
"""
from typing import *
from weakref import WeakSet


def track_instances(cls):
    """ Decorate `cls` to track instances in `instances` attribute. """
    def __init__(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        cls.instances.add(self)
    original_init = cls.__init__
    cls.instances = WeakSet()
    cls.__init__ = __init__
    return cls


# base problem
@track_instances
class Thing:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return "Thing({})".format(repr(self.name))

thing1 = Thing("Thing 1")
thing2 = Thing("Thing 2")
print(list(Thing.instances))	#[Thing('Thing 2'), Thing('Thing 1')]

# bonus 1, make sure that there is no memory leak
thing1 = Thing("Thing 1")
thing2 = Thing("Thing 2")
thing1 = Thing("Purple thing")
print(list(Thing.instances))	#[Thing('Thing 2'), Thing('Purple thing')]
del thing2
print(list(Thing.instances))	#[Thing('Purple thing')]

# bonus 2, allow `track_instances` to accept optional attribute name
@track_instances('things')
class Thing:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return "Thing({})".format(repr(self.name))
    
thing1, thing2 = Thing("Thing 1"), Thing("Thing 2")
print(list(Thing.things))	#[Thing('Thing 1'), Thing('Thing 2')]