# warningutils.py
"""
A script defining `error_on_warning`, a context manager that raises exceptions instaed of warnings.

(See Python Morsel's official test files for testing.)
"""
from typing import *
import os
import warnings
from contextlib import ContextDecorator


class error_on_warnings(ContextDecorator):
    """
    A context manager that will raise exceptions instead of warnings.
    This implementation wraps around `context.catch_warnings()` to temporarily save the previous settings.
    
    Attributes
    ----
        message: str, default ''
            the regex string of a warning message that, if matched, will be raised as exception;
            the default setting will raise exception for any warning message.
            
        category: Warning, default Warning
            a class of Warning that will be raised as an exception;
            the default setting will raise exception for any warning.
            
        pretext: warnings.catch_warnings
            the warning settings returned by `warnings.catch_warnings()`
            before entering an instance of `error_on_warnings()`;
            this setting will be restored after exiting `error_on_warnings()`.
    """
    
    def __init__(self, message: str = '', category: Warning = Warning) -> None:
        """
        `message` and `category` attributes are passed into `warnings.filterwarning()` upon entering the context.
        """
        self.message = message
        self.category = category
        self.pretext = warnings.catch_warnings()
    
    def __enter__(self) -> None:
        self.pretext.__enter__()
        warnings.filterwarnings('error', self.message, self.category, append=True)
    
    def __exit__(self, exc_value, exc_type, traceback) -> None:
        # You don't really need to define `__exit__` because you're already going to exit `self.pretext` automatically.
        self.pretext.__exit__()


# base problem, test `error_on_warnings`
# bonus 1, allow `error_on_warnings` to be used as function decorator