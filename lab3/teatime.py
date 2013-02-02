def british_time(toronto, toronto_dst, london_dst):
    ''' (float, bool, bool) -> float

    >>> british_time(10.0, True, False)
    15.0
    >>> british_time(8.0, False, True)
    15.0
    >>> british_time(5.0, True, True)
    11.0
    >>> british_time(16.0, False, False)
    22.0

    Return the time in London adjusted for daylight savings.
    '''

    if toronto_dst and london_dst:
        return (toronto + 6) % 24
    elif toronto_dst == False and london_dst == False:
        return (toronto + 6) % 24
    elif toronto_dst and london_dst == False:
        return (toronto + 5) % 24
    else:
        return (toronto + 7) % 24
    
