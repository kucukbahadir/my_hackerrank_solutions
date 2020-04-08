########################### my code #######################
def findDigits(n):
    number_string = [int(char) for char in str(n) if char != "0"]
    count = 0

    for i in number_string: 
        if n % i == 0: count += 1
    
    return count
####################### end of my code #####################