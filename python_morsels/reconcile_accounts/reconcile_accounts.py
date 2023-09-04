# reconcile_accounts.py
"""
A script defining `reconcile_accounts()` function that reconcile two accounts of financial transactions.
"""
from typing import *
import csv
from collections import Counter
from pathlib import Path

from rich import print

Transaction = Iterable[str]


def row_with_status(row: Transaction, found: bool) -> Transaction:
    return [*row, 'FOUND'] if found else [*row, 'MISSING']


def reconcile_accounts(acct1: list[Transaction], acct2: list[Transaction]) -> tuple[list[Transaction], list[Transaction]]:
    """
    Return a copy of the transactions with a column added indicating whether the row item
    was found in the other account.
    """
    new1, new2 = [], []
    
    acct1, acct2 = list(map(tuple, acct1)), list(map(tuple, acct2))	# make each transaction hashable
    groups1, groups2 = Counter(acct1), Counter(acct2)
    
    for row in acct1:
        new1.append(
            row_with_status(row, found=groups2[row] > 0)
        )
        groups2[row] -= 1
    
    for row in acct2:
        new2.append(
            row_with_status(row, found=groups1[row] > 0)
        )
        groups1[row] -= 1
    
    return new1, new2
    
    

# base problem, assume no duplicate items in an account
transactions1 = list(csv.reader(Path('transactions1.csv').open()))
transactions2 = list(csv.reader(Path('transactions2.csv').open()))
out1, out2 = reconcile_accounts(transactions1, transactions2)
expected1 = [
    ['2000-12-04', 'Engineering', '20.00', 'Python Morsels', 'FOUND'],
    ['2000-12-04', 'Finance', '60.00', 'Quick Books', 'FOUND'],
    ['2000-12-05', 'Engineering', '50.00', 'Zapier', 'MISSING']
]
expected2 = [
    ['2000-12-04', 'Engineering', '20.00', 'Python Morsels', 'FOUND'],
    ['2000-12-05', 'Engineering', '49.99', 'Zapier', 'MISSING'],
    ['2000-12-04', 'Finance', '60.00', 'Quick Books', 'FOUND']
]
assert out1 == expected1
assert out2 == expected2

# bonus 1, make the function work when transactions contain duplicate items
transactions3 = list(csv.reader(Path('transactions3.csv').open()))
transactions4 = list(csv.reader(Path('transactions4.csv').open()))
out3, out4 = reconcile_accounts(transactions3, transactions4)
expected3 = [
    ['2000-12-04', 'Engineering', '20.00', 'Python Morsels', 'FOUND'],
    ['2000-12-05', 'Engineering', '50.00', 'Zapier', 'FOUND'],
    ['2000-12-04', 'Education', '60.00', 'Python Book', 'FOUND']
]
expected4 = [
    ['2000-12-04', 'Engineering', '20.00', 'Python Morsels', 'FOUND'],
    ['2000-12-04', 'Education', '60.00', 'Python Book', 'FOUND'],
    ['2000-12-05', 'Engineering', '50.00', 'Zapier', 'FOUND'],
    ['2000-12-05', 'Engineering', '50.00', 'Zapier', 'MISSING'],
    ['2000-12-05', 'Engineering', '50.00', 'Zapier', 'MISSING']
]
assert out3 == expected3
assert out4 == expected4