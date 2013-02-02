import random
import puzzler_functions as pf


def get_puzzle():
    """() -> str

    Return a randomly chosen line from the file named pf.DATA_FILE.
    """

    data_file = open(pf.DATA_FILE)

    phrases = []
    for line in data_file:
        phrases.append(line.strip())

    data_file.close()
    return phrases[random.randint(0, len(phrases) - 1)]


def prompt_for_game_type():
    """() -> str

    Prompt for and return the game type.
    """

    game_type = input("""Choose the game type:
     [1] - One Player
     [2] - Two player (human opponent)
     [3] - Two player (computer opponent)\n""")

    while not (game_type == pf.HUMAN \
          or game_type == pf.HUMAN_HUMAN \
          or game_type == pf.HUMAN_COMPUTER):
        game_type = input('Invalid choice.  Enter [1], [2] or [3]: ').strip()
    return game_type


def select_computer_difficulty(game_type):
    """(str) -> str

    If game_type is pf.HUMAN_COMPUTER, prompt the user to enter the difficulty
    and return it. Otherwise, return None because there is no computer player.
    """

    if game_type == pf.HUMAN_COMPUTER:
        difficulty = input(
            "Enter the game difficulty ([E]asy or [H]ard):  ").strip().upper()

        while difficulty != pf.EASY and difficulty != pf.HARD:
            difficulty = input(
                "Enter the game difficulty ([E]asy or [H]ard):  ")
            difficulty = difficulty.strip().upper()

    else:
        difficulty = None

    return difficulty


def get_player_letter(unguessed_consonants, unguessed_vowels, move_type,
        difficulty):
    """(str, str, str, str) -> str

    Prompt the user to enter either an unguessed consonant or an unguesssed
    vowel based on the move_type, and return the letter. difficulty is
    ignored; it is supplied only because this function must have the same type
    contract as get_computer_letter.

    This function must have the same type contract as get_computer_letter.
    """


    if move_type == pf.CONSONANT:
        letter = input(
            'Please enter a consonant [{0}]: '.format(unguessed_consonants))
        while len(letter) != 1 or letter not in unguessed_consonants:
            letter = input("Invalid choice.  Please enter a consonant: ")
    else:
        letter = input("Please enter a vowel [{0}]: ".format(unguessed_vowels))
        while len(letter) != 1 or letter not in unguessed_vowels:
            letter = input("Invalid choice.  Please enter a vowel: ")

    return letter


def get_computer_letter(unguessed_consonants, unguessed_vowels, move_type,
        difficulty):
    """(str, str, str, str) -> str

    Return the letter the computer selects from unguessed_consonants based on
    difficulty, which is one of pf.EASY and pf.HARD. unguessed_vowels and
    move_type are ignored; they are supplied only because this function must
    have the same type contract as get_player_letter.

    This function must have the same type contract as get_player_letter. 
    """

    return pf.guess_letter(unguessed_consonants, difficulty)

def move_type_is_valid(move_type, score, unguessed_consonants,
        unguessed_vowels):
    """(str, int, str, str) -> bool
    Return whether move_type is one of pf.CONSONANT, pf.VOWEL, pf.SOLVE, or
    pf.QUIT. If it's pf.VOWEL, also check whether the player has a high
    enough score to buy a vowel and print a message if they do not.
    For pf.consonant and pf.vowel, ensure that there is something to guess.
    """

    valid = move_type == pf.CONSONANT or move_type == pf.VOWEL or \
        move_type == pf.SOLVE or move_type == pf.QUIT

    if move_type == pf.VOWEL and score < pf.VOWEL_PRICE:
        print('You do not have enough points to reveal a vowel. '
            'Vowels cost {0} point.'.format(pf.VOWEL_PRICE))
        valid = False

    elif move_type == pf.VOWEL and unguessed_vowels == '':
        print('You do not have any more vowels to guess!')
        valid = False

    elif move_type == pf.CONSONANT and unguessed_consonants == '':
        print('You do not have any more consonants to guess!')
        valid = False

    return valid


def is_human(current_player, game_type):
    """(str, str) -> bool
    Return True iff current_player represents a human in a game of type
    game_type.

    >>> is_human(pf.PLAYER_ONE, pf.HUMAN_COMPUTER)
    True
    >>> is_human(pf.PLAYER_TWO, pf.HUMAN_HUMAN)
    True

    """
    return current_player == pf.PLAYER_ONE or game_type != pf.HUMAN_COMPUTER


def get_player_move(current_player, view, difficulty, score,
        unguessed_consonants, unguessed_vowels):
    """(int, int, str, str, int, str, str) -> str

    Prompt current_player to choose the kind of move (pf.CONSONANT, pf.VOWEL,
    pf.SOLVE or pf.QUIT) and return it.

    view is the current state of the puzzle, difficulty and game_type are
    unused (and supplied only because of get_computer_move), score is provided
    for display to the player, and the unguessed_ parameters are the letters
    that have not yet been guessed.

    This function and get_computer_move must have the same type contract.
    """
    print('=' * 50)
    print('{0}, it\'s your turn. You have {1} points.'.format(
        current_player, score))
    print('\n' + view + '\n')
    move_type = input(
        '[C]onsonant, [V]owel, [S]olve, [Q]uit: ').strip().upper()
    while not move_type_is_valid(move_type, score, unguessed_consonants,
            unguessed_vowels):
        print('Invalid input.')
        move_type = input(
            '[C]onsonant, [V]owel, [S]olve, [Q]uit: ').strip().upper()

    return move_type


