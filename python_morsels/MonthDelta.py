# MonthDelta.py
"""
A script defining `Month` and `MonthDelta` class objects.
"""
from typing import *
from dataclasses import dataclass

from rich import print


M = TypeVar('Monthtype', 'Month', 'MonthDelta')

@dataclass
class Month:
    """ `Month` class has `year` and `month` attributes. """
    year: int
    month: int
    
    def __eq__(self, other: 'Month') -> bool:
        if not isinstance(other, Month):
            return NotImplemented
        else:
            return (self.year, self.month) == (other.year, other.month)
    
        
    def __sub__(self, other: M) -> M:
        """
        Month - Month = MonthDelta
        Month - MonthDelta = Month
        """
        if isinstance(other, Month):
            return MonthDelta((self.year - other.year) * 12 + (self.month - other.month))
        elif isinstance(other, MonthDelta):
            yr, m = divmod(self.month - other.months, 12)
            if not m:
                yr, m = yr - 1, 12
            return Month(self.year + yr, m)
        else:
            return NotImplemented


@dataclass
class MonthDelta:
    """ `MonthDelta` class has `months` attribute. """
    months: int
    
    def __eq__(self, other: 'MonthDelta') -> bool:
        if not isinstance(other, MonthDelta):
            return NotImplemented
        else:
            return self.months == other.months
    
    def __add__(self, other: M) -> M:
        """
        MonthDelta + MonthDelta = MonthDelta
        MonthDelta + Month = Month
        """
        if isinstance(other, Month):
            yr, m = divmod(self.months + other.month, 12)
            return Month(other.year + yr, 1 if not m else m)
        
        elif isinstance(other, MonthDelta):
            return MonthDelta(self.months + other.months)
        
        else:
            return NotImplemented
    
    __radd__ = __add__

    
    def __sub__(self, other: M) -> M:
        """
        MonthDelta - MonthDelta = MonthDelta
        MonthDelta - Month = undefined
        """
        if not isinstance(other, MonthDelta):
            return NotImplemented
        else:
            return MonthDelta(self.months - other.months)
            
                
# base problem
m = Month(1999, 12)
assert (m.year, m.month) == (1999, 12)
assert m == Month(1999, 12)

d = MonthDelta(5)
assert d.months == 5
assert d == MonthDelta(5)

assert Month(1999, 12) + MonthDelta(5) == Month(2000, 5)
assert Month(1999, 12) - MonthDelta(5) == Month(1999, 7)
assert Month(2020, 1) - Month(1999, 12) == MonthDelta(241)

e = Month(2020, 1)
assert MonthDelta(13) + e == Month(2021, 2)
assert e - MonthDelta(13) == Month(2018, 12)

l = e - Month(2000, 10)
assert l == MonthDelta(20*12 - 9)

# bonus 1, support MonthDelta addition and subtraction with each other
assert MonthDelta(4) + MonthDelta(2) == MonthDelta(6)
assert MonthDelta(4) - MonthDelta(2) == MonthDelta(2)