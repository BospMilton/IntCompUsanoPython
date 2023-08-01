import math
def coll(xa, ya, ra, xb, yb, rb):
    dist_a = math.sqrt(math.pow(xa, 2) + math.pow(ya, 2))
    dist_b = math.sqrt(math.pow(xb, 2) + math.pow(yb, 2))
    dist_ab = dist_b - dist_a
    if  dist_ab - (ra+rb)<= 0:
        return print(True)
    else:
        return print(False)