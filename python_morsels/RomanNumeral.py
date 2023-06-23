# RomanNumeral.py
"""
A script defining `RomanNumeral` class.
"""
from typing import *

from int_to_roman import int_to_roman, roman_to_int, ROMAN, ARABIC


class RomanNumeral:
    """ A class representing a Roman numeral. """
    
    def __init__(self, roman: str) -> None:
        self.roman: str = roman
    
    def __int__(self) -> int:
        return roman_to_int(self.roman)
        
    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.roman!r})"
    
    def __str__(self) -> str:
        return self.roman
    
    @classmethod
    def from_int(cls, integer: int) -> 'RomanNumeral':
        return RomanNumeral(int_to_roman(integer))
    
    def __add__(self, other) -> 'RomanNumeral':
        if isinstance(other, RomanNumeral):
            return RomanNumeral.from_int(int(self) + int(other))
        elif isinstance(other, int):
            return RomanNumeral.from_int(int(self) + other)
        else:
            return NotImplemented
    
    def __eq__(self, other) -> bool:
        if isinstance(other, RomanNumeral):
            return int(self) == int(other)
        elif isinstance(other, int):
            return int(self) == other
        else:
            return NotImplemented


# base problem
four = RomanNumeral('IV')
assert int(four) == 4

# bonus 1, test string representation and `from_int` method
nine = RomanNumeral('IX')
assert repr(nine) == "RomanNumeral('IX')"
nineteen_ninety_nine = RomanNumeral.from_int(1999)
assert str(nineteen_ninety_nine) == 'MCMXCIX'

# bonus 2, support addition
assert RomanNumeral('XI') + RomanNumeral('II') == RomanNumeral('XIII')
assert RomanNumeral('XI') + RomanNumeral('III') == RomanNumeral('XIV')
assert RomanNumeral('IIII') + 12 == RomanNumeral('XVI')