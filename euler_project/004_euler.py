############################ my code ############################
from bisect import bisect_left 
"""returns the position in the sorted list,
where the number passed in argument can be placed
so as to maintain the resultant list in sorted"""

arr, i = [], 999

while i > 100:
    for j in range(990, 100, (-11 if i%11 else -1)):
        num = i * j
        if str(num) == str(num)[::-1]:
            arr.append(num)
    i-=1
arr.sort()

for _ in range(int(input())):
    i = bisect_left(arr,int(input()))
    print(arr[i-1])
######################## end of my code #########################