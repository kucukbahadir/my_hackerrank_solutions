############################# my code #############################
def find_even_fibo(x):
    fibos , value, temp_value1, temp_value2 = [], 0, 1 , 0

    for i in range(x):
        value = temp_value1 + temp_value2
        temp_value2 = temp_value1
        temp_value1 = value
        
        if value > x: break
        if value % 2 == 0: fibos.append(value)
    return sum(fibos)
########################## end of  my code #########################