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
    return puzzle == view


def game_over(puzzle, view, current_selection):
    """(str, str, str) -> bool
    
    Return True iff the puzzle is the same as the view, or the selection 
    is QUIT.


    >>> game_over('banana', 'banana', 'Q')
    True
    >>> game_over('apple', 'a^^le', 'C')
    False
    >>> game_over('banana', 'banana', 'C')
    True
    >>> game_over('banana', '^anana', 'Q')
    True
    """
    return is_win(puzzle, view) or current_selection == QUIT


def get_view(puzzle):
    """(str) -> str
    
    Return the given puzzle with each alphabetic character replaced by the
    HIDDEN character.


    >>> get_view('Puzzle')
    '^^^^^^'
    >>> get_view('Test Case')
    '^^^^ ^^^^'
    """
    view = ''
    for letter in puzzle:
        if letter.isalpha():
            view = view + HIDDEN
        else:
            view = view + letter
    return view


def update_view(puzzle, view, letter):
    """(str, str, str) -> str
    
    Return the view of the puzzle with each occurrence of the letter in the 
    puzzle revealed.


    >>> update_view('Test Case', '^^^^ ^^^^', 'e')
    '^e^^ ^^^e'
    >>> update_view('Letters', '^^^^^^^', 't')
    '^^tt^^^'
    """
    for i in range(len(puzzle)):
        if puzzle[i] == letter:
            view = view[:i] + letter + view[i + 1:]
    return view


def make_guessed(unguessed_consonants, unguessed_vowels, letter):
    """(str, str, str) -> (str, str)
    
    Return unguessed_consonants and unguessed_vowels with the letter removed
    from whichever string, if any, contains it.


    >>> make_guessed('cdfgt', 'aeiou', 'a')
    ('cdfgt', 'eiou')
    >>> make_guessed('cdfgt', 'aeiou', 'c')
    ('dfgt', 'aeiou')
    >>> make_guessed('cdfgt', 'aeiou', 'w')
    ('cdfgt', 'aeiou')
    """
    if letter in unguessed_consonants:
        return (unguessed_consonants.replace(letter, ''), unguessed_vowels)
    elif letter in unguessed_vowels:
        return (unguessed_consonants, unguessed_vowels.replace(letter, ''))
    else:
        return (unguessed_consonants, unguessed_vowels)
