# reverse_words.py
"""
A script defining `reverse_words()` function that will accept a string of words and return a new sentence with the order of the words reversed
"""

def reverse_words(string: str) -> str:
    return ' '.join(reversed(string.split(' ')))


assert reverse_words("words some are these") == 'these are some words'
assert reverse_words("who is this") == 'this is who'