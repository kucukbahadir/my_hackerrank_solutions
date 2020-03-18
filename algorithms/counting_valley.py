############################### my code ##########################
def countingValleys(s):
    altitude = 0
    number_of_valley = 0
    seabelow = False

    for i in range(len(s)):
        altitude = altitude + 1 if s[i] =="U" else altitude - 1

        if (seabelow == True and altitude == 0): number_of_valley += 1

        seabelow = True if altitude < 0 else False
        
    return number_of_valley
############################ end of my code ######################