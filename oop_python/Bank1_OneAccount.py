# Bank1_OneAccount.py
"""
A script simulating bank accounts and operations on them.
"""
from typing import *
from textwrap import dedent

from rich import print

from fancy_input import fancy_input


NAME: str = 'Joe'
BALANCE: float = 100.0
PASSWORD: str = 'soup'
ACTION_PROMPT: str = dedent(
    """
    Press b to get the balance.
    Press d to make a deposit.
    Press w to make a withdrawal.
    Press s to show the account.
    Press q to quit."""
)
PASSWORD_PROMPT: str = 'Please enter your password'
INCORRECT_PASSWORD: str = 'Incorrect password'
WITHDRAW_PROMPT: str = 'Please enter the amount to withdraw'
NEGATIVE_WITHDRAW: str = 'You cannot withdraw a negative amount'
OVERDRAW: str = 'You cannot withdraw more than your account balance'


def validate_action(action: str) -> str:
    first_letter = action.casefold()[0]
    if first_letter.casefold() in ('b', 'd', 'w', 's', 'q'):
        return first_letter
    else:
        raise ValueError



if __name__ == '__main__':
    
    while True:
        action: str = fancy_input(ACTION_PROMPT, validate_action)
        
        match action:
            case 'b':
                print('Get balance:')
                password = fancy_input('Please enter the password:', str)
                if password != PASSWORD:
                    print(INCORRECT_PASSWORD)
                else:
                    print(f'Your balance is: {BALANCE})
            case 'd':
                print('Deposit')
                please 
            
        