# warningutils.py
"""
A script defining `error_on_warning`, a context manager that raises exceptions instaed of warnings.
"""
from typing import *
import warnings


class error_on_warnings:
    
    def __init__(self, message: str=None, category: tuple[Warning]=()) -> None:
        self.message = message
        self.category = category
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_value, exc_type, traceback):
        if isinstance(exc_type, Warning):
            return False

# base problem
with error_on_warnings():
    warnings.warn('generic warning')