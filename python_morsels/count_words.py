# count_words.py
"""
A script defining `count_words()`, which accepts a string and returns a mapping that maps words to the number of times each word was seen in the string.
"""
from collections import Counter
import re


def count_words(string: str) -> dict[str, int]:
    """ Return a dictionary of word count in `string`. """
    return Counter(re.findall(r"\b[\w'-]+\b", string.casefold()))


# base problem
assert count_words("oh what a day what a lovely day") == {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
assert count_words("don't stop believing") == {"don't": 1, 'stop': 1, 'believing': 1}

# bonus 1, make the word count case insensitive
assert count_words("The Queen will address the House of Commons today") ==\
       {'the': 2, 'queen': 1, 'will': 1, 'address': 1, 'house': 1, 'of': 1, 'commons': 1, 'today': 1}

# bonus 2, test that `count_words()` ignores punctuation marks
assert count_words("Oh what a day, what a lovely day!") == {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}