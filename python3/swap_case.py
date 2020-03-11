######################## my code ########################
def swap_case(s):
    temp_string = ""

    for i in range(0,len(s)):
        if s[i].isupper():
            temp_string += s[i].lower()
        else:
            temp_string += s[i].upper()
    return temp_string
#################### end of my code #####################