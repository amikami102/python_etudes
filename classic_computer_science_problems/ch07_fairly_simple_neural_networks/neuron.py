# neuron.py
"""
A script defining `Neuron` class.
"""
from typing import *
from dataclasses import dataclass

from util import dot_product, Vector


@dataclass
class Neuron:
    """ A neuron of a neural network. """
    weights: Vector
    learning_rate: float
    activation_func: Callable[Vector, float]
    derivative_activation_func: Callable[Vector, float]
    output_cache: float = 0.0
    delta: float = 0.0
    
    def output(self, inputs: Vector) -> float:
        """
        Return the output of the neuron, which is the
        dot product of the input with its `weights` passed
        into `activation_func`.
        """
        self.output_cache = dot_product(inputs, self.weights)
        return self.activation_func(self.output_cache)