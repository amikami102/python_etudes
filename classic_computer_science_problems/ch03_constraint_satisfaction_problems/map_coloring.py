# map_coloring.py
"""
Color the states of Australia so that no two adjacent regions share a color.
Can you color the regions of Australia with just three different colors?

This script solves the problem with Constraint Satisfaction Problem (CSP) framework.

Variables:
    7 regions of Australia (Western Australia, Northern Territory, South Australia, Queensland, New South Wales, Victoria, Tasmania)

Domains:
    3 colors (red, green, blue)

Constraints:
    Two regions that share a border must have different colors.
"""
from rich import print
from typing import *

from csp import Constraint, ConstraintSatisfactionProblem


class MapColoringConstraint(Constraint[str, str]):
    
    def __init__(self, region1: str, region2: str) -> None:
        super().__init__([region1, region2])
        self.region1, self.region2 = region1, region2
    
    def __repr__(self) -> str:
        return f'{type(self).__name__}({self.region1!r}, {self.region2!r})'
    
    def satisfied(self, assignment: dict[str, str]):
        """
        The constraint is trivially satisfied if either region is not in `assignment`.
        """
        if (self.region1 not in assignment) or (self.region2 not in assignment):
            return True
        else:
            return assignment[self.region1] != assignment[self.region2]
    

if __name__ == '__main__':
    print('[b]Coloring schema for the map of Australia[/b]:')
    
    variables: list[str] = [
        'Western Australia',
        'Northern Territory',
        'South Australia',
        'Queensland',
        'New South Wales',
        'Victoria',
        'Tasmania'
    ]
    domains: dict[str, list[str]] = {
        var: ['red', 'green', 'blue']
        for var in variables
    }
    csp: ConstraintSatisfactionProblem[str, str] = ConstraintSatisfactionProblem(variables, domains)
    
    adjacent_regions = [
        ('Western Australia', 'Northern Territory'),
        ('Western Australia', 'South Australia'),
        ('Northern Territory', 'Queensland'),
        ('Northern Territory', 'South Australia'),
        ('South Australia', 'Queensland'),
        ('Queensland', 'New South Wales'),
        ('South Australia', 'New South Wales'),
        ('South Australia', 'Victoria'),
        ('New South Wales', 'Victoria'),
        ('Victoria', 'Tasmania')
    ]
    
    for pair in adjacent_regions:
        csp.add_constraint(MapColoringConstraint(*pair))
    
    solution: dict[str, str] = csp.backtracking_search()
    if not solution:
        print('No solution found')
    else:
        print(solution)
    