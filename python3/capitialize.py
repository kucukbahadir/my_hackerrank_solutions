########################## my code ############################
def solve(s):
    string = s.split(' ')
    result = ['' if len(word) == 0 else word[0].upper() + word[1:] for word in string]
    return ' '.join(result)
##################### end of my code #########################