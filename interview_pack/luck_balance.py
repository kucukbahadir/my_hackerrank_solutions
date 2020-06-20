########################### my code #######################
def luckBalance(k, contests):
    a = contests
    a.sort(key=lambda x:x[0], reverse=True)

    luck = 0
    
    for i in range(len(a)):
        
        if a[i][1] == 1 and k > 0:
            k -= 1
            luck += a[i][0]
        elif(a[i][1] == 1 and k == 0):
            luck -= a[i][0]
        elif(a[i][1] == 0):
            luck += a[i][0]
        
    return luck
######################## end of my code ####################