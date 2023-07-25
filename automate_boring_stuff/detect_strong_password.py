# detect_strong_password.py
"""
A program that detects a strong password string, which is defined as one with
    - at least 8 characters long,
    - contains both uppercase and lowercase characters, and
    - contains one numerical digit.
    
The program will prompt you to try again until it gets a strong password.

Usage example:
    $ python detect_stong_password.py
    Type in your password to test for strength: 
    ❌ Need to be at least 8 characters long
    Try again: tyrabanks
    ❌ Need at least one uppercase
    Try again: tyraBanks
    ❌ Need at least one numerical digit
    Try again: tyr4Banks
    ✅ That looks like a strong password 
"""
import re


def is_strong(password: str) -> bool:
    """ Return True if `password` is strong, otherwise return False and print out the reason."""
    if len(password) < 8:
        print('\N{cross mark} Need to be at least 8 characters long')
        return False
    elif not re.search(r'[A-Z]', password):
        print('\N{cross mark} Need at least one uppercase')
        return False
    elif not re.search(r'[a-z]', password):
        print('\N{cross mark} Need at least one lowercase')
        return False
    elif not re.search(r'[0-9]', password):
        print('\N{cross mark} Need at least one numerical digit')
        return False
    else:
        print('\N{white heavy check mark} That looks like a strong password')
        return True


if __name__ == '__main__':
    
    text: str = input('Type in your password to test for strength: ')
    while not is_strong(text):
        text: str = input('Try again: ')