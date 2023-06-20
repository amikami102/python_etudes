# ProxyDict.py
"""
A script defining `ProxyDict` class, which works like regular mapping class but is immutable.
"""
from typing import *
from collections import ChainMap
from rich import print


class ProxyDict(Mapping):
    """ A class that makes an immutable dictionary. """
    
    def __init__(self, *mappings):
        self.mapping: ChainMap = ChainMap(*reversed(mappings))
    
    def __getitem__(self, key: str):
        return self.mapping[key]
    
    def __iter__(self) -> Iterator[str]:
        return iter(self.mapping)
    
    def __len__(self) -> int:
        return sum(1 for _ in self)
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}({repr(self.mapping)})'



# base problem
user_data = {'name': 'asako mikami', 'active': False}
proxy_data = ProxyDict(user_data)
assert proxy_data['name'] == 'asako mikami'
assert not proxy_data['active']
assert list(proxy_data.keys()) == ['name', 'active']
assert list(proxy_data.items()) == [('name', 'asako mikami'), ('active', False)]
assert list(proxy_data.values()) == ['asako mikami', False]
assert proxy_data.get('name') == 'asako mikami'
assert proxy_data.get('shoe_size', 0) == 0

proxy_data2 = ProxyDict(user_data.copy())
assert len(proxy_data) == 2
assert proxy_data == proxy_data2
assert proxy_data == user_data
assert list(proxy_data) == ['name', 'active']
print(proxy_data)

# cont. base problem, make sure your `ProxyDict` change whenever the passed-in dictionary changes:
user_data.pop('name')
assert proxy_data == ProxyDict({'active': False})
assert proxy_data2 == ProxyDict({'name': 'asako mikami', 'active': False})
assert proxy_data != proxy_data2

# cont. base problem, test that `ProxyDict` is immutable
try:
    proxy_data['active'] = False
except (TypeError, AttributeError) as e:
    print(e)

try:
    proxy_data.setdefault('active', False)
except (TypeError, AttributeError) as e:
    print(e)

try:
    proxy_data.update({'active': True})
except (TypeError, AttributeError) as e:
    print(e)
    
# bonus 1, accept any number of dictionaries but let the last dictionary win if two dictionaries have the same keys
user_data = {'name': 'asako mikami', 'active': False}
site_data = {'name': 'Python Morsels', 'last_updated': 1995}
proxy_data = ProxyDict(user_data, site_data)
assert proxy_data['name'] == 'Python Morsels'
assert not proxy_data['active']
assert proxy_data['last_updated'] == 1995
del site_data['name']
assert proxy_data['name'] == 'asako mikami'
print(proxy_data.mapping.maps)
