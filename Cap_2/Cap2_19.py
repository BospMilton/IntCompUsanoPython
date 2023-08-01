"""O mais dificil nesta questão é solucionar o 'negócio' da questão e não a 
lógica em si."""

"""importamos o módulo math para facilitar os cálculos e nos familiarizarmos com os
módulos Python.""" 
import math

x = float(input('Digite a coordenada X do dardo: '))
y = float(input('Digite a coordenada Y do dardo: '))
dst_dardo = math.sqrt((x-0)**2 + (y-0)**2) # dAB² = (xB – xA)² + (yB – yA)².
r_alvo = 10

#a_alvo = math.pi * math.pow(r_alvo,2) #area da circunferencia do alvo
#c_alvo = 2 * math.pi * r_alvo #circunferencia do alvo

if dst_dardo <= r_alvo:
    print(True)
else:
    print(False)
    print()
