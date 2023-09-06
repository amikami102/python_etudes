# NextDate.py
"""
A script defining a class, `NextDate`, that will help the date and number of days (from today) until the next given weekday.
"""
from datetime import date, timedelta
from enum import IntEnum
from functools import partial
from dataclasses import dataclass


class Weekday(IntEnum):
    """An enumeration of weekdays starting with Monday."""
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}.{self.name}"


@dataclass
class NextDate:
    """A class representing the next date of the given weekday from today."""
    weekday: Weekday
    after_today: bool = False
    
    def days_until(self) -> int:
        """
        Return the number of days until the next `self.weekday`.
        If `after_today` is True, return the number of days of the next matching `weekday`.
        Otherwise return today if today is `weekday`.
        """
        today = date.today()
        days_until = ((self.weekday - today.weekday()) + 7) % 7
        if self.after_today:
            return 7 if days_until == 0 else days_until
        else:
            return days_until
    
    def date(self) -> date:
        return date.today() + timedelta(days=self.days_until())

    def __repr__(self) -> str:
        return f"{type(self).__name__}({repr(self.weekday)}, after_today={self.after_today})"


def next_date(weekday: Weekday, after_today: bool = False) -> date:
    """Return the next date of `weekday`."""
    return NextDate(weekday, after_today=after_today).date()


def days_until(weekday: Weekday, after_today: bool = False) -> int:
    """Return the number of days until the next `weekday`."""
    return NextDate(weekday, after_today=after_today).days_until()


next_tuesday = partial(next_date, Weekday.TUESDAY)
days_to_tuesday = partial(next_date, Weekday.TUESDAY)