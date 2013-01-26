# String constants representing morning, noon, afternoon, and evening.
MORNING = 'morning'
NOON = 'noon'
AFTERNOON = 'afternoon'
EVENING = 'evening'


def is_a_digit(s):
    ''' (str) -> bool

    Precondition: len(s) == 1

    Return True iff s is a string containing a single digit character (between
    '0' and '9' inclusive).

    >>> is_a_digit('7')
    True
    >>> is_a_digit('b')
    False
    '''

    return '0' <= s and s <= '9'


# Write your three function definitions here:


def time_of_day(hours, minutes):
    ''' (int, int) -> str

    Return 
    '''
