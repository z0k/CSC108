import doctest
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


    >>> game_over('banana', 'banana', QUIT)
    True
    >>> game_over('apple', 'a^^le', CONSONANT)
    False
    >>> game_over('banana', 'banana', CONSONANT)
    True
    >>> game_over('banana', '^anana', QUIT)
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


def calculate_score(current_score, num_occurrences, letter_type):
    """(int, int, str) -> int
    
    Return the new score by adding one point per num_occurrences of the letter
    to current_score if letter_type is CONSONANT, or by deducting VOWEL_PRICE
    from current_score if letter_type is VOWEL.


    >>> calculate_score(0, 5, CONSONANT)
    5
    >>> calculate_score(5, 10, CONSONANT)
    15
    >>> calculate_score(5, 2, VOWEL)
    4
    """
    if letter_type == CONSONANT:
        return current_score + num_occurrences
    elif letter_type == VOWEL:
        return current_score - VOWEL_PRICE


#I feel a bit iffy about this function, make sure to check it thoroughly.
def finalize_score(puzzle, view, unguessed_consonants, current_score):
    """(str, str, str, int) -> int
    
    Return the final score, which is calculated by adding CONSONANT_BONUS to
    current_score for each unguessed consonants from the puzzle that is still
    hidden in the view. 
    

    >>> finalize_score('hello there', 'he^^o ^^e^e', 'bcdlthr', 0)
    10
    >>> finalize_score('which ones count', '^^^^^ ^^^^ ^^^^^', CONSONANTS, 2)
    20
    """
    j  = 0
    for i in range(len(puzzle)):
        if (not puzzle[i] == view[i]) and (puzzle[i] in unguessed_consonants):
            #guess = make_guessed(unguessed_consonants, '', puzzle[i])
            #unguessed_consonants = guess[0]
            j += 1
    return j * CONSONANT_BONUS + current_score
    

def update_score(playerone_score, playertwo_score, new_score, current_player):
    """(int, int, int, str) -> (int, int)
    
    Return an updated playerone_score or playertwo_score, depending on who is 
    the current_player, as the tuple (new_score, current_player)
    
    
    >>> update_score(10, 0, 12, PLAYER_ONE)
    (12, 0)
    >>> update_score(10, 0, 2, PLAYER_TWO)
    (10, 2)
    """
    if current_player == PLAYER_ONE:
        return (new_score, playertwo_score)
    elif current_player == PLAYER_TWO:
        return (playerone_score, new_score)
                     

def next_player(current_player, num_occurrences):
    """(str, int) -> str
                     
    Return the next player, depending on who the current_player is, and if they
    guessed num_occurrences to be greater than zero.


    >>> next_player(PLAYER_ONE, 0)
    'Player Two'
    >>> next_player(PLAYER_ONE, 3)
    'Player One'
    """
    if current_player == PLAYER_ONE:
        if num_occurrences == 0:
            return PLAYER_TWO
        return PLAYER_ONE
    elif current_player == PLAYER_TWO:
        if num_occurrences == 0:
            return PLAYER_ONE
        return PLAYER_TWO


def guess_letter(unguessed_consonants, difficulty):
    """(str, str) -> str
    
    Return the consonant to be guessed next by the computer player. If 
    the difficulty is EASY, the guess is randomly selected. If difficulty is
    HARD, the consonant to guess is the first consonant in PRIORITY_CONSONANTS
    that occurs in unguessed_consonants.


    >>> guess_letter('tfgh', HARD)
    't'
    >>> guess_letter('fgh', HARD)
    'h'
    """
    if difficulty == EASY:
        return random.choice(unguessed_consonants)
    elif difficulty == HARD:
        for e in PRIORITY_CONSONANTS:
            if e in unguessed_consonants:
                return e

    
def half_revealed(view):
    """(str) -> bool
    
    Return True iff at least half of the alphabetic characters in the view are
    revealed.
    
    
    >>> half_revealed('^e^^o t^e^e')
    True
    >>> half_revealed('h^ll^ ^h^^^')
    False
    """
    return  view.count(HIDDEN) <= get_view(view).count(HIDDEN) / 2.


def is_match(puzzle, view):
    """(str, str) -> bool
    
    Return True iff view could be a view of puzzle. 

    
    >>> is_match('csc', 'c^^')
    False
    >>> is_match('csc', 'c^c')
    True
    >>> is_match('csc', 'cc^')
    False
    """
    i = 0
    while i < len(puzzle):
        if len(puzzle) != len(view):
            return False
        if view[i].isalpha():
            if puzzle[i] != view[i]:
                return False
            if puzzle.count(puzzle[i]) != view.count(view[i]):
                return False
        i += 1
    return True

