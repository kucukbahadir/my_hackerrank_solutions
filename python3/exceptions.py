########################## my code ########################### 
n = input()

for i in range(0,int(n)):
    a, b = input().split()

    try:
        print(int(a)//int(b))
    except Exception as k:
        print("Error Code:", str(k))

####################### end of my code ########################