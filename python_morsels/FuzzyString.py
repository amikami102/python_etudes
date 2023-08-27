# FuzzyString.py
"""
A script defining `FuzzyString`, a class that acts like a string but compares in a case-insensitive manner.
"""
from typing import *
from functools import total_ordering
import unicodedata



def unicode_normalize(string: str) -> str:
    return unicodedata.normalize('NFKD', string.casefold())

def casefold_equal(string1: str, string2: str) -> bool:
    return unicode_normalize(string1) == unicode_normalize(string2)

def casefold_lt(string1: str, string2: str) -> bool:
    return unicode_normalize(string1) < unicode_normalize(string2)

def casefold_contains(string: str, substring: str) -> bool:
    return unicode_normalize(substring) in unicode_normalize(string)


@total_ordering
class FuzzyString:
    """ A string-like class that is case insensitive."""
    def __init__(self, string: str):
        self.data = string
    
    def __eq__(self, other) -> bool:
        if isinstance(other, FuzzyString):
            return casefold_equal(self.data, other.data)
        elif isinstance(other, str):
            return casefold_equal(self.data, other)
        else:
            return NotImplemented
    
    def __repr__(self) -> str:
        return repr(self.data)
    
    def __str__(self) -> str:
        return self.data
    
    def __lt__(self, other) -> bool:
        if isinstance(other, FuzzyString):
            return casefold_lt(self.data, other.data)
        elif isinstance(other, str):
            return casefold_lt(self.data, other)
        else:
            return NotImplemented
    
    def __add__(self, other) -> 'FuzzyString':
        if isinstance(other, FuzzyString):
            return FuzzyString(self.data + other.data)
        elif isinstance(other, str):
            return FuzzyString(self.data + other)
        else:
            return NotImplemented
    
    def __contains__(self, substring) -> bool:
        if isinstance(substring, FuzzyString):
            return casefold_contains(self.data, substring.data)
        elif isinstance(substring, str):
            return casefold_contains(self.data, substring)
        else:
            return NotImplemented
        

# base problem
title = FuzzyString('vinland saga')
assert title == 'VINLAND SAGA'
assert not title == 'vinlandsaga'
hello = FuzzyString("heLlO")
assert str(hello) == "heLlO"

# bonus 1, implement other comparison operators
octothorpe = FuzzyString('Octothorpe')
assert 'hashtag' < octothorpe
assert not 'what' < octothorpe
assert octothorpe < 'what'
assert not 'hashtag' > octothorpe
tokyo = FuzzyString("tokyo")
toronto = FuzzyString("TORONTO")
assert tokyo < toronto
assert not toronto < tokyo
apple = FuzzyString("Apple")
assert apple >= 'Animal'

# bonus 2, work with string concatenation and `in` operator
o_word = FuzzyString('Octothorpe')
assert 'OCTO' in o_word
new_string = o_word + ' (aka hashtag)'
assert new_string == 'octothorpe (AKA hashtag)'
city_name = FuzzyString("New Delhi")
city_name_part = FuzzyString("w del")
assert city_name_part in city_name

# bonus 3, normalize unicode string
ss = FuzzyString('ss')
assert '\u00df' == ss
e = FuzzyString('\u00e9')
assert '\u0065\u0301' == e
assert '\u0301' in e