# layer.py
"""
A script defining `Layer` class.
"""
from typing import *
from random import random
from dataclasses import dataclass, field

from util import dot_product, Vector
from neuron import Neuron


def generate_random_weights(n: int = 0) -> Vector:
    """ Generate a length-n vector of random float values. """
    return [ random() for _ in range(n)] if n else []


@dataclass
class Layer:
    """ A layer of a neural network. """
    
    previous_layer: Optional['Layer']
    num_neurons: int
    learning_rate: float
    activation_func: Callable[Vector, float]
    derivative_activation_func: Callable[Vector, float]
    neurons: list[Neuron] = field(init=False)
    output_cache: Vector = field(init=False)
    
    def __post_init__(self) -> None:
        self.neurons = [
            Neuron(
                generate_random_weights(self.previous_layer.num_neurons)
                    if self.previous_layer
                    else generate_random_weights(),
                self.learning_rate,
                self.activation_func,
                self.derivative_activation_func
            )
            for _ in range(self.num_neurons)
        ]
        self.output_cache = [0.0 for _ in range(self.num_neurons)]
    
    def outputs(self, inputs: Vector) -> Vector:
        """
        Feed `inputs` into every neuron in the layer and return the output vector.
        If there is no previous layer, then this layer is the input layer.
        """
        if not self.previous_layer:
            self.output_cache = inputs
        else:
            self.output_cache = [
                neuron.output(inputs)
                for neuron in self.neurons
            ]
        return self.output_cache
    
    def calculate_deltas_for_output_layer(self, expected: Vector) -> None:
        """
        Use this function if `self` is the output layer.
        Calculate the deltas for `self.neurons` during back-propogation phase of training.
        """
        error: Vector = expected - self.output_cache
        for neuron, expected_val, predicted_val in zip(self.neurons, expected, self.output_cache):
            neuron['delta'] = neuron.derivative_activation_func(predicted_val) \
                              * (expected_val - predicted_val)
    
    def calculate_deltas_for_hidden_layer(self, next_layer: 'Layer') -> None:
        """
        Use this function if `self` is a hidden layer.
        `next_layer` is the `Layer` that intakes `self`'s output during feed-forward phase.
        Calculate the deltas for `self.neurons` during the back-propogation phase.
        """
        for i, neuron in enumerate(self.neurons):
            sum_weights_and_deltas: float = sum(
                next_neuron.delta * next_neuron.weights[i]
                for next_neuron in next_layer.neurons
            )
            neuron.delta = neuron.derivative_activation_func(neuron.output_cache) * sum_weights_and_deltas
    
