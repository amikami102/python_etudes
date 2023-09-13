# zero.py
"""
A program that prints out 80 `0` characters.

Usage example:
    $ python zero.py 
    $ python zero.py 60
    $ python zero.py 80 120 90 79
"""
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('integers', nargs='*', type=int, default=[80])
    args = parser.parse_args()
    print(args)
    for n in args.integers:
        print('0' * n)
