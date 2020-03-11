############################## my code ##########################
def count_substring(string, sub_string):
    length_sub = len(sub_string)
    count = 0
    for i in range(0,len(string)):
        if string[i:i+length_sub] == sub_string:
            count += 1
        
    return count
########################### end of my code ######################