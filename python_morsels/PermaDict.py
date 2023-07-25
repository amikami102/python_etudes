# PermaDict.py
"""
A script defining `PermaDict` class, which acts like a dictionary but disallows updating.
"""
from typing import *
from collections import UserDict


class PermaDict(UserDict):
    """ A dictionary-like class that disallows updating. """
    
    def __init__(self, mapping: dict = None, *, silent: bool = False, **kwargs):
        self.data = {}
        if mapping:
            self.data.update(mapping)
        if kwargs:
            self.data.update(kwargs)
        self.silent = silent
    
    def __setitem__(self, key, value):
        if key in self.data:
            if not self.silent:
                raise KeyError(f'{key} already exists and cannot be updated')
        else:
            self.data[key] = value
    
    def force_set(self, key, value):
        """ Allow `key` to be reassigned to `value` without error. """
        self.data[key] = value
    
    def update(self, mapping: Iterable = (), *, force: bool = False, **kwargs):
        """ Dictionary `update` method but can bypass forbidden updates when `force` is True. """
        if force:
            for key, val in mapping:
                self.force_set(key, val)
            for key, val in kwargs.items():
                self.force_set(key, val)
        else:
            if mapping:
                super().update(mapping)
            if kwargs:
                super().update(kwargs)


# base problem
locations = PermaDict({'Trey': "San Diego", 'Al': "San Francisco"})
locations['Harry'] = "London"
locations.update({'Russell': "Perth", 'Katie': "Sydney"})
assert locations['Trey'] == 'San Diego'

locations = PermaDict([('Kojo', "Houston"), ('Tracy', "Toronto")])
assert list(locations) == ['Kojo', 'Tracy']
assert list(locations.keys()) == ['Kojo', 'Tracy']
assert list(locations.values()) == ['Houston', 'Toronto']
assert list(locations.items()) == [('Kojo', 'Houston'), ('Tracy', 'Toronto')]

from contextlib import suppress
locations = PermaDict({'David': 'Boston'})
with suppress(KeyError):
    locations['David'] = 'America'
locations['Asheesh'] = 'Boston'
with suppress(KeyError):
    locations.update({'Asheesh': 'Cambridge'})
assert locations == {'David': 'Boston', 'Asheesh': 'Boston'}

d = PermaDict()
d[4] = "the number four"
with suppress(KeyError):
    d[4] = "the number 4"
assert d[4] == 'the number four'

# bonus 1, test `PermaDict.force_set()` method
locations = PermaDict({'David': "Boston"})
locations.force_set('David', "Amsterdam")
locations.force_set('Asheesh', "Boston")
locations.force_set('Asheesh', "San Francisco")
assert locations == {'David': 'Amsterdam', 'Asheesh': 'San Francisco'}

# bonus 2, test `silent` keyword argument
locations = PermaDict({'David': "Boston"}, silent=True)
locations['David'] = "Amsterdam"
locations['Asheesh'] = "Boston"
assert locations == {'David': 'Boston', 'Asheesh': 'Boston'}

e = PermaDict(silent=True, not_silent=False, super_silent=True)
assert e == {'not_silent': False, 'super_silent': True}

# bonus 3, test `force` keyword argument on `PermaDict.update()` method
locations = PermaDict({'David': "Boston"})
locations.update([('David', 'Amsterdam'), ('Asheesh', 'SF')], force=True)
assert locations == {'David': 'Amsterdam', 'Asheesh': 'SF'}
e = PermaDict()
e.update(a=1, b=2, force=True)
assert e == {'a': 1, 'b': 2}