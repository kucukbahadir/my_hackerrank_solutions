######################## my code ####################
n = int(input())
arr = map(int, input().split())

arr = list(arr)
k = max(arr)
for i in range(0,n):
    if max(arr) == k:
        arr.remove(max(arr))

arr.sort(reverse=True)
print(arr[0])

##################### end of my code ###############
