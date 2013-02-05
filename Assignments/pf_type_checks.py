"""This module should be used to test the parameter and return types of your
functions. Before submitting your assignment, run this type-checker on your
puzzler_functions.py. If errors occur when you run this module, fix them
before you submit your assignment.  

When this module runs, if nothing is displayed and no errors occur, then the
type checks passed. This means that the function parameters and return types
match the assignment specification, but it does not mean that your code works
correctly in all situations. Be sure to test your code before submitting."""

import puzzler_functions as pf

# Get the initial values of the constants
constants_before = [pf.DATA_FILE, pf.HIDDEN, pf.VOWEL_PRICE, 
                    pf.CONSONANT_BONUS, pf.HUMAN, pf.HUMAN_HUMAN, 
                    pf.HUMAN_COMPUTER, pf.EASY, pf.HARD, pf.PLAYER_ONE,
                    pf.PLAYER_TWO, pf.CONSONANTS, pf.VOWELS, pf.CONSONANT,
                    pf.VOWEL, pf.SOLVE, pf.QUIT, pf.PRIORITY_CONSONANTS]
	
# Type check pf.is_win
result = pf.is_win('apple', 'about')
assert isinstance(result, bool), \
       """pf.is_win should return a bool, but returned {0}
       .""".format(type(result))


# Type check pf.game_over
result = pf.game_over('water', '^^te^', pf.CONSONANT)
assert isinstance(result, bool), \
       """pf.game_over should return a bool, but returned {0}.""" \
       .format(type(result))


# Type check pf.get_view
result = pf.get_view('happy')
assert isinstance(result, str), \
       """pf.get_view should return a str, but returned {0}.""" \
       .format(type(result))


# Type check pf.update_view
result = pf.update_view('apple', 'a^^l^', 'e')
assert isinstance(result, str), \
       """pf.update_view should return a str, but returned {0}.""" \
       .format(type(result))


# Type check pf.make_guessed
result = pf.make_guessed('jklmn', 'aeo', 'm')
assert isinstance(result, tuple) \
       and isinstance(result[0], str) \
       and isinstance(result[1], str), \
       """pf.make_guessed should return a tuple of (str, str),
but returned {0}.""" \
       .format(type(result))


# Type check pf.calculate_score
result = pf.calculate_score(4, 2, pf.CONSONANT)
assert isinstance(result, int), \
       """pf.calculate_score should return an int, but returned {0}.""" \
       .format(type(result))

# Type check pf.finalize_score
result = pf.finalize_score('apple', 'a^^l^', 'ghjklpq', 4)
assert isinstance(result, int), \
       """pf.finalize_score should return an int, but returned {0}.""" \
       .format(type(result))

# Type check pf.update_score
result = pf.update_score(2, 3, 4, pf.PLAYER_ONE)
assert isinstance(result, tuple)  \
       and isinstance(result[0], int) \
       and isinstance(result[1], int), \
       """pf.update_score should return a tuple of (int, int),
but returned {0}.""" \
       .format(type(result))

# Type check pf.next_player
result = pf.next_player(pf.PLAYER_ONE, 2)
assert isinstance(result, str), \
       """pf.next_player should return a str, but returned {0}.""" \
       .format(type(result))

# Type check pf.guess_letter
result = pf.guess_letter('bcd', pf.HARD)
assert isinstance(result, str), \
       """pf.guess_letter should return a str, but returned {0}.""" \
       .format(type(result))

# Type check pf.half_revealed
result = pf.half_revealed('a^^l^')
assert isinstance(result, bool), \
       """pf.half_revealed should return a bool, but returned {0}.""" \
       .format(type(result))

# Type check pf.is_match
result = pf.is_match('apple', 'a^^l^')
assert isinstance(result, bool), \
       """pf.is_match should return a bool, but returned {0}.""" \
       .format(type(result))

# Get the final values of the constants
constants_after = [pf.DATA_FILE, pf.HIDDEN, pf.VOWEL_PRICE, 
                   pf.CONSONANT_BONUS, pf.HUMAN, pf.HUMAN_HUMAN, 
                   pf.HUMAN_COMPUTER, pf.EASY, pf.HARD, pf.PLAYER_ONE,
                   pf.PLAYER_TWO, pf.CONSONANTS, pf.VOWELS, pf.CONSONANT,
                   pf.VOWEL, pf.SOLVE, pf.QUIT, pf.PRIORITY_CONSONANTS]

# Check whether the constants are unchanged.
assert constants_before == constants_after, \
       """Your function(s) modified the value of a constant(s). Edit your code
        so that the values of constants are unchanged by your functions."""
    
