# Month.py
"""
A script defining `Month` class that represents a specific month in a specific year.
"""
from typing import *
from dataclasses import dataclass, field, astuple
import datetime
import calendar


@dataclass(order=True, slots=True, frozen=True)
class Month:
    year: int
    month: int
    
    @property
    def first_day(self):
        return datetime.date(self.year, self.month, 1)
    
    @property
    def last_day(self):
        return datetime.date(
            self.year,
            self.month,
            calendar.monthrange(self.year, self.month)[1]
        )
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.year}, {self.month})'
    
    def __str__(self) -> str:
        return f'{self.year}-{self.month:02d}'
    
    @classmethod
    def from_date(cls, mydate: datetime.date) -> 'Month':
        return Month(mydate.year, mydate.month)
    
    def strftime(self, frmt: str) -> str:
        return self.first_day.strftime(frmt)


# base problem
dec99 = Month(1999, 12)
assert repr(dec99) == 'Month(1999, 12)'
assert str(dec99) == '1999-12'
assert sorted([Month(1998, 12), Month(2000, 1), Month(1999, 12)]) ==\
       [Month(1998, 12), Month(1999, 12), Month(2000, 1)]
assert not Month(1998, 12) == (1998, 12)
try:
    Month(1998, 12) < (1998, 12)
except TypeError:
    print('passed')
else:
    print('failed')
    
# bonus 1, test `first_day` and `last_day` attributes
dec99 = Month(1999, 12)
assert dec99.first_day == datetime.date(1999, 12, 1)
assert dec99.last_day == datetime.date(1999, 12, 31)

# bonus 2, test the factory method for creating `Month` object from `datetime.date` objects and instance method for converting `Month` to a string representation
from datetime import date
nye99 = date(1999, 12, 31)
dec99 = Month.from_date(nye99)
assert dec99 == Month(1999, 12)
assert dec99.strftime('%b %Y') == 'Dec 1999'

# bonus 3, make `Month` immutable, hashable, and memory efficient
dec99 = Month(1999, 12)
try:
    dec99.year = 1998
except AttributeError:
    print('passed')
else:
    print('failed')
assert {Month(1999, 12), dec99, Month(2000, 1)} == {Month(1999, 12), Month(2000, 1)}