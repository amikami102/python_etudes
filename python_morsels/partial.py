# partial.py
"""
A script defining `partial` callable that allows for partial evaluation of given functions.
"""
from typing import *
import functools


class SkipType:
    """ A partial argument to be skipped and filled-in later. """
    def __repr__(self):
        return "<partial SKIP argument>"


SKIP = SkipType()


def fill_in_skipped_args(placeholders: tuple, fillers: tuple) -> tuple:
    """ Fill in skpped arguments in `placeholders` with `fillers`. """
    if not fillers:
        return placeholders
    fillers = iter(fillers)
    filled = (
        arg if arg is not SKIP else next(fillers)
        for arg in placeholders
    )
    return (*filled, *fillers)


class partial(functools.partial):
    """ A class that impelments partial evaluation of a given function. """
    
    def __call__(self, *args, **kwargs):
        all_args = fill_in_skipped_args(self.args, args)
        if SKIP in all_args:
            raise TypeError('Not enough positional arguments')
        all_kwargs = {**self.keywords, **kwargs}
        return self.func(*all_args, **all_kwargs)
    
    def partial(self, *args, **kwargs) -> 'partial':
        return partial(self, *args, **kwargs)


# base problem can be solved by `from functools import partial`
print_lines = partial(print, sep='', end='')
print_lines('a\n', 'b\n', 'c\n')
enumerate1 = partial(enumerate, start=1)
assert list(enumerate1(['a', 'b', 'c'])) == [(1, 'a'), (2, 'b'), (3, 'c')]
all_to_strings = partial(map, str)
assert list(all_to_strings([1, 2, 3])) == ['1', '2', '3']

# bonus 1, test that `partial()` can skip positional arguments
has_length = partial(hasattr, SKIP, '__len__')
assert not has_length(4)
assert has_length([])
has_length = partial(hasattr, SKIP, '__len__')
try:
    has_length()
except TypeError:
    print('Passed')
else:
    print('Failed')
template = "{0} {1} {2} and {3}"
skip_last = partial(template.format, 1, 2, SKIP)
try:
    skip_last(3)
except Exception:
    print('Passed')
else:
    print('Failed')
    
# bonus 2, test that `partial()` returns an object with `partial` method
print_a_thing = partial(print, 1)
print_two_things = print_a_thing.partial(2)
print_more_things = print_two_things.partial(3, 4)
print_more_things() #1 2 3 4
print_more_things(sep=', ') #1, 2, 3, 4

# make `partial` cllable work as a decorator
@partial
def multiply(numbers):
    product = 1
    for n in numbers:
        product *= n
    return product

print_more_things_with_comma = print_more_things.partial(sep=', ')
print_more_things_with_comma.partial(sep=' ')() #1 2 3 4