# add.py
"""
A script defining `add()`, which accepts two or more nested lists of numbers and returns one nested list.
"""
from typing import *
from numbers import Number

def add(*matrices) -> list[list[Number]]:
    """ Do element-wise matrix addition. """
    return [
        [sum(elements) for elements in zip(*rows, strict=True)]
        for rows in zip(*matrices, strict=True)
    ]
    

# base problem, test adding two nested lists
matrix1 = [[1, -2], [-3, 4]]
matrix2 = [[2, -1], [0, -1]]
assert add(matrix1, matrix2) == [[3, -3], [-3, 3]]
matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
assert add(matrix1, matrix2) == [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

# bonus 1, test adding any number of nested lists
matrix1 = [[1, 9], [7, 3]]
matrix2 = [[5, -4], [3, 3]]
matrix3 = [[2, 3], [-3, 1]]
assert add(matrix1, matrix2, matrix3) == [[8, 8], [7, 7]]

# bonus 2, raise `ValueError` if matrices are not the same size
try:
    add([[1, 9], [7, 3]], [[1, 2], [3]])
except ValueError as e:
    print('Passed')
    print(e)
else:
    print('Failed')