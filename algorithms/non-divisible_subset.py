########################### my code########################
def nonDivisibleSubset(k, s):
    remains = [0] * k
     
    for value in s:
        remains[value%k] += 1

    output = 0
    for t in range(1, (k+1)//2):
        output += max(remains[t], remains[k-t])
    
    if k % 2 == 0 and remains[k//2]:
        output += 1

    if remains[0]:
        output += 1

    return output
######################## end of my code####################