import math

def distance(a,b):
    return math.sqrt(sum((a[i]-b[i])**2 for i in range(3)))