# is_anagram.py
"""
A script defining `is_anagram()` function that returns `True` if two strings are anagrams of each other.
"""
from typing import *
import re
import unicodedata
from collections import Counter

ALPHA_RE = re.compile('[^a-zA-Z]+')


def expand_accents(my_string: str) -> str:
    """ Return decomposed form of `string`. """
    return unicodedata.normalize('NFKD', my_string)


def clean_string(my_string: str) -> str:
    """ Return casefolded version of `my_string` with punctuation marks, white spaces, and accent components removed. """
    expanded = expand_accents(my_string)
    return ALPHA_RE.sub('', expanded.casefold().replace(' ', ''))


def is_anagram(word1: str, word2: str) -> bool:
    """ Return `True` if `word1` and `word2` are anagrams. """
    return Counter(clean_string(word1)) == Counter(clean_string(word2))


def is_anagram2(word1: str, word2: str) -> bool:
    """ Same as `is_anagram()` but has different implementation. """
    return sorted(clean_string(word1)) == sorted(clean_string(word2))


# base problem, come up with two ways of checking that two strings are anagrams
assert is_anagram("tea", "eat")
assert not is_anagram("tea", "treat")
assert not is_anagram("sinks", "skin")
assert is_anagram("Listen", "silent")

assert is_anagram2("tea", "eat")
assert not is_anagram2("tea", "treat")
assert not is_anagram2("sinks", "skin")
assert is_anagram2("Listen", "silent")

# bonus 1, make sure `is_anagram()` ignores spaces
assert is_anagram("coins kept", "in pockets")
assert is_anagram2("Tom Marvolo Riddle", "I am Lord Voldemort")

# bonus 2, make sure `is_anagram()` ignores punctuations
assert is_anagram("a diet", "I'd eat")
assert is_anagram2("a diet", "I'd eat")

# bonus 3, make sure `is_anagram()` ignores accent marks
assert is_anagram("cardiografía", "radiográfica")