# call_later.py
"""
A script implementing `call_later` function that will call a given function a later time.

In other words, it's equivalent to `functools.partial`.
"""
from typing import *

from rich import print


def call_later(func: Callable, /, *args, **kwargs) -> Callable:
    """
    Return a new function that when called would
    implement `func` with the provided arguments.
    
    Note that `func` is a positional-only argument.
    """
    def new_func():
        return func(*args, **kwargs)
    new_func.__doc__ = f'Calls {func} with {args} and {kwargs}'
    return new_func


print123 = call_later(print, 1, 2, 3, sep=', ', end='!\n')
print123()
print123()
print(help(print123))

names = []
append_name = call_later(names.append, "Shelby")
append_name()
assert names == ['Shelby']
append_name()
assert names == ['Shelby', 'Shelby']

call_zip = call_later(zip, [1, 2], [3, 4])
assert list(call_zip()) == [(1, 3), (2, 4)]