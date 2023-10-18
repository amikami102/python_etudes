# EasyDict.py
"""
A script defining `EasyDict` class that supports key and attribute lookup.
"""
from collections import UserDict


class EasyDict(UserDict):
    """A dictionary-like class that supports key and attribute lookup."""
    
    __slots__ = ('data', 'normalize', )
    
    def __init__(self, mapping: dict = None, normalize: bool = False, **kwargs):
        super().__init__()
        self.normalize = normalize
        if mapping:
            self.data.update(mapping)
        self.data.update(**kwargs)
                
    def _normalize(self, key: str) -> str:
        return key.replace(' ', '_') if self.normalize else key
    
    def __setitem__(self, key, value):
        self.data[self._normalize(key)] = value
    
    def __getitem__(self, key):
        return self.data[self._normalize(key)]
    
    def __getattr__(self, attrib):
        try:
            return self.data[attrib]
        except KeyError:
            raise AttributeError

    def __setattr__(self, attrib, value):
        if attrib in self.__slots__:
            return super().__setattr__(attrib, value)
        else:
            self.data[attrib] = value
    
    def get(self, key, default=None):
        # `UserDict.get()` no longer relies on `__getitem__` as of Python 3.12
        return self.data.get(self._normalize(key), default)


# base problem
person = EasyDict({'name': "Sakata Gintoki", 'location': "Edo"})
assert person['location'] == 'Edo'
assert person.name == 'Sakata Gintoki'
EasyDict()

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
assert person.get('profession', 'unemployed') == 'unemployed'
assert person.get('name', 'unknown') == 'asako'

# bonus 3, test `normalize` argument
person = EasyDict(name="Sakata Gintoki", location="Edo", normalize=True)
person['company name'] = "Yorozuya"
assert person.company_name == 'Yorozuya'
assert person['company name'] == 'Yorozuya'