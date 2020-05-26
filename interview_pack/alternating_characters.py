######################## my code #######################
def alternatingCharacters(s):
    check =  s[0]
    counter = 0
    
    for i in range(1,len(s)):
        if s[i] == check:
            counter += 1
        else:
            check = s[i]
    
    return counter
######################## end of my code #################