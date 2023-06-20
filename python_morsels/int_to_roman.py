# int_to_roman.py
"""
A script defining functions, `int_to_roman()` and `roman_to_int()`.

The function supports numerals from 1 to 2000.
"""
from rich import print
from collections import OrderedDict


ROMAN: dict[int, str] = OrderedDict(
    {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
)

ARABIC: dict[str, int] = OrderedDict(
    {v: k for k, v in ROMAN.items()}
)


def int_to_roman(num: int) -> str:
    """Convert integer `num` to Roman numerals."""
    roman_str: str = ''
    for arabic, roman in ROMAN.items():
        x, num = divmod(num, arabic)
        roman_str += roman * x
    return roman_str


def roman_to_int(roman: str):
    """Convert Roman numeral string, `roman`, to integer."""
    numbers: list[int] = []
    prev = None
    for letter in reversed(roman):
        n = ARABIC.get(letter, None)
        if not n:
            raise ValueError('Invalid roman numeral')
        
        if prev and n < prev:
            numbers.append(-n)
        else:
            numbers.append(n)
        prev = n
        
    return sum(numbers)


# bonus 1
assert int_to_roman(5) == 'V'
assert int_to_roman(9) == 'IX'
assert int_to_roman(1999) == 'MCMXCIX'
assert int_to_roman(8) == 'VIII'
assert int_to_roman(14) == 'XIV'

# bonus 2
assert roman_to_int('V') == 5
assert roman_to_int('VIII') == 8
assert roman_to_int('IX') == 9
assert roman_to_int('XLIX') == 49