# strip_with_regex.py
"""
A script that tries to reimplement the string `strip()` method with regex.

Unlike `str.strip()`, the function `strip_with_regex()` is unable to take care of edge cases involving special characters.
"""
import re

STRIP_PATTERN: str = """
^					# start of string
({0}*)?
(.*?)				# capture any character non-greedily
({0}*)?
$					# end of string
"""


def strip_with_regex(string: str, strip_char: str = '\s') -> str:
    """ Regex match the `strip_char` character at the start and end of `string` and trim them off. """
    pattern = re.compile(
        STRIP_PATTERN.format(strip_char),
        re.VERBOSE|re.DOTALL
    )
    if matched := pattern.match(string):
        return matched.group(2)
    else:
        return string


assert strip_with_regex(' wereworld  ') == ' wereworld  '.strip()
assert strip_with_regex('shelby') == 'shelby'.strip()
assert strip_with_regex('the simpsons') == 'the simpsons'.strip()
multiline = """
    the
    simpsons
    """
assert strip_with_regex(multiline) == multiline.strip()
assert strip_with_regex('barbie', 'b') == 'barbie'.strip('b')
assert strip_with_regex('190sf 0981', '1') == '190sf 0981'.strip('1')
assert strip_with_regex('ABBA', 'AB') == 'ABBA'.strip('AB')
assert strip_with_regex('\\barbie\\', '\\') == '\\barbie\\'.strip('\\')