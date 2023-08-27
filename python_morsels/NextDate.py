# NextDate.py
"""
A script defining a class, `NextDate`, that will help the date and number of days (from today) until the next given weekday.
"""
from datetime import date
from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class NextDate:
    """ A class representing the next date of the given weekday from today."""



    