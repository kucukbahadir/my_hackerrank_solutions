############################ my code ##############################
def pickingNumbers(a):
    main_lists = [0] * (max(a) + 1)
    max_value = main_lists[0] + main_lists[1]

    for i in a:
        main_lists[i] += 1
    
    for i in range(0, len(main_lists) - 1):
        if main_lists[i] + main_lists[i + 1] > max_value:
            max_value = main_lists[i] + main_lists[i + 1]
    
    return max_value
####################### end of my code ###########################