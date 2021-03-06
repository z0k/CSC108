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

    Return the value MORNING if the time is before 12:00, NOON if it is 12:00,
    AFTERNOON if it is after 12:00 and before 17:00, and EVENING otherwise.

    >>> time_of_day(12, 0)
    'noon'
    >>> time_of_day(8, 59)
    'morning'
    '''

    if hours < 12:
        return MORNING
    elif hours == 12 and minutes == 0:
        return NOON
    elif hours == 12 and not minutes == 0:
        return AFTERNOON
    elif 12 < hours < 17:
        return AFTERNOON
    else:
        return EVENING


def closest_time(time1, time2, actual_time):
    ''' (str, str, str) -> str

    Return the parameter between time1 and time2 that is closest to actual_time.

    >>> closest_time('11:59', '12:01', '12:00')
    '11:59'
    >>> closest_time('01:40', '13:40', '05:40')
    '1:40'
    ''' 
    time1_mins = int(time1[:2]) * 60 + int(time1[-2:])
    time2_mins = int(time2[:2]) * 60 + int(time2[-2:])
    actual_time_mins = int(actual_time[:2]) * 60 + int(actual_time[-2:]) 
    if abs(time1_mins - actual_time_mins) <= abs(time2_mins - actual_time_mins):
        return time1
    return time2


def sum_digits(string):
    ''' (str) -> int

    Return the sum of the values of each integer digit that appears in string.

    >>> sum_digits('CSC108H1S')
    10
    >>> sum_digits('2')
    2
    '''

    total = 0
    for e in string:
        if is_a_digit(e):
            total = total + int(e)
    return total

