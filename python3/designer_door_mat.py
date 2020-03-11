############################## my code #############################
height , width = map(int , input().split())

for line in range(1,height,2):
    print((".|." * line).center(width,"-"))

print("WELCOME".center(width,"-"))

for line in range(height - 2, -1, -2):
    print((".|." * line).center(width,"-"))

########################### end of my code ##########################