# meetup_date.py
"""
A script defining `meetup_date()`, returns the date of the month of the year that falls on the n-th weekday.
"""
from typing import *
import datetime
from calendar import monthcalendar
from enum import IntEnum


Weekday = IntEnum(
    'Weekday',
    ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'],
    start=0
)


def meetup_date(year: int, month: int, *, nth: int = 4, weekday: Weekday = Weekday.THURSDAY) -> datetime.date:
    """ Return the `nth` `weekday` of `year` and `month`. """
    weeks: list[int] = monthcalendar(year, month)
    first_weekday: int = weeks[0 if nth > 0 else -1][weekday]
    if nth > 0:
        n = nth - 1 if first_weekday else nth
    else:
        n = nth if first_weekday else nth - 1
    return datetime.date(year, month, weeks[n][weekday])


# base problem
assert meetup_date(2012, 3) == datetime.date(2012, 3, 22)
assert meetup_date(2015, 2) == datetime.date(2015, 2, 26)
assert meetup_date(2018, 6) == datetime.date(2018, 6, 28)
assert meetup_date(2020, 1) == datetime.date(2020, 1, 23)

# bonus 1, test optional arguments
assert str(meetup_date(2015, 8, nth=4, weekday=3)) == '2015-08-27'
assert str(meetup_date(2018, 7, nth=4, weekday=2)) == '2018-07-25'
assert str(meetup_date(2012, 2, nth=1, weekday=1)) == '2012-02-07'

# bonus 2, test that `nth` argument can be negative number, in which case the weeks are counted from the end of the month
assert str(meetup_date(2010, 6, nth=-1, weekday=4)) == '2010-06-25'
assert str(meetup_date(2020, 1, nth=-1, weekday=4)) == '2020-01-31'

# bonus 3, test `Weekday` object
assert str(meetup_date(2012, 2, nth=1, weekday=Weekday.TUESDAY)) == '2012-02-07'
assert str(meetup_date(2018, 7, nth=2, weekday=Weekday.WEDNESDAY)) == '2018-07-11'
assert str(meetup_date(2010, 6, nth=-1, weekday=Weekday.FRIDAY)) == '2010-06-25'