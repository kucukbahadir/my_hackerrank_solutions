############################## my code ############################
from collections import Counter

def makeAnagram(a, b):
    a = Counter(a)
    b = Counter(b)
    return sum((a - b).values()) + sum((b - a).values())

########################### end of my code ########################