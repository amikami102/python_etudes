# MutableString.py
"""
A script defining `MutableString` class.
"""
from typing import *
from collections import UserString

from rich import print


class MutableString(UserString):
    
    def __init__(self, string: str) -> None:
        super().__init__(string)
    
    def __setitem__(self, key: int, value: str) -> None:
        """ This makes `MutableString` mutable. """
        string_as_list: list[str] = list(self.data)
        string_as_list[key] = value
        self.data: str = ''.join(string_as_list)
    
    def __delitem__(self, key: int) -> None:
        """ This makes `MutableString` mutable. """
        string_as_list: list[str] = list(self.data)
        del string_as_list[key]
        self.data: str = ''.join(string_as_list)


# base problem
greeting = MutableString('Hello world!')
assert greeting == 'Hello world!'
greeting[4] = 'a'
assert greeting == 'Hella world!'

greeting = MutableString('Hello world!')
assert greeting.endswith('!')
assert greeting + MutableString('!') == 'Hello world!!'
assert (greeting + '?').lower() == 'hello world!?'
assert 'lo' in greeting
assert len(greeting) == 12


# bonus 1
greeting[6:-1] = 'there'
print(greeting)
del greeting[5:-1]
assert greeting == 'Hello!'
del greeting[-1]
assert greeting == 'Hello'