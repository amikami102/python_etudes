# genetic_alogrithm.py
"""
A script defining `GeneticAlgorithm` class with roulette-wheel selection method,
which gives each chromosome a chance of being picked, proportional to its fitness.

An alternative selection method is tournament selection where a number of
randomly chosen chromosomes are challenged against one another and that the survivor (i.e. the fittest) is selected.
"""
from typing import *
from enum import Enum
from random import choices, random
from statistics import mean

from chromosome import Chromosome

C = TypeVar('C', bound='Chromosome') # type of chromosomes


class GeneticAlgorithm(Generic[C]):
    SelectionType = Enum('SelectionType', ['ROULETTE', 'TOURNAMENT'])
    
    def __init__(self, initial_pop: list[C], threshold: float,
                 max_gen: int = 100,
                 mutate_prob: float = 0.01,
                 xover_prob: float = 0.7,
                 selection_type: SelectionType = SelectionType.TOURNAMENT) -> None:
        """
        initial_pop: list[C]
            the first generation of chromosomes
        
        threshold: float
            the fitness level that indicatest that a solution has been found
        
        max_gen: int
            maximum number of generations to run
        
        mutate_prob: float
            probability of each chromosome in each generation mutating
        
        xover_prob: float
            probability that two parents selected to reproduce have children that are a mixture of their genes;
            otherwise, the children are just duplicates of their parents
        
        selection_type: SelectionType
            the type of selection type used
        """
        
        self._population: list[C] = initial_pop
        self._threshold: float = threshold
        self._max_gen: int = max_gen
        self._mutate_prob: float = mutate_prob
        self._xover_prob: float = xover_prob
        self._selection_type: GeneticAlgorithm.SelectionType = selection_type
        self._fitness_key: Callable = type(self._population[0]).fitness
        
    def _pick_roulette(self, wheel: list[float]) -> tuple[C, C]:
        """ Use the probability distribution wheel to pick two parents """
        return tuple(choices(self._population, weights=wheel, k=2))
    
    def _pick_tournament(self, n: int) -> tuple[C, C]:
        """ Choose `n` chromosomes at random and take the two best. """
        participants: list[C] = choices(self._population, k=n)
        return tuple(sorted(participants, key=self._fitness_key, reverse=True)[:2])
    
    def _reproduce_and_replace(self) -> None:
        """
        Replace the population with a new generation of individuals.
        
        The code instantiates `new_pop` container, which will be filled up
        until there are as many elements as `_population`.
        
        The steps are:
            1. Two chrosomes (`parents`) are selected for reproduction.
            2. The parents will cross over with probability `_xover_prob`.
                If there is no cross over, just add the parents to `new_pop`.
            3. Repeat steps 2 and 3 until `new_pop` is filled up.
        """
        new_pop: list[C] = []
        
        while len(new_pop) < len(self._population):
            if self._selection_type == GeneticAlgorithm.SelectionType.ROULETTE:
                parents: tuple[C, C] = \
                    self._pick_roulette(
                        [x.fitness() for x in self._population]
                    )
            else:
                parents = self._pick_tournament(len(self._population)//2)
            
            if random() < self._xover_prob:
                new_pop.extend(parents[0].crossover(parents[1]))
            else:
                new_pop.extend(parents)
        
        if len(new_pop) > len(self._population):
            new_population.pop()	# remove 1 extra if population size is an odd number
        
        self._population = new_pop
            
    def _mutate(self) -> None:
        """ Mutate each individual """
        for individual in self._population:
            if random() < self._mutate_prob:
                individual.mutate()
    
    def run(self) -> C:
        """ Run the genetic algorithm for `max_gen` iterations and return the best individual found. """
        best: C = max(self._population, key=self._fitness_key)
        for gen in range(self._max_gen):
            
            if best.fitness() >= self._threshold:
                return best	# exit early if we beat the threshold
            
            print(f"Generation {gen} has best fitness {best.fitness()} and average fitness {mean(self._fitness_key(x) for x in self._population)}.")
            
            self._reproduce_and_replace()
            self._mutate()
            highest: C = max(self._population, key=self._fitness_key)
            if highest.fitness() > best.fitness():
                best = highest
        return best