def get_computer_move(current_player, view, difficulty, score,
        unguessed_consonants, unguessed_vowels):
    """(int, int, str, str, int, str, str) -> str

    Return the computer's next move, which will be either to guess a
    pf.CONSONANT or to pf.SOLVE. The computer chooses to solve when difficulty
    is pf.HARD, at least half of the letters in the puzzle have been revealed
    and there is a valid guess (according to guess_puzzle), otherwise the
    computer opts to guess a pf.CONSONANT.

    This function and get_player_move must have the same type contract.
    current_player and unguessed_vowels are unused.
    """

    print('=' * 50)
    print('Computer, it\'s your turn. You have {0} points.'.format(
        score))
    print('\n' + view + '\n')
    print('[C]onsonant, [V]owel, [S]olve, [Q]uit: ')
    guess = get_computer_guess(view) 
    if (difficulty == pf.HARD and pf.half_revealed(view)
       and guess != '') or unguessed_consonants == '':
        print('The Computer chooses to try to solve.')
        print('The computer guesses "{0}"'.format(guess))
        return pf.SOLVE

    return pf.CONSONANT


def get_player_guess(view):
    """(str, str, str, str) -> str

    Ask the player for a guess and return it. view is ignored (and is supplied
    because get_computer_guess requires it).

    This function and get_computer_guess must have the same type contract.
    """

    return input("Please enter your guess: ")


def get_computer_guess(view):
    """(str) -> str

    Return a line from the file named pf.DATA_FILE that contains string that
    could be represented by view, or, if no such line exists, the empty
    string.

    This function and get_player_guess must have the same type contract.
    """

    data_file = open(pf.DATA_FILE)
    for line in data_file:
        if pf.is_match(line.strip(), view):
            return line.strip()

    return ''


def play_game(puzzle, view, game_type):
    """(str, str, str) -> (bool, int)

    Prompt the player(s) to try to guess the puzzle. game_type is one of
    pf.HUMAN, pf.HUMAN_HUMAN, or pf.HUMAN_COMPUTER.
    Return whether there was a winner and the final score.
    """

    player_one_score = 0
    player_two_score = 0
    current_player = pf.PLAYER_ONE

    # The player move choice; will be one of pf.CONSONANT, pf.VOWEL,
    # pf.SOLVE and pf.QUIT.
    move_type = ''

    # The letters that have not yet been guessed.
    unguessed_consonants = pf.CONSONANTS
    unguessed_vowels = pf.VOWELS

    # This is None if there is no computer player.
    difficulty = select_computer_difficulty(game_type)

    # Note: you may find it helpful to display the solution while you
    # are testing. To do this, uncomment the following line:
    #print('Solution: {0}'.format(puzzle))

    while not pf.game_over(puzzle, view, move_type):
        quantity = 0
        if current_player == pf.PLAYER_ONE:
            score = player_one_score
        else:
            score = player_two_score

        # Set up function aliases based on whether it's a human's turn or a
        # computer's turn.
        if is_human(current_player, game_type):
            get_move = get_player_move
            get_guess = get_player_guess
            get_letter = get_player_letter
        else:
            get_move = get_computer_move
            get_guess = get_computer_guess
            get_letter = get_computer_letter

        move_type = get_move(current_player, view, difficulty,
            score, unguessed_consonants, unguessed_vowels)

        if move_type == pf.SOLVE:
            guess = get_guess(view)

            if guess == puzzle:
                newview = puzzle
                score = pf.finalize_score(puzzle, view,
                    unguessed_consonants, score)
                view = newview
            else:
                print("The guess '{0}' is Incorrect :-(".format(guess))

        elif move_type == pf.CONSONANT or move_type == pf.VOWEL:

            letter = get_letter(
                unguessed_consonants, unguessed_vowels, move_type, difficulty)

            quantity = puzzle.count(letter)
            view = pf.update_view(puzzle, view, letter)
            score = pf.calculate_score(score, quantity, move_type)
            unguessed_consonants, unguessed_vowels = pf.make_guessed(
                unguessed_consonants, unguessed_vowels, letter)

            print('The guess was {0}, which occurs {1} time(s).  '\
                  .format(letter,quantity), end='')
            print('Your score is {0}.'.format(score))
            

            player_one_score, player_two_score = pf.update_score(
                              player_one_score, player_two_score,
                              score, current_player)

        if game_type != pf.HUMAN:
            current_player = pf.next_player(current_player, quantity)

    # The game is over.
    display_outcome(pf.is_win(view, puzzle), score)


def display_outcome(won, score):
    """(bool, int) -> NoneType

    Display a message indicating whether the player won and, if so, their
    score.

    >>> display_outcome(True, 4)
    Winner! You scored 4 point(s).
    """

    if won:
        print("Winner! You scored {0} point(s).".format(score))
    else:
        print("Better luck next time!")


## The main Phrase Puzzler program
puzzle = get_puzzle()
view = pf.get_view(puzzle)

print('Welcome to Phrase Puzzler!')
game_type = prompt_for_game_type()
play_game(puzzle, view, game_type)
