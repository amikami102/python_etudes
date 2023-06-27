# check_helper.py
"""
A program that helps write money amount for checks in the U.S. by accepting the amount of money.
The program prints out  two lines:
    - the value in dollars formatted with commas and two digits after the decimal point;
    - the number spelled out in words if less than a million.
    
Usage example:
    $ python check_helper.py 1876.5
    $1,876.50
    one thousand eight hundred seventy six and 50/100
    
    $ python check_helper.py 76.6
    $76.60
    seventy six and 60/100
    
    $ python check_helper.py 17
    $17.00
    seventeen only
"""
from typing import *
import argparse

NUMBERS = {
    1000: 'thousand',
    100: 'hundred',
    90: 'ninety',
    80: 'eighty',
    70: 'seventy',
    60: 'sixty',
    50: 'fifty',
    40: 'forty',
    30: 'thirty',
    20: 'twenty',
    19: 'nineteen',
    18: 'eighteen',
    17: 'seventeen',
    16: 'sixteen',
    15: 'fifteen',
    14: 'fourteen',
    13: 'thirteen',
    12: 'twelve',
    11: 'eleven',
    10: 'ten',
    9: 'nine',
    8: 'eight',
    7: 'seven',
    6: 'six',
    5: 'five',
    4: 'four',
    3: 'three',
    2: 'two',
    1: 'one',
}


def print_amout(number: float) -> None:
    print(f'${number:,.2f}')


def spell_out(number: float) -> None:
    """ Spell out `whole_number` in words. """
    whole_number, N = int(number), int(round(number % 1, 2) * 100)
    cents = 'only' if not N else f'and {N}/100'
    
    if not whole_number:
        return f'zero {cents}'
    
    parts: list[str] = []
    for size, word in NUMBERS.items():
        q, r = divmod(whole_number, size)
        if not q:
            pass
        else:
            parts.append(
                f'{NUMBERS[q]} {NUMBERS[size]}' if size >= 100
                else NUMBERS[size]
                )
            whole_number = r
    print(f"{' '.join(parts)} {cents}")


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser('Help write money amount for checks in the U.S.')
    parser.add_argument('amount', type=float)
    args = parser.parse_args()

    print_amount(args.amount)
    if args.amount <= 1_000_000:
        spell_out(args.amount)