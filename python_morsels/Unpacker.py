# Unpacker.py
"""
A script implementing `Unpacker` class.
"""
from rich import print
from typing import *
from collections import OrderedDict


class Unpacker:
    
    def __init__(self, attributes: dict = None):
        if not attributes:
            attributes = {}
        for attrib, value in attributes.items():
            setattr(self, attrib, value)
    
    def __getitem__(self, key):
        return getattr(self, key)
    
    def __setitem__(self, key, value):
        setattr(self, key, value)
        
    def __iter__(self) -> Iterator:
        yield from self.__dict__.values()


d = {'hello': 4, 'hi': 5}
u = Unpacker(d)
print(u['hello'])
print(u.hi)
u['hello'] = 8
print(u.hello)

coordinates = OrderedDict([('x', 34), ('y', 67)])
point = Unpacker(coordinates)
x, y = point
print(x, y)