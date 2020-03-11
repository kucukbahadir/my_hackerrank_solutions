######################### my code #####################
y = int(input())
z = int(input())
n = int(input())

my_list = [[i,j,k] for i in range(0,x+1) for j in range(0, y+1) for k in range(0, z+1) if i + j + k != n ]

print(my_list)

###################### end of my code #################
