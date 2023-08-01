# tags_equal.py
"""
A script defining a function that accepts two strings of opening HTML tags and returns True if they have the same attributes and values.
"""
from typing import *
import shlex


def parse_tag(html_tag: str) -> tuple[str, dict[str, Optional[str]]]:
    """ Parse `html_tag` by returning an iterable of string starting with its tag name. """
    tag_name, *attr_strings = shlex.split(html_tag[1:-1].casefold())
    return tag_name, dict(parse_attributes(attr_strings))


def parse_attributes(strings: list[str]) -> Iterator:
    """
    Split each string in `strings` into key-value pair if there is a '=' in the string,
    otherwise return with `None` in the place of value.
    """
    return (
        attrib.split('=') if '=' in attrib else [attrib, None]
        for attrib in reversed(strings)
    )


def tags_equal(tag1: str, tag2: str) -> bool:
    """
    Return True if `tag1` and `tag2` have the same attributes with the same values.
    Ignore the order of attribues and case for both attribute names and values.
    """
    return parse_tag(tag1) == parse_tag(tag2)


# base problem, assume that
# - 1. attributes don't have single or double quotes around them
# - 2. attributes don't contain spaces
# - 3. no duplicate attributes in a HTML tag
# - 4. all attributes are key-value pairs
# - 5. no whitespace around key-value pairs (`key=value`, not `key = value`)
assert tags_equal("<img src=cats.jpg height=40>", "<IMG SRC=cats.jpg height=40>")
assert not tags_equal("<img src=dogs.jpg width=99>", "<img src=dogs.jpg width=20>")
assert tags_equal("<p>", "<P>")
assert not tags_equal("<b>", "<p>")

# bonus 1, remove assumption 3 so that if there are duplicates, make sure the first one wins
assert tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_email>")
assert not tags_equal("<LABEL FOR=id_email for=id_username>", "<LABEL FOR=id_username>")

# bonus 2, remove assumption 4
assert tags_equal("<OPTION NAME=hawaii SELECTED>", "<option selected name=hawaii>")
assert not tags_equal("<option name=hawaii>", "<option name=hawaii selected>")

# bonus 3, remove assumptions 1 and 2
assert tags_equal("<input value='hello there'>", '<input value="hello there">')
assert tags_equal("<input value=hello>", "<input value='hello'>")
assert not tags_equal("<input value='hi friend'>", "<input value='hi there'>")