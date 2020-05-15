############################## my code ############################
def sum_multiples(x):
    n3, n5, n15 = (x-1)//3 , (x-1)//5 , (x-1)//15
    
    multiples_3 = 3 * (n3 * (n3 + 1) // 2)
    multiples_5 = 5 * (n5 * (n5 + 1) // 2)
    multiples_15 = 15 * (n15 * (n15 + 1) // 2)

    return multiples_3 + multiples_5 - multiples_15
########################### end of my code ########################