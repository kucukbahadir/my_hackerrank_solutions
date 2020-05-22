################################ my code ###############################
def check_smallest_multiple(n):
    def check_divisible(k):
        for i in range(n,1,-1):
            if k % i != 0:
                return False
        return True
    output = n
    while True:
        if check_divisible(output):
            return output
        output += n
############################ end of my code ############################