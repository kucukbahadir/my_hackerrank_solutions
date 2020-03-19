########################### my code ########################
def angryProfessor(k, a):
    attendance = 0
    for i in a:
        if i <= 0:
            attendance += 1

    return "YES" if attendance < k else "NO"
######################## end of my code ####################
