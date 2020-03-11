########################## my code ##################################
def utopianTree(n):
    counter = 0
    height = 0

    for i in range(0,n + 1):
        if counter % 2 == 0:
            height += 1

        else:
            height *= 2

        counter += 1
    
    return height

####################### end of my code ##############################