######################### my code ######################
def sockMerchant(ar):
    number_of_pairs = 0
    for i in set(ar):
        number_of_pairs += ar.count(i) // 2

    return number_of_pairs
###################### end of my code ##################