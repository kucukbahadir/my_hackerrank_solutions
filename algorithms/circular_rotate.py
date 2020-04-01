############################# my code ############################
def circularArrayRotation(a, k, queries):
    new_list = a[-k:] + a[:-k]
    return [new_list[i] for i in queries]
########################## end of my code ########################