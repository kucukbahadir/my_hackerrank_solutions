############################ my code #########################
from collections import Counter
n = int(input())

shoes_list = dict(Counter(map(int,input().split())).items())

number_of_customers = int(input())
total_money = 0

for i in range(number_of_customers):
    current_customer = list(map(int,input().split()))
    
    if current_customer[0] in shoes_list:
        if shoes_list[current_customer[0]] > 0:
            total_money += current_customer[1]
            shoes_list[current_customer[0]] -= 1
    
print(total_money)
######################### end of my code ######################