# fancy_input.py
"""
A script defining `fancy_input` function that is a fancy extension of the built-in `input` function.
"""
from typing import *
import sys

from rich import print

T = TypeVar('T')

DEFAULT_ERROR = 'Please enter a valid response.'


def fancy_input(question: str, validator: Callable[Any, T], *, error_message: str = DEFAULT_ERROR) -> T:
    """
    Prompt input answering `question` until the input is validated by `validator`.
    If invalid input is given, print out `error_message`.
    """
    while True:
        response = input(question + ' ')
        try:
            return validator(response)
        except (ValueError, TypeError, IndexError, AssertionError):
            print(f'\n{error_message}\n', file=sys.stderr)


# base problem
response = fancy_input("What is your favorite integer?", int)
assert isinstance(response, int)

# bonus 1, allow `error_mesage` keyword argument
def parse_number(string): return int(string.replace(',', ''))

n = fancy_input(
    "What is your favorite number?",
    parse_number,
    error_message="Please enter only digits and commas in your number.",
)
print("Neat!", n, "is a nice number")

# bonus 2, print the error message and the line breaks surrounding it are printed to standard error