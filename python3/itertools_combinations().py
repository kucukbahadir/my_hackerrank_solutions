############################ my code ############################
from itertools import combinations

my_input = input().split()

string, r = my_input[0] , my_input[1]

for i in range(1,int(r) + 1):
    combination_list = list(combinations(sorted(string),i))
    for k in combination_list:
        print("".join(k))
########################## end of my code #######################