# EasyDict.py
"""
A script defining `EasyDict` class that is a bare-bones mapping class, even more so than `collections.abc.Mapping`.
"""
from typing import *


class EasyDict:
    """A class that can use key and attribute lookups and assignments interchangeably. """
    
    def __init__(self, mapping: dict = None, **kwargs):
        if mapping:
            self.__dict__.update(mapping)
        self.__dict__.update(**kwargs)
    
    def __getitem__(self, key):
        # return self.__dict__[key]
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        # self.__dict__[key] = value
        setattr(self, key, value)
    
    def __eq__(self, other: 'EasyDict') -> bool:
        if not isinstance(other, EasyDict):
            return NotImplemented
        else:
            return self.__dict__ == other.__dict__
            
    def get(self, key, default=None):
        return getattr(self, key, default)



# base problem
person = EasyDict({'name': "Trey Hunner", 'location': "San Diego"})
assert person['location'] == 'San Diego'
assert person.name == 'Trey Hunner'
assert EasyDict()

# bonus 1, allow key and attribute assignments
person['name'] = 'asako'
assert person.name == 'asako'
person.location = 'Boston'
assert person['location'] == 'Boston'

# bonus 2, test keyword arguments, equality checks, and `get` method
person = EasyDict(name='asako', location='Brookline, MA')
assert person.location == 'Brookline, MA'
assert person == EasyDict(name='asako', location='Brookline, MA')
assert person != EasyDict(name='ayako', location='Brookline, MA')
assert not person.get('profession')
assert person.get('profession', 'unknown') == 'unknown'
assert person.get('name', 'unknown') == 'asako'
