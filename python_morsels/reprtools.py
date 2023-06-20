# reprtools.py
"""
A script defining a series of helper utilities for implementing the `__repr__`
method for Python classes.
"""
from typing import *
from operator import attrgetter

from rich import print

T = TypeVar('T')


def format_arguments(*args, **kwargs) -> str:
    """ Return a programmer-readable string representation of positional and keyword arguments. """
    arguments: tuple[str, ...] = *(repr(arg) for arg in args),\
        *(f'{key}={value!r}' for key, value in kwargs.items())
    return ', '.join(arguments)


def make_repr(args: list[str] = None, kwargs: list[str] = None) -> Callable:
    """ Accept `*args` and `**kwargs` attributes and return an appropriate `__repr__` method for the class it's attached to. """
    
    def func(obj: T) -> str:
        arg_attrib = (getattr(obj, arg) for arg in args) if args else ()
        kwarg_attrib = {kwarg: getattr(obj, kwarg) for kwarg in kwargs} if kwargs else {}
        
        class_attr = format_arguments(*arg_attrib, **kwarg_attrib)
        return f'{type(obj).__name__}({class_attr})'
    
    return func


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
            