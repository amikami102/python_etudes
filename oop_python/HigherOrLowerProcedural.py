# HigherOrLowerProcedural.py
"""
A script implmenting the card game, Higher or Lower.

1. Eight cards are randomly chosen from a deck.
2. The dealer turns the first card face up.
3. The player predicts whether the next card of the eight is higher or lower than the one currently facing up.
4. The next card is shown.
5. If the player is correct, she gets 20 points;
    if wrong, which includes if the card has the same value as the previous one, she loses 15 points.
"""
from typing import *
import random
from collections import namedtuple
from textwrap import dedent
import sys

from rich import print

from fancy_input import fancy_input

T = TypeVar('T')


SUIT_TUPLE: tuple[str] = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
RANK_TUPLE: tuple[str] = (
    'Ace',
    *tuple(str(i) for i in range(2, 11)),
    'Jack',
    'Queen',
    'King'
)
NCARDS: int = 8
DEFAULT_ERROR: str = 'Please enter a valid response.'
PLAY_PROMPT: str = '\n'.join(
    (
        'Will the next card be higher or lower than {rank} of {suit}?',
        '(enter h or l):'
    )
)
PLAY_AGAIN_PROMPT: str = 'To play again, press ENTER or "q" to quit: '


# Define `Card` namedtuple
Card = namedtuple('Card', ['rank', 'suit', 'value'])


def higher_or_lower(input_str: str) -> bool:
    """ A helper function to validate that player input either 'h' or 'l'."""
    if input_str in ('h', 'l'):
        return input_str
    else:
        raise ValueError


def get_card(decklist: list[Card]) -> Card:
    """ Return a random card from `decklist`. """
    popped_card = decklist.pop()
    return popped_card


def shuffle(decklist: list[Card]) -> list[Card]:
    """ Return a shuffled copy of `decklist`. """
    copied = decklist.copy()
    random.shuffle(copied)
    return copied


if __name__ == '__main__':
    
    print(
        dedent("""
        Welcome to Higher or Lower.
        Choose whether the next card to be shown will be higher or lower than the current hard.
        Getting it right adds 20 points; get it wrong and lose 15 points.
        You have 50 points to start.
        """)
    )
    
    deck = [
        Card(rank, suit, value)
        for suit in SUIT_TUPLE
        for value, rank in enumerate(RANK_TUPLE, start=1)
    ]
    score = 50
    
    while True:
        game_deck = shuffle(deck)
        current = get_card(game_deck)
        print(f'Starting card is {current}')
    
        for n in range(NCARDS):
            player_input: str = fancy_input(
                PLAY_PROMPT.format(suit=current.suit, rank=current.rank),
                higher_or_lower
            ).casefold()
            nextcard = get_card(game_deck)
            print(f'Next card is {nextcard}')
            
            if player_input == 'h':
                if nextcard.value > current.value:
                    print('You got it right; it was higher')
                    score += 20
                else:
                    print('You got it wrong; it was not higher')
                    score -= 15
            else:
                if nextcard.value < current.value:
                    print('You got it right; it was lower')
                    score += 20
                else:
                    print('You got it wrong; it was not lower')
                    score -= 15
            current = nextcard
            
        playagain = input(PLAY_AGAIN_PROMPT)
        if playagain == 'q':
            break
    
    print('Thanks for playing!')