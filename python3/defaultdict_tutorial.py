############################ my code ############################
from collections import defaultdict

N,M=map(int,input().split())
my_dictionary =defaultdict(list)

for i in range(N):
    s=input().rstrip()
    my_dictionary[s].append(i+1)

for _ in range(M):
    s=input().rstrip()
    if s in my_dictionary:
        print(' '.join(map(str,my_dictionary[s])))
    else:
        print('-1')
######################### end of my code ########################