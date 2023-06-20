# constraint_satisfaction_problem.py
"""
A module containing classes and functions for constraint-satisfaction problem.
"""
from typing import *
import collections
from abc import ABC, abstractmethod

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type


class Constraint(Generic[V, D], ABC):
    """ Base class for all constraints """
    
    def __init__(self, variables: list[V]) -> None:
        """Instantiate with the variables that the constraint is between"""
        self.variables = variables
    
    @abstractmethod
    def satisfied(self, assignment: dict[V, D]) -> bool:
        """(Must be overridden by subclasses)"""
    

class ConstraintSatisfactionProblem(Generic[V, D]):
    """
    A constraint satisfaction problem consists of (V)ariables
    that have ranges of values known as (D)omains
    and constraints that determine whether a particular variable's domain selection is valid.
    """
    
    def __init__(self, variables: list[V], domains: dict[V, list[D]]) -> None:
        self.variables: list[V] = variables
        self.domains: dict[V, list[D]] = domains
        self.constraints: dict[V, list[Constraint[V, D]]] = collections.defaultdict(list)       
        
        for var in self.variables:
            if var not in self.domains:
                raise LookupError(f'Every variable should have a domain assigned to it. Variable {var!r} is missing.')

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        for var in constraint.variables:
            if var not in self.variables:
                raise LookupError(f'Variable {var!r} in constraint not in CSP')
            else:
                self.constraints[var].append(constraint)
    
    def consistent(self, variable: V, assignment: dict[V, D]) -> bool:
        """
        Check if variable-to-domain assignment is consistent with the constraints
        """
        return all(
            constraint.satisfied(assignment)
            for constraint in self.constraints[variable]
        )
    
    def backtracking_search(self, assignment: dict[V, D] = {}) -> Optional[dict[V, D]]:
            
        if assignment is None or list(assignment.keys()) == self.variables:
            return assignment
        
        unassigned: Iterator[V] = (
            var for var in self.variables
            if var not in assignment
        )
        
        first: V = next(unassigned)
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
            # print(local_assignment)
            # if we're still consistent, we recurse
            if self.consistent(first, local_assignment):
                result: dict[V, D] = self.backtracking_search(local_assignment)
                # if we didn't find the result, we will end up backtracking
                if result:
                    return result
        return None