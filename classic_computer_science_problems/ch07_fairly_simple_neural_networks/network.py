# network.py
"""
A script defining `Network` class.
"""
from typing import *
from functools import reduce
from itertools import pairwise
from dataclasses import dataclass, field

from layer import Layer
from util import sigmoid, derivative_sigmoid, Vector

T = TypeVar('OutputType')


def feed_forward(previous_layer_output: Vector, layer: Layer) -> Vector:
    """ Feed `previous_layer_output`, which is the output of previous layer, into `layer`."""
    return layer.outputs(previous_layer_output)

@dataclass
class Network:
    """ A feed-forward neural network with back propogation step that will classify. """
    
    layer_structure: Iterable[int]	# lists the number of neurons in each layer
    learning_rate: float
    layers: list[Layer] = field(init=False, default_factory=list)
    activation_func: Callable[Vector, float] = field(default=sigmoid)
    derivative_activation_func: Callable[Vector, float] = field(default=derivative_sigmoid)
    
    def __post_init__(self):
        if len(self.layer_structure) < 3:
            raise ValueError('Should have at least 3 layers (1 input, 1 hidden, 1 output)')
        
        num_neurons = iter(self.layer_structure)
        
        input_layer: Layer = Layer(
            None,
            next(num_neurons),
            self.learning_rate,
            self.activation_func,
            self.derivative_activation_func
        )
        
        self.layers.append(input_layer)
        
        for previous, n in enumerate(num_neurons):
            hidden_layer: Layer = Layer(
                self.layers[previous],
                n,
                self.learning_rate,
                self.activation_func,
                self.derivative_activation_func
            )
            self.layers.append(hidden_layer)
        
    def output(self, input_data: Vector) -> Vector:
        """
        The output of the neural network are the results of signals running through its layers.
        """
        return reduce(feed_forward, self.layers, input_data)
    
    def calculate_deltas(self, expected: Vector) -> None:
        """
        Calculate the back propogation deltas.
        
        The process will broadly proceed as follows.
            1. Calculate the deltas for output layer neurons.
            2. Calculate the deltas for the hidden layers in backward order.
        """
        it_layers_backward = iter(reversed(self.layers))
        
        last_layer = next(it_layers_backward)
        last_layer.calculate_deltas_for_output_layer(expected)
        
        for current in it_layers_backward:
            current.calculate_deltas_for_hidden_layer(last_layer)
            last_layer = current
        
    def update_weights(self) -> None:
        """
        Update the weights according to the backpropogation deltas calculated by `calculate_deltas()`.
        """
        it_forward = iter(self.layers)
        next(it_forward, None)
        
        for layer in it_forward:
            for neuron in layer.neurons:
                neuron.weights: Vector = [
                    weight + neuron.learning_rate * last_input * neuron.delta
                    for weight, last_input in zip(neuron.weights, layer.previous_layer.output_cache)
                ]
    
    def backpropogate(self, expected: list[Vector]) -> None:
        """
        Implement back-propogation phase by calculating the deltas and then updating the weights
        in that order.
        """
        self.calculate_deltas()
        self.update_weights(expected)
    
    def train(self, input_data: list[Vector], expected_output: list[Vector]) -> None:
        """
        Train the neural network by running each unit of `input_data` through the neural network
        and back-propogating the network against the unit's `expected_output.
        """
        for x, y in zip(input_data, expected_output):
            self.output(x)
            self.backpropogate()
    
    def validate(self, input_data: list[Vector], expeted_output: list[Vector],
                 interpret: Callable[Vector, T]) -> tuple[int, int, float]:
        """
        Return the number of classification
        """
        n, n_correct = len(input_data), 0
        
        for x, y in zip(input_data, expected_output):
            yhat: T = interpret(self.output(x))
            if result == yhat:
                n_correct += 1
        
        return n_correct, n, n_correct/n
    
