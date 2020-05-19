############################ my code #########################
def countSwaps(a):
    n_swaps = 0

    for i in range(len(a) - 1):
        for k in range(len(a) - 1):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]
                n_swaps +=1
                
    print("Array is sorted in {} swaps.".format(n_swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a) - 1]))
######################## end of my code ######################