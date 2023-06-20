# natural_sort.py
"""
A script defining `natural_sort()` function that sorts strings case-insensitively.
"""
from typing import *

from rich import print


natural_key: Callable = str.casefold

def natural_sort(my_list: list[str], reverse: bool=False, key: Callable=None) -> list[str]:
    """ Return string elements in `my_list` sorted case-insensitvely. """
    return sorted(my_list, key=natural_key if not key else key, reverse=reverse)


# base problem
assert natural_sort(['uncle', 'Yankee', 'India', 'hotel', 'zebra', 'Oscar'])\
    == ['hotel', 'India', 'Oscar', 'uncle', 'Yankee', 'zebra']
assert natural_sort(['Uruguay', 'echo', 'Charlie', 'golf'])\
    == ['Charlie', 'echo', 'golf', 'Uruguay']
assert natural_sort(['Uruguay', 'echo', 'Charlie', 'golf'], reverse=True)\
    == ['Uruguay', 'golf', 'echo', 'Charlie']

# bonus 1
assert natural_sort(['McDonald', 'MCDONALD', 'Mcdonald', 'MacDonald'])\
    == ['MacDonald', 'McDonald', 'MCDONALD', 'Mcdonald']


def reverse_name(name):
    """Key function to sort by last name first."""
    first, last = name.rsplit(' ', 1)
    return natural_key(last + ' ' + first)


names = ['Sarah Clarke', 'Sara Hillard', 'Sarah Chiu']
assert natural_sort(names, key=reverse_name)\
    == ['Sarah Chiu', 'Sarah Clarke', 'Sara Hillard']
assert natural_sort(names) == ['Sara Hillard', 'Sarah Chiu', 'Sarah Clarke']