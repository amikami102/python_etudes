# easyjson.py
"""
A script defining a callable `parse` which accepts a JSON string and returns a data structure representing the JSON output.
"""
import json
from collections import UserDict


class ParsedObject(UserDict):
    """ A class for reprsenting a JSON object. """
    
    def __getitem__(self, key):
        return self.data[key]
    
    __getattr__ = __getitem__
    

def parse(json_str: str) -> ParsedObject:
    """ Parse `json_str` and return a Python data structure representing the parsed json object. """
    return json.loads(json_str, object_hook = lambda d: ParsedObject(d))


# base problem
obj = parse('{"pink": false, "purple": true, "red": false}')
assert obj['purple']
assert not obj.pink

obj = parse('{"p": {"pink": false, "purple": true}, "r": {"red": false}}')
assert obj.p.purple
assert not obj.r['red']

# bonus 1, test the pared object's equality, string representation, and convertibility to dictionary
obj = parse('{"pink": false, "purple": true, "red": false}')
assert obj == {'pink': False, 'purple': True, 'red': False}
assert obj == {'pink': False, 'purple': True, 'red': False}
assert {**obj, 'green': True} == {'pink': False, 'purple': True, 'red': False, 'green': True}