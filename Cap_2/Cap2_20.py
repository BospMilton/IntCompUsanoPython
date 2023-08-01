"""importamos o módulo math para facilitar os cálculos e nos familiarizarmos com os
módulos Python.""" 
import math


while True:
    comp = int(input('Digite a distancia em pés: '))
    ang = float(input('Digite o grau que é formado entre a escada e o chão: '))

    rad = (math.pi*ang)/180
    alt = comp*math.sin(rad)
    print()
    print(f'A altura da escada na parede é de: {alt:6.2f} pés.')
    print()

