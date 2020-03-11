################################ my code ################################
my_list = []

for i in range(0,N):
    commit = input().split()

    if commit[0] == 'insert':
        my_list.insert(int(commit[1]),int(commit[2]))
    elif commit[0] == 'print':
        print(my_list)
    elif commit[0] == 'remove':
        my_list.remove(int(commit[1]))
    elif commit[0] == 'append':
        my_list.append(int(commit[1]))
    elif commit[0] == 'sort':
        my_list.sort()
    elif commit[0] == 'pop':
        del my_list[-1]
    elif commit[0] == 'reverse':
        my_list.reverse()
############################## end of my code ############################