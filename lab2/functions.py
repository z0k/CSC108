def cookies_needed(num_adults, num_teens, num_children):    
    ''' (int, int, int) -> int

    Return the number of cookies needed to feed num_adults adults, num_teens
    teens and num_children children.
    Each adult gets 3 cookies, each teenager gets 5, and each child gets 2.
    
    >>> cookies_needed(2, 3, 1)
    23
    '''
    return num_adults * 3 + num_teens * 5 + num_children * 2

def is_multiple_of_3(value):
    ''' (int) -> bool

    Return True iff value is an integer multiple of 3.
    
    >>> is_multiple_of_3(15)
    True
    >>> is_multiple_of_3(7)
    False
    '''
    return (value % 3) == 0
   
def is_multiple(value1, value2):
    ''' (int, int) -> bool

    Return True iff value1 is an integer multiple of value2.
    
    >>> is_multiple(15, 3)
    True
    >>> is_multiple(7, 2)
    False
    '''
    return value1 % value2 == 0
