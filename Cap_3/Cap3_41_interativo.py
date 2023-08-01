import math
def acerto(x,y,r,x1,y1):
    dist = math.sqrt(math.pow(x1-x,2)+math.pow(y1-y,2))
    if dist <= r:
        return True
    else:
        return False