# get_hypotenuse.py
"""
A script defining `get_hypotenuse()` function that returns the hypotenuse of a right triangle given the other two sides.
"""
from math import sqrt

def get_hypotenuse(side1, side2) -> float:
    return sqrt(side1**2 + side2**2)


assert get_hypotenuse(0, 0) == 0.0
assert get_hypotenuse(3, 4) == 5.0
assert get_hypotenuse(20, 21) == 29.0