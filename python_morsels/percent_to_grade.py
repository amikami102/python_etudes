# percent_to_grade.py
"""
A script implementing `percent_to_grade` function that will convert percentages to letter grades.
"""
from rich import print
from typing import *
from decimal import Decimal, ROUND_HALF_UP


def percent_to_grade(percentage: float, *, suffix: bool = False, round: bool = False) -> str:
    """
    Convert to letter grade.
    - If `suffix` option is set to True, add '-' or '+' suffix.
    - If `round` option is set to True, round the percentage to the nearest whole number, with .5 always rounding up.
    """
    if round:
        percentage = Decimal(percentage).to_integral_value(rounding=ROUND_HALF_UP)
    
    if percentage < 60:
        return 'F'
    elif 60 <= percentage < 70:
        return 'D+' if suffix and percentage >= 67 \
            else 'D-' if suffix and percentage < 63 \
            else 'D'
    elif 70 <= percentage < 80:
        return 'C+' if suffix and percentage >= 77 \
            else 'C-' if suffix and percentage < 73 \
            else 'C'
    elif 80 <= percentage < 90:
        return 'B+' if suffix and percentage >= 87 \
            else 'B-' if suffix and percentage < 83 \
            else 'B'
    else:
        return 'A+' if suffix and percentage >= 97 \
            else 'A-' if suffix and percentage < 93 \
            else 'A'


# base problem
print(percent_to_grade(72.5))
print(percent_to_grade(89.6))
print(percent_to_grade(60))
print(percent_to_grade(100))
print(percent_to_grade(2))

# bonus 1
print(percent_to_grade(72.5, suffix=True))
print(percent_to_grade(89.6, suffix=True))
print(percent_to_grade(60, suffix=True))
print(percent_to_grade(100, suffix=True))
print(percent_to_grade(2, suffix=True))

# bonus 2
print(percent_to_grade(69.4, round=True))
print(percent_to_grade(69.6, round=True))
print(percent_to_grade(72.5, suffix=True, round=True))
print(percent_to_grade(89.6, suffix=True, round=True))
