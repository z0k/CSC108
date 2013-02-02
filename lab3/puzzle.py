'''This module contains Python functions corresponding to the hints
given to the "poisonous potions" problem in CSC108 booleans lab.'''

def hint1(p1, p2, p3, p4):
    ''' (bool, bool, bool, bool) -> bool

    Return True iff at least one of the boolen parameters 
    p1, p2, p3, or p4 is True. 

    >>> hint1(False, True, False, True)
    True
    '''
    return p1 or p2 or p3 or p4


def hint2(p2):
    if p2:
        return False
    return True
    

def hint3(p1, p3):
    if p1 or p3:
        return True
    return False


def hint4(p3, p4):
    ''' (bool, bool) -> bool

    Return True iff at least one of potions p3 and p4 is not poisonous.

    >>> hint4(True, True)
    False
    >>> hint4(True, False)
    True
    >>> hint4(False, True)
    True
    >>> hint4(False, False)
    True
    '''
    
    if not (p3 and p4):
        return True
    return False


def hint5(p1, p3, p4):
    truth = 0
    if p1:
        truth = truth +1
    if p3:
        truth = truth +1
    if p4:
        truth = truth +1
    if truth == 1:
        return True
    if truth != 1:
        return False
    

def solution(p1, p2, p3, p4):
    ''' (bool, bool, bool, bool) -> bool

    Return True iff the values of the boolean parameters p1, p2,
    p3, and p4 are such that when they are passed to the hint functions 
    in this module, all five functions return True. 
    
    >>> solution(False, False, False, False)
    False
    '''
    
    h1 = hint1(p1, p2, p3, p4)
    h2 = hint2(p2)
    h3 = hint3(p1, p3)
    h4 = hint4(p3, p4)
    h5 = hint5(p1, p3, p4)
    return h1 and h2 and h3 and h4 and h5

def make_bool(s):
    ''' (str) -> bool
    
    Return the bool equivalent of string s.  If s is not recognizable
    as a bool, return False.
    
    >>> make_bool('True')
    True
    >>> make_bool('f')
    False
    '''    
    
    # make a lowercase version of s so there will be fewer comparisons to make.
    converted = s.lower()
    return converted == "true" or converted == "t"


print("Tell me your hypothesis!")
print("For each question, type true or false")
guess1 = make_bool(input("Is potion 1 poisonous? "))
guess2 = make_bool(input("Is potion 2 poisonous? "))
guess3 = make_bool(input("Is potion 3 poisonous? "))
guess4 = make_bool(input("Is potion 4 poisonous? "))
if solution(guess1, guess2, guess3, guess4):
    print("You're right!")
else:
    print("Sorry, your hypothesis is not correct.")
