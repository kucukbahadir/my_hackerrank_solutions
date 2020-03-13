################################## my code ##############################
from itertools import permutations

my_input = input().split()

output = list(permutations(my_input[0],int(my_input[1]))) if len(my_input) == 2  else list(permutations(my_input[0]))

for i in sorted(output):
    print("".join(i))

############################## end of my code ###########################
