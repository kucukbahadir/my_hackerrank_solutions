############################ my code ############################
def bonAppetit(bill, k, b):
    bill.pop(k)
    sum_others = sum(bill)

    print('Bon Appetit' if b - sum_others//2 == 0 else b - sum_others//2)
######################### end of my code ########################