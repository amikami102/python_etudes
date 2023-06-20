# to_percent.py
"""
A script holding `to_percent()` function.
"""
from rich import print
from typing import *

def to_percent(ratio: float) -> str:
    return f'{ratio:.1%}'


print(to_percent(0.25))
print(to_percent(1.0))
print(to_percent(1.567))
print(to_percent(0.7248))