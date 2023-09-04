# concat_check.py
"""
A program that accepts one or more .py files and prints an error if any of them seem to have implicit string concatenation.

The program will check for single line and multiple line concatenation.

Usage example:
    $ python concat_check.py file1.py file2.py my_regex.py
"""
from typing import *
import sys
import tokenize
from itertools import pairwise

from rich import print

T = TypeVar('T')
MESSAGE = "{file}, line {line_num}: implicit concatenation, {line!r}"


def triplewise(iterable: Iterable[T]) -> Iterator[tuple[T, T, T]]:
    """
    (Taken from `itertools` module recipe)
    Returns a sliding window of three items from `iterable`.
    """
    for (a, _), (b, c) in pairwise(pairwise(iterable)):
        yield a, b, c
        
        
def check_implicit_concat(*tokens) -> bool:
    """ Return True if `tokens` has a pattern of implicit string concatenation. """
    token1, token2, token3 = tokens
    oneline = (
        token1.type == tokenize.STRING and
        token2.type == tokenize.STRING
    )
    multline = (
        token1.type == tokenize.STRING and
        token2.type == tokenize.NL and
        token3.type == tokenize.STRING
    )
    return oneline or multline


def format_message(file: str, token: tokenize.TokenInfo) -> str:
    """ Format `MESSAGE` with the correct line number taken from `token1`. """
    return MESSAGE.format(
        file=file,
        line_num=token.end[0] if '\n' in token.string else token.start[0],
        line=token.line
    )
    

if __name__ == '__main__':
    
    for file in sys.argv[1:]:
        with tokenize.open(file) as f:
            tokens = tokenize.generate_tokens(f.readline)
            for tokens in triplewise(tokens):
                token1, *_ = tokens
                if check_implicit_concat(*tokens):
                     print(format_message(file, token1))
