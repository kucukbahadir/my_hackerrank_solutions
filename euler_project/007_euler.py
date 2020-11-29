import math

################################ MY CODE ###############################
max_n = 105000
prime_list = [0] * (max_n) + [-1]

for i in range(2,int(math.sqrt(max_n) + 1)):
    if(prime_list[i] == 0):
        for j in range(2,int(max_n / i) + 1):
            prime_list[i * j] = 1

main_list = [i for i in range(2,len(prime_list)) if(prime_list[i] == 0)]

############################# END OF MY CODE ###########################

for a0 in range(int(input().strip())):
    n = int(input().strip())
    print(main_list[n-1])
    