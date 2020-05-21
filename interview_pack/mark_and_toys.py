############################ my code #########################
def maximumToys(prices, k):
    prices.sort()
    total = 0

    for i in range(len(prices)):
        if total + prices[i] < k:
            total += prices[i]
        else:
            return i
######################## end of my code #######################