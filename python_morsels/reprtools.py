# reprtools.py
"""
A script defining a series of helper utilities for implementing the `__repr__`
method for Python classes.
"""
from typing import *
from operator import attrgetter

T = TypeVar('T')


def format_arguments(*args, **kwargs) -> str:
    """
    Return a programmer-readable string representation
    of `*args` and `**kwargs`.
    """
    arg_strings  = (repr(arg) for arg in args)
    kwarg_strings = (f'{key}={value!r}' for key, value in kwargs.items())
    return ', '.join([*arg_strings, *kwarg_strings])


def make_repr(*, args: list[str] = (), kwargs: list[str] = ()) -> Callable:
    """
    Return a `__repr__` method that formats attributes named in `args`
    and `kwargs` with `format_arguments()`.
    """
    def repr_method(self: T) -> str:
        """A ` __repr__` method."""
        arg_attrib = (getattr(self, arg) for arg in args)
        kwarg_attrib = {kwarg: getattr(self, kwarg) for kwarg in kwargs}
        return f'{type(self).__name__}({format_arguments(*arg_attrib, **kwarg_attrib)})'
    
    return repr_method


def auto_repr(*, args: list[str] = (), kwargs: list[str] = ()) -> Callable:
    """Return a decorator that adds `__repr__` method to the class passed into it."""
    def decorator(cls):
        cls.__repr__ = make_repr(args=args, kwargs=kwargs)
        return cls
    return decorator


# base problem, test `format_arguments()`
assert format_arguments(1, 2, 3) == '1, 2, 3'
assert format_arguments("expenses.csv", mode="wt", encoding="utf-8")\
    == "'expenses.csv', mode='wt', encoding='utf-8'"

# bonus 1, test `make_repr()`
class Point:
    def __init__(self, x: int, y: int, color: str = 'purple') -> None:
        self.x, self.y = x, y
        self.color = color
    
    __repr__ = make_repr(args=['x', 'y'], kwargs=['color'])

class Empty:
    __repr__ = make_repr()

assert repr(Point(1, 2)) == "Point(1, 2, color='purple')"
assert repr(Point(x=3, y=4, color='green')) == "Point(3, 4, color='green')"
assert str(Empty()) == "Empty()"
assert repr(Empty()) == "Empty()"

# bonus 2, test `@auto_repr()` decorator
@auto_repr(args=['x', 'y'], kwargs=['color'])
class Point:
    def __init__(self, x, y, color='purple'):
        self.x, self.y = x, y
        self.color = color

assert repr(Point(1, 2)) == "Point(1, 2, color='purple')"
assert repr(Point(x=3, y=4, color='green')) == "Point(3, 4, color='green')"