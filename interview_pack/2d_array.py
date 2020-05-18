############################### my code #######################
def hourglassSum(arr):
    hourglass = []

    for y in range(1, len(arr) - 1):
        for x in range(1, len(arr[y]) - 1):
            first_line = arr[y-1][x-1] + arr[y-1][x] + arr[y-1][x+1]
            second_line = arr[y][x]
            third_line = arr[y+1][x-1] + arr[y+1][x] + arr[y+1][x+1]
            hourglass.append(first_line + second_line + third_line)

    return max(hourglass)
########################### end of my code ####################