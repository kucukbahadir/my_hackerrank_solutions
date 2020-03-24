########################## my code ##########################
def catAndMouse(x, y, z):
    if abs(z - x) < abs(z - y):
        return "Cat A"
    elif abs(z - y) < abs(z - x):
        return "Cat B"
    else:
        return "Mouse C"
###################### end of my code #######################
