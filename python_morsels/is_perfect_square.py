# is_perfect_square.py
"""
A script defining `is_perfect_square` function that tells whether or not a number is a perfect square.
"""
from typing import *
from decimal import Decimal, getcontext, localcontext
from math import sqrt
import cmath
from numbers import Number

def is_complex_perfect_square(cnumber: Number):
    """ A complex number perfect square has integers for both real and imaginary component of its square root. """
    return not (cmath.sqrt(cnumber).real % 1 or cmath.sqrt(cnumber).imag % 1)


def is_perfect_square(number: Number, *, complex: bool = False) -> bool:
    """
    Returns `True` if `number` is a perfect square,
    `False` otherwise or if `number` is negative.
    Assume that large numbers will not be used with `complex=True` option.
    """
    if not isinstance(number, Number):
        raise TypeError('Not a number')
    
    if complex:
        return is_complex_perfect_square(number)
    elif number < 0:
        return False

    if Decimal(number) > getcontext().Emax:
        with localcontext() as ctx:
            ctx.prec = 50	# for really big numbers
            return not Decimal(number).sqrt() % 1
    else:
        return not sqrt(number) % 1

# base problem
assert is_perfect_square(64)
assert not is_perfect_square(65)
assert is_perfect_square(100)
assert not is_perfect_square(1000)

# bonus 1, return False if `number` is negative
assert not is_perfect_square(-1)
assert not is_perfect_square(-4)

# bonus 2, make sure `is_perfect_square()` works with large numbers
assert is_perfect_square(4624000000000000)
assert not is_perfect_square(4623999999999999)
n = 838382848348234**2
m = 8383828483252752341748234**2
assert is_perfect_square(n)
assert not is_perfect_square(n-1)
assert is_perfect_square(m)
assert not is_perfect_square(m-1)

# bonus 3, test `complex` keyword option
assert is_perfect_square(-4, complex=True)
assert not is_perfect_square(-5, complex=False)
assert is_perfect_square(512j, complex=True)