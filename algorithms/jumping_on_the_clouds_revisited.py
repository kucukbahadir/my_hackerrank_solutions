######################### my code #######################
def jumpingOnClouds(c, k):
    total_energy = 100

    for i in range(0, len(c) - k, k):
        if c[i + k] == 1:
            total_energy -= 3
        else:
            total_energy -= 1
   
    return total_energy - 1 if len(c) != k else total_energy - 3
###################### end of my code ###################