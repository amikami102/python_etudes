# roll.py
"""
A CLI program that prints out the sum of simulated dice rolls.

Usage example:
    $ python roll.py
    $ python roll.py 17
    $ python roll.py 6 6 6 10
"""
from random import randint
import argparse


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(
        'A program that prints out the sum of simulated dice rolls'
    )
    parser.add_argument(
        'sides',
        type=int,
        default=[6],
        nargs='*',
        help='Number of sides on each die'
    )
    args = parser.parse_args()
    
    # print out the sum of rolls
    print(sum(randint(1, sides) for sides in args.sides))
