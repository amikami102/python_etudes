# OrderedDict.py
"""
A script defining `OrderedDict` class that works like Python 3.6's (oredered) dictionary.
"""
from typing import *
from collections import UserDict
from collections.abc import KeysView, ValuesView


class OrderedDictKeysView(KeysView):
    """A view of `OrderedDict` keys. """
    
    def __getitem__(self, index: int):
        mapping: OrderedDict = self._mapping
        return mapping._keys[index]
    

class OrderedDictValuesView(ValuesView):
    """ A view of `OrderedDict` values. """
    
    def __getitem__(self, index: int):
        """ Get the value of the key corresponding to `index`."""
        return self._mapping[self._mapping._keys[index]]
    

class OrderedDict(UserDict):
    """ An ordered dictionary with `index` method. """
    
    def __init__(self, data: Iterable = ()):
        self._keys = []
        self.data = {}
        self.update(data)
    
    def __setitem__(self, key, value):
        if key not in self:
            self._keys.append(key)
        super().__setitem__(key, value)
    
    def __delitem__(self, key):
        super().__delitem__(key)
        self._keys.remove(key)
    
    def index(self, key):
        for i, elem in enumerate(self):
            if elem == key:
                return i
        else:
            raise KeyError(f'Key {key} not found')
    
    def keys(self) -> OrderedDictKeysView:
        return OrderedDictKeysView(self)
    
    def values(self) -> OrderedDictValuesView:
        return OrderedDictValuesView(self)


# base problem
colors = OrderedDict([('blue', 0.3), ('purple', 0.2), ('pink', 0.1)])
assert list(colors.items()) == [('blue', 0.3), ('purple', 0.2), ('pink', 0.1)]
assert colors.index('pink') == 2
assert colors.index('blue') == 0
assert len(colors) == 3
colors['green'] = 0.0
assert list(colors.values()) == [0.3, 0.2, 0.1, 0.0]
del colors['purple']
colors['purple'] = 0.1
assert list(colors.keys()) == ['blue', 'pink', 'green', 'purple']

# bonus 1, make `keys()` and `values()` indexable
colors = OrderedDict([('blue', 0.3), ('purple', 0.2), ('pink', 0.1)])
assert colors.keys()[0] == 'blue'
assert colors.values()[-1] == 0.1