############################# my code ##############################
def getMoneySpent(keyboards, drives, b):
    max_value = -1

    for i in keyboards:
        for j in drives:
            if (i + j) <= b:
                if (i + j) > max_value:
                    max_value = i + j
    
    return max_value

########################## end of my code #########################