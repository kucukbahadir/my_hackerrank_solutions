########################## my code ########################
def permutationEquation(p):
    return [p.index(p.index(i) + 1) + 1 for i in range(1,len(p) + 1)]
####################### end of my code ###################