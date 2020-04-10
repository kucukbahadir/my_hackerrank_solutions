############################## my code ###########################
def beautifulDays(i, j, k):
    count = 0
    for number in range(i, j + 1):
        if (abs(number - int(str(number)[::-1])) / k).is_integer():
            count +=1
    
    return count
########################### end of my code #######################