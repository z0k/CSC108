"""Phrase Puzzler: functions"""

import random


# Phrase Puzzler constants

DATA_FILE = 'puzzles_small.txt'

HIDDEN = '^'

VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Game types
HUMAN = '1'
HUMAN_HUMAN = '2'
HUMAN_COMPUTER = '3'

# Computer difficulty levels
EASY = 'E'
HARD = 'H'

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Consonant and vowel sets
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
VOWELS = 'aeiou'

# Menu options
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'

# The order in which a computer player, hard difficulty, will guess consonants.
PRIORITY_CONSONANTS = 'tnrslhdcmpfygbwvkqxjz'


# Define your functions here.

def is_win(puzzle, view):
    """(str, str) -> bool

    Return True iff puzzle is the same as view.


    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    # put the function body here
