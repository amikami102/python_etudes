# at.py
"""A decorator class that chains multiple decorators."""
from typing import Callable


def at(*decorators):
    """(Base problem solution)"""
    def new_decorator(func: Callable):
        for decorator in decorators:
            func = decorator(func)
        return func
    return new_decorator


class at:
    """A decorator class that chains decorators."""
    def __init__(self, *decorators):
        self.decorators = decorators

    def __call__(self, func: Callable):
        for decorator in self.decorators:
            func = decorator(func)
        return func
    
    def __matmul__(self, decorator: Callable) -> 'at':
        if isinstance(decorator, Callable):
            return at(*self.decorators, decorator)
        else:
            return NotImplemented


# base problem
from contextlib import ContextDecorator, suppress
from json import dumps

def jsonify(func):
    def wrapper(*args, **kwargs): return dumps(func(*args, **kwargs))
    return wrapper

class Suppress(suppress, ContextDecorator):
    pass

@at(Suppress(TypeError), jsonify)
def multiply(x, y):
    return x * y

assert multiply(3, 4) == '12'
assert multiply(3, "4") == '"444"'
assert multiply("3", "4") == 'null'

# bonus 1, test @ operator works
json_no_exceptions = at(Suppress(TypeError)) @ jsonify
assert json_no_exceptions(multiply)(3, 4) == '"12"'