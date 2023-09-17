# mutable_hash.py
"""
A script defining `mutable_hash()` function which returns a hash value for
common mutable (and therefore unhashable) types such as lists, dictionaries,
and sets.
"""
from typing import TypeVar, Any
from collections.abc import Set, Mapping, Sequence
from collections import UserDict

M = TypeVar('Mutable', list, dict, set)


def mutable_hash(mutable: M) -> int:
    """Return an integer hash value for `mutable`."""
    if isinstance(mutable, set):
        return hash(frozenset(mutable))
    if isinstance(mutable, dict):
        return hash(frozenset(mutable.items()))
    if isinstance(mutable, list):
        return hash(tuple(mutable))
    else:
        return hash(mutable)


class HashWrapper:
    """A class that accepts unhashable objects and returns it hashable."""
    __slots__ = ('data',)
    
    def __init__(self, obj: M):
        self.data = obj
    
    def __repr__(self) -> str:
        return repr(self.data)
    
    def __eq__(self, other):
        if isinstance(other, HashWrapper):
            return self.data.__eq__(other.data)
        return self.data.__eq__(other)
        
    def __hash__(self):
        return mutable_hash(self.data)    


class UnsafeDict(UserDict):
    """Dictionary-like class that accepts unhashable objects as keys."""
    @staticmethod
    def _wrap(obj: M):
        """
        Return the hash of an object. If unhashable, wrap it in HashWrapper.
        """
        try:
            hash(obj)
        except TypeError:
            return HashWrapper(obj)
        else:
            return obj
    
    @staticmethod
    def _unwrap(obj: HashWrapper):
        """
        Return `data` attribute if `obj` is HashWrapper, otherwise itself.
        """
        return obj.data if isinstance(obj, HashWrapper) else obj
    
    def __setitem__(self, key: M, value: Any):
        return super().__setitem__(self._wrap(key), value)
    
    def __getitem__(self, key: M):
        return super().__getitem__(self._wrap(key))
    
    def __delitem__(self, key: M):
        return super().__delitem__(self._wrap(key))
    
    def __contains__(self, key: M):
        return super().__contains__(self._wrap(key))
    
    def __iter__(self):
        for key in self.data:
            yield self._unwrap(key)

    
# base problem
print(mutable_hash({'a', 'b'}))
print(mutable_hash([1, 2, 3]))
print(mutable_hash({'a': 'b', 'c': 'd'}))
assert mutable_hash([1, 2, 3]) != mutable_hash([3, 2, 1])
colors = {
    'red': 1,
    'blue': 4,
    'green': 3,
}
colors2 = colors.copy()
assert mutable_hash(colors) == mutable_hash(colors)
assert mutable_hash(colors) == mutable_hash(colors2)
colors2['green'] = 2
assert mutable_hash(colors) != mutable_hash(colors2)
assert mutable_hash({1: 2, 3: 4}) == mutable_hash({3: 4, 1: 2})
assert mutable_hash('hello') == mutable_hash('hello')


# bonus 1, test `HashWrapper` and `UnsafeDict`
assert HashWrapper([1, 2, 3]) == [1, 2, 3]
assert HashWrapper([1, 2, 3]) == HashWrapper([1, 2, 3])
d = UnsafeDict()
d[[1, 2]] = 3
assert [1, 2] in d
assert d[[1, 2]] == 3
assert str(d) == '{[1, 2]: 3}'
assert d.pop([1, 2]) == 3