# util.py
"""
A script containing utility functions for implementing neural network.
"""
from typing import *
from math import exp

Vector = list[float]


def dot_product(vector1: Vector, vector2: Vector) -> float:
    """ Return dot product of `vector1` and `vector2`. """
    return sum(p1 * p2 for p1, p2 in zip(vector1, vector2))


def sigmoid(x: float) -> float:
    """ Return S(x) = 1 / (1 + e^(-x)). """
    return 1.0 / (1.0 + exp(-x))


def derivative_sigmoid(x: float) -> float:
    """ Return the derivative of S(x) = S(x) * (1 - S(x)). """
    return sigmoid(x) * (1 - sigmoid(x))


def minmax_scale(data: list[Vector]) -> None:
    """
    Scale the data so that each feature's values fall between 0 an 1,
    where 0 corresponds to the minimum value and 1 the maximum value.
    """
    if not all(len(row) == len(data[0]) for row in data):
        raise ValueError('Make sure that all rows have the same number of features.')
    
    n_features, n = len(data[0]), len(data)
    
    
    for p in range(n_features):
        values: Vector = [row[p] for row in data]
        minimum, maximum = min(values), max(values)
        scaled: Vector = [(x - minimum)/(maximum - minimum) for x in values]
        for i in range(n):
            data[i][p] = scaled[i]