########################## my code ########################
def check_prime(number):
        if number == 2:
            return True
        if number % 2 != 0:
            i = 3
            while i**2 <= number:  
                if (number % i) == 0:
                    return False
                i += 2
            return True

def find_prime_factor(n):
    for j in range(1,n+1):   
        if n % j == 0:
            if check_prime(n//j): return n//j 
####################### end of my code ####################