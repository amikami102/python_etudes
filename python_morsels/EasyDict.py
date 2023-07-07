# EasyDict.py
"""
A script defining `EasyDict` class that is a bare-bones mapping class, even more so than `collections.abc.Mapping`.
"""
from typing import *


from collections import UserDict

class EasyDict(UserDict):

    def __init__(self, mapping = {}, normalize = False, **kwargs):
        self.normalize = normalize
        super().__init__(mapping, **kwargs)
    
    @property
    def data(self):
        return self.__dict__
    
    @data.setter
    def data(self, data):
        self.__dict__.update(data)
    
    def normalized(self, key):
        return key.replace(' ', '_') if self.normalize else key 
    
    def __getitem__(self, key):
        return self.__dict__[self.normalized(key)]
    
    def __setitem__(self, key, value):
        self.__dict__[self.normalized(key)] = value


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
