def all_fluffy(s):
    count = 0
    for e in s:
        if e not in 'fluffy':
            return False
    return True
