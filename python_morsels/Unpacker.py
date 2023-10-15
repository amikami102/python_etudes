# Unpacker.py
"""
A script implementing `Unpacker` class.
"""
from typing import *
from collections import UserDict


class Unpacker(UserDict):
    """A dictionary-like class that allows attribute/key unpacking."""
    __slots__ = ('data',)
    
    def __getattr__(self, name):
        try:
            return self.data[name]
        except KeyError:
            raise AttributeError

    def __setattr__(self, name, value):
        if name == 'data':
            return super().__setattr__(name, value)
        else:
            self.data[name] = value

    def __iter__(self):
        yield from self.data.values()
    
    def __repr__(self) -> str:
        attributes = (
            f'{attrib}={value!r}' 
            for attrib, value in self.data.items()
        )
        return f"{type(self).__name__}({', '.join(attributes)})"
    
    def __getitem__(self, keys):
        try:
            return super().__getitem__(keys)
        except KeyError:
            return tuple(self.data[key] for key in keys)
    
    def __setitem__(self, keys: str|tuple[str], values: Iterable) -> None:
        if isinstance(keys, tuple) and len(keys) > 1:
            values = tuple(values)
            for key, value in zip(keys, tuple(values), strict=True):
                self.data[key] = value
        else:
            return super().__setitem__(keys, values)


# base problem
d = {'hello': 4, 'hi': 5}
u = Unpacker(d)
assert u['hello'] == 4
assert u.hi == 5
u['hello'] = 8
assert u.hello == 8

# bonus 1, test that `Unpacker` is unpackable 
coordinates = OrderedDict([('x', 34), ('y', 67)])
point = Unpacker(coordinates)
x, y = point
assert x == 34
assert y == 67

# bonus 2, test string representation
row = Unpacker({'a': 234, 'b': 54})
assert repr(row) == 'Unpacker(a=234, b=54)'

# bonus 3, test multiple attributes
row = Unpacker({'a': 234, 'b': 54})
assert row['a', 'b'] == (234, 54)
row['b', 'a'] = (11, 22)
assert repr(row) == 'Unpacker(a=22, b=11)'
row['b', 'c'] = (n**2 for n in [2, 3])
assert row['c'] == 9