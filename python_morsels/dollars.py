# dollars.py
"""
A program that takes a number and prints that number written as US dollars with cents.

Usage example:
    $ python dollars.py 80
    $80.00
    $ python dollars.py 3.048
    $3.05
    $ python dollars.py 5.5
    $5.50
"""
import sys

if __name__ == '__main__':
    [amount] = sys.argv[1:]
    dollars = float(amount)
    print(f'${dollars:.2f}')