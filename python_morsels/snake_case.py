# snake_case.py
"""
A script defining utilities to help use snake_case with classes
that normally use camelCase.
"""
from itertools import dropwhile
import re
import unittest


def is_snake(string: str) -> bool:
    """
    Return True if `string` can be partitioned by an underscore and all lowercase.
    """
    before, _, after = string.partition('_')
    return before and after and before.islower() and after.islower()


def is_camel(string: str) -> bool:
    """
    Return True if `string` contains a lowercase letter immediately followed
    by an uppercase letter.
    """
    first_uppercase = next(dropwhile(str.islower, string), '')
    return first_uppercase.isupper()


def to_snake(camelCase: str) -> str:
    """Convert camelCase string to snake_case."""
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camelCase).lower()

    
def to_camel(snake_case: str) -> str:
    """Convert snake_case string to camelCase."""
    [first, *rest] = snake_case.split('_')
    capitalized = [r.capitalize() for r in rest]
    return f"{first}{''.join(capitalized)}"


class SnakeCaseMixin:
    for __attr in dir(unittest.TestCase):
        if is_camel(__attr):
            locals()[to_snake(__attr)] = getattr(unittest.TestCase, __attr)


# base problem
assert not is_snake('setup')
assert not is_snake('setUp')
assert is_snake('set_up')
assert not is_snake('__init__')
assert not is_camel('setup')
assert is_camel('setUp')
assert not is_camel('set_up')
assert not is_camel('__init__')
assert to_snake('setUp') == 'set_up'
assert to_snake('assertAlmostEqual') == 'assert_almost_equal'
assert to_camel('set_up') == 'setUp'
assert to_camel('assert_almost_equal') == 'assertAlmostEqual'

# bonus 1, test `SnakeCaseMixin` class
from math import sqrt


def quadratic(a, b, c):
    x1 = -b/(2*a)
    x2 = sqrt(b**2 - 4*a*c)/(2*a)
    return (x1+x2), (x1-x2)


class QuadraticTests(SnakeCaseMixin, unittest.TestCase):

    def test_zero_division(self):
        with self.assert_raises(ZeroDivisionError):
            quadratic(0, 8, 8)

    def test_negative_square_root(self):
        with self.assert_raises(ValueError):
            quadratic(8, 0, 8)

    def test_round_numbers(self):
        self.assert_equal(quadratic(1, 3, 2), (-1, -2))
        self.assert_equal(quadratic(2, 5, 2), (-0.5, -2))
        self.assert_not_equal(quadratic(2, 5, 2), (0.5, 2))
        self.assert_equal(quadratic(2, 5, 0), (0, -2.5))

    def test_assert_almost_equal(self):
        x, y = quadratic(20, 5000, 10000)
        self.assert_almost_equal(x, -2.0162, places=3)
        self.assert_almost_equal(y, -247.9837, places=3),
        self.assert_not_almost_equal(x, -2.02, places=3)
        self.assert_not_almost_equal(y, -247.98, places=3)

unittest.main()
    