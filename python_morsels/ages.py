# ages.py
"""
A module of functions related to working with birthdates and ages.

The functions assume a date variable named `CURRENT_DATE`.
"""
from datetime import date, timedelta
import calendar
from fractions import Fraction

CURRENT_DATE: date = date(3000, 2, 28)


def get_recent_birthdate(birthdate: date, year: int) -> date:
    """
    Return `birthdate` on `year`, correcting leap day birthdays to March 1st on non-leap years.
    """
    try:
        return birthdate.replace(year=year)
    except ValueError:
        return birthdate.replace(year=year, month=3, day=1)


def is_over(age: int, birthdate: str) -> bool:
    """
    Return True if the person had their birthdate turning to age `age` already.
    """
    year, *_ = birthdate.split('-')
    
    birthdate_of_age = get_recent_birthdate(
        date.fromisoformat(birthdate),
        int(year) + age
    )
    
    return birthdate_of_age <= CURRENT_DATE


def get_age(birthdate: str, *, exact: bool = False) -> int|Fraction:
    """
    Return the age of the person given their `birthdate`.
    If `exact` is set to `True`, return the exact age in fraction form.
    """
    days_in_year: int = 366 if calendar.isleap(CURRENT_DATE.year) else 365
    
    birthdate: date = date.fromisoformat(birthdate)
    recent_birthdate = get_recent_birthdate(birthdate, CURRENT_DATE.year)
    
    if CURRENT_DATE >= recent_birthdate:	# the person has already had their birthday
        age_years: int = CURRENT_DATE.year - birthdate.year
        age_days: int = (CURRENT_DATE - recent_birthdate).days
    else:	# the person has yet to have her birthday 
        age_years: int = CURRENT_DATE.year - birthdate.year - 1
        age_days: int = days_in_year + (CURRENT_DATE - recent_birthdate).days
    
    return age_years if not exact else age_years + Fraction(age_days, days_in_year)


# base problem
assert not is_over(18, '2982-03-15')
assert is_over(18, '2982-02-15')
assert not is_over(18, '2990-04-15')

CURRENT_DATE: date = date(2000, 2, 1)
assert is_over(18, '1982-02-01')
assert not is_over(18, '1990-12-31')


# bonus 1, test `is_over()` works with leap years
CURRENT_DATE: date = date.fromisoformat('3000-02-28')
assert not is_over(16, '2984-02-29')
assert is_over(16, '2984-02-27')
assert not is_over(16, '2984-03-01')

CURRENT_DATE = date(2018, 3, 16)
assert is_over(41, '1976-02-29')
assert is_over(42, '1976-02-29')
assert not is_over(43, '1976-02-29')

CURRENT_DATE = date(2016, 2, 29)
assert is_over(40, '1976-02-28')
assert is_over(1, '2015-02-28')
assert not is_over(1, '2015-03-01')
assert is_over(201, '1815-02-28')
assert not is_over(201, '1815-03-01')
assert is_over(1001, '1015-02-28')
assert not is_over(1002, '1015-02-28')

# bonus 2, test `get_age()` function
CURRENT_DATE: date = date(3000, 2, 28)
assert get_age('2984-02-29') == 15
assert get_age('2984-02-27') == 16
assert get_age('2980-02-28') == 20
assert get_age('2980-08-28') == 19

# bonus3, test `get_age(..., exact=True)`
assert get_age('2984-02-29', exact=True) == Fraction(5839, 365)
assert get_age('2984-02-28', exact=True) == Fraction(16, 1)

CURRENT_DATE = date(2018, 3, 17)
assert get_age('1979-12-25', exact=True) == 38 + Fraction('82/365')
            
CURRENT_DATE = date(2016, 3, 17)
assert get_age('1979-12-25', exact=True) == 36 + Fraction('83/366')