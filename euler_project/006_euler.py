############################### my code ###########################
def find_sum_square_difference(n):
    ind_square_total = (n*(n+1)*(2*n+1))//6
    all_total = (n*(n+1)//2) **2
    
    return all_total - ind_square_total
########################### end of my code ########################