############################## my code ##############################
def print_formatted(number):
    for i in range(1,number + 1):
        print(' '.join(map(lambda x: x.rjust(len(bin(number)[2:])), [str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]])))
########################### end of my code ##########################