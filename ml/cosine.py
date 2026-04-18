import math

def cosine(a,b):
    dot = sum(a[i]*b[i] for i in range(3))
    ma = math.sqrt(sum(i*i for i in a))
    mb = math.sqrt(sum(i*i for i in b))
    return dot/(ma*mb)