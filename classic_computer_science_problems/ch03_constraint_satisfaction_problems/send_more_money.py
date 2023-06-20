# send_more_money.py
"""
Each letter represents a digit (0-9). Replace letters with digits so that the
rendered statement is mathematically true.

Variables:
    Letters

Domain:
    Digits 0-9

Constraint:
    No two letters can represent the same digit.
"""
from rich import print
from textwrap import dedent
from typing import *

from csp import Constraint, ConstraintSatisfactionProblem


class SendMoreMoneyConstraint(Constraint[str, int]):
    
    def __init__(self, letters: list[str]) -> None:
        super().__init__(letters)
        self.letters: list[str] = letters
    
    def satisfied(self, assignment: dict[str, int]) -> bool:
        """
        Check the constraints in order. 
        First, check that there are no duplicate assignments.
        Next, if all the letters have been assigned and there are no duplicates,
            the mathematical statement rendered by the assignment is true.
        If the first condition passes but not all the letters have been assigned,
            return True.
        """
        
        if len(set(assignment.values())) < len(assignment):
            return False
        
        if len(assignment) == len(self.letters):
            # only check the sum if all the letters have been assigned
            send: int = sum(
                (
                    assignment['S'] * 1000,
                    assignment['E'] * 100,
                    assignment['N'] * 10,
                    assignment['D'] * 1
                )
            )
            more: int = sum(
                (
                    assignment['M'] * 1000,
                    assignment['O'] * 100,
                    assignment['R'] * 10,
                    assignment['E'] * 1
                )
            )
            money: int = sum(
                (
                    assignment['M'] * 10_000,
                    assignment['O'] * 1000,
                    assignment['N'] * 100,
                    assignment['E'] * 10,
                    assignment['Y'] * 1
                )
            )
            return send + more == money
        
        return True
    

if __name__ == '__main__':
    
    letters: list[str] = list(set('sendmoremoney'.upper()))
    digits: dict[str, list[int]] = {
        letter: list(range(10))
        for letter in letters
    }
    digits['M'] = [1] # so we don't get answers starting with a zero
    
    csp: ConstraintSatisfactionProblem[str, int] = ConstraintSatisfactionProblem(letters, digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters))
    
    solution: Optional[dict[str, int]] = csp.backtracking_search()
    if not solution:
        print('No solution found')
    else:
        print(solution)
        send, more, money = (
            ''.join(str(solution[l]) for l in 'SEND'),
            ''.join(str(solution[l]) for l in 'MORE'),
            ''.join(str(solution[l]) for l in 'MONEY')
        )
        print(dedent(f"""
          {send}
        + {more}
        --------
         {money}
        """))
