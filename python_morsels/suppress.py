# suppress.py
"""
A script defining `suppress` context manager that suppresses exceptions of a given type.
"""
from typing import *
from contextlib import ContextDecorator


class suppress(ContextDecorator):
    """ A context manager that suppresses exceptions of a given type. """
    
    def __init__(self, *suppressed):
        self.suppressed = suppressed
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback) -> bool:
        expected: bool = any(
            isinstance(exc_value, suppressed)
            for suppressed in self.suppressed
        )
        if expected:
            self.exception, self.traceback = exc_value, traceback
        else:
            self.exception, self.traceback = None, None
        return expected
    
    def __call__(self, func: Callable):
        """ The class can be used as a function decorator. """
        def decorated(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return decorated
               


# base problem, which is just the built-in `contextlib.suppress` class
with suppress(NameError):
    print("Hi!")
    print("It's nice to meet you,", name)
    print("Goodbye!")
x = 0
with suppress(ValueError):
    x = int('hello')
assert x == 0
try:
    with suppress(TypeError):
        print("Hi!")
        print("It's nice to meet you,", name)
        print("Goodbye!")
except NameError:
    print('passed')
else:
    print('failed')

# bonus 1, accept any number of exceptions to suppress
with suppress(ValueError, TypeError):
    x = int('hello')
with suppress(ValueError, TypeError):
    x = int(None)

# bonus 2, store exception and trackback information on an object that can be accessed using the `with X as Y` syntax
with suppress(ValueError, TypeError) as context:
    x = int('hello')
print(context.exception)
print(context.traceback)

# bonus 3, allow the context manager to be used as a decorator
@suppress(TypeError)
def len_or_none(thing):
    return len(thing)

len_or_none('hello')
len_or_none(64)
len_or_none([2, 4, 8])
len_or_none()
len_or_none([])