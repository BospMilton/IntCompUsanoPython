import math
def pontos(x1, y1, x2, y2):
    #distancia
    dist = (math.sqrt(math.pow((x2-x1), 2)) + math.pow((y2-y1), 2))
    incli = math.atan2((x2-x1), (y2-y1))
    return print(f'Inclinação da reta é: {(incli):6.2f} e a distancia entre os pontos: {(dist):6.2f}.')
