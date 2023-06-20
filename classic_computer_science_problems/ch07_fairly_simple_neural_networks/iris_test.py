# iris_test.py
"""
A script testing `nework.Network` on iris sample classification.

Data source: 'iris.csv' from https://gist.github.com/netj/8836201
"""
import csv
from pathlib import Path
from typing import *
from random import shuffle

from rich import print

from network import Network
from util import Vector, minmax_scale


VARIETY_CODE: dict[str, Vector] = {
    'Setosa': [1.0, 0.0, 0.0],
    'Versicolor': [0.0, 1.0, 0.0],
    'Virginica': [0.0, 0.0, 1.0]
}
OUTPUT_CODE: dict[int, str] = {
    v.index(max(v)): k for v, k in VARIETY_CODE.items()
}
TRAIN_RUNS: int = 50					# train the network TRAIN_RUN times
TRAIN_SIZE: int = 140			# subset the first 140 observations for training
LAYER_STRUCTURE: list[int] = [4, 6, 3]	# number of neurons in each layer
LEARNING_RATE: float = 0.3


def iris_interpreter(output: Vector) -> str:
    """Return the iris species label corresponding to the `output` vector."""
    return OUTPUT_CODE[output.index(max(output))]


if __name__ == '__main__':
    
    X: list[Vector] = []				# the input data 
    y: list[Vector] = []				# the expected output data
    labels: list[str] = []				# the species labels
    
    reader = csv.reader(Path('iris.csv').open())	# read the csv file
    next(reader)								# skip the header row
    
    rows = list(reader)
    shuffle(rows)
    for row in rows:
        *xs, label = tuple(row)
        
        X.append([float(x) for x in xs])
        labels.append(label)
        y.append(VARIETY_CODE[label])
    
    minmax_scale(X)
    
    iris_network: Network = Network(LAYER_STRUCTURE, LEARNING_RATE)
    
    # split into training and testing sets
    X_train, y_train = X[:TRAIN_SIZE], y[:TRAIN_SIZE]
    X_test, y_test = X[TRAIN_SIZE:], y[TRAIN_SIZE: ]
    
    for _ in range(TRAIN_RUNS):
        iris_network.train(X_train, y_train)

