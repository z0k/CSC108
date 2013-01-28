#def add_underscores(s):
    #return '_'.join(s)

def add_underscores(s):
    underscored_string = ''
    for e in s:
        underscored_string = underscored_string + e + '_'
    return underscored_string[:-1]
