def marathon_time(half_time, hilly):
    ''' (num, bool) -> num

    >>> marathon_time(10, False)
    30
    >>> marathon_time(10, True)
    50

    Return half_time * 2 + 10 if hilly == True
    Return half_time * 2 + 30 if hilly == False
    '''
    if hilly == False:
        return half_time * 2 + 10
    if hilly == True:
        return half_time * 2 + 30


