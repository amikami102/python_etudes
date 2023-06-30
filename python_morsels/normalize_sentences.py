# normalize_sentences.py
"""
A script defining `normalize_sentences`,
which accepts a string of text and makes sure there are two spaces between senteces. 
"""
import re

SENTENCE_END_RE = re.compile("(\w+[!.?])[ ]+")


def normalize_sentences(text: str) -> str:
    """ Put two and only two spaces between sentences in `string`. """
    return SENTENCE_END_RE.sub(r'\1  ', text)


# base problem
assert normalize_sentences("I am. I was. I will be.") == 'I am.  I was.  I will be.'
assert normalize_sentences("Hello? Yes, this is dog!") == 'Hello?  Yes, this is dog!'

from textwrap import dedent
multiline = dedent("""
    This is a paragraph. With two sentences in it.

    And this is one. With three. Three short sentences.
""").strip()
expected = dedent("""
    This is a paragraph.  With two sentences in it.

    And this is one.  With three.  Three short sentences.
""").strip()
assert normalize_sentences(multiline) == expected
